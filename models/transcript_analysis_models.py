# Updated transcript_analysis_models.py
from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any, Union

class ProcessStep(BaseModel):
    """Model for a step in a process"""
    description: str
    order: int
    transcript_reference: str = ""

class MarketingKeyword(BaseModel):
    """Model for a marketing keyword extracted from transcript"""
    keyword: str
    relevance_score: float = 1.0
    context: str = ""
    frequency: int = 1

class BusinessProcessModel(BaseModel):
    """Model for a business process identified in transcript"""
    name: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    steps: List[ProcessStep] = []
    transcript_references: List[str] = []

class TechnicalProcessModel(BaseModel):
    """Model for a technical process identified in transcript"""
    name: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    steps: List[ProcessStep] = []
    transcript_references: List[str] = []

class TechnologyModel(BaseModel):
    """Model for a technology mentioned in transcript"""
    name: str
    category: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    transcript_references: List[str] = []

class TranscriptAnalysisReport(BaseModel):
    """Complete analysis report model"""
    video_title: str
    video_id: str
    marketing_keywords: List[MarketingKeyword] = []
    business_processes: List[BusinessProcessModel] = []
    technical_processes: List[TechnicalProcessModel] = []
    technologies: List[TechnologyModel] = []
    summary: str = ""

class TranscriptSegment(BaseModel):
    """Model for a segment of the transcript"""
    topic: str
    content: str
    start_time_approx: Optional[str] = None  # Optional timestamp

class SegmentStats(BaseModel):
    """Statistics about transcript segmentation"""
    total_segments: Dict[str, int] = Field(default_factory=lambda: {"value": 0})
    total_transcript_words: Dict[str, int] = Field(default_factory=lambda: {"value": 0})
    total_segment_words: Dict[str, int] = Field(default_factory=lambda: {"value": 0})
    coverage_percentage: Dict[str, float] = Field(default_factory=lambda: {"value": 0.0})
    processing_time_seconds: Dict[str, float] = Field(default_factory=lambda: {"value": 0.0})
    
class TopicList(BaseModel):
    """List of topics for segmentation first step"""
    sections: List[str]

class TranscriptAnalysisResult(BaseModel):
    """Complete analysis result including segments and stats"""
    segments: List[TranscriptSegment]
    stats: List[SegmentStats]
    summary: str

# Models specifically for function calling with Ollama
class KeywordList(BaseModel):
    """Model for extracting a list of keywords"""
    keywords: List[str]

class BusinessProcessStep(BaseModel):
    """Step in a business process for function calling"""
    description: str
    order: int
    
class BusinessProcessExtraction(BaseModel):
    """Business process extraction model for function calling"""
    name: str
    description: str
    steps: List[BusinessProcessStep]
    inference_type: str
    transcript_references: List[str]
    
class BusinessProcessList(BaseModel):
    """List of business processes for function calling"""
    processes: List[BusinessProcessExtraction]

class TechnologyExtraction(BaseModel):
    """Technology extraction model for function calling"""
    name: str
    category: str
    description: str
    inference_type: str
    transcript_references: List[str]
    
class TechnologyList(BaseModel):
    """List of technologies for function calling"""
    technologies: List[TechnologyExtraction]

class SummaryGeneration(BaseModel):
    """Summary generation model for function calling"""
    summary: str

class TechnicalProcessStep(BaseModel):
    """Step in a technical process for function calling"""
    description: str
    order: int
    
class TechnicalProcessExtraction(BaseModel):
    """Technical process extraction model for function calling"""
    name: str
    description: str
    steps: List[TechnicalProcessStep]
    inference_type: str
    transcript_references: List[str]
    
class TechnicalProcessList(BaseModel):
    """List of technical processes for function calling"""
    processes: List[TechnicalProcessExtraction]