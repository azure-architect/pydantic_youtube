# tests/test_function_calling.py
import pytest
import json
from unittest.mock import patch, MagicMock

from ollama_toolkit.function_calling import call_with_function, create_function_schema
from models.transcript_analysis_models import TopicList, TranscriptSegment

def test_create_function_schema():
    """Test schema creation from Pydantic models"""
    schema = create_function_schema(
        TopicList, 
        "identify_topics", 
        "Identify main topics in a transcript"
    )
    
    assert schema["type"] == "function"
    assert schema["function"]["name"] == "identify_topics"
    assert "parameters" in schema["function"]
    assert "properties" in schema["function"]["parameters"]
    assert "sections" in schema["function"]["parameters"]["properties"]

def test_call_with_function_success(patch_ollama_chat, mock_ollama_response):
    """Test successful function calling with proper response"""
    # Configure mock
    patch_ollama_chat.return_value = mock_ollama_response
    
    # Patch the chat function at the correct path where it's imported in your module
    with patch('ollama_toolkit.function_calling.chat', patch_ollama_chat):
        result = call_with_function(
            prompt="Identify topics in this text",
            model_class=TopicList,
            function_name="identify_topics",
            description="Identify topics",
            model="test-model"
        )
    
    assert result["success"] is True
    assert len(result["data"].sections) == 3
    assert result["data"].sections[0] == "Introduction"
    assert "response_time" in result

# tests/test_function_calling.py
# For test_call_with_function_invalid_json function

def test_call_with_function_invalid_json(patch_ollama_chat):
    """Test function calling with invalid JSON response"""
    # Configure mock to return invalid JSON
    patch_ollama_chat.return_value = {
        "message": {
            "content": 'Invalid JSON response'
        }
    }
    
    # Properly patch the ollama.chat module where it's imported
    with patch('ollama_toolkit.function_calling.chat', patch_ollama_chat):
        result = call_with_function(
            prompt="Identify topics in this text",
            model_class=TopicList,
            function_name="identify_topics",
            description="Identify topics",
            model="test-model"
        )
    
    assert result["success"] is False
    assert "error" in result
    assert "Invalid JSON" in result["error"] or "JSON" in result["error"]

# tests/test_function_calling.py
# For test_call_with_function_error_handling function

def test_call_with_function_error_handling(patch_ollama_chat):
    """Test error handling during function calling"""
    # Configure mock to raise an exception
    patch_ollama_chat.side_effect = Exception("Connection error")
    
    # Properly patch the ollama.chat module where it's imported
    with patch('ollama_toolkit.function_calling.chat', patch_ollama_chat):
        result = call_with_function(
            prompt="Identify topics in this text",
            model_class=TopicList,
            function_name="identify_topics",
            description="Identify topics",
            model="test-model"
        )
    
    assert result["success"] is False
    assert "error" in result
    assert "Connection error" in result["error"] or "Error in Ollama request" in result["error"]