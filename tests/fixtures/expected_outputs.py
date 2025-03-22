# tests/fixtures/expected_outputs.py
"""
Expected outputs for various test cases
"""
from models.transcript_analysis_models import (
    TranscriptSegment, MarketingKeyword, BusinessProcessModel,
    TechnicalProcessModel, TechnologyModel, ProcessStep
)

# Expected segments for the short transcript
SHORT_TRANSCRIPT_SEGMENTS = [
    TranscriptSegment(
        topic="Introduction",
        content="Hello and welcome to this tutorial on Python programming. Today we'll be covering the basics of Python syntax and how to get started."
    ),
    TranscriptSegment(
        topic="Variables",
        content="First, let's talk about variables. In Python, you don't need to declare variable types."
    ),
    TranscriptSegment(
        topic="Control Structures",
        content="Next, we'll look at control structures like if statements and loops."
    ),
    TranscriptSegment(
        topic="Functions",
        content="Finally, we'll discuss functions and how to create them in Python."
    )
]

# Expected keywords for the short transcript
SHORT_TRANSCRIPT_KEYWORDS = [
    "Python programming",
    "Python syntax",
    "variables",
    "control structures",
    "if statements",
    "loops",
    "functions"
]

# Expected business processes for the short transcript
SHORT_TRANSCRIPT_PROCESSES = [
    BusinessProcessModel(
        name="Learning Python Programming",
        description="Process of learning Python programming fundamentals",
        inference_type="INFERRED",
        confidence_score=0.9,
        steps=[
            ProcessStep(description="Learn Python variables", order=1, transcript_reference="First, let's talk about variables."),
            ProcessStep(description="Understand control structures", order=2, transcript_reference="Next, we'll look at control structures"),
            ProcessStep(description="Learn Python functions", order=3, transcript_reference="Finally, we'll discuss functions")
        ],
        transcript_references=["Hello and welcome to this tutorial on Python programming."]
    )
]

# Expected technologies for the short transcript
SHORT_TRANSCRIPT_TECHNOLOGIES = [
    TechnologyModel(
        name="Python",
        category="Programming Language",
        description="A high-level programming language known for its readability and versatility",
        inference_type="DIRECT",
        confidence_score=1.0,
        transcript_references=["Hello and welcome to this tutorial on Python programming."]
    )
]

# Add more expected outputs for other test cases as needed