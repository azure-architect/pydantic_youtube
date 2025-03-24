# transcript_service.py
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled


def get_video_transcript_data(url):
    """
    Fetch comprehensive transcript data for a given YouTube video URL.

    Args:
        url (str): YouTube video URL

    Returns:
        dict: Transcript data including video ID and transcript details, or None on error.
    """
    try:
        # Extract video ID using pytube
        yt = YouTube(url)
        video_id = yt.video_id

        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Try to get available transcripts
        try:
            available_transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            transcript_info = {
                "video_id": video_id,
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
        except (NoTranscriptFound, TranscriptsDisabled):
            # Handle cases where no transcript is found or transcripts are disabled
            return {
                "video_id": video_id,
                "transcript": transcript,  # Still return the fetched transcript
                "available_transcripts": [] # Empty list if no other transcripts
            }
        except Exception as info_error:
             print(f"Error fetching transcript info: {info_error}")
             return {
                "video_id": video_id,
                "transcript": transcript  # still return main transcript
            }


    except RegexMatchError:
        print(f"Invalid YouTube URL: {url}")
        return None
    except VideoUnavailable:
        print(f"Video unavailable: {url}")
        return None
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None