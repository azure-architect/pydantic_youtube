from typing import Optional
import os
import re

def load_transcript_from_file(filepath: str) -> str:
    """Load a transcript from a text file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def clean_transcript(transcript: str) -> str:
    """Clean a transcript by removing timestamps and unnecessary characters"""
    # Remove [00:00:00] style timestamps
    cleaned = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', transcript)
    
    # Remove multiple newlines
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)
    
    return cleaned.strip()

def get_youtube_video_id(url: str) -> Optional[str]:
    """Extract YouTube video ID from URL"""
    pattern = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None