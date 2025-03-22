# tests/test_graph_workflow.py

from pydantic_graph import End
import pytest
from unittest.mock import patch, MagicMock, AsyncMock
import json
import asyncio

from graph.transcript_analysis_graph import transcript_analysis_graph
from graph.transcript_analysis_nodes import (
    SegmentTranscript, ExtractKeywords, ExtractBusinessProcesses,
    ExtractTechnicalProcesses, ExtractTechnologies, CreateFinalReport
)
from state.transcript_analysis_state import TranscriptAnalysisState, AnalysisResources
@pytest.fixture
def mock_resources():
    """Create mock analysis resources"""
    return AnalysisResources(
        http_client=MagicMock(),
        api_key="test-key",
        model="test-model"
    )

@pytest.fixture
def mock_state(sample_transcript):
    """Create a mock state for the graph"""
    return TranscriptAnalysisState(
        transcript=sample_transcript,
        video_title="Test Video",
        video_id="test123"
    )

# tests/test_graph_workflow.py
# For test_full_graph_workflow function

@pytest.mark.asyncio
async def test_full_graph_workflow(mock_state, mock_resources):
    """Test the full graph workflow with mocked components"""
    # Mock all the node 'run' methods to isolate the graph flow
    with patch('graph.transcript_analysis_nodes.SegmentTranscript.run', new_callable=AsyncMock) as mock_segment, \
         patch('graph.transcript_analysis_nodes.ExtractKeywords.run', new_callable=AsyncMock) as mock_keywords, \
         patch('graph.transcript_analysis_nodes.ExtractBusinessProcesses.run', new_callable=AsyncMock) as mock_business, \
         patch('graph.transcript_analysis_nodes.ExtractTechnicalProcesses.run', new_callable=AsyncMock) as mock_technical, \
         patch('graph.transcript_analysis_nodes.ExtractTechnologies.run', new_callable=AsyncMock) as mock_technologies, \
         patch('graph.transcript_analysis_nodes.CreateFinalReport.run', new_callable=AsyncMock) as mock_report:
        
        # Configure mocks to return actual node instances, not strings
        mock_segment.return_value = ExtractKeywords()
        mock_keywords.return_value = ExtractBusinessProcesses()
        mock_business.return_value = ExtractTechnicalProcesses()
        mock_technical.return_value = ExtractTechnologies()
        mock_technologies.return_value = CreateFinalReport()
        
        # For the final node, return End object, not a MagicMock
        from models.transcript_analysis_models import TranscriptAnalysisReport
        mock_report.return_value = End(
            TranscriptAnalysisReport(
                video_title="Test Video",
                video_id="test123",
                summary="Test summary"
            )
        )
        
        # Run the graph
        result = await transcript_analysis_graph.run(
            SegmentTranscript(),
            state=mock_state,
            deps=mock_resources
        )
        
        # Verify the final result
        assert result.output.video_title == "Test Video"
        assert result.output.video_id == "test123"
        assert result.output.summary == "Test summary"

@pytest.mark.asyncio
async def test_realistic_graph_workflow(mock_state, mock_resources):
    """Test realistic graph workflow with some real components and some mocks"""
    # Create patch for function calls to return predetermined data
    with patch('ollama_toolkit.function_calling.call_with_function') as mock_call:
        # Configure mock to return different values for different function calls
        def side_effect(*args, **kwargs):
            function_name = kwargs.get('function_name', '')
            
            if 'identify_transcript_topics' in function_name:
                return {
                    "success": True,
                    "data": MagicMock(sections=["Introduction", "Main Content"])
                }
            elif 'extract_transcript_segment' in function_name:
                return {
                    "success": True,
                    "data": MagicMock(
                        topic="Test Topic", 
                        content="Test Content",
                        model_dump=lambda: {"topic": "Test Topic", "content": "Test Content"}
                    )
                }
            elif 'extract_marketing_keywords' in function_name:
                return {
                    "success": True,
                    "data": MagicMock(keywords=["test", "keyword"])
                }
            # Add more conditions for other function calls
            
            return {"success": False, "error": "Unexpected function call"}
            
        mock_call.side_effect = side_effect
        
        # Run the actual graph with real nodes but mocked function calls
        result = await transcript_analysis_graph.run(
            SegmentTranscript(),
            state=mock_state,
            deps=mock_resources
        )
        
        # Verify the graph ran successfully
        assert result is not None
        assert hasattr(result, 'output')
        # Further assertions would depend on the graph output