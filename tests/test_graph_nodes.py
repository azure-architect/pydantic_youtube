# tests/test_graph_nodes.py
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
import json
import asyncio

from graph.transcript_analysis_nodes import (
    SegmentTranscript, ExtractKeywords, ExtractBusinessProcesses,
    ExtractTechnicalProcesses, ExtractTechnologies, CreateFinalReport
)
from state.transcript_analysis_state import TranscriptAnalysisState, AnalysisResources
from pydantic_graph import GraphRunContext

# Helper to create a mock context for testing
@pytest.fixture
def mock_context(sample_transcript):
    """Create a mock GraphRunContext for testing nodes"""
    # Create a state with sample transcript
    state = TranscriptAnalysisState(
        transcript=sample_transcript,
        video_title="Test Video",
        video_id="test123"
    )
    
    # Create mock resources
    deps = AnalysisResources(
        http_client=MagicMock(),
        api_key="test-key",
        model="test-model"
    )
    
    # Create a mock GraphRunContext
    ctx = MagicMock(spec=GraphRunContext)
    ctx.state = state
    ctx.deps = deps
    
    return ctx

@pytest.mark.asyncio
async def test_segment_transcript_node(mock_context):
    """Test the SegmentTranscript node"""
    node = SegmentTranscript()
    
    # Mock the segmentation function
    with patch('ollama_toolkit.tools.text_segmentation.segment_transcript') as mock_segment:
        mock_segment.return_value = {
            "success": True,
            "segments": [
                MagicMock(topic="Topic 1", content="Content 1", model_dump=lambda: {"topic": "Topic 1", "content": "Content 1"}),
                MagicMock(topic="Topic 2", content="Content 2", model_dump=lambda: {"topic": "Topic 2", "content": "Content 2"})
            ]
        }
        
        result = await node.run(mock_context)
        
        # Verify the node ran successfully
        assert result.__class__.__name__ == "ExtractKeywords"
        assert len(mock_context.state.segments) == 2
        assert mock_context.state.segments[0]["topic"] == "Topic 1"
        assert mock_context.state.function_call_successes["segment_transcript"] is True

@pytest.mark.asyncio
async def test_segment_transcript_node_fallback(mock_context):
    """Test the SegmentTranscript node with fallback"""
    node = SegmentTranscript()
    
    # Mock the segmentation function to fail
    with patch('ollama_toolkit.tools.text_segmentation.segment_transcript') as mock_segment:
        mock_segment.return_value = {
            "success": False,
            "error": "Segmentation failed"
        }
        
        # Mock the _fallback_segmentation method
        with patch.object(node, '_fallback_segmentation') as mock_fallback:
            mock_fallback.return_value = [
                {"topic": "Fallback Topic", "content": "Fallback Content"}
            ]
            
            result = await node.run(mock_context)
            
            # Verify the node used fallback and continued
            assert result.__class__.__name__ == "ExtractKeywords"
            assert len(mock_context.state.segments) == 1
            assert mock_context.state.segments[0]["topic"] == "Fallback Topic"
            assert mock_context.state.function_call_successes["segment_transcript"] is False
            assert "Segmentation failed" in mock_context.state.function_call_errors["segment_transcript"]

@pytest.mark.asyncio
async def test_extract_keywords_node(mock_context):
    """Test the ExtractKeywords node"""
    # Set up state with segments
    mock_context.state.segments = [
        {"topic": "Topic 1", "content": "Content about Python and programming"},
        {"topic": "Topic 2", "content": "More content about data science"}
    ]
    
    node = ExtractKeywords()
    
    # Mock the function calling
    with patch('ollama_toolkit.function_calling.call_with_function') as mock_call:
        mock_call.return_value = {
            "success": True,
            "data": MagicMock(keywords=["Python", "programming", "data science"])
        }
        
        result = await node.run(mock_context)
        
        # Verify the node ran successfully
        assert result.__class__.__name__ == "ExtractBusinessProcesses"
        assert len(mock_context.state.marketing_keywords) == 3
        assert "Python" in mock_context.state.marketing_keywords
        assert mock_context.state.function_call_successes["extract_keywords"] is True

# Similar tests for other nodes would follow the same pattern