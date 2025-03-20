# test_ollama_pydantic_db.py
import asyncio
import sqlite3
import json
from pydantic import BaseModel, Field
from typing import List, Dict
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

# Set up database
def setup_database():
    """Set up SQLite database for testing"""
    conn = sqlite3.connect('test_analysis.db')
    c = conn.cursor()
    
    # Create tables
    c.execute('''
    CREATE TABLE IF NOT EXISTS segments (
        id INTEGER PRIMARY KEY,
        analysis_id TEXT,
        topic TEXT,
        content TEXT
    )
    ''')
    
    c.execute('''
    CREATE TABLE IF NOT EXISTS analysis (
        id TEXT PRIMARY KEY,
        text TEXT,
        summary TEXT,
        stats TEXT
    )
    ''')
    
    conn.commit()
    return conn

# Define models
class TextSegment(BaseModel):
    topic: str = Field(description="Topic of the segment")
    content: str = Field(description="Content of the segment")

class AnalysisResult(BaseModel):
    segments: List[TextSegment]
    summary: str

async def test_ollama_pydantic_db():
    """Test Ollama + PydanticAI with database storage"""
    # Setup database
    conn = setup_database()
    c = conn.cursor()
    
    # Create a unique ID for this analysis
    import uuid
    analysis_id = str(uuid.uuid4())
    
    # Set up Ollama provider and agent
    ollama_provider = OpenAIProvider(base_url='http://localhost:11434/v1')
    
    agent = Agent(
        OpenAIModel(model_name='mistral:latest-32', provider=ollama_provider),
        result_type=AnalysisResult,
        system_prompt="""
        Analyze the provided text and return:
        1. A list of segments with topic and content
        2. A concise summary of the entire text
        
        Format as a JSON object with 'segments' (array) and 'summary' (string) fields.
        """
    )
    
    test_text = """
    SQLite is a C library that provides a lightweight disk-based database.
    It doesn't require a separate server process and allows accessing the database
    using a nonstandard variant of the SQL query language. It's a popular choice
    for local/client storage in application software such as web browsers.
    
    SQLite uses dynamic typing, so the datatype can be specified for each value.
    It also supports the concept of ROWID, which is a unique integer key for each row.
    """
    
    try:
        print("Running analysis with Ollama...")
        result = await agent.run(
            f"Analyze this text:\n\n{test_text}",
            model_settings={"temperature": 0.1}
        )
        
        # Store the analysis
        c.execute(
            "INSERT INTO analysis VALUES (?, ?, ?, ?)",
            (
                analysis_id,
                test_text,
                result.data.summary,
                json.dumps({"segments_count": len(result.data.segments)})
            )
        )
        
        # Store each segment
        for segment in result.data.segments:
            c.execute(
                "INSERT INTO segments (analysis_id, topic, content) VALUES (?, ?, ?)",
                (
                    analysis_id,
                    segment.topic,
                    segment.content
                )
            )
        
        conn.commit()
        
        # Verify storage
        print("\n✅ Database storage successful!")
        print("\nVerifying storage:")
        
        c.execute("SELECT id, summary FROM analysis WHERE id = ?", (analysis_id,))
        analysis_row = c.fetchone()
        print(f"Analysis ID: {analysis_row[0]}")
        print(f"Summary: {analysis_row[1][:100]}...")
        
        c.execute("SELECT topic, content FROM segments WHERE analysis_id = ?", (analysis_id,))
        segments = c.fetchall()
        print(f"\nStored {len(segments)} segments:")
        for i, (topic, content) in enumerate(segments, 1):
            print(f"Segment {i}: '{topic}' - {len(content)} characters")
            
        # Clean up
        conn.close()
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"Error type: {type(e)}")
        
        # Clean up
        conn.close()
        return False

if __name__ == "__main__":
    success = asyncio.run(test_ollama_pydantic_db())
    print(f"\nDatabase test {'passed' if success else 'failed'}!")