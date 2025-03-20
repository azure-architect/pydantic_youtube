import ollama
import asyncio
import re
import json
import tiktoken
from typing import List, Dict, Any
from models.transcript_analysis_models import TranscriptSegment, SegmentStats, TranscriptAnalysisResult

# Improved JSON extraction function
def extract_json(text):
    """Extract JSON from text that may contain explanatory content or formatting."""
    # First, try to find JSON blocks in markdown code blocks
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text, re.DOTALL)
    if json_match:
        potential_json = json_match.group(1).strip()
    else:
        # Try to find a JSON object with curly braces
        json_match = re.search(r'(\{[\s\S]*\})', text, re.DOTALL)
        if json_match:
            potential_json = json_match.group(1).strip()
        else:
            return None
    
    # Clean up the JSON string
    # Sometimes models include explanatory text before the actual JSON
    curly_start = potential_json.find('{')
    if curly_start > 0:
        potential_json = potential_json[curly_start:]
    
    try:
        return json.loads(potential_json)
    except json.JSONDecodeError:
        return None

# Initialize tokenizer for counting tokens
def count_tokens(text):
    try:
        # Using tiktoken for token counting - compatible with OpenAI models
        # For Mistral models, this is an approximation
        encoder = tiktoken.get_encoding("cl100k_base")  # Using OpenAI's encoding
        return len(encoder.encode(text))
    except:
        # Fallback to simple estimation (rough approximation)
        return len(text.split()) * 1.3  # Average tokens per word

