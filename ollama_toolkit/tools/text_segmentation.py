# Updated ollama_toolkit/tools/text_segmentation.py
from typing import List, Dict, Any, Optional
import logging
import re  # Adding missing import
from ..function_calling import call_with_function, extract_json_from_text
from ..context import calculate_optimal_ctx_size, split_long_text
from models.transcript_analysis_models import TopicList, TranscriptSegment

def segment_transcript(
    transcript_text: str,
    model: str = "mistral:latest-32", 
    context_size: Optional[int] = None,
    max_topics: int = 7,
    temperature: float = 0.1
) -> Dict[str, Any]:
    """
    Segment a transcript using the two-step process with Ollama's function calling.
    
    Args:
        transcript_text: The transcript to segment
        model: The Ollama model to use
        context_size: Optional context window size, calculated automatically if None
        max_topics: Maximum number of topics to extract
        temperature: Temperature setting for the model (lower = more deterministic)
        
    Returns:
        Dictionary with success flag and either segments or error information
    """
    # Calculate context size if not provided
    if context_size is None:
        context_size = calculate_optimal_ctx_size(transcript_text)
    
    options = {
        "num_ctx": context_size,
        "temperature": temperature
    }
    
    # Handle transcripts that are too large
    if len(transcript_text.split()) * 1.3 > context_size * 0.9:
        logging.warning(f"Transcript too large for context window. Using text splitting.")
        return segment_long_transcript(transcript_text, model, context_size, max_topics)
    
    # Step 1: Identify topics
    topics_prompt = f"""Read this YouTube transcript and identify {max_topics-2}-{max_topics} main sections or topics.

The transcript appears to be from a video about: {transcript_text[:100]}...

Analyze the full transcript and return a list of distinct topics that capture the main sections of the video.

TRANSCRIPT:
{transcript_text}"""
    
    topics_result = call_with_function(
        prompt=topics_prompt,
        model_class=TopicList,
        function_name="identify_transcript_topics",
        description="Identify main topics in a transcript and return a list of section names",
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
        extraction_prompt = f"""Extract the exact text from this transcript that corresponds to the section: '{section}'

IMPORTANT: Return only the precise text from the transcript that belongs to this section. Do not summarize or paraphrase.

SECTION: {section}

TRANSCRIPT:
{transcript_text}"""
        
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
                logging.warning(f"Content validation failed for '{section}' - content doesn't match transcript")
                # Try a simpler approach with more direct instructions
                retry_prompt = f"""Extract the EXACT TEXT from this transcript for the section: '{section}'

DO NOT paraphrase or summarize. Extract only the precise words that appear in the transcript.

SECTION: {section}

TRANSCRIPT:
{transcript_text}"""
                
                retry_result = call_with_function(
                    prompt=retry_prompt,
                    model_class=TranscriptSegment,
                    function_name="extract_transcript_segment_retry",
                    description=f"Extract exact transcript content for the topic: {section}",
                    model=model,
                    options=options
                )
                
                if retry_result["success"] and validate_segment_content(retry_result["data"].content, transcript_text):
                    all_segments.append(retry_result["data"])
                    logging.info(f"Successfully extracted segment on retry for '{section}'")
        else:
            logging.warning(f"Failed to extract segment for '{section}': {segment_result.get('error')}")
    
    # Return results
    if all_segments:
        # Check for and resolve potential overlaps
        all_segments = detect_and_resolve_overlaps(all_segments)
        return {"success": True, "segments": all_segments}
    else:
        return {"success": False, "error": "No valid segments extracted"}

def segment_long_transcript(
    transcript_text: str, 
    model: str = "mistral:latest-32",
    context_size: int = 32768,
    max_topics: int = 7
) -> Dict[str, Any]:
    """
    Handle segmentation for transcripts that exceed context window size
    
    Args:
        transcript_text: The transcript to segment
        model: The Ollama model to use
        context_size: Context window size
        max_topics: Maximum number of topics to extract
        
    Returns:
        Dictionary with success flag and segments or error information
    """
    # Split the transcript into chunks
    chunks = split_long_text(transcript_text, int(context_size * 0.8))
    logging.info(f"Split transcript into {len(chunks)} chunks")
    
    all_segments = []
    topics_per_chunk = max(3, max_topics // len(chunks))
    
    # Process each chunk separately
    for i, chunk in enumerate(chunks):
        chunk_result = segment_transcript(
            chunk, 
            model=model, 
            context_size=context_size,
            max_topics=topics_per_chunk
        )
        
        if chunk_result["success"]:
            # Add chunk number to topic names to avoid confusion
            for segment in chunk_result["segments"]:
                segment.topic = f"Part {i+1}: {segment.topic}"
                all_segments.append(segment)
        else:
            logging.warning(f"Failed to segment chunk {i+1}: {chunk_result.get('error')}")
    
    # Return results
    if all_segments:
        # Check for and resolve potential overlaps
        all_segments = detect_and_resolve_overlaps(all_segments)
        return {"success": True, "segments": all_segments}
    else:
        # Fallback to simple splitting if all else fails
        return fallback_segmentation(transcript_text)

def validate_segment_content(segment_content: str, transcript: str, threshold: float = 0.6) -> bool:
    """
    Validate that segment content actually comes from the transcript
    
    Args:
        segment_content: The extracted content
        transcript: The original transcript
        threshold: Minimum word overlap required (default: 0.6)
        
    Returns:
        Boolean indicating if content is valid
    """
    # Extract words, ignoring case and punctuation
    content_words = set(re.findall(r'\b\w+\b', segment_content.lower()))
    transcript_words = set(re.findall(r'\b\w+\b', transcript.lower()))
    
    if not content_words:
        return False
        
    overlap = len(content_words.intersection(transcript_words)) / len(content_words)
    return overlap > threshold

def detect_and_resolve_overlaps(segments: List[TranscriptSegment]) -> List[TranscriptSegment]:
    """
    Detect and resolve content overlap between segments
    
    Args:
        segments: List of transcript segments
        
    Returns:
        List of segments with overlaps resolved
    """
    # Sort segments by length of content (longer segments first)
    segments.sort(key=lambda s: len(s.content), reverse=True)
    
    for i in range(len(segments)):
        for j in range(i+1, len(segments)):
            # Detect significant word overlap
            words_i = set(re.findall(r'\b\w+\b', segments[i].content.lower()))
            words_j = set(re.findall(r'\b\w+\b', segments[j].content.lower()))
            overlap = words_i.intersection(words_j)
            
            # If significant overlap (more than 40% of smaller segment)
            if len(overlap) > 0.4 * min(len(words_i), len(words_j)):
                # Keep content in the more relevant segment based on topic names
                if is_more_relevant_to(overlap, segments[i].topic, segments[j].topic):
                    # Remove overlapping content from segment j
                    segments[j].content = remove_overlapping_content(segments[j].content, overlap)
                else:
                    # Remove overlapping content from segment i
                    segments[i].content = remove_overlapping_content(segments[i].content, overlap)
    
    return segments

def is_more_relevant_to(words: set, topic1: str, topic2: str) -> bool:
    """
    Determine if content is more relevant to topic1 or topic2
    Simplified implementation - in a real system this would be more sophisticated
    
    Args:
        words: The words in the overlapping content
        topic1: First topic name
        topic2: Second topic name
        
    Returns:
        True if more relevant to topic1, False if more relevant to topic2
    """
    # Simple heuristic: check word overlap with topic names
    topic1_words = set(re.findall(r'\b\w+\b', topic1.lower()))
    topic2_words = set(re.findall(r'\b\w+\b', topic2.lower()))
    
    overlap1 = len(words.intersection(topic1_words))
    overlap2 = len(words.intersection(topic2_words))
    
    return overlap1 >= overlap2

def remove_overlapping_content(content: str, overlap_words: set) -> str:
    """
    Remove overlapping content from a segment
    Simplified implementation that removes sentences containing overlapping words
    
    Args:
        content: The content of the segment
        overlap_words: The words that appear in the overlap
        
    Returns:
        Content with overlapping parts removed
    """
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', content)
    filtered_sentences = []
    
    for sentence in sentences:
        # Check if sentence contains multiple overlapping words
        sentence_words = set(re.findall(r'\b\w+\b', sentence.lower()))
        if len(sentence_words.intersection(overlap_words)) < 3:
            filtered_sentences.append(sentence)
    
    # Rejoin the non-overlapping sentences
    return ' '.join(filtered_sentences)

def fallback_segmentation(transcript_text: str) -> Dict[str, Any]:
    """
    Simple fallback segmentation when other methods fail
    
    Args:
        transcript_text: The transcript to segment
        
    Returns:
        Dictionary with success flag and segments
    """
    # Simple algorithm to split by paragraphs
    paragraphs = transcript_text.split('\n\n')
    
    segments = []
    for i, para in enumerate(paragraphs):
        if len(para.split()) < 10:  # Skip very short paragraphs
            continue
            
        segment = TranscriptSegment(
            topic=f"Section {i+1}",
            content=para
        )
        segments.append(segment)
    
    # If we couldn't even get paragraphs, just use the full text
    if not segments:
        segments = [TranscriptSegment(
            topic="Full Transcript",
            content=transcript_text
        )]
    
    return {"success": True, "segments": segments}