"""
Resume optimization pipeline with streaming status updates
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
from src.generator import Generator
from src.evaluator import Evaluator
from src.factuality_checker import FactualityChecker
from src.reviser import Reviser
from src.renderer import Renderer
from src.providers import UserProvider, JobProvider, ResumeProvider
from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv
import json
import time

load_dotenv()


def optimize_resume_stream(username: str, jd_text: str, company: str, role: str):
    """
    Resume optimization with streaming status updates.
    Yields status dictionaries at each stage.
    """
    try:
        # Setup
        yield {
            "stage": "setup",
            "message": "Loading user profile and initializing components...",
            "progress": 5
        }
        time.sleep(0.5)  # Allow SSE to flush
        
        user_profile = UserProvider.get(username)
        llm = create_llm_adapter("gemini")
        generator = Generator(llm)
        evaluator = Evaluator(llm, debug=False)
        factuality_checker = FactualityChecker(llm, debug=False)
        reviser = Reviser(llm, debug=False)
        
        # PHASE 1: Generation
        yield {
            "stage": "generating",
            "message": "Generating initial resume from job description...",
            "progress": 10
        }
        time.sleep(0.5)  # Allow SSE to flush
        
        resume = generator.generate(
            jd_text=jd_text,
            user_profile=user_profile,
            company=company,
            role=role
        )
        
        yield {
            "stage": "generated",
            "message": "Initial resume created successfully",
            "progress": 25
        }
        time.sleep(0.5)  # Allow SSE to flush
        
        # PHASE 2: Evaluation Loop
        eval_threshold = 90
        max_eval_revisions = 3
        eval_result = None
        
        for eval_iteration in range(1, max_eval_revisions + 2):
            yield {
                "stage": "evaluating",
                "message": f"Evaluating resume against job requirements (attempt {eval_iteration}/{max_eval_revisions + 1})...",
                "progress": 25 + (eval_iteration * 10),
                "iteration": eval_iteration
            }
            
            eval_result = evaluator.evaluate(resume, jd_text)
            score = eval_result['total_score']
            
            yield {
                "stage": "evaluation_result",
                "message": f"Evaluation score: {score}/100",
                "progress": 30 + (eval_iteration * 10),
                "score": score,
                "iteration": eval_iteration
            }
            
            if score >= eval_threshold:
                yield {
                    "stage": "evaluation_passed",
                    "message": f"Resume meets quality threshold ({score}/100)",
                    "progress": 50
                }
                break
            
            if eval_iteration > max_eval_revisions:
                yield {
                    "stage": "evaluation_max_reached",
                    "message": f"Maximum evaluation attempts reached. Proceeding with score: {score}/100",
                    "progress": 50
                }
                break
            
            yield {
                "stage": "revising_evaluation",
                "message": f"Improving resume based on feedback (revision {eval_iteration})...",
                "progress": 35 + (eval_iteration * 10)
            }
            
            feedback_text = json.dumps(eval_result, indent=2)
            resume = reviser.revise(resume, jd_text, user_profile, feedback_text, "evaluation")
        
        # PHASE 3: Factuality Check Loop
        fact_threshold = 90
        max_fact_revisions = 3
        fact_result = None
        
        for fact_iteration in range(1, max_fact_revisions + 2):
            yield {
                "stage": "checking_factuality",
                "message": f"Verifying factual accuracy (attempt {fact_iteration}/{max_fact_revisions + 1})...",
                "progress": 50 + (fact_iteration * 10),
                "iteration": fact_iteration
            }
            
            fact_result = factuality_checker.check(resume, user_profile)
            score = fact_result['factuality_score']
            
            yield {
                "stage": "factuality_result",
                "message": f"Factuality score: {score}/100",
                "progress": 55 + (fact_iteration * 10),
                "score": score,
                "iteration": fact_iteration
            }
            
            if score >= fact_threshold:
                yield {
                    "stage": "factuality_passed",
                    "message": f"Resume is factually accurate ({score}/100)",
                    "progress": 80
                }
                break
            
            if fact_iteration > max_fact_revisions:
                yield {
                    "stage": "factuality_max_reached",
                    "message": f"Maximum factuality attempts reached. Proceeding with score: {score}/100",
                    "progress": 80
                }
                break
            
            yield {
                "stage": "revising_factuality",
                "message": f"Fixing factuality issues (revision {fact_iteration})...",
                "progress": 60 + (fact_iteration * 10)
            }
            
            feedback_text = json.dumps(fact_result, indent=2)
            resume = reviser.revise(resume, jd_text, user_profile, feedback_text, "factuality")
        
        # PHASE 4: Save and Render
        yield {
            "stage": "saving",
            "message": "Saving resume to database...",
            "progress": 85
        }
        
        # Create temporary job_id from company and role
        job_id = f"temp_{company.lower().replace(' ', '_')}_{role.lower().replace(' ', '_')}"
        
        # Save job first
        JobProvider.save({
            "job_id": job_id,
            "company": company,
            "role": role,
            "jd_text": jd_text
        })
        
        # Save resume
        saved_json_path = ResumeProvider.save(resume, username, job_id)
        
        yield {
            "stage": "rendering",
            "message": "Creating formatted DOCX document...",
            "progress": 90
        }
        
        # Render to DOCX
        template_path = Path(__file__).parent.parent.parent / "templates" / "Chandan_Resume_Format.docx"
        saved_docx_path = None
        
        if template_path.exists():
            renderer = Renderer(str(template_path))
            output_dir = Path(__file__).parent.parent / "output"
            output_dir.mkdir(exist_ok=True)
            docx_output = output_dir / f"{username}_{job_id}.docx"
            saved_docx_path = renderer.render(resume, str(docx_output))
        
        # Final result
        yield {
            "stage": "complete",
            "message": "Resume optimization complete!",
            "progress": 100,
            "data": {
                "resume": resume,
                "scores": {
                    "evaluation": eval_result,
                    "factuality": fact_result
                },
                "paths": {
                    "json_path": saved_json_path,
                    "docx_path": saved_docx_path,
                    "job_id": job_id
                }
            }
        }
        
    except Exception as e:
        yield {
            "stage": "error",
            "message": f"Error: {str(e)}",
            "progress": 0,
            "error": str(e)
        }
