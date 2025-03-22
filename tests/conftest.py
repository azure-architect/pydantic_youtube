# tests/conftest.py
import pytest
import sys
import os
import json
from unittest.mock import patch

# Add the project root to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.transcript_analysis_models import (
    TopicList, TranscriptSegment, KeywordList,
    BusinessProcessList, TechnologyList
)

@pytest.fixture
def sample_transcript():
    """Sample transcript for testing"""
    return """
    Hello and welcome to this tutorial. Today we'll discuss Python programming.
    First, we'll cover basic syntax. Python is known for its readability.
    Next, we'll look at data structures like lists and dictionaries.
    Finally, we'll discuss functions and how to organize your code.
    """

@pytest.fixture
def sample_topics():
    """Sample topics for testing"""
    return TopicList(sections=["Introduction", "Basic Syntax", "Data Structures", "Functions"])

@pytest.fixture
def sample_segments():
    """Sample transcript segments for testing"""
    return [
        TranscriptSegment(topic="Introduction", content="Hello and welcome to this tutorial. Today we'll discuss Python programming."),
        TranscriptSegment(topic="Basic Syntax", content="First, we'll cover basic syntax. Python is known for its readability."),
        TranscriptSegment(topic="Data Structures", content="Next, we'll look at data structures like lists and dictionaries."),
        TranscriptSegment(topic="Functions", content="Finally, we'll discuss functions and how to organize your code.")
    ]

@pytest.fixture
def mock_ollama_response():
    """Mock a successful Ollama response"""
    return {
        "message": {
            "content": json.dumps({
                "sections": ["Introduction", "Main Content", "Conclusion"]
            })
        }
    }

@pytest.fixture
def patch_ollama_chat():
    """Patch the ollama.chat function for testing"""
    with patch('ollama.chat') as mock_chat:
        yield mock_chat