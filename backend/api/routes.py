"""
API Routes for Resume Optimization Service
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, List, Optional
import sys
import os

# Add parent directory to path to import aro
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aro.llm_adapter import create_llm_adapter

router = APIRouter()


# Request/Response Models
class GenerateRequest(BaseModel):
    """Request model for resume generation"""
    jd_text: str
    profile_data: Dict[str, Any]
    settings: Optional[Dict[str, Any]] = {
        "max_iterations": 5,
        "score_threshold": 85,
        "stop_if_no_improvement": 2
    }


class GenerateResponse(BaseModel):
    """Response model for resume generation"""
    resume_json: Dict[str, Any]
    iterations: List[Dict[str, Any]]
    final_score: float
    generation_time: float


class EvaluateRequest(BaseModel):
    """Request model for resume evaluation"""
    jd_text: str
    resume_json: Dict[str, Any]


class EvaluateResponse(BaseModel):
    """Response model for evaluation"""
    total_score: float
    breakdown: Dict[str, float]
    missing_keywords: List[str]
    improvements: List[Dict[str, Any]]
    overall_feedback: str


@router.post("/generate", response_model=GenerateResponse)
async def generate_resume(request: GenerateRequest):
    """
    Generate optimized resume using multi-agent system
    
    Process:
    1. Generator creates initial resume
    2. Evaluator scores it
    3. Reviser plans improvements
    4. Loop until threshold met or max iterations
    """
    try:
        # TODO: Implement full generation loop
        # For now, return mock response
        
        return {
            "resume_json": {
                "summary": "Generated summary...",
                "skills": [],
                "experience": [],
                "projects": []
            },
            "iterations": [],
            "final_score": 0.0,
            "generation_time": 0.0
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/evaluate", response_model=EvaluateResponse)
async def evaluate_resume(request: EvaluateRequest):
    """
    Evaluate resume against job description
    
    Returns scoring breakdown and improvement suggestions
    """
    try:
        # TODO: Implement evaluator agent
        
        return {
            "total_score": 0.0,
            "breakdown": {
                "keyword_match": 0.0,
                "semantic_alignment": 0.0,
                "quant_metrics": 0.0,
                "role_specific_skills": 0.0
            },
            "missing_keywords": [],
            "improvements": [],
            "overall_feedback": ""
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/test")
async def test_llm():
    """Test LLM connection"""
    try:
        provider = os.getenv("LLM_PROVIDER", "mock")
        llm = create_llm_adapter(provider)
        
        response = llm.generate("Say 'Hello from the LLM!' in one sentence.", max_tokens=50, temperature=0)
        
        return {
            "status": "success",
            "provider": provider,
            "response": response
        }
    
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }
