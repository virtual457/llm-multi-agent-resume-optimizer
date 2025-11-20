"""
API Routes
"""
from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from fastapi.responses import StreamingResponse
from pathlib import Path
import json
import sys
import os

# Add parent to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.models import (
    GenerateRequest, GenerateResponse,
    EvaluateRequest, EvaluateResponse,
    FactualityRequest, FactualityResponse,
    CreateJobRequest,
    ResumeResponse, JobListResponse, ResumeListResponse,
    HealthResponse, ErrorResponse
)
from src.generator import Generator
from src.evaluator import Evaluator
from src.factuality_checker import FactualityChecker
from src.reviser import Reviser
from src.renderer import Renderer
from src.providers import UserProvider, JobProvider, ResumeProvider
from src.streaming_pipeline import optimize_resume_stream
from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

router = APIRouter()

# Initialize LLM (reuse across requests)
llm = create_llm_adapter("gemini")


@router.post("/generate", response_model=GenerateResponse)
async def generate_resume(request: GenerateRequest):
    """Generate optimized resume"""
    try:
        # Get user profile
        user_profile = UserProvider.get(request.username)
        
        # Create job entry
        job_id = f"temp_{request.company.lower().replace(' ', '_')}"
        job_data = {
            "company": request.company,
            "role": request.role,
            "jd_text": request.jd_text
        }
        
        # Save job temporarily
        job_path = Path(__file__).parent.parent / "database" / "jobs" / f"{job_id}.json"
        job_path.parent.mkdir(exist_ok=True)
        with open(job_path, 'w') as f:
            json.dump(job_data, f, indent=2)
        
        if request.optimize:
            # Run full optimization pipeline
            from src.main import optimize_resume
            # Temporarily save job, run optimization
            resume, eval_result, fact_result = optimize_resume(request.username, job_id)
            
            return GenerateResponse(
                success=True,
                resume=resume,
                scores={
                    "evaluation": eval_result['total_score'],
                    "factuality": fact_result['factuality_score']
                },
                paths={
                    "json": str(ResumeProvider.save(resume, request.username, job_id)),
                    "docx": f"output/{request.username}_{job_id}.docx"
                }
            )
        else:
            # Just generate, no optimization
            generator = Generator(llm)
            resume = generator.generate(request.jd_text, user_profile, request.company, request.role)
            
            return GenerateResponse(
                success=True,
                resume=resume,
                scores=None,
                paths=None
            )
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/evaluate", response_model=EvaluateResponse)
async def evaluate_resume(request: EvaluateRequest):
    """Evaluate resume against JD"""
    try:
        resume = ResumeProvider.get(request.username, request.job_id)
        job = JobProvider.get(request.job_id)
        
        evaluator = Evaluator(llm)
        result = evaluator.evaluate(resume, job['jd_text'])
        
        return EvaluateResponse(**result)
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/factuality", response_model=FactualityResponse)
async def check_factuality(request: FactualityRequest):
    """Check resume factuality"""
    try:
        resume = ResumeProvider.get(request.username, request.job_id)
        profile = UserProvider.get(request.username)
        
        checker = FactualityChecker(llm)
        result = checker.check(resume, profile)
        
        return FactualityResponse(**result)
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/resume/{username}/{job_id}", response_model=ResumeResponse)
async def get_resume(username: str, job_id: str):
    """Get generated resume"""
    try:
        # Get resume with metadata
        resume_dir = Path(__file__).parent.parent / "database" / "resumes" / username
        filepath = resume_dir / f"{job_id}.json"
        
        if not filepath.exists():
            raise HTTPException(status_code=404, detail=f"Resume not found for {username}/{job_id}")
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return ResumeResponse(
            resume=data['resume'],
            metadata=data['metadata']
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/user/upload")
async def upload_user_profile(username: str = Query(...), file: UploadFile = File(...)):
    """Upload user profile JSON"""
    try:
        # Read file
        content = await file.read()
        profile_data = json.loads(content)
        
        # Save to database
        user_dir = Path(__file__).parent.parent / "database" / username
        user_dir.mkdir(parents=True, exist_ok=True)
        
        profile_path = user_dir / "profile.json"
        with open(profile_path, 'w') as f:
            json.dump(profile_data, f, indent=2)
        
        return {
            "success": True,
            "message": "Profile uploaded successfully",
            "username": username,
            "path": str(profile_path)
        }
        
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON file")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/job/create")
async def create_job(request: CreateJobRequest):
    """Create job description"""
    try:
        job_data = {
            "company": request.company,
            "role": request.role,
            "jd_text": request.jd_text
        }
        
        job_path = Path(__file__).parent.parent / "database" / "jobs" / f"{request.job_id}.json"
        job_path.parent.mkdir(exist_ok=True)
        
        with open(job_path, 'w') as f:
            json.dump(job_data, f, indent=2)
        
        return {
            "success": True,
            "job_id": request.job_id,
            "path": str(job_path)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/jobs", response_model=JobListResponse)
async def list_jobs():
    """List all jobs"""
    try:
        jobs_dir = Path(__file__).parent.parent / "database" / "jobs"
        jobs = []
        
        if jobs_dir.exists():
            for job_file in jobs_dir.glob("*.json"):
                with open(job_file, 'r') as f:
                    job_data = json.load(f)
                    jobs.append({
                        "job_id": job_file.stem,
                        "company": job_data.get('company', ''),
                        "role": job_data.get('role', '')
                    })
        
        return JobListResponse(jobs=jobs)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/resumes/{username}", response_model=ResumeListResponse)
async def list_resumes(username: str):
    """List all resumes for user"""
    try:
        resumes_dir = Path(__file__).parent.parent / "database" / "resumes" / username
        resumes = []
        
        if resumes_dir.exists():
            for resume_file in resumes_dir.glob("*.json"):
                with open(resume_file, 'r') as f:
                    data = json.load(f)
                    
                    # Get job info
                    job_id = resume_file.stem
                    try:
                        job = JobProvider.get(job_id)
                        company = job.get('company', '')
                        role = job.get('role', '')
                    except:
                        company = ''
                        role = ''
                    
                    resumes.append({
                        "job_id": job_id,
                        "company": company,
                        "role": role,
                        "updated_at": data['metadata'].get('updated_at', '')
                    })
        
        return ResumeListResponse(username=username, resumes=resumes)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/generate/stream")
async def generate_resume_stream(request: GenerateRequest):
    """Generate resume with real-time status updates via SSE"""
    import asyncio
    
    def event_generator():
        try:
            for update in optimize_resume_stream(
                username=request.username,
                jd_text=request.jd_text,
                company=request.company,
                role=request.role
            ):
                # Send as SSE format
                yield f"data: {json.dumps(update)}\n\n"
        except Exception as e:
            error_update = {
                "stage": "error",
                "message": f"Error: {str(e)}",
                "progress": 0,
                "error": str(e)
            }
            yield f"data: {json.dumps(error_update)}\n\n"
    
    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no"  # Disable buffering in nginx
        }
    )


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """API health check"""
    try:
        # Quick test of Gemini API with higher token limit
        test_response = llm.generate("test", max_tokens=100)
        gemini_status = "available" if test_response else "unavailable"
    except:
        gemini_status = "unavailable"
    
    return HealthResponse(
        status="healthy",
        gemini_api=gemini_status,
        version="0.1.0"
    )
