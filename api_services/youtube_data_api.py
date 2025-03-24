# youtube_data_api.py
import os
import logging
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from datetime import datetime  # Import datetime for proper date handling

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def get_youtube_video_data(video_id):
    """
    Retrieve comprehensive YouTube video and channel data.

    Args:
        video_id (str): YouTube video ID

    Returns:
        dict: Detailed video and channel information, or None on error.
    """
    try:
        # Get API key from environment variable
        api_key = os.getenv('YT_DATA_API_KEY')
        if not api_key:
            logger.error("YouTube Data API key not found in environment variables")
            return None

        # Build YouTube service
        youtube = build('youtube', 'v3', developerKey=api_key)

        # Retrieve video details
        video_response = youtube.videos().list(
            part='snippet,contentDetails,statistics,topicDetails',  # Include topicDetails
            id=video_id
        ).execute()

        if not video_response['items']:
            logger.warning(f"No video found with ID: {video_id}")
            return None

        video = video_response['items'][0]  # Get the first item (the video)
        video_snippet = video['snippet']
        video_statistics = video.get('statistics', {})
        video_topic_details = video.get('topicDetails', {}) # Get topic details

        # Retrieve channel details
        channel_response = youtube.channels().list(
            part='snippet,statistics',
            id=video_snippet['channelId']
        ).execute()

        if not channel_response['items']:  # Handle channel not found
            logger.warning(f"Channel not found for video ID: {video_id}")
            channel_data = { # Return N/A for channel details.
                "id": video_snippet['channelId'],
                "title": video_snippet['channelTitle'],
                "description": "N/A",
                "subscriberCount": "N/A"
            }
        else:
            channel_snippet = channel_response['items'][0]['snippet']
            channel_statistics = channel_response['items'][0].get('statistics', {})

            channel_data = {
                "id": video_snippet['channelId'],
                "title": video_snippet['channelTitle'],
                "description": channel_snippet.get('description', 'N/A'),  # Use .get()
                "subscriberCount": int(channel_statistics.get('subscriberCount', 0)) if channel_statistics.get('subscriberCount') else 'N/A' # Handle potential None and convert to int
            }
        
        # Format publishedAt date using datetime
        try:
            published_at = datetime.strptime(video_snippet['publishedAt'], '%Y-%m-%dT%H:%M:%SZ').isoformat()
        except (ValueError, TypeError):
            published_at = 'N/A'

        return {
            "video": {
                "id": video_id,
                "title": video_snippet['title'],
                "description": video_snippet.get('description', 'N/A'),  # Use get for safety
                "publishedAt": published_at,  # Use the formatted date
                "views": int(video_statistics.get('viewCount', 0)) if video_statistics.get('viewCount') else 'N/A',  # Handle None and convert to int
                "likes": int(video_statistics.get('likeCount', 0)) if video_statistics.get('likeCount') else 'N/A', # Handle None and convert to int
                "tags": video_snippet.get('tags', []),
                "topicDetails": video_topic_details, # Include topic details
                "thumbnail": video_snippet['thumbnails']['standard']['url'] if 'standard' in video_snippet.get('thumbnails',{}) else 'N/A', # Check if standard exists
            },
            "channel": channel_data
        }

    except HttpError as e:
        logger.error(f"HTTP error occurred: {e.status_code} - {e.error_details}")  # More specific error
        return None
    except Exception as e:
        logger.exception(f"Error retrieving YouTube video data: {e}")  # Log stack trace
        return None