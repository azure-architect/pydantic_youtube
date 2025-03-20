from pydantic import BaseModel, Field
from typing import List, Dict, Optional, Any, Union

class ProcessStep(BaseModel):
    description: str
    order: int
    transcript_reference: str = ""

class MarketingKeyword(BaseModel):
    keyword: str
    relevance_score: float = 1.0
    context: str = ""
    frequency: int = 1

class BusinessProcessModel(BaseModel):
    name: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    steps: List[ProcessStep] = []
    transcript_references: List[str] = []

class TechnicalProcessModel(BaseModel):
    name: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    steps: List[ProcessStep] = []
    transcript_references: List[str] = []

class TechnologyModel(BaseModel):
    name: str
    category: str
    description: str
    inference_type: str  # "DIRECT" or "INFERRED"
    confidence_score: float = 1.0
    transcript_references: List[str] = []

class TranscriptAnalysisReport(BaseModel):
    video_title: str
    video_id: str
    marketing_keywords: List[MarketingKeyword] = []
    business_processes: List[BusinessProcessModel] = []
    technical_processes: List[TechnicalProcessModel] = []
    technologies: List[TechnologyModel] = []
    summary: str = ""

class TranscriptSegment(BaseModel):
    topic: str
    content: str

class SegmentStats(BaseModel):
    segment_id: str
    word_count: int
    sentence_count: int
    avg_word_length: float = 0.0
    
class TopicList(BaseModel):
    sections: List[str]

class TranscriptAnalysisResult(BaseModel):
    segments: List[TranscriptSegment]
    stats: List[SegmentStats]
    summary: str

# Models for function calling
class KeywordList(BaseModel):
    keywords: List[str]

class BusinessProcessStep(BaseModel):
    description: str
    order: int
    
class BusinessProcessExtraction(BaseModel):
    name: str
    description: str
    steps: List[BusinessProcessStep]
    inference_type: str
    transcript_references: List[str]
    
class BusinessProcessList(BaseModel):
    processes: List[BusinessProcessExtraction]

class TechnologyExtraction(BaseModel):
    name: str
    category: str
    description: str
    inference_type: str
    transcript_references: List[str]
    
class TechnologyList(BaseModel):
    technologies: List[TechnologyExtraction]

class SummaryGeneration(BaseModel):
    summary: str