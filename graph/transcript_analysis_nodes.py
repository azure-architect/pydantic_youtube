# Required imports at the top of the file
import time
import logging
import json
from dataclasses import dataclass
from pydantic_graph import BaseNode, End, GraphRunContext, Edge
from pydantic_ai import RunContext
from pydantic_ai.format_as_xml import format_as_xml
from typing import Annotated, Union, List, Dict, Any, Optional, Set
from pydantic import BaseModel
from enum import Enum
import re
import sys
import os

# Add parent directory to path to allow imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import models and state classes
from models.transcript_analysis_models import (
    TranscriptAnalysisReport, ProcessStep, MarketingKeyword,
    BusinessProcessModel, TechnicalProcessModel, TechnologyModel,
    TranscriptSegment, TopicList, KeywordList, BusinessProcessList,
    TechnicalProcessList, TechnologyList, SummaryGeneration
)

from state.transcript_analysis_state import (
    TranscriptAnalysisState, AnalysisResources, BusinessProcess,
    TechnicalProcess, Technology, InferenceType
)

# Import agent implementations for fallbacks
from agents.transcript_analysis_agents import (
    segment_agent, keyword_agent, business_process_agent,
    tech_process_agent, technology_agent, summary_agent
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('transcript_analysis.log')
    ]
)

# Define Status enum for state tracking
class Status(Enum):
    SUCCESS = "success"
    FAILURE = "failure"



