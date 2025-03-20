from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from ollama import chat
import logging
import json
import os
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class TranscriptSegment(BaseModel):
    topic: str
    content: str

class TopicList(BaseModel):
    sections: List[str]

def segment_transcript(transcript_text: str, model: str = "mistral:latest-32") -> Dict[str, Any]:
    """Segment a transcript with enforced JSON formatting"""
    print(f"Segmenting transcript ({len(transcript_text.split())} words)...")
    
    # Step 1: Identify main topics
    topics_prompt = f"""Read this YouTube transcript and identify 5-7 main sections.
    Transcript: {transcript_text}"""
    
    try:
        # Use format parameter to enforce JSON structure
        start_time = time.time()
        topics_response = chat(
            model=model,
            messages=[{"role": "user", "content": topics_prompt}],
            format=TopicList.model_json_schema(),
            options={"num_ctx": 32768}
        )
        end_time = time.time()
        
        logging.info(f"Topics extraction took {end_time - start_time:.2f} seconds")
        
        topics_data = TopicList.model_validate_json(topics_response['message']['content'])
        sections = topics_data.sections
        print(f"✅ Identified {len(sections)} topics: {', '.join(sections)}")
        
    except Exception as e:
        print(f"❌ Failed to identify topics: {str(e)}")
        return {"success": False, "error": str(e)}
    
    # Step 2: Extract content for each section
    all_segments = []
    
    for section in sections:
        print(f"Extracting content for '{section}'...")
        
        extraction_prompt = f"""Extract the exact text from this transcript for the section: '{section}'
        Transcript: {transcript_text}"""
        
        try:
            start_time = time.time()
            segment_response = chat(
                model=model,
                messages=[{"role": "user", "content": extraction_prompt}],
                format=TranscriptSegment.model_json_schema(),
                options={"num_ctx": 32768}
            )
            end_time = time.time()
            
            logging.info(f"Content extraction for '{section}' took {end_time - start_time:.2f} seconds")
            
            segment = TranscriptSegment.model_validate_json(segment_response['message']['content'])
            print(f"  ✅ Extracted {len(segment.content.split())} words")
            all_segments.append(segment)
            
        except Exception as e:
            print(f"  ❌ Failed: {str(e)}")
    
    # Return results
    if all_segments:
        print(f"✅ Extracted {len(all_segments)}/{len(sections)} segments")
        return {"success": True, "segments": all_segments}
    else:
        return {"success": False, "error": "No segments extracted"}

def test_model_connectivity(model: str = "mistral:latest-32"):
    """Test basic connectivity with the model"""
    print(f"Testing connectivity with {model}...")
    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": "Respond with a simple 'Hello World'"}]
        )
        print(f"✅ Model responded: {response['message']['content'][:50]}...")
        return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

def test_json_formatting(model: str = "mistral:latest-32"):
    """Test if model correctly formats JSON responses"""
    print(f"Testing JSON formatting with {model}...")
    
    class TestResponse(BaseModel):
        message: str
        count: int
    
    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": "Return a simple JSON with a message and count"}],
            format=TestResponse.model_json_schema()
        )
        
        result = TestResponse.model_validate_json(response['message']['content'])
        print(f"✅ Model returned valid JSON: {result}")
        return True
    except Exception as e:
        print(f"❌ JSON formatting failed: {str(e)}")
        return False

def load_transcript(file_path: str) -> Optional[str]:
    """Load transcript from the specific JSON structure in your file"""
    try:
        if not os.path.exists(file_path):
            print(f"❌ Transcript file not found: {file_path}")
            return None
            
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        # Your JSON is a list with one dictionary item that contains a nested structure
        if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
            # Check if it has the state key
            if 'state' in data[0] and isinstance(data[0]['state'], dict):
                state = data[0]['state']
                if 'transcript' in state and isinstance(state['transcript'], str):
                    transcript_text = state['transcript']
                    print(f"Successfully loaded transcript ({len(transcript_text)} characters, {len(transcript_text.split())} words)")
                    return transcript_text
        
        print("❌ Could not locate transcript in the JSON structure")
        return None
        
    except Exception as e:
        print(f"❌ Failed to load transcript: {str(e)}")
        return None

def main():
    print("Starting YouTube transcript analysis test...")
    
    # Test model connectivity first
    if not test_model_connectivity():
        print("Exiting due to model connectivity issues")
        return
        
    # Test JSON formatting 
    if not test_json_formatting():
        print("⚠️ JSON formatting test failed, but continuing anyway")
    
    # Load transcript from file
    file_path = 'yt_analysis_xVe87QpNE80_1742436881.json'  # Replace with your file path
    transcript_text = load_transcript(file_path)
    
    if not transcript_text:
        return
    
    # Call the segment_transcript function
    result = segment_transcript(transcript_text)
    
    # Process and display results
    if result.get('success'):
        segments = result.get('segments', [])
        print("\n===== SEGMENTATION RESULTS =====")
        print(f"Successfully segmented transcript into {len(segments)} segments.")
        
        # Calculate coverage metrics
        total_words = len(transcript_text.split())
        segment_words = sum(len(segment.content.split()) for segment in segments)
        coverage = (segment_words / total_words) * 100
        
        print(f"Transcript coverage: {coverage:.2f}% ({segment_words}/{total_words} words)")
        if coverage < 90:
            print("⚠️ Incomplete transcript coverage")
        else:
            print("✅ Good transcript coverage")
            
        print(f"Total words in segments: {segment_words}")
        print(f"Average segment length: {segment_words/len(segments):.1f} words")
        
        # Save results to file for inspection
        output_file = 'segmentation_results.json'
        with open(output_file, 'w') as f:
            json.dump(
                {
                    "success": True,
                    "segments": [segment.model_dump() for segment in segments],
                    "metrics": {
                        "total_words": total_words,
                        "segment_words": segment_words,
                        "coverage": coverage,
                        "avg_segment_length": segment_words/len(segments)
                    }
                }, 
                f, 
                indent=2
            )
        print(f"Results saved to {output_file}")
    else:
        print("\n===== SEGMENTATION FAILED =====")
        print(f"Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()