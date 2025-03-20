# Implementation Plan: Structured Output Processing with Ollama Function Calling and PydanticAI

## 1. Project Objectives

- Integrate direct Ollama function calling for structured outputs
- Leverage Pydantic models for schema generation and validation
- Maintain existing PydanticAI graph workflow for orchestration
- Implement the two-step segmentation approach from `test_methods.py`
- Enhance error handling and validation for robust processing

## 2. Implementation Components

### 2.1. Ollama Integration Layer (`/ollama_integration/`)

#### `__init__.py`
- Package initialization and exports

#### `function_caller.py`
- Core utilities for Ollama function calling
- Schema generation from Pydantic models
- Response processing and validation
- Timing and token usage tracking

#### `segmentation.py`
- Two-step segmentation implementation
- Topic extraction function
- Content extraction function
- Segment validation and overlap detection

#### `context_optimizer.py`
- Context window size optimization
- Token counting utilities
- Input handling for long transcripts

### 2.2. Model Updates

#### `models/transcript_analysis_models.py`
- Add `TopicList` model for topic extraction
- Update `TranscriptSegment` model for content extraction
- Add validation fields and methods

### 2.3. Graph Node Updates

#### `graph/transcript_analysis_nodes.py`
- Update `SegmentTranscript` node to use function calling
- Implement progressive error handling
- Add fallback mechanisms
- Improve reporting and logging

## 3. Detailed Implementation Steps

### Phase 1: Core Function Calling Infrastructure

1. Create the `ollama_integration` package structure
2. Implement `function_caller.py` with:
   - `create_function_schema()` - Converts Pydantic models to function schemas
   - `call_with_function()` - Makes Ollama API calls with function definitions
   - `process_function_response()` - Processes and validates responses

### Phase 2: Segmentation Implementation

1. Implement `segmentation.py` with:
   - `extract_topics()` - First-stage extraction of section topics
   - `extract_content()` - Second-stage extraction of content for each topic
   - `segment_transcript()` - Full two-step process with error handling
   - `validate_segment_content()` - Validation function for segment quality

### Phase 3: Context Optimization

1. Implement `context_optimizer.py` with:
   - `calculate_optimal_ctx_size()` - Dynamically determines context window size
   - `estimate_tokens()` - Estimates token count for text
   - `split_long_transcript()` - Handles transcripts too large for context window

### Phase 4: Graph Node Integration

1. Update `SegmentTranscript` node to use the new segmentation service
2. Implement proper error handling and fallbacks
3. Add detailed logging and timing information
4. Update state management for the graph workflow

### Phase 5: Additional Model Updates

1. Update other graph nodes to use function calling where appropriate:
   - `ExtractKeywords`
   - `ExtractBusinessProcesses`
   - `ExtractTechnicalProcesses`
   - `ExtractTechnologies`

## 4. Example Implementation Code

### 4.1. Function Caller

```python
# ollama_integration/function_caller.py
from typing import Type, TypeVar, List, Dict, Any, Optional
from pydantic import BaseModel
from ollama import chat
import time
import logging
import json

T = TypeVar('T', bound=BaseModel)

def create_function_schema(model_class: Type[T], function_name: str, description: str) -> Dict:
    """Create a function schema from a Pydantic model for Ollama/Mistral function calling"""
    schema = model_class.model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": function_name,
            "description": description,
            "parameters": schema
        }
    }

def call_with_function(
    prompt: str, 
    model_class: Type[T], 
    function_name: str, 
    description: str,
    model: str = "mistral:latest-32",
    options: Dict[str, Any] = None
) -> Dict[str, Any]:
    """
    Make a call to Ollama with function calling to get structured output
    """
    options = options or {"num_ctx": 32768}
    function_schema = create_function_schema(model_class, function_name, description)
    
    logging.info(f"Calling {function_name} with model {model}")
    
    try:
        start_time = time.time()
        response = chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            tools=[function_schema],
            options=options
        )
        end_time = time.time()
        
        logging.info(f"Request to {model} took {end_time - start_time:.2f} seconds")
        
        # Process the response to extract the function call result
        tool_calls = response.get('tool_calls', [])
        if tool_calls and len(tool_calls) > 0 and tool_calls[0]['function']['name'] == function_name:
            try:
                # Parse and validate the function arguments
                args = json.loads(tool_calls[0]['function']['arguments'])
                validated_data = model_class.model_validate(args)
                return {
                    "success": True, 
                    "data": validated_data, 
                    "response_time": end_time - start_time,
                    "raw_response": response
                }
            except Exception as e:
                logging.error(f"Error validating function result: {str(e)}")
                return {"success": False, "error": f"Validation error: {str(e)}"}
        else:
            return {"success": False, "error": "No function call in response"}
            
    except Exception as e:
        logging.error(f"Error in Ollama request: {str(e)}")
        return {"success": False, "error": str(e), "error_type": type(e).__name__}
```

