import sys
import json
from api_services.transcript_service import get_video_transcript_data

def main():
    # Check if URL is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL as an argument")
        print("Usage: python main.py 'https://www.youtube.com/watch?v=example'")
        sys.exit(1)
    
    # Get YouTube URL from command-line argument
    youtube_url = sys.argv[1]
    
    # Fetch transcript
    transcript_data = get_video_transcript_data(youtube_url)
    
    if transcript_data:
        # Pretty print the transcript as JSON
        print(json.dumps(transcript_data, indent=2))

if __name__ == "__main__":
    main()