async def run_transcript_analysis():
    # Sample transcript
    sample_transcript = """
    Hello and welcome to this video on Python programming. Today we'll cover the basics.
    First, let's talk about variables. Variables are containers for storing data values.
    Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
    
    Next, we'll look at control flow. If statements and loops are important for controlling program flow.
    Python uses indentation to indicate a block of code.
    
    Finally, let's discuss functions. A function is a block of code which only runs when it is called.
    You can pass data, known as parameters, into a function. A function can return data as a result.
    """
    
    # Initialize token counters
    input_tokens = 0
    output_tokens = 0
    
    print("Starting transcript analysis using Ollama...")
    
    # Count tokens in the transcript
    transcript_tokens = count_tokens(sample_transcript)
    input_tokens += transcript_tokens
    print(f"Transcript: {transcript_tokens} tokens")
    
    # Initialize the client
    client = ollama.Client(host="http://localhost:11434")
    
    # Step 1: Segment the text
    print("\nStep 1: Segmenting transcript...")
    try:
        # Use a more direct prompt for getting JSON
        segmentation_prompt = f"""
        Analyze this transcript and divide it into logical segments by topic.
        Return your answer in JSON format with an array named "segments" containing objects with "topic" and "content" fields.
        Example format:
        {{
          "segments": [
            {{ "topic": "Introduction", "content": "text here..." }},
            {{ "topic": "Main Topic", "content": "text here..." }}
          ]
        }}
        
        Transcript to analyze:
        {sample_transcript}
        """
        
        # Count tokens in the prompt
        prompt_tokens = count_tokens(segmentation_prompt)
        input_tokens += prompt_tokens
        print(f"Segmentation prompt: {prompt_tokens} tokens")
        
        segmentation_response = client.chat(
            model='mistral:latest',
            messages=[{'role': 'user', 'content': segmentation_prompt}]
        )
        
        # Try to extract JSON from the response
        response_content = segmentation_response.message.content
        
        # Count tokens in the response
        response_tokens = count_tokens(response_content)
        output_tokens += response_tokens
        print(f"Segmentation response: {response_tokens} tokens")
        
        print("Raw response from segmentation:")
        print(response_content[:200] + "..." if len(response_content) > 200 else response_content)
        
        # Use the improved JSON extraction function
        json_data = extract_json(response_content)
        if json_data and 'segments' in json_data:
            segments = json_data['segments']
        else:
            print("⚠️ Could not parse JSON, using fallback")
            segments = [{"topic": "Full Text", "content": sample_transcript}]
            
        if not segments:
            # Fallback if no segments were created
            segments = [{"topic": "Full Text", "content": sample_transcript}]
            
        print(f"✅ Successfully segmented transcript into {len(segments)} segments:")
        for i, segment in enumerate(segments):
            print(f"  Segment {i+1}: '{segment['topic']}' - {len(segment['content'].split())} words")
            
    except Exception as e:
        print(f"❌ Error in segmentation: {str(e)}")
        segments = [{"topic": "Full Text", "content": sample_transcript}]
    
    # Step 2: Calculate stats for each segment
    print("\nStep 2: Calculating statistics for each segment...")
    stats = []
    
    for i, segment in enumerate(segments):
        try:
            # Prepare a stats prompt
            stats_prompt = f"""
            Calculate statistics for this transcript segment with topic '{segment['topic']}':
            
            {segment['content']}
            
            Return your answer in JSON format with these fields:
            {{
              "segment_id": "{segment['topic']}",
              "word_count": (number of words),
              "sentence_count": (number of sentences),
              "avg_word_length": (average length of words as a float)
            }}
            """
            
            # Count tokens in the prompt
            prompt_tokens = count_tokens(stats_prompt)
            input_tokens += prompt_tokens
            print(f"Stats prompt for '{segment['topic']}': {prompt_tokens} tokens")
            
            stats_response = client.chat(
                model='mistral:latest',
                messages=[{'role': 'user', 'content': stats_prompt}]
            )
            
            # Try to extract JSON from the response
            response_content = stats_response.message.content
            
            # Count tokens in the response
            response_tokens = count_tokens(response_content)
            output_tokens += response_tokens
            print(f"Stats response for '{segment['topic']}': {response_tokens} tokens")
            
            print(f"Raw stats response for segment '{segment['topic']}':")
            print(response_content[:100] + "..." if len(response_content) > 100 else response_content)
            
            # Use the improved JSON extraction function
            segment_stats = extract_json(response_content)
            if segment_stats:
                stats.append(segment_stats)
                print(f"✅ Statistics calculated for segment '{segment['topic']}'")
            else:
                # Create basic stats as fallback
                word_count = len(segment['content'].split())
                sentence_count = len(re.split(r'[.!?]+', segment['content']))
                stats.append({
                    "segment_id": segment['topic'],
                    "word_count": word_count,
                    "sentence_count": sentence_count,
                    "avg_word_length": 5.0  # default fallback
                })
                print(f"⚠️ Basic statistics calculated for segment '{segment['topic']}' (fallback)")
                
        except Exception as e:
            print(f"❌ Error calculating stats for segment '{segment['topic']}': {str(e)}")
            # Create basic stats as fallback
            word_count = len(segment['content'].split())
            sentence_count = len(re.split(r'[.!?]+', segment['content']))
            stats.append({
                "segment_id": segment['topic'],
                "word_count": word_count,
                "sentence_count": sentence_count,
                "avg_word_length": 5.0  # default fallback
            })
    
    # Step 3: Generate summary
    print("\nStep 3: Generating summary...")
    try:
        # Prepare segments and stats for the summary prompt
        segments_str = "\n".join([f"- {s['topic']}: {s['content'][:50]}..." for s in segments])
        stats_str = "\n".join([f"- {s['segment_id']}: {s['word_count']} words, {s['sentence_count']} sentences" for s in stats])
        
        summary_prompt = f"""
        Generate a concise summary of this transcript based on these segments and statistics:
        
        Segments:
        {segments_str}
        
        Statistics:
        {stats_str}
        
        Return your answer in JSON format with a "summary" field:
        {{
          "summary": "(your summary here)"
        }}
        """
        
        # Count tokens in the prompt
        prompt_tokens = count_tokens(summary_prompt)
        input_tokens += prompt_tokens
        print(f"Summary prompt: {prompt_tokens} tokens")
        
        summary_response = client.chat(
            model='mistral:latest',
            messages=[{'role': 'user', 'content': summary_prompt}]
        )
        
        # Try to extract JSON from the response
        response_content = summary_response.message.content
        
        # Count tokens in the response
        response_tokens = count_tokens(response_content)
        output_tokens += response_tokens
        print(f"Summary response: {response_tokens} tokens")
        
        print("Raw summary response:")
        print(response_content[:100] + "..." if len(response_content) > 100 else response_content)
        
        # Use the improved JSON extraction function
        summary_data = extract_json(response_content)
        if summary_data and 'summary' in summary_data:
            summary = summary_data['summary']
        else:
            # Just use the raw text if we can't parse JSON
            summary = response_content
            if len(summary) > 500:
                summary = summary[:500] + "..."
                
        print(f"✅ Summary generated: {summary[:100]}...")
        
    except Exception as e:
        print(f"❌ Error generating summary: {str(e)}")
        summary = "Error generating summary."
    
    # Create final result
    result = TranscriptAnalysisResult(
        segments=[TranscriptSegment(**s) for s in segments],
        stats=[SegmentStats(**s) for s in stats],
        summary=summary
    )
    
    print("\n===== ANALYSIS RESULTS =====")
    print(f"Segments: {len(result.segments)}")
    print(f"Stats: {len(result.stats)} entries")
    print(f"Summary: {result.summary[:100]}...")
    
    print("\nAccessing structured data:")
    for i, segment in enumerate(result.segments):
        matching_stats = next((s for s in result.stats if s.segment_id == segment.topic), None)
        if matching_stats:
            print(f"Segment {i+1}: '{segment.topic}' - {matching_stats.word_count} words, {matching_stats.sentence_count} sentences")
        else:
            print(f"Segment {i+1}: '{segment.topic}' - No stats available")
    
    print("\n===== TOKEN USAGE =====")
    print(f"Total input tokens: {input_tokens}")
    print(f"Total output tokens: {output_tokens}")
    print(f"Total tokens: {input_tokens + output_tokens}")
    
    print("\n✅ Transcript analysis test completed!")
    return result

if __name__ == "__main__":
    asyncio.run(run_transcript_analysis())