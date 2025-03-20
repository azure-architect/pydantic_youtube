import asyncio
import httpx
import time
import sys
import os
import json
from pathlib import Path
from pydantic_graph.persistence.file import FileStatePersistence

# Add module directories to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from state.transcript_analysis_state import TranscriptAnalysisState, AnalysisResources
from graph.transcript_analysis_graph import transcript_analysis_graph
from graph.transcript_analysis_nodes import SegmentTranscript
from utils.transcript_loader import load_transcript_from_file, clean_transcript, get_youtube_video_id
from utils.youtube_downloader import fetch_transcript_from_url
from utils.export_utils import (
    export_report_to_json, export_keywords_to_csv,
    export_technologies_to_csv, create_report_folder
)

async def analyze_youtube_transcript(transcript: str, video_title: str, video_id: str, run_id: str = None, model: str = "mistral:latest-32"):
    """Run a complete YouTube transcript analysis workflow"""
    
    if not run_id:
        run_id = f"yt_analysis_{video_id}_{int(time.time())}"
    
    # Set up persistence
    persistence = FileStatePersistence(Path(f"{run_id}.json"))
    
    # Initialize dependencies
    async with httpx.AsyncClient() as http_client:
        deps = AnalysisResources(
            http_client=http_client,
            api_key="your-api-key",
            model=model,
            # Optional: load technology taxonomy from file or database
            tech_taxonomy={
                "programming_languages": ["Python", "JavaScript", "Java", "C++"],
                "databases": ["MySQL", "PostgreSQL", "MongoDB", "Redis"],
                "cloud_services": ["AWS", "Azure", "GCP", "Heroku"],
                # Add more categories as needed
            },
            # Optional: load marketing keywords database
            marketing_keywords_db=["conversion", "engagement", "ROI", "KPI"]
        )
        
        # Set up state
        state = TranscriptAnalysisState(
            transcript=transcript,
            video_title=video_title,
            video_id=video_id
        )
        
        print(f"Starting analysis of: {video_title} (ID: {video_id})")
        print(f"Transcript length: {len(transcript)} characters")
        print(f"Using model: {model}")
        
        # Run the graph
        result = await transcript_analysis_graph.run(
            SegmentTranscript(), 
            state=state,
            deps=deps,
            persistence=persistence
        )
        
        print(f"Analysis completed successfully!")
        
        # Return the final report
        return result.output
        
async def main():
    # Example command line usage
    import argparse
    
    parser = argparse.ArgumentParser(description='Analyze YouTube video transcript')
    parser.add_argument('--transcript-file', help='Path to the transcript file')
    parser.add_argument('--url', help='YouTube video URL')
    parser.add_argument('--title', help='Video title (optional if URL is provided)')
    parser.add_argument('--video-id', help='YouTube video ID (optional if URL is provided)')
    parser.add_argument('--run-id', help='Optional run ID for persistence')
    parser.add_argument('--language', default='en', help='Preferred transcript language')
    parser.add_argument('--model', default='mistral:latest-32', help='Ollama model to use')
    parser.add_argument('--output-dir', help='Custom output directory for results')
    args = parser.parse_args()
    
    if not args.transcript_file and not args.url:
        parser.error("Either --transcript-file or --url must be provided")
    
    # Determine video information and get transcript
    transcript = None
    video_id = args.video_id
    video_title = args.title
    
    if args.url:
        print(f"Fetching transcript from URL: {args.url}")
        result = fetch_transcript_from_url(args.url, languages=[args.language])
        
        if result["success"]:
            transcript = result["transcript"]
            video_id = result["video_id"]
            # Use provided title if available, otherwise use the one from the video
            video_title = args.title if args.title else result["title"]
            print(f"Successfully fetched transcript for video: {video_title}")
        else:
            print(f"Error: {result['error']}")
            return
    else:
        # Load and clean transcript from file
        transcript = load_transcript_from_file(args.transcript_file)
        
        # If URL was in the title, try to extract video ID
        if not video_id and args.title and ("youtube.com" in args.title or "youtu.be" in args.title):
            video_id = get_youtube_video_id(args.title)
    
    # Clean the transcript
    transcript = clean_transcript(transcript)
    
    # Generate a video ID if still not available
    if not video_id:
        video_id = f"video_{int(time.time())}"
    
    # Make sure we have a title
    if not video_title:
        video_title = f"Video {video_id}"
    
    # Run analysis
    report = await analyze_youtube_transcript(
        transcript=transcript,
        video_title=video_title,
        video_id=video_id,
        run_id=args.run_id,
        model=args.model
    )
    
    # Create output folder
    if args.output_dir:
        output_folder = Path(args.output_dir)
        output_folder.mkdir(parents=True, exist_ok=True)
    else:
        output_folder = create_report_folder(video_id)
    
    # Export results
    export_report_to_json(report, f"{output_folder}/full_report.json")
    export_keywords_to_csv(report, f"{output_folder}/marketing_keywords.csv")
    export_technologies_to_csv(report, f"{output_folder}/technologies.csv")
    
    # Print results
    print(f"\nAnalysis complete for: {report.video_title}")
    print(f"Results saved to: {output_folder}")
    
    print("\n=== SUMMARY ===")
    print(report.summary)
    
    print("\n=== STATISTICS ===")
    print(f"Marketing Keywords: {len(report.marketing_keywords)}")
    print(f"Business Processes: {len(report.business_processes)}")
    print(f"Technical Processes: {len(report.technical_processes)}")
    print(f"Technologies: {len(report.technologies)}")

if __name__ == "__main__":
    asyncio.run(main())