### 4.2. Segmentation Service

```python
# ollama_integration/segmentation.py
from typing import List, Dict, Any, Optional
from .function_caller import call_with_function
from .context_optimizer import calculate_optimal_ctx_size
from models.transcript_analysis_models import TopicList, TranscriptSegment
import logging

def segment_transcript(
    transcript_text: str, 
    model: str = "mistral:latest-32", 
    context_size: Optional[int] = None
) -> Dict[str, Any]:
    """
    Segment a transcript using the two-step process with Ollama's function calling.
    
    Args:
        transcript_text: The transcript text to segment
        model: The Ollama model to use
        context_size: Optional context window size, calculated automatically if None
        
    Returns:
        Dict with success flag and either segments or error information
    """
    # Calculate context size if not provided
    if context_size is None:
        context_size = calculate_optimal_ctx_size(transcript_text)
    
    options = {"num_ctx": context_size}
    
    # Step 1: Identify topics
    topics_prompt = f"""Read this YouTube transcript and identify 5-7 main sections.
    Transcript: {transcript_text}"""
    
    topics_result = call_with_function(
        prompt=topics_prompt,
        model_class=TopicList,
        function_name="identify_transcript_topics",
        description="Identify main topics in a transcript",
        model=model,
        options=options
    )
    
    if not topics_result["success"]:
        return {"success": False, "error": f"Failed to identify topics: {topics_result.get('error')}"}
    
    sections = topics_result["data"].sections
    logging.info(f"Identified {len(sections)} topics: {', '.join(sections)}")
    
    # Step 2: Extract content for each section
    all_segments = []
    
    for section in sections:
        extraction_prompt = f"""Extract the exact text from this transcript for the section: '{section}'
        Transcript: {transcript_text}"""
        
        segment_result = call_with_function(
            prompt=extraction_prompt,
            model_class=TranscriptSegment,
            function_name="extract_transcript_segment",
            description=f"Extract transcript content for the topic: {section}",
            model=model,
            options=options
        )
        
        if segment_result["success"]:
            # Check if the segment content is actually from the transcript
            segment = segment_result["data"]
            if validate_segment_content(segment.content, transcript_text):
                all_segments.append(segment)
                logging.info(f"Successfully extracted segment for '{section}' ({len(segment.content.split())} words)")
            else:
                logging.warning(f"Content validation failed for '{section}'")
        else:
            logging.warning(f"Failed to extract segment for '{section}': {segment_result.get('error')}")
    
    # Return results
    if all_segments:
        return {"success": True, "segments": all_segments}
    else:
        return {"success": False, "error": "No valid segments extracted"}

def validate_segment_content(segment_content: str, transcript: str, threshold: float = 0.7) -> bool:
    """
    Validate that segment content actually comes from the transcript
    
    Args:
        segment_content: The extracted content
        transcript: The original transcript
        threshold: Minimum word overlap required
        
    Returns:
        Boolean indicating if content is valid
    """
    content_words = set(segment_content.lower().split())
    transcript_words = set(transcript.lower().split())
    
    if not content_words:
        return False
        
    overlap = len(content_words.intersection(transcript_words)) / len(content_words)
    return overlap > threshold
```

