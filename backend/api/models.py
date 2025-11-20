"""
Pydantic Models for API Request/Response
"""
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List


# Request Models

class GenerateRequest(BaseModel):
    """Request to generate resume"""
    username: str = Field(default="chandan", description="Username")
    jd_text: str = Field(..., description="Job description text")
    company: str = Field(..., description="Company name")
    role: str = Field(..., description="Job role")
    optimize: bool = Field(default=True, description="Run optimization loops")


class EvaluateRequest(BaseModel):
    """Request to evaluate resume"""
    username: str = Field(default="chandan")
    job_id: str = Field(..., description="Job ID")


class FactualityRequest(BaseModel):
    """Request to check factuality"""
    username: str = Field(default="chandan")
    job_id: str = Field(..., description="Job ID")


class CreateJobRequest(BaseModel):
    """Request to create job"""
    job_id: str = Field(..., description="Job ID")
    company: str = Field(..., description="Company name")
    role: str = Field(..., description="Job role")
    jd_text: str = Field(..., description="Job description")


# Response Models

class GenerateResponse(BaseModel):
    """Response from generate endpoint"""
    success: bool
    resume: Optional[Dict[str, Any]] = None
    scores: Optional[Dict[str, float]] = None
    paths: Optional[Dict[str, str]] = None
    error: Optional[str] = None


class EvaluateResponse(BaseModel):
    """Response from evaluate endpoint"""
    total_score: float
    keyword_score: float
    llm_score: float
    section_scores: Dict[str, float]
    feedback: str
    section_feedback: Dict[str, str]


class FactualityResponse(BaseModel):
    """Response from factuality endpoint"""
    is_factual: bool
    factuality_score: float
    issues: List[str]
    summary_check: Dict[str, Any]
    experience_check: Dict[str, Any]
    projects_check: Dict[str, Any]
    skills_check: Dict[str, Any]


class ResumeResponse(BaseModel):
    """Response for get resume"""
    resume: Dict[str, Any]
    metadata: Dict[str, Any]


class JobListResponse(BaseModel):
    """Response for list jobs"""
    jobs: List[Dict[str, str]]


class ResumeListResponse(BaseModel):
    """Response for list resumes"""
    username: str
    resumes: List[Dict[str, Any]]


class HealthResponse(BaseModel):
    """Response for health check"""
    status: str
    gemini_api: str
    version: str


class ErrorResponse(BaseModel):
    """Error response"""
    success: bool = False
    error: str
    detail: Optional[str] = None
