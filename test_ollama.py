# ollama_test.py
import requests
import json
import sys

def test_ollama(prompt):
    """Test Ollama with a simple prompt"""
    url = "http://localhost:11434/v1/chat/completions"
    
    payload = {
        "model": "mistral:latest-32",  # Update to your model name
        "messages": [
            {
                "role": "system", 
                "content": "You are a helpful assistant that structures information clearly."
            },
            {
                "role": "user", 
                "content": prompt
            }
        ],
        "temperature": 0.1
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        
        print("\nOllama Response:")
        if "choices" in result and len(result["choices"]) > 0:
            content = result["choices"][0].get("message", {}).get("content", "")
            print(content)
        else:
            print(json.dumps(result, indent=2))
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    prompt = "Divide this text into 3 segments with topics and content:\n\n"
    prompt += "Hello and welcome to this video on Python programming. "
    prompt += "Today we'll cover the basics. First, let's talk about variables. "
    prompt += "Variables are containers for storing data values. Next, we'll look at control flow. "
    prompt += "If statements and loops are important for controlling program flow."
    
    test_ollama(prompt)