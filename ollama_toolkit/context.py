# ollama_toolkit/context.py
from typing import Optional, List

def calculate_optimal_ctx_size(text: str) -> int:
    """
    Determine optimal context window size based on input length
    
    Args:
        text: Input text
        
    Returns:
        Optimal context window size
    """
    token_estimate = len(text.split()) * 1.3  # Rough token estimate
    return min(max(int(token_estimate * 2), 4096), 32768)  # Min 4K, max 32K

def estimate_tokens(text: str) -> int:
    """
    Estimate the number of tokens in a text
    
    Args:
        text: Input text
        
    Returns:
        Estimated token count
    """
    # Simple estimation based on words
    return int(len(text.split()) * 1.3)

def split_long_text(text: str, max_tokens: int = 30000) -> List[str]:
    """
    Split text that's too long for context window into manageable chunks
    
    Args:
        text: Text to split
        max_tokens: Maximum tokens per chunk
        
    Returns:
        List of text chunks
    """
    # Simple paragraph-based splitting
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = []
    current_size = 0
    
    for para in paragraphs:
        para_size = estimate_tokens(para)
        
        if current_size + para_size > max_tokens:
            # This paragraph would exceed the limit, start a new chunk
            if current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [para]
                current_size = para_size
            else:
                # Single paragraph is too large, just add it and move on
                chunks.append(para)
                current_chunk = []
                current_size = 0
        else:
            # Add paragraph to current chunk
            current_chunk.append(para)
            current_size += para_size
    
    # Don't forget the last chunk
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks