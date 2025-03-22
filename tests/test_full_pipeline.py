# tests/test_full_pipeline.py
import pytest
import os
import asyncio
import json
from unittest.mock import patch, MagicMock

from graph.transcript_analysis_graph import transcript_analysis_graph
from graph.transcript_analysis_nodes import SegmentTranscript
from state.transcript_analysis_state import TranscriptAnalysisState, AnalysisResources
from models.transcript_analysis_models import TranscriptAnalysisReport
from fixtures.sample_transcripts import SHORT_TRANSCRIPT, MEDIUM_TRANSCRIPT

class TestFullPipeline:
    """Test the full transcript analysis pipeline"""
    
    @pytest.mark.asyncio
    @patch('ollama_toolkit.function_calling.chat')
    async def test_short_transcript_pipeline(self, mock_chat, mock_resources):
        """Test the full pipeline with a short transcript"""
        from mocks.ollama_responses import get_mock_response
        
        # Configure mock to return different responses based on function name
        def side_effect(*args, **kwargs):
            messages = args[1] if len(args) > 1 else kwargs.get('messages', [])
            tools = args[2] if len(args) > 2 else kwargs.get('tools', [])
            
            # Determine the function being called
            function_name = None
            if tools and len(tools) > 0 and 'function' in tools[0]:
                function_name = tools[0]['function'].get('name', '')
            
            return get_mock_response(function_name)
            
        mock_chat.side_effect = side_effect
        
        # Create state with short transcript
        state = TranscriptAnalysisState(
            transcript=SHORT_TRANSCRIPT,
            video_title="Python Tutorial",
            video_id="python123"
        )
        
        # Run the graph
        result = await transcript_analysis_graph.run(
            SegmentTranscript(),
            state=state,
            deps=mock_resources
        )
        
        # Save the output to a file for inspection
        os.makedirs('test_outputs', exist_ok=True)
        with open('test_outputs/short_transcript_result.json', 'w') as f:
            # Convert Pydantic model to dict for JSON serialization
            if hasattr(result.output, 'model_dump'):
                output_dict = result.output.model_dump()
            else:
                output_dict = result.output.dict()
            json.dump(output_dict, f, indent=2)
        
        # Verify the results
        assert result.output.video_title == "Python Tutorial"
        assert result.output.video_id == "python123"
        assert len(result.output.marketing_keywords) > 0
        assert len(result.output.business_processes) > 0
        assert len(result.output.technologies) > 0
        assert len(result.output.summary) > 0
    
    @pytest.mark.asyncio
    @patch('ollama_toolkit.function_calling.chat')
    async def test_error_handling(self, mock_chat, mock_resources):
        """Test error handling in the pipeline"""
        from mocks.ollama_responses import get_mock_response, ERROR_RESPONSE, EXCEPTION_RESPONSE
        
        # Configure mock to fail at different stages
        call_count = 0
        def side_effect(*args, **kwargs):
            nonlocal call_count
            call_count += 1
            
            # Fail at the segmentation step
            if call_count == 1:
                return ERROR_RESPONSE
            
            # Throw exception at the keyword extraction step
            if call_count == 2:
                raise EXCEPTION_RESPONSE
            
            # Return normal responses for other calls
            messages = args[1] if len(args) > 1 else kwargs.get('messages', [])
            tools = args[2] if len(args) > 2 else kwargs.get('tools', [])
            
            # Determine the function being called
            function_name = None
            if tools and len(tools) > 0 and 'function' in tools[0]:
                function_name = tools[0]['function'].get('name', '')
            
            return get_mock_response(function_name)
            
        mock_chat.side_effect = side_effect
        
        # Create state with short transcript
        state = TranscriptAnalysisState(
            transcript=SHORT_TRANSCRIPT,
            video_title="Error Test",
            video_id="error123"
        )
        
        # Run the graph - should complete despite errors due to fallbacks
        result = await transcript_analysis_graph.run(
            SegmentTranscript(),
            state=state,
            deps=mock_resources
        )
        
        # Save the output to a file for inspection
        os.makedirs('test_outputs', exist_ok=True)
        with open('test_outputs/error_handling_result.json', 'w') as f:
            # Convert Pydantic model to dict for JSON serialization
            if hasattr(result.output, 'model_dump'):
                output_dict = result.output.model_dump()
            else:
                output_dict = result.output.dict()
            json.dump(output_dict, f, indent=2)
        
        # Verify the graph completed and produced a report despite errors
        assert result.output.video_title == "Error Test"
        assert result.output.video_id == "error123"
        # Fallbacks should have been used
        assert "error" in state.function_call_errors