### 4.3. Context Optimizer

```python
# ollama_integration/context_optimizer.py
def calculate_optimal_ctx_size(text: str) -> int:
    """
    Determine optimal context window size based on input length
    
    Args:
        text: Input text
        
    Returns:
        Optimal context window size
    """
    token_estimate = len(text.split()) * 1.3  # Rough token estimate
    return min(max(int(token_estimate * 2), 4096), 32768)  # Min 4K, max 32K

def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text
    
    Args:
        text: Input text
        
    Returns:
        Estimated token count
    """
    # Simple estimation based on words
    return int(len(text.split()) * 1.3)
```

### 4.4. Graph Node Update

```python
# graph/transcript_analysis_nodes.py
from dataclasses import dataclass
from pydantic_graph import BaseNode, GraphRunContext
from ollama_integration.segmentation import segment_transcript
import logging

@dataclass
class SegmentTranscript(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Segment the transcript into logical parts by topic using function calling"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractKeywords":
        logging.info(f"Segmenting transcript for video: {ctx.state.video_title} ({len(ctx.state.transcript)} chars)")
        
        try:
            # Use the segmentation service
            result = segment_transcript(
                ctx.state.transcript,
                model="mistral:latest-32",  # Or get from resources
            )
            
            if result["success"]:
                ctx.state.segments = [segment.model_dump() for segment in result["segments"]]
                logging.info(f"Successfully segmented transcript into {len(ctx.state.segments)} segments")
                return ExtractKeywords()
            else:
                # Handle error with fallback
                logging.error(f"Segmentation failed: {result.get('error')}")
                # Implement fallback segmentation
                ctx.state.segments = [{"topic": "Full Transcript", "content": ctx.state.transcript}]
                logging.info("Using fallback segmentation")
                return ExtractKeywords()
                
        except Exception as e:
            logging.exception(f"Error in segmentation: {str(e)}")
            # Implement fallback
            ctx.state.segments = [{"topic": "Full Transcript", "content": ctx.state.transcript}]
            logging.info("Using fallback segmentation due to exception")
            return ExtractKeywords()
```

## 5. Testing Plan

1. **Unit Tests**:
   - Test function schema generation
   - Test response validation
   - Test context window calculation

2. **Integration Tests**:
   - Test segmentation with sample transcripts
   - Test error handling and fallbacks
   - Test with different model configurations

3. **End-to-End Tests**:
   - Test full graph workflow
   - Test with real YouTube transcripts
   - Measure performance and accuracy

## 6. Implementation Timeline

1. **Week 1**: Core Function Calling (Phase 1)
   - Set up package structure
   - Implement function calling utilities
   - Basic tests

2. **Week 1-2**: Segmentation Implementation (Phase 2)
   - Implement two-step segmentation
   - Add validation
   - Test with sample transcripts

3. **Week 2**: Context Optimization (Phase 3)
   - Implement context window optimization
   - Test with various input sizes

4. **Week 3**: Graph Integration (Phase 4)
   - Update graph nodes
   - Implement error handling
   - Test workflow integration

5. **Week 3-4**: Additional Updates (Phase 5)
   - Update other nodes as needed
   - Final testing and optimization

## 7. Success Metrics

1. **Segmentation Quality**:
   - Minimum 90% transcript coverage
   - Coherent topic separation
   - Minimal content overlap between segments

2. **Error Handling**:
   - No unhandled exceptions
   - Clear fallback mechanisms
   - Detailed error logging

3. **Performance**:
   - Response times within acceptable limits
   - Efficient token usage
   - Reasonable memory footprint

This implementation plan provides a comprehensive roadmap for integrating Ollama function calling with the existing PydanticAI graph workflow, focusing on maintainability, robustness, and performance.