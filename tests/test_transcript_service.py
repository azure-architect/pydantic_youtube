import os
import sys
import pytest
from unittest.mock import patch
from api_services.transcript_service import get_video_transcript_data

# Mocking classes more closely aligned with actual library behaviors
class MockYouTube:
    def __init__(self, url):
        self.video_id = url.split('v=')[1].split('&')[0] if 'v=' in url else 'test_video_id'

class MockTranscriptApi:
    @staticmethod
    def get_transcript(video_id):
        return [
            {
                "text": "Hello world",
                "start": 0.0,
                "duration": 5.0
            },
            {
                "text": "This is a test transcript",
                "start": 5.0,
                "duration": 3.0
            }
        ]
    
    @staticmethod
    def list_transcripts(video_id):
        class MockTranscriptList:
            def __init__(self):
                self.transcripts = [
                    type('MockTranscript', (), {
                        'language_code': 'en',
                        'language': 'English',
                        'is_generated': False,
                        'is_translatable': True
                    })()
                ]
            
            def __iter__(self):
                return iter(self.transcripts)
        
        return MockTranscriptList()

def test_successful_transcript_retrieval():
    test_url = "https://www.youtube.com/watch?v=test_video_id"
    
    with (
        patch('pytube.YouTube', side_effect=MockYouTube),
        patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript', 
              side_effect=MockTranscriptApi.get_transcript),
        patch('youtube_transcript_api.YouTubeTranscriptApi.list_transcripts', 
              side_effect=MockTranscriptApi.list_transcripts)
    ):
        result = get_video_transcript_data(test_url)
        
        # Assertions
        assert result is not None
        assert "transcript" in result
        assert "available_transcripts" in result
        
        # Verify transcript details
        assert len(result["transcript"]) == 2
        assert result["transcript"][0]["text"] == "Hello world"
        assert result["transcript"][0]["start"] == 0.0
        
        # Verify available transcripts
        assert len(result["available_transcripts"]) == 1
        assert result["available_transcripts"][0]["language_code"] == "en"

def test_transcript_retrieval_failure():
    test_url = "https://www.youtube.com/watch?v=invalid_video"
    
    with (
        patch('pytube.YouTube', side_effect=Exception("Invalid YouTube URL")),
    ):
        result = get_video_transcript_data(test_url)
        
        # Verify failure scenario
        assert result is None

def test_no_additional_transcripts():
    test_url = "https://www.youtube.com/watch?v=test_video_id"
    
    with (
        patch('pytube.YouTube', side_effect=MockYouTube),
        patch('youtube_transcript_api.YouTubeTranscriptApi.get_transcript', 
              side_effect=MockTranscriptApi.get_transcript),
        patch('youtube_transcript_api.YouTubeTranscriptApi.list_transcripts', 
              side_effect=Exception("No additional transcripts"))
    ):
        result = get_video_transcript_data(test_url)
        
        # Verify fallback behavior
        assert result is not None
        assert "transcript" in result
        assert "available_transcripts" not in result