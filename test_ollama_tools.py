# test_ollama_tools.py
import asyncio
from pydantic import BaseModel, Field
from typing import List, Optional
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

class SegmentInfo(BaseModel):
    topic: str
    word_count: int

async def test_ollama_tools():
    """Test Ollama with PydanticAI function tools"""
    ollama_provider = OpenAIProvider(base_url='http://localhost:11434/v1')
    
    agent = Agent(
        OpenAIModel(
            model_name='mistral:latest-32',  # Change to your preferred model
            provider=ollama_provider
        ),
        system_prompt="""
        You are an expert at analyzing text.
        Use the provided tools to extract information from the text.
        """
    )
    
    @agent.tool_plain
    def create_segment(content: str, topic: str) -> dict:
        """Create a new text segment with the given content and topic"""
        print(f"Tool called: create_segment with topic '{topic}'")
        word_count = len(content.split())
        return {
            "topic": topic,
            "content": content,
            "word_count": word_count
        }
    
    @agent.tool_plain
    def analyze_sentiment(text: str) -> str:
        """Analyze the sentiment of the given text (positive, negative, neutral)"""
        print(f"Tool called: analyze_sentiment for text length {len(text)}")
        # In a real implementation, this would use a sentiment analysis library
        return "This is a placeholder sentiment analysis result."
    
    test_text = """
    Python is a great programming language for beginners. It has a simple syntax
    that's easy to learn. However, it can sometimes be slower than compiled languages
    for certain tasks. Overall, most developers enjoy working with Python.
    """
    
    try:
        print("Sending request to Ollama with tools...")
        result = await agent.run(
            f"Analyze this text and create segments for each main point. Also analyze the sentiment:\n\n{test_text}",
            model_settings={"temperature": 0.1}
        )
        
        print(f"\n✅ Result: {result.data}")
        
        # Check tool call history
        print("\nTool call history:")
        messages = result.all_messages()
        tool_calls_found = False
        
        for msg in messages:
            if hasattr(msg, 'parts'):
                for part in msg.parts:
                    if hasattr(part, 'tool_name') and part.tool_name:
                        tool_calls_found = True
                        print(f"- Tool called: {part.tool_name}")
                        if hasattr(part, 'args') and part.args:
                            print(f"  Arguments: {part.args}")
        
        return tool_calls_found
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e)}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_ollama_tools())
    print(f"\nTool calling test {'passed' if success else 'failed'}!")