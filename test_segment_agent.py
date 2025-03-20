# test_segment_agent.py
import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from typing import List
from models.transcript_analysis_models import TranscriptSegment

# Define a simplified segment agent
test_agent = Agent(
            OpenAIModel(
        model_name='mistral:7b-instruct', # or whatever model you have in Ollama
        provider=OpenAIProvider(base_url='http://localhost:11434/v1')
    ),  # Or replace with your local model
    result_type=List[TranscriptSegment],
    system_prompt='''
    Divide a YouTube transcript into logical segments by topic.
    Return a list of segments with "content" and "topic" fields.
    '''
)

async def test_segmentation():
    # Short sample transcript
    sample_transcript = """
    Hello and welcome to this video on Python programming. Today we'll cover the basics.
    First, let's talk about variables. Variables are containers for storing data values.
    Next, we'll look at control flow. If statements and loops are important for controlling program flow.
    """
    
    try:
        result = await test_agent.run(f"Segment this transcript into topics:\n\n{sample_transcript}")
        print("Success! Segments:")
        for i, segment in enumerate(result.data):
            print(f"Segment {i+1}:")
            print(f"  Topic: {segment.topic}")
            print(f"  Content: {segment.content[:50]}...")
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    asyncio.run(test_segmentation())