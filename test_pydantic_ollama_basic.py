# test_pydantic_ollama.py
import asyncio
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from typing import List
from models.transcript_analysis_models import TranscriptSegment

async def test_segment_agent():
    # Set up the Ollama provider
    ollama_provider = OpenAIProvider(base_url='http://localhost:11434/v1')
    
    # Create a test agent using the same configuration as your main app
    test_agent = Agent(
        OpenAIModel(
            model_name='mistral:latest-32',  # Or your preferred model
            provider=ollama_provider
        ),
        result_type=List[TranscriptSegment],
        system_prompt='''
        Divide a transcript into logical segments by topic.
        IMPORTANT: Return a list of JSON objects with "content" and "topic" fields.
        '''
    )
    
    # Test with a short transcript
    sample_transcript = """
    Hello and welcome to this video on Python programming. Today we'll cover the basics.
    First, let's talk about variables. Variables are containers for storing data values.
    Next, we'll look at control flow. If statements and loops are important for controlling program flow.
    """
    
    try:
        print("Sending request to model...")
        result = await test_agent.run(
            f"Segment this transcript into topics:\n\n{sample_transcript}",
            model_settings={"temperature": 0.1}
        )
        
        print("Success! Got segments:")
        for i, segment in enumerate(result.data):
            print(f"Segment {i+1}:")
            print(f"  Topic: {segment.topic}")
            print(f"  Content: {segment.content[:50]}...")
        
        # Also print the raw response to help with debugging
        print("\nFull response data structure:")
        print(result.data)
        
    except Exception as e:
        print(f"Error: {e}")
        print(f"Error type: {type(e)}")

if __name__ == "__main__":
    asyncio.run(test_segment_agent())