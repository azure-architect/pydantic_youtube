from pydantic_ai import Agent
from typing import List
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Use relative imports
from models.transcript_analysis_models import (
    TranscriptSegment, MarketingKeyword, BusinessProcessModel,
    TechnicalProcessModel, TechnologyModel, TranscriptAnalysisReport
)
from state.transcript_analysis_state import AnalysisResources

# Rest of the file remains the same
# Rest of the file remains the same

# Create specialized agents
segment_agent = Agent(
    'anthropic:claude-3-5-sonnet-latest',
    result_type=List[TranscriptSegment],
    system_prompt='Divide a YouTube transcript into logical segments by topic.'
)

keyword_agent = Agent(
    'openai:gpt-4o',
    deps_type=AnalysisResources,
    result_type=List[MarketingKeyword],
    system_prompt='''
    Extract marketing keywords from a transcript segment.
    Focus on terms that would be valuable for SEO, advertising, or target audience identification.
    Include only significant marketing terms with clear relevance.
    '''
)

business_process_agent = Agent(
    'anthropic:claude-3-5-sonnet-latest',
    result_type=List[BusinessProcessModel],
    system_prompt='''
    Identify business processes described in the transcript.
    For each process:
    1. Provide a clear name and description
    2. List all steps in the process in order
    3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
    4. Include verbatim transcript references that evidence this process
    
    Only include processes with strong evidence. Maintain high precision over recall.
    '''
)

tech_process_agent = Agent(
    'openai:gpt-4o',
    result_type=List[TechnicalProcessModel],
    system_prompt='''
    Identify technical processes described in the transcript.
    For each process:
    1. Provide a clear name and description
    2. List all steps in the process in order
    3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
    4. Include verbatim transcript references that evidence this process
    
    Only include processes with strong evidence. Maintain high precision over recall.
    '''
)

technology_agent = Agent(
    'anthropic:claude-3-5-sonnet-latest',
    deps_type=AnalysisResources,
    result_type=List[TechnologyModel],
    system_prompt='''
    Extract all technologies mentioned in the transcript.
    For each technology:
    1. Provide the exact name as mentioned
    2. Categorize it (e.g., "database", "programming language", "cloud service")
    3. Provide a brief description
    4. Specify if the technology is directly mentioned (DIRECT) or inferred from context (INFERRED)
    5. Include verbatim transcript references
    
    Be comprehensive but precise - only include technologies with clear evidence.
    '''
)

summary_agent = Agent(
    'openai:gpt-4o',
    result_type=TranscriptAnalysisReport,
    system_prompt='Create a comprehensive analysis report from the extracted information about a YouTube transcript.'
)