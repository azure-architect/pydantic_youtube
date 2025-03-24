# main.py
import sys
import json
from api_services.transcript_service import get_video_transcript_data
from api_services.youtube_data_api import get_youtube_video_data  # Correct import

def main():
    # Check if URL is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Please provide a YouTube URL as an argument")
        print("Usage: python main.py 'https://www.youtube.com/watch?v=example'")
        sys.exit(1)

    # Get YouTube URL from command-line argument
    youtube_url = sys.argv[1]

    # Fetch transcript data
    transcript_data = get_video_transcript_data(youtube_url)

    if transcript_data:
        # Extract video ID from transcript data
        video_id = transcript_data['video_id']

        # Fetch YouTube video and channel data using the video ID
        video_info = get_youtube_video_data(video_id)

        # Add video info to the transcript data object
        if video_info:
            transcript_data['video_info'] = video_info

        # Pretty print the combined data as JSON
        print(json.dumps(transcript_data, indent=2))
    else:  # Handle cases where transcript data is None
        print("Could not retrieve transcript data.")

if __name__ == "__main__":
    main()