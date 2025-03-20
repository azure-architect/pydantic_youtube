from dataclasses import dataclass
from pydantic_graph import BaseNode, End, GraphRunContext, Edge
from pydantic_ai import RunContext
from pydantic_ai.format_as_xml import format_as_xml
from typing import Annotated, Union

import sys
import os
# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.transcript_analysis_models import (
    TranscriptAnalysisReport, ProcessStep, MarketingKeyword,
    BusinessProcessModel, TechnicalProcessModel, TechnologyModel
)
from state.transcript_analysis_state import (
    TranscriptAnalysisState, AnalysisResources, BusinessProcess,
    TechnicalProcess, Technology, InferenceType
)
from agents.transcript_analysis_agents import (
    segment_agent, keyword_agent, business_process_agent,
    tech_process_agent, technology_agent, summary_agent
)

# Important: Define all node classes with string literals for return types
@dataclass
class SegmentTranscript(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Segment the transcript into logical parts by topic"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractKeywords":  # Use string literal here
        prompt = f"""
        Segment this YouTube video transcript into logical parts by topic.
        Video title: {ctx.state.video_title}
        
        TRANSCRIPT:
        {ctx.state.transcript}
        """
        
        result = await segment_agent.run(
            prompt,
            message_history=ctx.state.segmentation_agent_messages
        )
        ctx.state.segmentation_agent_messages += result.all_messages()
        ctx.state.segments = [segment.dict() for segment in result.data]
        
        return ExtractKeywords()

@dataclass
class ExtractKeywords(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract marketing keywords from each segment"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractBusinessProcesses":  # Use string literal here
        all_keywords = []
        
        for i, segment in enumerate(ctx.state.segments):
            prompt = f"""
            Extract marketing keywords from this transcript segment.
            Video title: {ctx.state.video_title}
            Segment topic: {segment['topic']}
            
            SEGMENT CONTENT:
            {segment['content']}
            """
            
            result = await keyword_agent.run(
                prompt,
                deps=ctx.deps,
                message_history=ctx.state.keyword_agent_messages
            )
            ctx.state.keyword_agent_messages += result.all_messages()
            all_keywords.extend(result.data)
        
        # Store unique keywords
        ctx.state.marketing_keywords = {kw.keyword for kw in all_keywords}
        
        return ExtractBusinessProcesses()

@dataclass
class ExtractBusinessProcesses(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract business processes from the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractTechnicalProcesses":  # Use string literal here
        prompt = format_as_xml({
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        })
        
        result = await business_process_agent.run(
            f"Extract all business processes from this transcript: {prompt}",
            message_history=ctx.state.business_process_agent_messages
        )
        ctx.state.business_process_agent_messages += result.all_messages()
        
        # Convert Pydantic models to dataclass instances
        for bp in result.data:
            process = BusinessProcess(
                name=bp.name,
                description=bp.description,
                steps=[step.description for step in bp.steps],
                inference_type=InferenceType(bp.inference_type),
                transcript_references=bp.transcript_references
            )
            ctx.state.business_processes.append(process)
        
        return ExtractTechnicalProcesses()

@dataclass
class ExtractTechnicalProcesses(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract technical processes from the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractTechnologies":  # Use string literal here
        prompt = format_as_xml({
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        })
        
        result = await tech_process_agent.run(
            f"Extract all technical processes from this transcript: {prompt}",
            message_history=ctx.state.tech_process_agent_messages
        )
        ctx.state.tech_process_agent_messages += result.all_messages()
        
        # Convert Pydantic models to dataclass instances
        for tp in result.data:
            process = TechnicalProcess(
                name=tp.name,
                description=tp.description,
                steps=[step.description for step in tp.steps],
                inference_type=InferenceType(tp.inference_type),
                transcript_references=tp.transcript_references
            )
            ctx.state.technical_processes.append(process)
        
        return ExtractTechnologies()

@dataclass
class ExtractTechnologies(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract technologies mentioned in the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "CreateFinalReport":  # Use string literal here
        prompt = format_as_xml({
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        })
        
        result = await technology_agent.run(
            f"Extract all technologies mentioned in this transcript: {prompt}",
            deps=ctx.deps,
            message_history=ctx.state.technology_agent_messages
        )
        ctx.state.technology_agent_messages += result.all_messages()
        
        # Convert Pydantic models to dataclass instances
        for tech in result.data:
            technology = Technology(
                name=tech.name,
                category=tech.category,
                description=tech.description,
                inference_type=InferenceType(tech.inference_type),
                transcript_references=tech.transcript_references
            )
            ctx.state.technologies.append(technology)
        
        return CreateFinalReport()

@dataclass
class CreateFinalReport(BaseNode[TranscriptAnalysisState, AnalysisResources, TranscriptAnalysisReport]):
    """Create the final analysis report"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> End[TranscriptAnalysisReport]:
        # ... rest of the method remains the same
        # Prepare data for the final report
        marketing_keywords = [
            MarketingKeyword(
                keyword=kw,
                relevance_score=1.0,  # Simplified for this example
                context="From transcript",
                frequency=1  # Simplified
            ) for kw in ctx.state.marketing_keywords
        ]
        
        business_processes = [
            BusinessProcessModel(
                name=bp.name,
                description=bp.description,
                inference_type=bp.inference_type.value,
                confidence_score=1.0,  # Simplified
                steps=[
                    ProcessStep(description=step, order=i+1, transcript_reference="")
                    for i, step in enumerate(bp.steps)
                ],
                transcript_references=bp.transcript_references
            ) for bp in ctx.state.business_processes
        ]
        
        technical_processes = [
            TechnicalProcessModel(
                name=tp.name,
                description=tp.description,
                inference_type=tp.inference_type.value,
                confidence_score=1.0,  # Simplified
                steps=[
                    ProcessStep(description=step, order=i+1, transcript_reference="")
                    for i, step in enumerate(tp.steps)
                ],
                transcript_references=tp.transcript_references
            ) for tp in ctx.state.technical_processes
        ]
        
        technologies = [
            TechnologyModel(
                name=tech.name,
                category=tech.category,
                description=tech.description,
                inference_type=tech.inference_type.value,
                confidence_score=1.0,  # Simplified
                transcript_references=tech.transcript_references
            ) for tech in ctx.state.technologies
        ]
        
        # Create summary with summary agent
        summary_prompt = format_as_xml({
            "video_title": ctx.state.video_title,
            "marketing_keywords": list(ctx.state.marketing_keywords),
            "business_processes": [
                {"name": bp.name, "description": bp.description}
                for bp in ctx.state.business_processes
            ],
            "technical_processes": [
                {"name": tp.name, "description": tp.description}
                for tp in ctx.state.technical_processes
            ],
            "technologies": [
                {"name": tech.name, "category": tech.category}
                for tech in ctx.state.technologies
            ]
        })
        
        summary_result = await summary_agent.run(
            f"Create a summary of this transcript analysis: {summary_prompt}"
        )
        
        # Create the final report
        final_report = TranscriptAnalysisReport(
            video_title=ctx.state.video_title,
            video_id=ctx.state.video_id,
            marketing_keywords=marketing_keywords,
            business_processes=business_processes,
            technical_processes=technical_processes,
            technologies=technologies,
            summary=summary_result.data.summary
        )
        
        return End(final_report)