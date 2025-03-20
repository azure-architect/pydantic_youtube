# Specification: Structured JSON Output Generation with Ollama and Pydantic

## 1. Overview

The implementation in `test_methods.py` demonstrates an effective approach for generating structured, validated JSON output from Large Language Models (LLMs) using Ollama as the inference backend and Pydantic for schema definition and validation. This specification details the approach, key components, and potential improvements.

## 2. Core Components

### 2.1 Schema Definition with Pydantic

```python
class TranscriptSegment(BaseModel):
    topic: str
    content: str

class TopicList(BaseModel):
    sections: List[str]
```

**Purpose**: Define explicit schemas that serve as both a validation mechanism and a guide for the LLM to structure its output.

**Implementation Details**:
- Simple, clear field definitions with appropriate types
- Fields kept minimal to reduce complexity for the model
- Schema designed for a two-stage process

### 2.2 LLM Instruction with Format Guidance

```python
topics_prompt = f"""Read this YouTube transcript and identify 5-7 main sections.
Transcript: {transcript_text}"""
```

**Purpose**: Provide clear, concise instructions to the LLM about the expected output structure.

**Implementation Details**:
- Direct, explicit instructions
- Limited to a single task for clarity
- Number range provided to guide the model (5-7 sections)

### 2.3 Ollama Format Parameter Usage

```python
topics_response = chat(
    model=model,
    messages=[{"role": "user", "content": topics_prompt}],
    format=TopicList.model_json_schema(),
    options={"num_ctx": 32768}
)
```

**Purpose**: Enforce JSON structure in the model's response through Ollama's format parameter.

**Implementation Details**:
- Uses Pydantic's `model_json_schema()` to generate a JSON schema
- Passes this schema to Ollama via the `format` parameter
- Sets appropriate context window size (`num_ctx=32768`)

### 2.4 Response Validation

```python
topics_data = TopicList.model_validate_json(topics_response['message']['content'])
```

**Purpose**: Ensure responses adhere to the expected structure and handle validation errors.

**Implementation Details**:
- Uses Pydantic's `model_validate_json` method to parse and validate JSON strings
- Validates against the predefined schema
- Wrapped in try/except blocks to handle validation failures

### 2.5 Two-Step Extraction Process

**Purpose**: Break down complex tasks into simpler subtasks for better LLM performance.

**Implementation Details**:
1. **Topic Identification**: First extract just the section names/topics
2. **Content Extraction**: For each topic, separately extract the relevant content
3. **Aggregation**: Combine results into a single structured output

## 3. Process Flow

1. **Initialize**: Define Pydantic models for response structure
2. **Step 1 - Topic Extraction**:
   - Create a prompt asking for section identification
   - Send request to Ollama with format parameter
   - Validate and extract topics from response
3. **Step 2 - Content Extraction**:
   - For each topic, create a targeted extraction prompt
   - Send request to Ollama with format parameter
   - Validate and extract content for each segment
4. **Combine Results**: Aggregate all segments into final structure
5. **Validate & Measure**: Calculate coverage and other metrics

## 4. Technical Considerations

### 4.1 Context Window Management

- Explicitly sets `num_ctx=32768` to ensure full transcript processing
- Particularly important for the initial topic identification phase

### 4.2 Error Handling and Resilience

- Comprehensive try/except blocks throughout
- Logs detailed error information
- Continues processing remaining segments if one fails

### 4.3 Performance Monitoring

- Measures and logs execution time for each operation
- Reports per-segment extraction time
- Calculates overall transcript coverage

## 5. Potential Improvements

### 5.1 Optimization of Context Window Size

**Current Limitation**: Uses a fixed large context window (`num_ctx=32768`) for all operations.

**Improvement**: Dynamically adjust context window size based on input length:
```python
def calculate_optimal_ctx_size(text: str) -> int:
    """Determine optimal context window size based on input length."""
    token_estimate = len(text.split()) * 1.3  # Rough token estimate
    return min(max(int(token_estimate * 2), 4096), 32768)  # Min 4K, max 32K

# Usage
ctx_size = calculate_optimal_ctx_size(transcript_text)
topics_response = chat(
    model=model,
    messages=[{"role": "user", "content": topics_prompt}],
    format=TopicList.model_json_schema(),
    options={"num_ctx": ctx_size}
)
```

### 5.2 Model Selection Based on Task Complexity

**Current Limitation**: Uses same model for all operations regardless of complexity.

