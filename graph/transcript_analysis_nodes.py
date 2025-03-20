from dataclasses import dataclass
from pydantic_graph import BaseNode, End, GraphRunContext, Edge
from pydantic_ai import RunContext
from pydantic_ai.format_as_xml import format_as_xml
from typing import Annotated, Union
import logging
from pydantic import BaseModel
from typing import List

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

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Important: Define all node classes with string literals for return types
@dataclass
class SegmentTranscript(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Segment the transcript into logical parts by topic using function calling"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractKeywords":  # Use string literal here
        logging.info(f"Segmenting transcript for video: {ctx.state.video_title} ({len(ctx.state.transcript)} chars)")
        
        try:
            # Use the segmentation service from ollama_toolkit
            from ollama_toolkit.tools.text_segmentation import segment_transcript
            
            result = segment_transcript(
                ctx.state.transcript,
                model="mistral:latest-32",  # Or get from resources
            )
            
            if result["success"]:
                # Convert Pydantic models to dictionaries for state storage
                ctx.state.segments = [segment.model_dump() for segment in result["segments"]]
                logging.info(f"Successfully segmented transcript into {len(ctx.state.segments)} segments")
                return ExtractKeywords()
            else:
                # Handle error with fallback
                logging.error(f"Segmentation failed: {result.get('error')}")
                # Implement fallback segmentation
                ctx.state.segments = [{"topic": "Full Transcript", "content": ctx.state.transcript}]
                logging.info("Using fallback segmentation")
                return ExtractKeywords()
                
        except Exception as e:
            logging.exception(f"Error in segmentation: {str(e)}")
            # Implement fallback
            ctx.state.segments = [{"topic": "Full Transcript", "content": ctx.state.transcript}]
            logging.info("Using fallback segmentation due to exception")
            return ExtractKeywords()

@dataclass
class ExtractKeywords(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract marketing keywords from each segment"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractBusinessProcesses":  # Use string literal here
        all_keywords = []
        
        # Define keyword model for structured output
        class KeywordList(BaseModel):
            keywords: List[str]
            
        try:
            # Use ollama toolkit for all segments combined
            from ollama_toolkit.function_calling import call_with_function
            
            # Combine segment content for more context
            all_content = "\n\n".join([f"SEGMENT: {segment['topic']}\n{segment['content']}" 
                                      for segment in ctx.state.segments])
            
            prompt = f"""
            Extract important marketing keywords from this transcript:
            Video title: {ctx.state.video_title}
            
            TRANSCRIPT CONTENT:
            {all_content}
            
            Identify keywords that would be valuable for SEO, advertising, or target audience identification.
            Include only significant marketing terms with clear relevance.
            """
            
            result = call_with_function(
                prompt=prompt,
                model_class=KeywordList,
                function_name="extract_marketing_keywords",
                description="Extract marketing keywords from transcript",
                model="mistral:latest-32"
            )
            
            if result["success"]:
                # Store unique keywords
                ctx.state.marketing_keywords = set(result["data"].keywords)
                logging.info(f"Extracted {len(ctx.state.marketing_keywords)} marketing keywords")
            else:
                # Fallback to using PydanticAI agent
                logging.warning(f"Function calling failed, using backup agent: {result.get('error')}")
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
        except Exception as e:
            logging.exception(f"Error in keyword extraction: {str(e)}")
            # Fallback to using PydanticAI agent
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
        # Define business process model for structured output
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
            
        try:
            # Use ollama toolkit for structured extraction
            from ollama_toolkit.function_calling import call_with_function
            
            prompt = f"""
            Identify business processes described in this transcript:
            Video title: {ctx.state.video_title}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each business process:
            1. Provide a clear name and description
            2. List all steps in the process in order
            3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
            4. Include verbatim transcript references that evidence this process
            
            Only include processes with strong evidence. Maintain high precision over recall.
            """
            
            result = call_with_function(
                prompt=prompt,
                model_class=BusinessProcessList,
                function_name="extract_business_processes",
                description="Extract business processes from transcript",
                model="mistral:latest-32"
            )
            
            if result["success"]:
                # Convert to our internal format
                for bp in result["data"].processes:
                    process = BusinessProcess(
                        name=bp.name,
                        description=bp.description,
                        steps=[step.description for step in bp.steps],
                        inference_type=InferenceType(bp.inference_type),
                        transcript_references=bp.transcript_references
                    )
                    ctx.state.business_processes.append(process)
                logging.info(f"Extracted {len(ctx.state.business_processes)} business processes")
            else:
                # Fallback to using PydanticAI agent
                logging.warning(f"Function calling failed, using backup agent: {result.get('error')}")
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
        except Exception as e:
            logging.exception(f"Error in business process extraction: {str(e)}")
            # Fallback to using PydanticAI agent
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
        # Define technical process model for structured output
        class TechnicalProcessStep(BaseModel):
            description: str
            order: int
            
        class TechnicalProcessExtraction(BaseModel):
            name: str
            description: str
            steps: List[TechnicalProcessStep]
            inference_type: str
            transcript_references: List[str]
            
        class TechnicalProcessList(BaseModel):
            processes: List[TechnicalProcessExtraction]
            
        try:
            # Use ollama toolkit for structured extraction
            from ollama_toolkit.function_calling import call_with_function
            
            prompt = f"""
            Identify technical processes described in this transcript:
            Video title: {ctx.state.video_title}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each technical process:
            1. Provide a clear name and description
            2. List all steps in the process in order
            3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
            4. Include verbatim transcript references that evidence this process
            
            Only include processes with strong evidence. Maintain high precision over recall.
            Focus on technical implementation details, coding procedures, and development workflows.
            """
            
            result = call_with_function(
                prompt=prompt,
                model_class=TechnicalProcessList,
                function_name="extract_technical_processes",
                description="Extract technical processes from transcript",
                model="mistral:latest-32"
            )
            
            if result["success"]:
                # Convert to our internal format
                for tp in result["data"].processes:
                    process = TechnicalProcess(
                        name=tp.name,
                        description=tp.description,
                        steps=[step.description for step in tp.steps],
                        inference_type=InferenceType(tp.inference_type),
                        transcript_references=tp.transcript_references
                    )
                    ctx.state.technical_processes.append(process)
                logging.info(f"Extracted {len(ctx.state.technical_processes)} technical processes")
            else:
                # Fallback to using PydanticAI agent
                logging.warning(f"Function calling failed, using backup agent: {result.get('error')}")
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
        except Exception as e:
            logging.exception(f"Error in technical process extraction: {str(e)}")
            # Fallback to using PydanticAI agent
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
        # Define technology model for structured output
        class TechnologyExtraction(BaseModel):
            name: str
            category: str
            description: str
            inference_type: str
            transcript_references: List[str]
            
        class TechnologyList(BaseModel):
            technologies: List[TechnologyExtraction]
            
        try:
            # Use ollama toolkit for structured extraction
            from ollama_toolkit.function_calling import call_with_function
            
            prompt = f"""
            Extract all technologies mentioned in this transcript:
            Video title: {ctx.state.video_title}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each technology:
            1. Provide the exact name as mentioned
            2. Categorize it (e.g., "database", "programming language", "cloud service")
            3. Provide a brief description
            4. Specify if the technology is directly mentioned (DIRECT) or inferred from context (INFERRED)
            5. Include verbatim transcript references
            
            Be comprehensive but precise - only include technologies with clear evidence.
            """
            
            result = call_with_function(
                prompt=prompt,
                model_class=TechnologyList,
                function_name="extract_technologies",
                description="Extract technologies from transcript",
                model="mistral:latest-32"
            )
            
            if result["success"]:
                # Convert to our internal format
                for tech in result["data"].technologies:
                    technology = Technology(
                        name=tech.name,
                        category=tech.category,
                        description=tech.description,
                        inference_type=InferenceType(tech.inference_type),
                        transcript_references=tech.transcript_references
                    )
                    ctx.state.technologies.append(technology)
                logging.info(f"Extracted {len(ctx.state.technologies)} technologies")
            else:
                # Fallback to using PydanticAI agent
                logging.warning(f"Function calling failed, using backup agent: {result.get('error')}")
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
        except Exception as e:
            logging.exception(f"Error in technology extraction: {str(e)}")
            # Fallback to using PydanticAI agent
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
        # Define summary model for structured output
        class SummaryGeneration(BaseModel):
            summary: str
            
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
        
        try:
            # Use ollama toolkit for structured summary
            from ollama_toolkit.function_calling import call_with_function
            
            # Prepare summary data
            summary_data = {
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
            }
            
            prompt = f"""
            Create a comprehensive summary of this transcript analysis:
            
            VIDEO TITLE: {summary_data['video_title']}
            
            MARKETING KEYWORDS: {', '.join(summary_data['marketing_keywords'])}
            
            BUSINESS PROCESSES:
            {json.dumps(summary_data['business_processes'], indent=2)}
            
            TECHNICAL PROCESSES:
            {json.dumps(summary_data['technical_processes'], indent=2)}
            
            TECHNOLOGIES:
            {json.dumps(summary_data['technologies'], indent=2)}
            
            Write a well-structured summary that covers the key points of the video
            based on the extracted information.
            """
            
            result = call_with_function(
                prompt=prompt,
                model_class=SummaryGeneration,
                function_name="generate_summary",
                description="Generate a comprehensive summary of transcript analysis",
                model="mistral:latest-32"
            )
            
            if result["success"]:
                summary = result["data"].summary
            else:
                # Fallback to using PydanticAI agent
                logging.warning(f"Function calling failed, using backup agent: {result.get('error')}")
                summary_prompt = format_as_xml(summary_data)
                
                summary_result = await summary_agent.run(
                    f"Create a summary of this transcript analysis: {summary_prompt}"
                )
                summary = summary_result.data.summary
        except Exception as e:
            logging.exception(f"Error generating summary: {str(e)}")
            # Fallback to using PydanticAI agent
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
            summary = summary_result.data.summary
        
        # Create the final report
        final_report = TranscriptAnalysisReport(
            video_title=ctx.state.video_title,
            video_id=ctx.state.video_id,
            marketing_keywords=marketing_keywords,
            business_processes=business_processes,
            technical_processes=technical_processes,
            technologies=technologies,
            summary=summary
        )
        
        return End(final_report)