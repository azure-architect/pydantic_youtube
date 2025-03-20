# test_ollama_graph.py
import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
from pydantic_graph import BaseNode, End, Graph, GraphRunContext
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Define models
class TextSegment(BaseModel):
    topic: str
    content: str

class SegmentStats(BaseModel):
    word_count: int
    sentence_count: int

class AnalysisResult(BaseModel):
    segments: List[TextSegment]
    stats: Dict[str, SegmentStats]
    summary: str

# Define state
@dataclass
class AnalysisState:
    text: str
    segments: List[Dict[str, Any]] = field(default_factory=list)
    stats: Dict[str, Dict[str, int]] = field(default_factory=dict)
    summary: str = ""

# Set up Ollama provider
ollama_provider = OpenAIProvider(base_url='http://localhost:11434/v1')

# Create agents
segment_agent = Agent(
    OpenAIModel(model_name='mistral:latest-32', provider=ollama_provider),
    result_type=List[TextSegment],
    system_prompt="Divide text into logical segments."
)

stats_agent = Agent(
    OpenAIModel(model_name='mistral:latest-32', provider=ollama_provider),
    result_type=SegmentStats,
    system_prompt="Calculate statistics about text."
)

summary_agent = Agent(
    OpenAIModel(model_name='mistral:latest-32', provider=ollama_provider),
    result_type=str,
    system_prompt="Write a concise summary of the given text."
)

# Define graph nodes
@dataclass
class SegmentText(BaseNode[AnalysisState]):
    """Segment the text into logical parts"""
    
    async def run(self, ctx: GraphRunContext[AnalysisState]) -> "CalculateStats":
        print("Running SegmentText node...")
        try:
            result = await segment_agent.run(
                f"Segment this text into logical parts:\n\n{ctx.state.text}",
                model_settings={"temperature": 0.1}
            )
            
            # Store segments
            ctx.state.segments = [segment.model_dump() for segment in result.data]
            print(f"Created {len(ctx.state.segments)} segments")
            
        except Exception as e:
            print(f"Error in segmentation: {e}")
            # Create a fallback segment
            ctx.state.segments = [{
                "topic": "Full Text",
                "content": ctx.state.text
            }]
            
        return CalculateStats()

@dataclass
class CalculateStats(BaseNode[AnalysisState]):
    """Calculate statistics for each segment"""
    
    async def run(self, ctx: GraphRunContext[AnalysisState]) -> "GenerateSummary":
        print("Running CalculateStats node...")
        
        for segment in ctx.state.segments:
            topic = segment["topic"]
            content = segment["content"]
            
            try:
                prompt = f"Calculate stats for this text:\n\n{content}"
                result = await stats_agent.run(prompt)
                
                # Store stats
                ctx.state.stats[topic] = result.data.model_dump()
                
            except Exception as e:
                print(f"Error calculating stats for segment '{topic}': {e}")
                # Create fallback stats
                ctx.state.stats[topic] = {
                    "word_count": len(content.split()),
                    "sentence_count": content.count('.') + content.count('!') + content.count('?')
                }
                
        return GenerateSummary()

@dataclass
class GenerateSummary(BaseNode[AnalysisState, None, AnalysisResult]):
    """Generate a summary of all segments"""
    
    async def run(self, ctx: GraphRunContext[AnalysisState]) -> End[AnalysisResult]:
        print("Running GenerateSummary node...")
        
        segments_text = "\n\n".join([
            f"SEGMENT: {segment['topic']}\n{segment['content']}"
            for segment in ctx.state.segments
        ])
        
        try:
            prompt = f"Summarize the following text segments:\n\n{segments_text}"
            result = await summary_agent.run(prompt)
            
            # Store summary
            ctx.state.summary = result.data
            
        except Exception as e:
            print(f"Error generating summary: {e}")
            ctx.state.summary = "Summary generation failed."
            
        # Create final result
        final_result = AnalysisResult(
            segments=[TextSegment(**segment) for segment in ctx.state.segments],
            stats={topic: SegmentStats(**stats) for topic, stats in ctx.state.stats.items()},
            summary=ctx.state.summary
        )
        
        return End(final_result)

# Create graph
analysis_graph = Graph(
    nodes=[SegmentText, CalculateStats, GenerateSummary]
)

async def test_ollama_graph():
    """Test the graph-based workflow with Ollama"""
    test_text = """
    Python is a high-level programming language known for its readability and simplicity.
    It was created by Guido van Rossum and released in 1991. Python supports multiple
    programming paradigms including procedural, object-oriented, and functional programming.
    
    One of Python's key strengths is its extensive standard library and rich ecosystem of
    third-party packages. These make it suitable for a wide range of applications from web
    development to data science and machine learning.
    
    However, Python can be slower than compiled languages for certain operations. Despite
    this limitation, its productivity benefits often outweigh performance concerns for many
    use cases.
    """
    
    state = AnalysisState(text=test_text)
    
    try:
        print("Running graph workflow...")
        result = await analysis_graph.run(SegmentText(), state=state)
        
        print("\n✅ Graph execution successful!")
        
        # Access the final data
        final_data = result.output
        print(f"\nSegments: {len(final_data.segments)}")
        print(f"Stats: {len(final_data.stats)} entries")
        print(f"Summary: {final_data.summary[:100]}...")
        
        # Demonstrate data access
        print("\nAccessing structured data:")
        for i, segment in enumerate(final_data.segments):
            stats = final_data.stats.get(segment.topic, None)
            if stats:
                print(f"Segment {i+1}: '{segment.topic}' - {stats.word_count} words, {stats.sentence_count} sentences")
                
        return True
        
    except Exception as e:
        print(f"❌ Graph execution error: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_ollama_graph())
    print(f"\nGraph test {'passed' if success else 'failed'}!")