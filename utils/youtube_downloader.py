from typing import Optional, List, Dict
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import re

def extract_youtube_id(url: str) -> Optional[str]:
    """Extract YouTube video ID from various URL formats"""
    # Handle escaped characters
    cleaned_url = url.replace('\\?', '?').replace('\\=', '=')
    
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([\w-]{11})',
        r'youtube\.com\/watch\?.*v=([\w-]{11})'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, cleaned_url)
        if match:
            return match.group(1)
    
    return None

def fetch_transcript(video_id: str, languages=['en']) -> Optional[str]:
    """Fetch transcript from YouTube video ID"""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Try to get transcript in specified languages
        for lang in languages:
            try:
                transcript = transcript_list.find_transcript([lang])
                data = transcript.fetch()
                formatter = TextFormatter()
                return formatter.format_transcript(data)
            except:
                continue
                
        # If no specified language found, get the default one
        transcript = transcript_list.find_generated_transcript(languages)
        data = transcript.fetch()
        formatter = TextFormatter()
        return formatter.format_transcript(data)
        
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def fetch_video_info(video_id: str) -> Dict:
    """
    Fetch video title and other metadata
    Note: This is a simplified version using just the transcript API capabilities
    For more complete data you might want to use youtube-dl or the YouTube Data API
    """
    try:
        # This is a workaround as youtube_transcript_api doesn't directly provide video title
        # In a full implementation, you might want to use the YouTube Data API instead
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        
        # Get available info
        return {
            "video_id": video_id,
            "title": f"YouTube Video {video_id}",  # Placeholder
            "languages": [t.language for t in transcript_list._transcripts.values()]
        }
    except Exception as e:
        print(f"Error fetching video info: {e}")
        return {"video_id": video_id, "title": f"YouTube Video {video_id}"}

def fetch_transcript_from_url(url: str, languages=['en']) -> Dict:
    """Fetch transcript and video info from a YouTube URL"""
    video_id = extract_youtube_id(url)
    if not video_id:
        return {"success": False, "error": "Could not extract video ID from URL"}
    
    transcript = fetch_transcript(video_id, languages)
    if not transcript:
        return {"success": False, "error": "Could not fetch transcript"}
    
    video_info = fetch_video_info(video_id)
    
    return {
        "success": True,
        "video_id": video_id,
        "title": video_info.get("title"),
        "transcript": transcript
    }