# Important: Define all node classes with string literals for return types
@dataclass
class SegmentTranscript(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Segment the transcript into logical parts by topic using function calling"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractKeywords":
        logging.info(f"Segmenting transcript for video: {ctx.state.video_title} ({len(ctx.state.transcript)} chars)")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            context_size = ctx.deps.context_window_size
            temperature = ctx.deps.temperature
            
            # Use the segmentation tool from ollama_toolkit
            from ollama_toolkit.tools.text_segmentation import segment_transcript
            
            # Record the start time for performance tracking
            start_time = time.time()
            
            result = segment_transcript(
                transcript_text=ctx.state.transcript,
                model=model,
                context_size=context_size,
                temperature=temperature
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Segmentation completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["segment_transcript"] = result["success"]
            
            if result["success"]:
                # Convert Pydantic models to dictionaries for state storage
                ctx.state.segments = [segment.model_dump() for segment in result["segments"]]
                
                # Ensure all segments have start_time_approx as a string, not None
                for segment in ctx.state.segments:
                    if segment.get("start_time_approx") is None:
                        segment["start_time_approx"] = ""  # Empty string instead of None
                
                # Calculate and store some statistics about the segmentation
                total_words = len(ctx.state.transcript.split())
                segment_words = sum(len(segment["content"].split()) for segment in ctx.state.segments)
                coverage = (segment_words / total_words) * 100 if total_words > 0 else 0
                
                ctx.state.segment_stats = {
                    "total_segments": {"value": len(ctx.state.segments)},
                    "total_transcript_words": {"value": total_words},
                    "total_segment_words": {"value": segment_words}, 
                    "coverage_percentage": {"value": coverage},
                    "processing_time_seconds": {"value": elapsed_time}
                }
                
                logging.info(f"Successfully segmented transcript into {len(ctx.state.segments)} segments")
                logging.info(f"Transcript coverage: {coverage:.2f}% ({segment_words}/{total_words} words)")
                
                # Success - continue to keyword extraction
                return ExtractKeywords()
            else:
                # Handle error with fallback
                error_message = result.get("error", "Unknown error in segmentation")
                logging.error(f"Segmentation failed: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["segment_transcript"] = error_message
                
                # Implement fallback segmentation - simple paragraph-based approach
                fallback_segments = self._fallback_segmentation(ctx.state.transcript)
                ctx.state.segments = fallback_segments
                
                # Ensure all segments have start_time_approx as a string in fallback
                for segment in ctx.state.segments:
                    if segment.get("start_time_approx") is None:
                        segment["start_time_approx"] = ""
                
                logging.info(f"Using fallback segmentation with {len(fallback_segments)} segments")
                return ExtractKeywords()
                
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in segmentation: {str(e)}")
            
            # Store error information
            ctx.state.function_call_errors["segment_transcript"] = str(e)
            
            # Implement simple fallback - treat entire transcript as one segment
            ctx.state.segments = [{"topic": "Full Transcript", "content": ctx.state.transcript, "start_time_approx": ""}]
            logging.info("Using emergency fallback segmentation (single segment)")
            return ExtractKeywords()
    
    def _fallback_segmentation(self, transcript: str) -> List[Dict[str, str]]:
        """
        Fallback segmentation method when function calling fails
        Uses a simple paragraph-based approach
        """
        segments = []
        
        # Split transcript by double newlines to identify paragraphs
        paragraphs = transcript.split("\n\n")
        
        # Group paragraphs into reasonable segments
        current_segment = []
        current_topic = "Introduction"
        segment_count = 1
        
        for i, paragraph in enumerate(paragraphs):
            paragraph = paragraph.strip()
            if not paragraph:
                continue
                
            # Start a new segment every ~5 paragraphs or 500 words
            # This is a simple heuristic that can be adjusted
            if (len(current_segment) >= 5 or 
                sum(len(p.split()) for p in current_segment) > 500):
                if current_segment:
                    segments.append({
                        "topic": current_topic,
                        "content": "\n\n".join(current_segment)
                    })
                    current_segment = []
                    segment_count += 1
                    current_topic = f"Section {segment_count}"
            
            current_segment.append(paragraph)
        
        # Don't forget the last segment
        if current_segment:
            segments.append({
                "topic": current_topic,
                "content": "\n\n".join(current_segment)
            })
        
        # If we couldn't create any segments, use the entire transcript
        if not segments:
            segments = [{"topic": "Full Transcript", "content": transcript}]
            
        return segments

@dataclass
class ExtractKeywords(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract marketing keywords from each segment"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractBusinessProcesses":
        logging.info(f"Extracting marketing keywords from transcript")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            temperature = ctx.deps.temperature
            
            # Use the function calling approach for keyword extraction
            from ollama_toolkit.function_calling import call_with_function
            from models.transcript_analysis_models import KeywordList
            
            # Create a combined text from all segments for better context
            segments_text = "\n\n".join([
                f"SEGMENT: {segment['topic']}\n{segment['content']}" 
                for segment in ctx.state.segments
            ])
            
            # Record start time for performance tracking
            start_time = time.time()
            
            # Prepare a prompt that focuses on marketing keywords
            prompt = f"""
            Extract marketing keywords from this transcript that would be valuable for:
            - SEO and search visibility
            - Target audience identification
            - Marketing campaign focus
            - Content categorization
            
            VIDEO TITLE: {ctx.state.video_title}
            VIDEO ID: {ctx.state.video_id}
            
            TRANSCRIPT CONTENT:
            {segments_text}
            
            Extract ONLY keywords that have clear marketing value and relevance.
            Return just the keywords without explanations.
            """
            
            # Call the function with our KeywordList model
            result = call_with_function(
                prompt=prompt,
                model_class=KeywordList,
                function_name="extract_marketing_keywords",
                description="Extract marketing keywords from transcript for SEO and marketing purposes",
                model=model,
                options={"temperature": temperature}
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Keyword extraction completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["extract_keywords"] = result["success"]
            
            if result["success"]:
                # Store unique keywords - convert to set to remove duplicates
                extracted_keywords = set(result["data"].keywords)
                
                # Filter out any low-quality keywords (too short, etc.)
                filtered_keywords = {
                    kw for kw in extracted_keywords 
                    if len(kw) > 2  # Remove very short keywords
                    and not kw.lower() in ["the", "and", "for", "with"]  # Remove common words
                }
                
                # Store the keywords
                ctx.state.marketing_keywords = filtered_keywords
                
                logging.info(f"Extracted {len(ctx.state.marketing_keywords)} marketing keywords")
                
                # Success - continue to business process extraction
                return ExtractBusinessProcesses()
            else:
                # Handle error with fallback to PydanticAI agent
                error_message = result.get("error", "Unknown error in keyword extraction")
                logging.warning(f"Function calling failed, using backup agent: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["extract_keywords"] = error_message
                
                # Fallback to using PydanticAI agent if available
                keywords = await self._extract_keywords_with_agent(ctx)
                
                # Store the keywords
                ctx.state.marketing_keywords = set(keywords)
                logging.info(f"Extracted {len(ctx.state.marketing_keywords)} keywords using backup agent")
                
                return ExtractBusinessProcesses()
                
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in keyword extraction: {str(e)}")
            
            # Store error information
            ctx.state.function_call_errors["extract_keywords"] = str(e)
            
            # Attempt fallback or use empty list
            try:
                keywords = await self._extract_keywords_with_agent(ctx)
                ctx.state.marketing_keywords = set(keywords)
            except:
                # Emergency fallback - derive basic keywords from segment topics
                ctx.state.marketing_keywords = self._emergency_keyword_extraction(ctx.state)
                
            logging.info(f"Using fallback keywords: {len(ctx.state.marketing_keywords)} keywords found")
            return ExtractBusinessProcesses()
    
    async def _extract_keywords_with_agent(self, ctx) -> List[str]:
        """Extract keywords using the PydanticAI agent as fallback"""
        all_keywords = []
        
        # Use the original keyword agent implementation
        from agents.transcript_analysis_agents import keyword_agent
        
        for i, segment in enumerate(ctx.state.segments):
            prompt = f"""
            Extract marketing keywords from this transcript segment.
            VIDEO TITLE: {ctx.state.video_title}
            SEGMENT TOPIC: {segment['topic']}
            
            SEGMENT CONTENT:
            {segment['content']}
            """
            
            result = await keyword_agent.run(
                prompt,
                deps=ctx.deps,
                message_history=ctx.state.keyword_agent_messages
            )
            ctx.state.keyword_agent_messages += result.all_messages()
            
            # Convert MarketingKeyword objects to simple strings
            keywords = [kw.keyword for kw in result.data]
            all_keywords.extend(keywords)
        
        # Return unique keywords
        return list(set(all_keywords))
    
    def _emergency_keyword_extraction(self, state: TranscriptAnalysisState) -> Set[str]:
        """Emergency fallback keyword extraction from segment topics"""
        keywords = set()
        
        # Add video title words as keywords
        for word in state.video_title.split():
            if len(word) > 3 and word.lower() not in ["the", "and", "for", "with"]:
                keywords.add(word)
        
        # Add segment topics as keywords
        for segment in state.segments:
            topic = segment["topic"]
            # Skip generic topics like "Introduction", "Section 1", etc.
            if topic.lower() in ["introduction", "conclusion", "summary"] or "section" in topic.lower():
                continue
                
            for word in topic.split():
                if len(word) > 3 and word.lower() not in ["the", "and", "for", "with"]:
                    keywords.add(word)
        
        return keywords

@dataclass
class ExtractBusinessProcesses(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract business processes from the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractTechnicalProcesses":
        logging.info(f"Extracting business processes from transcript")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            temperature = ctx.deps.temperature
            
            # Use the function calling approach for business process extraction
            from ollama_toolkit.function_calling import call_with_function
            from models.transcript_analysis_models import BusinessProcessList
            
            # Record start time for performance tracking
            start_time = time.time()
            
            # Prepare a detailed prompt for business process extraction
            prompt = f"""
            Identify business processes described in this transcript.
            
            VIDEO TITLE: {ctx.state.video_title}
            VIDEO ID: {ctx.state.video_id}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each business process:
            1. Provide a clear name and description
            2. List all steps in the process in order
            3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
            4. Include verbatim transcript references that evidence this process
            
            Only include processes with strong evidence. Maintain high precision over recall.
            Focus on workflows, procedures, and methodologies relevant to businesses.
            """
            
            # Call the function with our BusinessProcessList model
            result = call_with_function(
                prompt=prompt,
                model_class=BusinessProcessList,
                function_name="extract_business_processes",
                description="Extract business processes from transcript",
                model=model,
                options={"temperature": temperature}
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Business process extraction completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["extract_business_processes"] = result["success"]
            
            if result["success"]:
                # Convert extracted processes to our internal format
                extracted_processes = []
                
                for bp in result["data"].processes:
                    process = BusinessProcess(
                        name=bp.name,
                        description=bp.description,
                        steps=[step.description for step in bp.steps],
                        inference_type=InferenceType(bp.inference_type),
                        transcript_references=bp.transcript_references
                    )
                    extracted_processes.append(process)
                
                # Only keep processes with sufficient detail (at least 2 steps)
                filtered_processes = [p for p in extracted_processes if len(p.steps) >= 2]
                
                # Store the business processes
                ctx.state.business_processes = filtered_processes
                
                logging.info(f"Extracted {len(ctx.state.business_processes)} business processes")
                
                # Success - continue to technical process extraction
                return ExtractTechnicalProcesses()
            else:
                # Handle error with fallback to PydanticAI agent
                error_message = result.get("error", "Unknown error in business process extraction")
                logging.warning(f"Function calling failed, using backup agent: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["extract_business_processes"] = error_message
                
                # Fallback to using PydanticAI agent
                processes = await self._extract_processes_with_agent(ctx)
                
                # Store the processes
                ctx.state.business_processes = processes
                logging.info(f"Extracted {len(processes)} business processes using backup agent")
                
                return ExtractTechnicalProcesses()
                
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in business process extraction: {str(e)}")
            
            # Store error information
            ctx.state.function_call_errors["extract_business_processes"] = str(e)
            
            # Attempt fallback with agent
            try:
                processes = await self._extract_processes_with_agent(ctx)
                ctx.state.business_processes = processes
                logging.info(f"Extracted {len(processes)} business processes using backup agent")
            except Exception as agent_error:
                # Emergency fallback - create simple processes from segment topics
                logging.error(f"Backup agent failed: {str(agent_error)}")
                ctx.state.business_processes = self._emergency_process_extraction(ctx.state)
                logging.info(f"Using emergency fallback: {len(ctx.state.business_processes)} processes")
            
            return ExtractTechnicalProcesses()
    
    async def _extract_processes_with_agent(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> List[BusinessProcess]:
        """Extract business processes using the PydanticAI agent as fallback"""
        # Use the original business process agent implementation
        from agents.transcript_analysis_agents import business_process_agent
        from pydantic_ai.format_as_xml import format_as_xml
        
        # Prepare XML-formatted data for the agent
        prompt_data = {
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        }
        
        prompt = format_as_xml(prompt_data)
        
        # Run the agent
        result = await business_process_agent.run(
            f"Extract all business processes from this transcript: {prompt}",
            message_history=ctx.state.business_process_agent_messages
        )
        ctx.state.business_process_agent_messages += result.all_messages()
        
        # Convert agent results to our internal format
        processes = []
        for bp in result.data:
            process = BusinessProcess(
                name=bp.name,
                description=bp.description,
                steps=[step.description for step in bp.steps],
                inference_type=InferenceType(bp.inference_type),
                transcript_references=bp.transcript_references
            )
            processes.append(process)
            
        return processes
    
    def _emergency_process_extraction(self, state: TranscriptAnalysisState) -> List[BusinessProcess]:
        """Emergency fallback business process extraction from segments"""
        processes = []
        
        # Try to identify potential processes from segment topics and content
        potential_process_indicators = [
            "process", "workflow", "procedure", "method", "approach", "steps",
            "implementation", "deployment", "installation", "setup", "configuration"
        ]
        
        # Check for segments that might describe processes
        for i, segment in enumerate(state.segments):
            topic = segment["topic"].lower()
            
            # Check if the topic suggests a business process
            is_process = False
            process_name = ""
            
            for indicator in potential_process_indicators:
                if indicator in topic:
                    is_process = True
                    process_name = segment["topic"]
                    break
            
            # If not found in topic, check first few lines of content
            if not is_process:
                content_start = " ".join(segment["content"].split()[:30]).lower()
                for indicator in potential_process_indicators:
                    if indicator in content_start:
                        is_process = True
                        # Extract a potential name from the content
                        sentences = segment["content"].split('.')
                        if sentences:
                            process_name = sentences[0].strip()
                            # Limit process name length
                            if len(process_name) > 50:
                                process_name = process_name[:50] + "..."
                        else:
                            process_name = f"Process from {segment['topic']}"
                        break
            
            if is_process:
                # Create a simple process with minimal information
                process = BusinessProcess(
                    name=process_name,
                    description=f"Process extracted from segment: {segment['topic']}",
                    steps=["Step identified from transcript"],  # Minimal placeholder
                    inference_type=InferenceType.INFERRED,
                    transcript_references=[segment["content"][:100] + "..."]
                )
                processes.append(process)
        
        return processes

@dataclass
class ExtractTechnicalProcesses(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract technical processes from the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "ExtractTechnologies":
        logging.info(f"Extracting technical processes from transcript")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            temperature = ctx.deps.temperature
            
            # Use the function calling approach for technical process extraction
            from ollama_toolkit.function_calling import call_with_function
            from models.transcript_analysis_models import TechnicalProcessList
            
            # Record start time for performance tracking
            start_time = time.time()
            
            # Prepare a detailed prompt for technical process extraction
            prompt = f"""
            Identify technical processes described in this transcript.
            
            VIDEO TITLE: {ctx.state.video_title}
            VIDEO ID: {ctx.state.video_id}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each technical process:
            1. Provide a clear name and description
            2. List all steps in the process in order
            3. Specify if the process is directly described (DIRECT) or inferred from context (INFERRED)
            4. Include verbatim transcript references that evidence this process
            
            Focus on technical implementation details, coding procedures, system configuration,
            infrastructure setup, and technical workflows. Only include processes with strong
            evidence. Maintain high precision over recall.
            """
            
            # Call the function with our TechnicalProcessList model
            result = call_with_function(
                prompt=prompt,
                model_class=TechnicalProcessList,
                function_name="extract_technical_processes",
                description="Extract technical processes from transcript",
                model=model,
                options={"temperature": temperature}
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Technical process extraction completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["extract_technical_processes"] = result["success"]
            
            if result["success"]:
                # Convert extracted processes to our internal format
                extracted_processes = []
                
                for tp in result["data"].processes:
                    process = TechnicalProcess(
                        name=tp.name,
                        description=tp.description,
                        steps=[step.description for step in tp.steps],
                        inference_type=InferenceType(tp.inference_type),
                        transcript_references=tp.transcript_references
                    )
                    extracted_processes.append(process)
                
                # Only keep processes with sufficient detail (at least 2 steps)
                filtered_processes = [p for p in extracted_processes if len(p.steps) >= 2]
                
                # Store the technical processes
                ctx.state.technical_processes = filtered_processes
                
                logging.info(f"Extracted {len(ctx.state.technical_processes)} technical processes")
                
                # Success - continue to technology extraction
                return ExtractTechnologies()
            else:
                # Handle error with fallback to PydanticAI agent
                error_message = result.get("error", "Unknown error in technical process extraction")
                logging.warning(f"Function calling failed, using backup agent: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["extract_technical_processes"] = error_message
                
                # Fallback to using PydanticAI agent
                processes = await self._extract_processes_with_agent(ctx)
                
                # Store the processes
                ctx.state.technical_processes = processes
                logging.info(f"Extracted {len(processes)} technical processes using backup agent")
                
                return ExtractTechnologies()
                
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in technical process extraction: {str(e)}")
            
            # Store error information
            ctx.state.function_call_errors["extract_technical_processes"] = str(e)
            
            # Attempt fallback with agent
            try:
                processes = await self._extract_processes_with_agent(ctx)
                ctx.state.technical_processes = processes
                logging.info(f"Extracted {len(processes)} technical processes using backup agent")
            except Exception as agent_error:
                # Emergency fallback - create simple processes from segment topics
                logging.error(f"Backup agent failed: {str(agent_error)}")
                ctx.state.technical_processes = self._emergency_process_extraction(ctx.state)
                logging.info(f"Using emergency fallback: {len(ctx.state.technical_processes)} processes")
            
            return ExtractTechnologies()
    
    async def _extract_processes_with_agent(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> List[TechnicalProcess]:
        """Extract technical processes using the PydanticAI agent as fallback"""
        # Use the original technical process agent implementation
        from agents.transcript_analysis_agents import tech_process_agent
        from pydantic_ai.format_as_xml import format_as_xml
        
        # Prepare XML-formatted data for the agent
        prompt_data = {
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        }
        
        prompt = format_as_xml(prompt_data)
        
        # Run the agent
        result = await tech_process_agent.run(
            f"Extract all technical processes from this transcript: {prompt}",
            message_history=ctx.state.tech_process_agent_messages
        )
        ctx.state.tech_process_agent_messages += result.all_messages()
        
        # Convert agent results to our internal format
        processes = []
        for tp in result.data:
            process = TechnicalProcess(
                name=tp.name,
                description=tp.description,
                steps=[step.description for step in tp.steps],
                inference_type=InferenceType(tp.inference_type),
                transcript_references=tp.transcript_references
            )
            processes.append(process)
            
        return processes
    
    def _emergency_process_extraction(self, state: TranscriptAnalysisState) -> List[TechnicalProcess]:
        """Emergency fallback technical process extraction from segments"""
        processes = []
        
        # Try to identify potential technical processes from segment topics and content
        potential_process_indicators = [
            "installation", "setup", "configuration", "deployment", "implementation",
            "coding", "programming", "building", "development", "integration",
            "testing", "execution", "compiling", "running", "launching"
        ]
        
        # Check for segments that might describe technical processes
        for i, segment in enumerate(state.segments):
            topic = segment["topic"].lower()
            
            # Check if the topic suggests a technical process
            is_technical = False
            process_name = ""
            
            for indicator in potential_process_indicators:
                if indicator in topic:
                    is_technical = True
                    process_name = segment["topic"]
                    break
            
            # If not found in topic, check first few lines of content
            if not is_technical:
                content_start = " ".join(segment["content"].split()[:30]).lower()
                for indicator in potential_process_indicators:
                    if indicator in content_start:
                        is_technical = True
                        # Extract a potential name from the content
                        sentences = segment["content"].split('.')
                        if sentences:
                            process_name = sentences[0].strip()
                            # Limit process name length
                            if len(process_name) > 50:
                                process_name = process_name[:50] + "..."
                        else:
                            process_name = f"Technical process from {segment['topic']}"
                        break
            
            if is_technical:
                # Create a simple process with minimal information
                process = TechnicalProcess(
                    name=process_name,
                    description=f"Technical process extracted from segment: {segment['topic']}",
                    steps=["Step identified from transcript"],  # Minimal placeholder
                    inference_type=InferenceType.INFERRED,
                    transcript_references=[segment["content"][:100] + "..."]
                )
                processes.append(process)
        
        return processes

@dataclass
class ExtractTechnologies(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    """Extract technologies mentioned in the transcript"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> "CreateFinalReport":
        logging.info(f"Extracting technologies from transcript")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            temperature = ctx.deps.temperature
            
            # Use the function calling approach for technology extraction
            from ollama_toolkit.function_calling import call_with_function
            from models.transcript_analysis_models import TechnologyList
            
            # Record start time for performance tracking
            start_time = time.time()
            
            # Prepare a detailed prompt for technology extraction
            prompt = f"""
            Extract all technologies mentioned in this transcript.
            
            VIDEO TITLE: {ctx.state.video_title}
            VIDEO ID: {ctx.state.video_id}
            
            TRANSCRIPT:
            {ctx.state.transcript}
            
            For each technology:
            1. Provide the exact name as mentioned
            2. Categorize it (e.g., "database", "programming language", "cloud service")
            3. Provide a brief description
            4. Specify if the technology is directly mentioned (DIRECT) or inferred from context (INFERRED)
            5. Include verbatim transcript references
            
            Be comprehensive but precise - only include technologies with clear evidence.
            Include software, programming languages, frameworks, libraries, platforms,
            cloud services, hardware, and other technical tools.
            """
            
            # Enhanced options for technology extraction
            options = {
                "temperature": temperature,
                "num_ctx": ctx.deps.context_window_size
            }
            
            # Call the function with our TechnologyList model
            result = call_with_function(
                prompt=prompt,
                model_class=TechnologyList,
                function_name="extract_technologies",
                description="Extract technologies from transcript",
                model=model,
                options=options
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Technology extraction completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["extract_technologies"] = result["success"]
            
            if result["success"]:
                # Convert extracted technologies to our internal format
                extracted_technologies = []
                
                for tech in result["data"].technologies:
                    technology = Technology(
                        name=tech.name,
                        category=tech.category,
                        description=tech.description,
                        inference_type=InferenceType(tech.inference_type),
                        transcript_references=tech.transcript_references
                    )
                    extracted_technologies.append(technology)
                
                # Filter out any low-quality technology entries
                filtered_technologies = [
                    t for t in extracted_technologies 
                    if len(t.name) > 1 and len(t.description) > 10  # Basic quality checks
                ]
                
                # Store the technologies
                ctx.state.technologies = filtered_technologies
                
                logging.info(f"Extracted {len(ctx.state.technologies)} technologies")
                
                # Success - continue to final report creation
                return CreateFinalReport()
            else:
                # Handle error with fallback to PydanticAI agent
                error_message = result.get("error", "Unknown error in technology extraction")
                logging.warning(f"Function calling failed, using backup agent: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["extract_technologies"] = error_message
                
                # Fallback to using PydanticAI agent
                technologies = await self._extract_technologies_with_agent(ctx)
                
                # Store the technologies
                ctx.state.technologies = technologies
                logging.info(f"Extracted {len(technologies)} technologies using backup agent")
                
                return CreateFinalReport()
                
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in technology extraction: {str(e)}")
            
            # Store error information
            ctx.state.function_call_errors["extract_technologies"] = str(e)
            
            # Attempt fallback with agent
            try:
                technologies = await self._extract_technologies_with_agent(ctx)
                ctx.state.technologies = technologies
                logging.info(f"Extracted {len(technologies)} technologies using backup agent")
            except Exception as agent_error:
                # Emergency fallback - create basic technologies from known patterns
                logging.error(f"Backup agent failed: {str(agent_error)}")
                ctx.state.technologies = self._emergency_technology_extraction(ctx.state)
                logging.info(f"Using emergency fallback: {len(ctx.state.technologies)} technologies")
            
            return CreateFinalReport()
    
    async def _extract_technologies_with_agent(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> List[Technology]:
        """Extract technologies using the PydanticAI agent as fallback"""
        # Use the original technology agent implementation
        from agents.transcript_analysis_agents import technology_agent
        from pydantic_ai.format_as_xml import format_as_xml
        
        # Prepare XML-formatted data for the agent
        prompt_data = {
            "video_title": ctx.state.video_title,
            "transcript": ctx.state.transcript
        }
        
        prompt = format_as_xml(prompt_data)
        
        # Run the agent
        result = await technology_agent.run(
            f"Extract all technologies mentioned in this transcript: {prompt}",
            deps=ctx.deps,
            message_history=ctx.state.technology_agent_messages
        )
        ctx.state.technology_agent_messages += result.all_messages()
        
        # Convert agent results to our internal format
        technologies = []
        for tech in result.data:
            technology = Technology(
                name=tech.name,
                category=tech.category,
                description=tech.description,
                inference_type=InferenceType(tech.inference_type),
                transcript_references=tech.transcript_references
            )
            technologies.append(technology)
            
        return technologies
    
    def _emergency_technology_extraction(self, state: TranscriptAnalysisState) -> List[Technology]:
        """Emergency fallback technology extraction using pattern matching"""
        technologies = []
        
        # Common technology categories and examples for pattern matching
        tech_patterns = {
            "Programming Language": ["Python", "Java", "JavaScript", "TypeScript", "C++", "C#", "Go", "Rust", "PHP", "Ruby"],
            "Framework": ["React", "Angular", "Vue", "Django", "Flask", "Spring", "Express", "Rails", "Laravel", "ASP.NET"],
            "Database": ["MySQL", "PostgreSQL", "MongoDB", "Redis", "SQLite", "Oracle", "SQL Server", "Cassandra", "Elasticsearch"],
            "Cloud Service": ["AWS", "Azure", "GCP", "Google Cloud", "Heroku", "DigitalOcean", "Cloudflare"],
            "Development Tool": ["Git", "GitHub", "VS Code", "Visual Studio", "IntelliJ", "PyCharm", "Docker", "Kubernetes", "Jenkins"],
            "Machine Learning": ["TensorFlow", "PyTorch", "scikit-learn", "Keras", "NLTK", "Hugging Face", "OpenAI", "GPT"]
        }
        
        # Scan the transcript for technology references
        transcript_lower = state.transcript.lower()
        
        for category, techs in tech_patterns.items():
            for tech in techs:
                tech_lower = tech.lower()
                if tech_lower in transcript_lower:
                    # Search for the actual match with proper casing
                    import re
                    # Create a regex pattern that's case insensitive
                    pattern = re.compile(re.escape(tech_lower), re.IGNORECASE)
                    matches = pattern.finditer(transcript_lower)
                    
                    # Get the surrounding context for the first few occurrences
                    references = []
                    for i, match in enumerate(matches):
                        if i >= 3:  # Limit to 3 references
                            break
                            
                        start = max(0, match.start() - 50)
                        end = min(len(transcript_lower), match.end() + 50)
                        context = state.transcript[start:end]
                        references.append(f"...{context}...")
                    
                    if references:
                        technology = Technology(
                            name=tech,
                            category=category,
                            description=f"A {category.lower()} mentioned in the transcript",
                            inference_type=InferenceType.DIRECT,
                            transcript_references=references
                        )
                        technologies.append(technology)
        
        return technologies

@dataclass
class CreateFinalReport(BaseNode[TranscriptAnalysisState, AnalysisResources, TranscriptAnalysisReport]):
    """Create the final analysis report"""
    
    async def run(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> End[TranscriptAnalysisReport]:
        logging.info(f"Creating final analysis report for {ctx.state.video_title}")
        
        try:
            # Get configuration from resources
            model = ctx.deps.model
            temperature = ctx.deps.temperature
            
            # Prepare data for the final report
            marketing_keywords = [
                MarketingKeyword(
                    keyword=kw,
                    relevance_score=1.0,  # Default value
                    context="From transcript",
                    frequency=1  # Default value
                ) for kw in ctx.state.marketing_keywords
            ]
            
            business_processes = [
                BusinessProcessModel(
                    name=bp.name,
                    description=bp.description,
                    inference_type=bp.inference_type.value,
                    confidence_score=1.0,  # Default value
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
                    confidence_score=1.0,  # Default value
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
                    confidence_score=1.0,  # Default value
                    transcript_references=tech.transcript_references
                ) for tech in ctx.state.technologies
            ]
            
            # Use the function calling approach for generating a summary
            from ollama_toolkit.function_calling import call_with_function
            from models.transcript_analysis_models import SummaryGeneration
            
            # Record start time for performance tracking
            start_time = time.time()
            
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
            
            # Create a concise prompt for summary generation
            prompt = f"""
            Create a comprehensive summary of this transcript analysis:
            
            VIDEO TITLE: {summary_data['video_title']}
            
            MARKETING KEYWORDS: {', '.join(summary_data['marketing_keywords'][:10])}
            {'' if len(summary_data['marketing_keywords']) <= 10 else f'... and {len(summary_data["marketing_keywords"]) - 10} more'}
            
            BUSINESS PROCESSES:
            {self._format_process_list(summary_data['business_processes'])}
            
            TECHNICAL PROCESSES:
            {self._format_process_list(summary_data['technical_processes'])}
            
            TECHNOLOGIES:
            {self._format_technology_list(summary_data['technologies'])}
            
            Write a well-structured summary (250-300 words) that covers the key points of the video
            based on the extracted information. Focus on the main subject matter, key processes,
            and technologies discussed.
            """
            
            # Call the function with our SummaryGeneration model
            result = call_with_function(
                prompt=prompt,
                model_class=SummaryGeneration,
                function_name="generate_summary",
                description="Generate a comprehensive summary of transcript analysis",
                model=model,
                options={"temperature": temperature}
            )
            
            # Record elapsed time
            elapsed_time = time.time() - start_time
            logging.info(f"Summary generation completed in {elapsed_time:.2f} seconds")
            
            # Store function call status
            ctx.state.function_call_successes["generate_summary"] = result["success"]
            
            if result["success"]:
                summary = result["data"].summary
            else:
                # Handle error with fallback to PydanticAI agent
                error_message = result.get("error", "Unknown error in summary generation")
                logging.warning(f"Function calling failed, using backup agent: {error_message}")
                
                # Store error information
                ctx.state.function_call_errors["generate_summary"] = error_message
                
                # Fallback to using PydanticAI agent or generate basic summary
                summary = await self._generate_summary_with_agent(ctx)
            
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
            
            logging.info(f"Final report created successfully")
            
            # Log function call statistics
            success_calls = sum(1 for success in ctx.state.function_call_successes.values() if success)
            total_calls = len(ctx.state.function_call_successes)
            logging.info(f"Function call success rate: {success_calls}/{total_calls} ({success_calls/total_calls*100:.1f}%)")
            
            return End(final_report)
            
        except Exception as e:
            # Log the full exception for debugging
            logging.exception(f"Error in final report creation: {str(e)}")
            
            # Create a minimal report with available data
            try:
                # Try to generate a basic summary if possible
                summary = self._generate_emergency_summary(ctx.state)
                
                # Create a minimal report with whatever data we have
                final_report = TranscriptAnalysisReport(
                    video_title=ctx.state.video_title,
                    video_id=ctx.state.video_id,
                    marketing_keywords=marketing_keywords if 'marketing_keywords' in locals() else [],
                    business_processes=business_processes if 'business_processes' in locals() else [],
                    technical_processes=technical_processes if 'technical_processes' in locals() else [],
                    technologies=technologies if 'technologies' in locals() else [],
                    summary=summary
                )
                
                logging.warning("Created minimal report due to error in final report creation")
                return End(final_report)
                
            except Exception as emergency_error:
                # Absolute last resort - create an empty report with error information
                logging.critical(f"Emergency report creation failed: {str(emergency_error)}")
                error_report = TranscriptAnalysisReport(
                    video_title=ctx.state.video_title,
                    video_id=ctx.state.video_id,
                    marketing_keywords=[],
                    business_processes=[],
                    technical_processes=[],
                    technologies=[],
                    summary=f"Error in report generation: {str(e)}"
                )
                return End(error_report)
    
    def _format_process_list(self, processes: List[Dict[str, str]]) -> str:
        """Format a list of processes for the summary prompt"""
        if not processes:
            return "None identified."
            
        formatted = []
        for i, proc in enumerate(processes[:5]):  # Limit to top 5 for brevity
            formatted.append(f"{i+1}. {proc['name']}: {proc['description'][:100]}...")
            
        if len(processes) > 5:
            formatted.append(f"... and {len(processes) - 5} more")
            
        return "\n".join(formatted)
    
    def _format_technology_list(self, technologies: List[Dict[str, str]]) -> str:
        """Format a list of technologies for the summary prompt"""
        if not technologies:
            return "None identified."
            
        formatted = []
        for i, tech in enumerate(technologies[:7]):  # Limit to top 7 for brevity
            formatted.append(f"{i+1}. {tech['name']} ({tech['category']})")
            
        if len(technologies) > 7:
            formatted.append(f"... and {len(technologies) - 7} more")
            
        return "\n".join(formatted)
    
    async def _generate_summary_with_agent(
        self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]
    ) -> str:
        """Generate a summary using the PydanticAI agent as fallback"""
        # Use the original summary agent implementation
        from agents.transcript_analysis_agents import summary_agent
        from pydantic_ai.format_as_xml import format_as_xml
        
        # Prepare XML-formatted data for the agent
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
        
        prompt = format_as_xml(summary_data)
        
        try:
            # Run the agent
            result = await summary_agent.run(
                f"Create a summary of this transcript analysis: {prompt}"
            )
            return result.data.summary
        except Exception as e:
            logging.error(f"Agent-based summary generation failed: {str(e)}")
            return self._generate_emergency_summary(ctx.state)
    
    def _generate_emergency_summary(self, state: TranscriptAnalysisState) -> str:
        """Generate a basic summary in case all other methods fail"""
        parts = []
        
        # Add basic video information
        parts.append(f"Analysis of video: {state.video_title} (ID: {state.video_id})")
        
        # Add segment information if available
        if state.segments:
            topics = [segment["topic"] for segment in state.segments]
            parts.append(f"The video contains {len(topics)} main sections: {', '.join(topics[:5])}")
            if len(topics) > 5:
                parts.append(f"...and {len(topics) - 5} more sections.")
        
        # Add keyword information if available
        if state.marketing_keywords:
            keywords = list(state.marketing_keywords)[:10]
            parts.append(f"Key terms: {', '.join(keywords)}.")
        
        # Add business and technical process counts
        process_counts = []
        if state.business_processes:
            process_counts.append(f"{len(state.business_processes)} business processes")
        if state.technical_processes:
            process_counts.append(f"{len(state.technical_processes)} technical processes")
        
        if process_counts:
            parts.append(f"The analysis identified {' and '.join(process_counts)}.")
        
        # Add technology information if available
        if state.technologies:
            tech_categories = {}
            for tech in state.technologies:
                category = tech.category
                tech_categories[category] = tech_categories.get(category, 0) + 1
                
            category_counts = [f"{count} {category.lower()} technologies" 
                              for category, count in tech_categories.items()]
            
            if category_counts:
                parts.append(f"Technologies mentioned include {', '.join(category_counts)}.")
        
        # Add note about emergency generation
        parts.append("Note: This is an automatically generated summary created when other summary methods failed.")
        
        return "\n\n".join(parts)


# For the ExtractMarketingKeywordsNode class, if it's needed
class ExtractMarketingKeywordsNode(BaseNode[TranscriptAnalysisState, AnalysisResources]):
    def __init__(self, model_name: str = "default"):
        super().__init__()
        self.model_name = model_name
    
    async def run(self, ctx: GraphRunContext[TranscriptAnalysisState, AnalysisResources]) -> Status:
        try:
            # Get transcript content from context
            transcript = ctx.state.transcript
            
            # Create agent with explicit output schema
            from pydantic_ai import Agent
            
            marketing_keywords_agent = Agent.from_recipe(
                name="marketing_keywords_extractor",
                system_prompt=f"""You are an expert at extracting marketing keywords from text.
                Analyze the transcript and extract marketing keywords that would be valuable for SEO and marketing.
                Each keyword MUST be returned as an object with 'keyword' and 'relevance' fields.
                Example format:
                {{
                    "keyword": "machine learning framework",
                    "relevance": 0.95
                }}
                The relevance score should be between 0 and 1, with higher values indicating greater relevance.
                Do not return plain strings - all keywords must be objects with the specified structure.
                """,
                user_input="Extract marketing keywords from this transcript: {transcript}",
                model=self.model_name,
                output_schema=List[MarketingKeyword],
            )
            
            logging.info(f"Calling extract_marketing_keywords with model {self.model_name}")
            result = await marketing_keywords_agent.run(
                transcript=transcript
            )
            
            # Ensure results match schema
            keywords = result.output
            
            # Manual schema compliance check and conversion
            if keywords and not isinstance(keywords[0], MarketingKeyword):
                compliant_keywords = []
                for item in keywords:
                    if isinstance(item, MarketingKeyword):
                        compliant_keywords.append(item)
                    elif isinstance(item, dict):
                        compliant_keywords.append(MarketingKeyword(**item))
                    else:
                        # Assume it's a string
                        compliant_keywords.append(MarketingKeyword(keyword=str(item), relevance_score=1.0))
                keywords = compliant_keywords
            
            logging.info(f"Extracted {len(keywords)} marketing keywords")
            ctx.state.marketing_keywords = keywords
            return Status.SUCCESS
        except Exception as e:
            logging.error(f"Error in marketing keyword extraction: {e}")
            # Provide an empty default
            ctx.state.marketing_keywords = []
            return Status.FAILURE