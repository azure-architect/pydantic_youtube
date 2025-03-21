# state/transcript_analysis_state.py
import json
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Set
from datetime import datetime
from enum import Enum
import httpx

class InferenceType(str, Enum):
    DIRECT = "direct"
    INFERRED = "inferred"
    
    @classmethod
    def _missing_(cls, value):
        # Handle case insensitivity
        if isinstance(value, str):
            for member in cls:
                if member.value.lower() == value.lower():
                    return member
        return None

@dataclass
class BusinessProcess:
    """Representation of a business process mentioned in the transcript"""
    name: str
    description: str
    steps: List[str]
    inference_type: InferenceType
    transcript_references: List[str]  # Snippets from transcript that reference this process

@dataclass
class TechnicalProcess:
    """Representation of a technical process mentioned in the transcript"""
    name: str
    description: str
    steps: List[str]
    inference_type: InferenceType
    transcript_references: List[str]

@dataclass
class Technology:
    """Technology mentioned in the transcript"""
    name: str
    category: str
    description: str
    inference_type: InferenceType
    transcript_references: List[str]

@dataclass
class TranscriptAnalysisState:
    """State for the transcript analysis workflow graph"""
    transcript: str
    video_title: str
    video_id: str
    segments: List[Dict[str, str]] = field(default_factory=list)  # Segmented transcript
    marketing_keywords: Set[str] = field(default_factory=set)
    business_processes: List[BusinessProcess] = field(default_factory=list)
    technical_processes: List[TechnicalProcess] = field(default_factory=list)
    technologies: List[Technology] = field(default_factory=list)
    start_time: datetime = field(default_factory=datetime.now)
    
    # Message histories for agents
    segmentation_agent_messages: List = field(default_factory=list)
    keyword_agent_messages: List = field(default_factory=list)
    business_process_agent_messages: List = field(default_factory=list)
    tech_process_agent_messages: List = field(default_factory=list)
    technology_agent_messages: List = field(default_factory=list)

@dataclass
class AnalysisResources:
    """Container for API clients and resources needed for transcript analysis"""
    http_client: httpx.AsyncClient
    api_key: str
    model: str = "mistral:latest-32"  # Default model to use
    tech_taxonomy: Optional[dict] = None  # Optional reference data for technology classification
    marketing_keywords_db: Optional[List[str]] = None  # Optional reference marketing keywords