**Improvement**: Implement model selection based on task complexity:
```python
def select_model_for_task(task_type: str, input_length: int) -> str:
    """Select appropriate model based on task type and input length."""
    if task_type == "topic_identification" and input_length > 5000:
        return "mistral:latest-32"  # Large context model for initial segmentation
    elif task_type == "content_extraction":
        return "mistral:7b-instruct"  # Faster model for content extraction
    else:
        return "mistral:latest"  # Default model
```

### 5.3 Batch Processing for Content Extraction

**Current Limitation**: Processes each segment extraction as a separate request.

**Improvement**: Implement batching for similar extraction tasks:
```python
def batch_extract_content(sections: List[str], transcript: str, batch_size: int = 3) -> List[TranscriptSegment]:
    """Extract content for multiple sections in batched requests."""
    results = []
    for i in range(0, len(sections), batch_size):
        batch = sections[i:i+batch_size]
        batch_prompt = "Extract content for multiple sections from this transcript:\n\n"
        for idx, section in enumerate(batch):
            batch_prompt += f"SECTION {idx+1}: {section}\n"
        batch_prompt += f"\nTranscript: {transcript}"
        
        # Define a batch result model
        class BatchResult(BaseModel):
            segments: List[TranscriptSegment]
        
        batch_response = chat(
            model=model,
            messages=[{"role": "user", "content": batch_prompt}],
            format=BatchResult.model_json_schema(),
            options={"num_ctx": 32768}
        )
        
        batch_results = BatchResult.model_validate_json(batch_response['message']['content'])
        results.extend(batch_results.segments)
    
    return results
```

### 5.4 Enhanced Validation and Error Recovery

**Current Limitation**: Limited validation beyond schema checking.

**Improvement**: Add content-aware validation and recovery:
```python
def validate_segment_content(segment: TranscriptSegment, transcript: str) -> bool:
    """Validate that segment content is actually from the transcript."""
    # Simple check: at least 70% of words in content should be in transcript
    content_words = set(segment.content.lower().split())
    transcript_words = set(transcript.lower().split())
    overlap = len(content_words.intersection(transcript_words)) / len(content_words)
    return overlap > 0.7

# Usage in extraction loop
if not validate_segment_content(segment, transcript_text):
    print(f"  ⚠️ Content validation failed for '{section}', retrying...")
    # Implement retry logic with more explicit instructions
```

### 5.5 Progressive Enhancement of Prompts

**Current Limitation**: Uses static prompts regardless of model performance.

**Improvement**: Implement progressive enhancement based on validation results:
```python
def extract_with_progressive_enhancement(section: str, transcript: str, max_attempts: int = 3) -> Optional[TranscriptSegment]:
    """Extract content with progressively enhanced prompts if validation fails."""
    prompts = [
        f"Extract the exact text from this transcript for the section: '{section}'\nTranscript: {transcript}",
        f"Look carefully through this transcript and extract all content related to: '{section}'\nReturn ONLY text that appears in the transcript.\nTranscript: {transcript}",
        f"Find the part of this transcript that discusses '{section}'.\nExtract the relevant sentences word-for-word.\nDo not paraphrase or summarize.\nTranscript: {transcript}"
    ]
    
    for attempt, prompt in enumerate(prompts[:max_attempts]):
        try:
            # Extraction logic
            # Validation logic
            if valid:
                return segment
        except Exception as e:
            print(f"  Attempt {attempt+1} failed: {e}")
    
    return None
```

### 5.6 Content Overlap Detection and Resolution

**Current Limitation**: No handling of potential content overlap between segments.

**Improvement**: Implement overlap detection and resolution:
```python
def detect_and_resolve_overlaps(segments: List[TranscriptSegment]) -> List[TranscriptSegment]:
    """Detect and resolve content overlap between segments."""
    # Sort segments by length of content (longer segments first)
    segments.sort(key=lambda s: len(s.content), reverse=True)
    
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            overlap = find_longest_common_substring(segments[i].content, segments[j].content)
            if len(overlap) > 50:  # Significant overlap
                # Determine which segment should keep the overlapping content
                # based on relevance to topic
                if is_more_relevant_to(overlap, segments[i].topic, segments[j].topic):
                    segments[j].content = segments[j].content.replace(overlap, "").strip()
                else:
                    segments[i].content = segments[i].content.replace(overlap, "").strip()
    
    return segments
```

## 6. Conclusion

The implementation in `test_methods.py` provides a robust approach to generating structured output from LLMs using Ollama and Pydantic. The two-step process with clear schema definition and validation ensures high-quality, structured results. The proposed improvements would further enhance performance, accuracy, and efficiency, particularly for production-grade applications processing large volumes of content.