# tests/mocks/ollama_responses.py
"""
Mock responses for Ollama API calls
"""
import json

# Mock response for topic identification
TOPICS_RESPONSE = {
    "message": {
        "content": json.dumps({
            "sections": ["Introduction", "Variables", "Control Structures", "Functions"]
        })
    }
}

# Mock response for segment extraction
SEGMENT_RESPONSE = {
    "message": {
        "content": json.dumps({
            "topic": "Introduction",
            "content": "Hello and welcome to this tutorial on Python programming."
        })
    }
}

# Mock response for keyword extraction
KEYWORDS_RESPONSE = {
    "message": {
        "content": json.dumps({
            "keywords": ["Python", "programming", "variables", "control structures", "functions"]
        })
    }
}

# Mock response for business process extraction
BUSINESS_PROCESS_RESPONSE = {
    "message": {
        "content": json.dumps({
            "processes": [
                {
                    "name": "Learning Python",
                    "description": "Process of learning Python programming",
                    "inference_type": "INFERRED",
                    "transcript_references": ["This tutorial on Python programming"],
                    "steps": [
                        {"description": "Learn variables", "order": 1},
                        {"description": "Learn control structures", "order": 2},
                        {"description": "Learn functions", "order": 3}
                    ]
                }
            ]
        })
    }
}

# Mock response for technology extraction
TECHNOLOGY_RESPONSE = {
    "message": {
        "content": json.dumps({
            "technologies": [
                {
                    "name": "Python",
                    "category": "Programming Language",
                    "description": "High-level programming language",
                    "inference_type": "DIRECT",
                    "transcript_references": ["Python programming"]
                }
            ]
        })
    }
}

# tests/mocks/ollama_responses.py (continued)
ERROR_RESPONSE = {
   "message": {
       "content": "Invalid JSON response that does not conform to the expected schema"
   }
}

# Mock general error
EXCEPTION_RESPONSE = Exception("Connection error with Ollama server")

# Mock timeout error
TIMEOUT_RESPONSE = Exception("Request timed out after 30 seconds")

# Dictionary mapping function names to mock responses
MOCK_RESPONSES = {
   "identify_transcript_topics": TOPICS_RESPONSE,
   "extract_transcript_segment": SEGMENT_RESPONSE,
   "extract_marketing_keywords": KEYWORDS_RESPONSE,
   "extract_business_processes": BUSINESS_PROCESS_RESPONSE,
   "extract_technologies": TECHNOLOGY_RESPONSE,
   "error_response": ERROR_RESPONSE
}

# Mock function to get appropriate response based on function name
def get_mock_response(function_name, error=False, timeout=False):
   """
   Get a mock response for a particular function call
   
   Args:
       function_name: The name of the function being called
       error: Whether to return an error response
       timeout: Whether to simulate a timeout
   
   Returns:
       A mock response object
   """
   if timeout:
       return TIMEOUT_RESPONSE
   
   if error:
       return ERROR_RESPONSE
   
   return MOCK_RESPONSES.get(function_name, MOCK_RESPONSES["error_response"])