from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript_data(url):
    """
    Fetch comprehensive transcript data for a given YouTube video URL.
    
    Args:
        url (str): YouTube video URL
    
    Returns:
        dict: Transcript data including transcript and available transcripts
    """
    try:
        # Extract video ID
        yt = YouTube(url)
        video_id = yt.video_id
        
        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Try to get available transcripts
        try:
            available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript_info = {
                "transcript": transcript,
                "available_transcripts": [
                    {
                        "language_code": t.language_code,
                        "language_name": t.language,
                        "is_generated": t.is_generated,
                        "is_translatable": t.is_translatable
                    } for t in available_transcripts
                ]
            }
            return transcript_info
        except Exception as info_error:
            return {"transcript": transcript}
    
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None