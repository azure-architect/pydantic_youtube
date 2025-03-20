# ollama_toolkit/__init__.py
"""
Ollama Toolkit for structured output generation with function calling.

This toolkit provides utilities for generating structured output from Ollama models
using function calling with Pydantic models for validation and schema definition.
"""

from .function_calling import call_with_function, create_function_schema
from .context import calculate_optimal_ctx_size, estimate_tokens, split_long_text

__all__ = [
    'call_with_function',
    'create_function_schema',
    'calculate_optimal_ctx_size',
    'estimate_tokens',
    'split_long_text'
]