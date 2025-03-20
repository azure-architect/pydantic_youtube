from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
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
            OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),  # Or your local model like 'ollama:llama3'
    result_type=List[TranscriptSegment],
    system_prompt='''
    Divide a YouTube transcript into logical segments by topic.
    
    IMPORTANT: Your response must be a valid list of JSON objects, with each object having:
    - "content": the transcript text for this segment
    - "topic": a short title describing the topic of this segment
    - Optional "start_time_approx": approximate timestamp if available
    
    Example response format:
    [
      {
        "content": "Welcome to this tutorial...",
        "topic": "Introduction",
        "start_time_approx": "0:00"
      },
      {
        "content": "First, let's download the necessary packages...",
        "topic": "Setup",
        "start_time_approx": "1:30"
      }
    ]
    ''',
    retries=3  # Increase retries
)

keyword_agent = Agent(
        OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),
    deps_type=AnalysisResources,
    result_type=List[MarketingKeyword],
    system_prompt='''
    Extract marketing keywords from a transcript segment.
    Focus on terms that would be valuable for SEO, advertising, or target audience identification.
    Include only significant marketing terms with clear relevance.
    '''
)

business_process_agent = Agent(
        OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),
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
        OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),
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
        OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),
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
        OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),
    result_type=TranscriptAnalysisReport,
    system_prompt='Create a comprehensive analysis report from the extracted information about a YouTube transcript.'
)