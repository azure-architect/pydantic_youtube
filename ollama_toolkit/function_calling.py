# ollama_toolkit/function_calling.py
from typing import Type, TypeVar, List, Dict, Any, Optional
from pydantic import BaseModel
from ollama import chat
import time
import logging
import json

T = TypeVar('T', bound=BaseModel)

def create_function_schema(model_class: Type[T], function_name: str, description: str) -> Dict:
    """Create a function schema from a Pydantic model for Ollama function calling"""
    schema = model_class.model_json_schema()
    return {
        "type": "function",
        "function": {
            "name": function_name,
            "description": description,
            "parameters": schema
        }
    }

def call_with_function(
    prompt: str, 
    model_class: Type[T], 
    function_name: str, 
    description: str,
    model: str = "mistral:latest-32",
    options: Dict[str, Any] = None
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
    
    Returns:
        Dict with success status, data, and metadata
    """
    options = options or {"num_ctx": 32768}
    
    logging.info(f"Calling {function_name} with model {model}")
    
    try:
        start_time = time.time()
        
        # Modify the prompt to explicitly request JSON output
        enhanced_prompt = f"""{prompt}

IMPORTANT: Respond ONLY with a valid JSON object that matches the specified schema.
Do NOT include any additional text or explanation."""
        
        response = chat(
            model=model,
            messages=[{"role": "user", "content": enhanced_prompt}],
            format=model_class.model_json_schema(),
            options=options
        )
        
        end_time = time.time()
        logging.info(f"Request to {model} took {end_time - start_time:.2f} seconds")
        
        # Try to parse the response
        try:
            # Attempt to parse the raw content as JSON
            result = model_class.model_validate_json(response['message']['content'])
            return {
                "success": True, 
                "data": result, 
                "response_time": end_time - start_time,
                "raw_response": response
            }
        except json.JSONDecodeError as json_err:
            # If JSON parsing fails, try to extract JSON from the response
            logging.warning(f"JSON decoding error: {json_err}")
            try:
                # Use regex or other extraction methods if needed
                import re
                json_match = re.search(r'(\{.*\})', response['message']['content'], re.DOTALL)
                if json_match:
                    result = model_class.model_validate_json(json_match.group(1))
                    return {
                        "success": True, 
                        "data": result, 
                        "response_time": end_time - start_time,
                        "raw_response": response
                    }
            except Exception as extract_err:
                logging.error(f"JSON extraction failed: {extract_err}")
                return {
                    "success": False, 
                    "error": f"Could not parse JSON: {str(extract_err)}",
                    "raw_response": response['message']['content']
                }
        
    except Exception as e:
        logging.error(f"Error in Ollama request: {str(e)}")
        return {"success": False, "error": str(e), "error_type": type(e).__name__}