from pydantic import BaseModel
from typing import List, Dict, Optional

class TranscriptSegment(BaseModel):
    topic: str
    content: str

class SegmentStats(BaseModel):
    segment_id: str
    word_count: int
    sentence_count: int
    avg_word_length: float = 0.0
    
class TranscriptAnalysisResult(BaseModel):
    segments: List[TranscriptSegment]
    stats: List[SegmentStats]
    summary: str