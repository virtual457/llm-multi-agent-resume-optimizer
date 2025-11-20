"""
ARO - Autonomous Resume Optimizer

Multi-agent system for resume generation and optimization.
"""

__version__ = "0.1.0"
__author__ = "Chandan Gowda K S"

from .llm_adapter import LLMAdapter, GeminiAdapter, MockAdapter, create_llm_adapter

__all__ = [
    "LLMAdapter",
    "GeminiAdapter",
    "MockAdapter",
    "create_llm_adapter"
]
