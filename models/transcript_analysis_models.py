from pydantic import BaseModel, Field
from typing import List, Dict, Literal, Optional
from enum import Enum

class TranscriptSegment(BaseModel):
    """A logical segment of the transcript"""
    content: str
    topic: str
    start_time_approx: Optional[str] = None

class MarketingKeyword(BaseModel):
    """A marketing keyword with context"""
    keyword: str
    relevance_score: float = Field(ge=0.0, le=1.0)
    context: str
    frequency: int

class ProcessStep(BaseModel):
    """A step in a business or technical process"""
    description: str
    order: int
    transcript_reference: str

class BusinessProcessModel(BaseModel):
    """A business process extracted from the transcript"""
    name: str
    description: str
    inference_type: Literal["direct", "inferred"]
    confidence_score: float = Field(ge=0.0, le=1.0)
    steps: List[ProcessStep]
    transcript_references: List[str]

class TechnicalProcessModel(BaseModel):
    """A technical process extracted from the transcript"""
    name: str 
    description: str
    inference_type: Literal["direct", "inferred"]
    confidence_score: float = Field(ge=0.0, le=1.0)
    steps: List[ProcessStep]
    transcript_references: List[str]

class TechnologyModel(BaseModel):
    """A technology mentioned in the transcript"""
    name: str
    category: str
    description: str
    inference_type: Literal["direct", "inferred"]
    confidence_score: float = Field(ge=0.0, le=1.0)
    transcript_references: List[str]

class TranscriptAnalysisReport(BaseModel):
    """Complete analysis report of a YouTube transcript"""
    video_title: str
    video_id: str
    marketing_keywords: List[MarketingKeyword]
    business_processes: List[BusinessProcessModel]
    technical_processes: List[TechnicalProcessModel]
    technologies: List[TechnologyModel]
    summary: str