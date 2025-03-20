import json
import csv
from pathlib import Path
from datetime import datetime
from models.transcript_analysis_models import TranscriptAnalysisReport

def export_report_to_json(report: TranscriptAnalysisReport, output_file: str):
    """Serialize and save the report to a JSON file"""
    # Convert Pydantic model to dict
    report_dict = report.dict()
    
    # Write to file with pretty formatting
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report_dict, f, indent=2)
    
    print(f"Report exported to {output_file}")

def export_keywords_to_csv(report: TranscriptAnalysisReport, output_file: str):
    """Export marketing keywords to CSV file"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Keyword', 'Relevance Score', 'Context', 'Frequency'])
        
        for keyword in report.marketing_keywords:
            writer.writerow([
                keyword.keyword,
                keyword.relevance_score,
                keyword.context,
                keyword.frequency
            ])
    
    print(f"Keywords exported to {output_file}")

def export_technologies_to_csv(report: TranscriptAnalysisReport, output_file: str):
    """Export technologies to CSV file"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Category', 'Description', 'Inference Type', 'Confidence'])
        
        for tech in report.technologies:
            writer.writerow([
                tech.name,
                tech.category,
                tech.description,
                tech.inference_type,
                tech.confidence_score
            ])
    
    print(f"Technologies exported to {output_file}")

def create_report_folder(video_id: str) -> Path:
    """Create a folder for storing report files"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = Path(f"reports/{video_id}_{timestamp}")
    folder.mkdir(parents=True, exist_ok=True)
    return folder