# tests/test_extraction.py
import pytest
from unittest.mock import patch, MagicMock
import json

from ollama_toolkit.function_calling import call_with_function
from models.transcript_analysis_models import (
    KeywordList, BusinessProcessList, TechnologyList,
    BusinessProcessExtraction, ProcessStep, TechnologyExtraction
)

@patch('ollama_toolkit.function_calling.chat')
def test_keyword_extraction(mock_chat, sample_transcript):
    """Test keyword extraction with function calling"""
    # Mock the chat response
    mock_chat.return_value = {
        "message": {
            "content": json.dumps({
                "keywords": ["Python", "programming", "tutorial", "syntax", "readability", 
                             "data structures", "lists", "dictionaries", "functions"]
            })
        }
    }
    
    result = call_with_function(
        prompt=f"Extract keywords from: {sample_transcript}",
        model_class=KeywordList,
        function_name="extract_keywords",
        description="Extract keywords from transcript",
        model="test-model"
    )
    
    assert result["success"] is True
    assert len(result["data"].keywords) >= 5
    assert "Python" in result["data"].keywords
    assert "programming" in result["data"].keywords

@patch('ollama_toolkit.function_calling.chat')
def test_business_process_extraction(mock_chat, sample_transcript):
    """Test business process extraction with function calling"""
    # Create a sample business process
    sample_process = {
        "processes": [
            {
                "name": "Learning Python",
                "description": "Process of learning Python programming",
                "inference_type": "DIRECT",
                "transcript_references": ["First, we'll cover basic syntax."],
                "steps": [
                    {"description": "Learn basic syntax", "order": 1},
                    {"description": "Study data structures", "order": 2},
                    {"description": "Learn functions", "order": 3}
                ]
            }
        ]
    }
    
    # Mock the chat response
    mock_chat.return_value = {
        "message": {
            "content": json.dumps(sample_process)
        }
    }
    
    result = call_with_function(
        prompt=f"Extract business processes from: {sample_transcript}",
        model_class=BusinessProcessList,
        function_name="extract_business_processes",
        description="Extract business processes from transcript",
        model="test-model"
    )
    
    assert result["success"] is True
    assert len(result["data"].processes) == 1
    assert result["data"].processes[0].name == "Learning Python"
    assert len(result["data"].processes[0].steps) == 3
    assert result["data"].processes[0].steps[0].description == "Learn basic syntax"

@patch('ollama_toolkit.function_calling.chat')
def test_technology_extraction(mock_chat, sample_transcript):
    """Test technology extraction with function calling"""
    # Create a sample technology list
    sample_tech = {
        "technologies": [
            {
                "name": "Python",
                "category": "Programming Language",
                "description": "A high-level programming language known for readability",
                "inference_type": "DIRECT",
                "transcript_references": ["Python is known for its readability."]
            },
            {
                "name": "Lists",
                "category": "Data Structure",
                "description": "A built-in data structure in Python",
                "inference_type": "DIRECT",
                "transcript_references": ["data structures like lists and dictionaries"]
            }
        ]
    }
    
    # Mock the chat response
    mock_chat.return_value = {
        "message": {
            "content": json.dumps(sample_tech)
        }
    }
    
    result = call_with_function(
        prompt=f"Extract technologies from: {sample_transcript}",
        model_class=TechnologyList,
        function_name="extract_technologies",
        description="Extract technologies from transcript",
        model="test-model"
    )
    
    assert result["success"] is True
    assert len(result["data"].technologies) == 2
    assert result["data"].technologies[0].name == "Python"
    assert result["data"].technologies[0].category == "Programming Language"
    assert "readability" in result["data"].technologies[0].description