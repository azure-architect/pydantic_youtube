# test_ollama_toolkit.py
import logging
import json
from ollama_toolkit.tools.text_segmentation import segment_transcript

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    print("Testing Ollama Toolkit segmentation...")
    
    # Load sample transcript
    try:
        with open('yt_analysis_xVe87QpNE80_1742436881.json', 'r') as f:
            data = json.load(f)
            transcript_text = data[0]['state']['transcript']
    except Exception as e:
        print(f"Error loading transcript: {e}")
        transcript_text = """
        Hello and welcome to this video. Today we'll cover the basics
        of Python programming. Let's start with variables and data types.
        
        Next, we'll look at control structures like loops and conditionals.
        Finally, we'll discuss functions and how to organize your code.
        """
    
    print(f"Segmenting transcript ({len(transcript_text.split())} words)...")
    
    # Call the segmentation function
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
        print(f"Total words in segments: {segment_words}")
        print(f"Average segment length: {segment_words/len(segments):.1f} words")
        
        # Print segment details
        for i, segment in enumerate(segments, 1):
            print(f"\nSegment {i}: {segment.topic}")
            print(f"Word count: {len(segment.content.split())}")
            print(f"Content preview: {segment.content[:100]}...")
        
        # Save results to file for inspection
        output_file = 'ollama_toolkit_segmentation_results.json'
        with open(output_file, 'w') as f:
            json.dump(
                {
                    "success": True,
                    "segments": [{"topic": segment.topic, "content": segment.content} for segment in segments],
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
        print(f"\nResults saved to {output_file}")
    else:
        print("\n===== SEGMENTATION FAILED =====")
        print(f"Error: {result.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()