# Enhanced ollama_toolkit/function_calling.py
from typing import Type, TypeVar, List, Dict, Any, Optional, Union
from pydantic import BaseModel
from ollama import chat
import time
import logging
import json
import re

T = TypeVar('T', bound=BaseModel)

def create_function_schema(model_class: Type[T], function_name: str, description: str) -> Dict:
    """
    Create a function schema from a Pydantic model for Ollama function calling
    
    Args:
        model_class: Pydantic model class to convert to schema
        function_name: Name of the function
        description: Description of the function
        
    Returns:
        Function schema dictionary
    """
    schema = model_class.model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": function_name,
            "description": description,
            "parameters": schema
        }
    }

def extract_json_from_text(text: str) -> Optional[Dict[str, Any]]:
    """
    Extract JSON from text that may contain explanatory content
    
    Args:
        text: Text that may contain JSON
        
    Returns:
        Extracted JSON as dict or None if extraction failed
    """
    # First try to find JSON in markdown code blocks
    json_match = re.search(r'```(?:json)?\s*([\s\S]*?)\s*```', text, re.DOTALL)
    if json_match:
        json_str = json_match.group(1).strip()
    else:
        # Try to find JSON object with braces
        json_match = re.search(r'(\{[\s\S]*\})', text, re.DOTALL)
        if json_match:
            json_str = json_match.group(1).strip()
        else:
            # Try to find JSON array
            json_match = re.search(r'(\[[\s\S]*\])', text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1).strip()
            else:
                return None
    
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None

def call_with_function(
    prompt: str, 
    model_class: Type[T], 
    function_name: str, 
    description: str,
    model: str = "mistral:latest-32",
    options: Dict[str, Any] = None,
    timeout: int = 120,
    max_retries: int = 2
) -> Dict[str, Any]:
    """
    Make a call to Ollama with function calling to get structured output
    
    Args:
        prompt: Input prompt
        model_class: Pydantic model class for validation
        function_name: Name of the function
        description: Function description
        model: Ollama model to use
        options: Additional Ollama API options
        timeout: Timeout in seconds
        max_retries: Maximum number of retries for failures
        
    Returns:
        Dict with success status, data, and metadata
    """
    options = options or {"num_ctx": 32768}
    
    logging.info(f"Calling {function_name} with model {model}")
    
    # Add explicit instructions for structured output
    enhanced_prompt = f"""{prompt}

IMPORTANT: Your response must be a valid JSON object that precisely matches this schema:
{json.dumps(model_class.model_json_schema(), indent=2)}

DO NOT include any explanatory text outside the JSON.
"""
    
    # Try with retries
    for attempt in range(max_retries + 1):
        try:
            start_time = time.time()
            
            response = chat(
                model=model,
                messages=[{"role": "user", "content": enhanced_prompt}],
                format=model_class.model_json_schema(),
                options=options
            )
            
            end_time = time.time()
            logging.info(f"Request to {model} took {end_time - start_time:.2f} seconds")
            
            # Try to parse the response - first as proper JSON
            try:
                if "message" in response and "content" in response["message"]:
                    content = response["message"]["content"]
                    
                    # First attempt: direct validation
                    try:
                        result = model_class.model_validate_json(content)
                        return {
                            "success": True, 
                            "data": result, 
                            "response_time": end_time - start_time,
                            "raw_response": response
                        }
                    except Exception as e:
                        # Second attempt: extract JSON from text
                        logging.warning(f"Direct validation failed: {e}")
                        extracted_json = extract_json_from_text(content)
                        
                        if extracted_json:
                            result = model_class.model_validate(extracted_json)
                            return {
                                "success": True, 
                                "data": result, 
                                "response_time": end_time - start_time,
                                "raw_response": response
                            }
                        else:
                            logging.error(f"Could not extract valid JSON from response")
                            if attempt < max_retries:
                                logging.info(f"Retrying... (attempt {attempt + 1}/{max_retries})")
                                continue
                            return {
                                "success": False, 
                                "error": "Invalid JSON format in response",
                                "raw_response": response
                            }
                else:
                    if attempt < max_retries:
                        logging.info(f"Unexpected response format. Retrying... (attempt {attempt + 1}/{max_retries})")
                        continue
                    return {
                        "success": False, 
                        "error": "Unexpected response format",
                        "raw_response": response
                    }
            except Exception as json_err:
                logging.error(f"Error processing response: {json_err}")
                if attempt < max_retries:
                    logging.info(f"Retrying... (attempt {attempt + 1}/{max_retries})")
                    continue
                return {
                    "success": False, 
                    "error": f"Error processing response: {json_err}",
                    "raw_response": response
                }
        except Exception as e:
            logging.error(f"Error in Ollama request: {e}")
            if attempt < max_retries:
                logging.info(f"Retrying... (attempt {attempt + 1}/{max_retries})")
                continue
            return {
                "success": False, 
                "error": f"Error in Ollama request: {e}",
                "error_type": type(e).__name__
            }
    
    # If we reached here, all retries failed
    return {
        "success": False, 
        "error": "All retry attempts failed",
    }