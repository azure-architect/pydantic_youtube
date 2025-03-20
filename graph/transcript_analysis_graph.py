from pydantic_graph import Graph
import sys
import os
# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from state.transcript_analysis_state import TranscriptAnalysisState, AnalysisResources
from graph.transcript_analysis_nodes import (
    SegmentTranscript, ExtractKeywords, ExtractBusinessProcesses,
    ExtractTechnicalProcesses, ExtractTechnologies, CreateFinalReport
)

# Define the transcript analysis graph
transcript_analysis_graph = Graph(
    nodes=[
        SegmentTranscript,
        ExtractKeywords,
        ExtractBusinessProcesses,
        ExtractTechnicalProcesses,
        ExtractTechnologies,
        CreateFinalReport
    ]
)