"""
Main Loop - Complete resume optimization pipeline
"""
import sys
import os

# Add parent directory to path
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

load_dotenv()


def optimize_resume(username: str = "chandan", job_id: str = "job1"):
    """
    Complete optimization pipeline:
    1. Generate resume
    2. Evaluate against JD (up to 3 revisions if score < 90)
    3. Check factuality (up to 3 revisions if score < 90)
    4. Save final resume
    """
    print("=" * 70)
    print("RESUME OPTIMIZATION PIPELINE")
    print("=" * 70)
    
    # Load data
    print("\n[SETUP] Loading data...")
    user_profile = UserProvider.get(username)
    job = JobProvider.get(job_id)
    print(f"  User: {user_profile['personal']['name']}")
    print(f"  Job: {job['role']} at {job['company']}")
    
    # Initialize components
    print("\n[SETUP] Initializing components...")
    llm = create_llm_adapter("gemini")
    generator = Generator(llm)
    evaluator = Evaluator(llm, debug=False)
    factuality_checker = FactualityChecker(llm, debug=False)
    reviser = Reviser(llm, debug=False)
    print("  ✓ All components ready")
    
    # PHASE 1: Initial Generation
    print("\n" + "="*70)
    print("PHASE 1: INITIAL GENERATION")
    print("="*70)
    
    resume = generator.generate(
        jd_text=job['jd_text'],
        user_profile=user_profile,
        company=job['company'],
        role=job['role']
    )
    print("  ✓ Resume generated")
    
    # PHASE 2: Evaluation Loop (max 3 revisions)
    print("\n" + "="*70)
    print("PHASE 2: EVALUATION OPTIMIZATION")
    print("="*70)
    
    eval_threshold = 90
    max_eval_revisions = 3
    
    for eval_iteration in range(1, max_eval_revisions + 2):  # +1 for initial, +3 for revisions
        print(f"\n[EVAL ITERATION {eval_iteration}]")
        
        eval_result = evaluator.evaluate(resume, job['jd_text'])
        score = eval_result['total_score']
        
        print(f"  Score: {score}/100")
        print(f"  - Keyword: {eval_result['keyword_score']}/35")
        print(f"  - LLM: {eval_result['llm_score']}/65")
        print(f"  Feedback: {eval_result['feedback'][:100]}...")
        
        if score >= eval_threshold:
            print(f"  ✓ Score >= {eval_threshold}, evaluation passed!")
            break
        
        if eval_iteration > max_eval_revisions:
            print(f"  ⚠️  Max revisions reached, proceeding with score {score}")
            break
        
        # Revise
        print(f"  → Revising to improve score...")
        feedback_text = json.dumps(eval_result, indent=2)
        resume = reviser.revise(resume, job['jd_text'], user_profile, feedback_text, "evaluation")
        print(f"  ✓ Revision {eval_iteration} complete")
    
    # PHASE 3: Factuality Loop (max 3 revisions)
    print("\n" + "="*70)
    print("PHASE 3: FACTUALITY VERIFICATION")
    print("="*70)
    
    fact_threshold = 90
    max_fact_revisions = 3
    
    for fact_iteration in range(1, max_fact_revisions + 2):
        print(f"\n[FACT ITERATION {fact_iteration}]")
        
        fact_result = factuality_checker.check(resume, user_profile)
        score = fact_result['factuality_score']
        
        print(f"  Factuality Score: {score}/100")
        print(f"  Is Factual: {fact_result['is_factual']}")
        
        if fact_result['issues']:
            print(f"  Issues found: {len(fact_result['issues'])}")
            for issue in fact_result['issues'][:3]:
                print(f"    - {issue}")
        
        if score >= fact_threshold:
            print(f"  ✓ Score >= {fact_threshold}, factuality check passed!")
            break
        
        if fact_iteration > max_fact_revisions:
            print(f"  ⚠️  Max revisions reached, proceeding with score {score}")
            break
        
        # Revise
        print(f"  → Revising to fix factuality issues...")
        feedback_text = json.dumps(fact_result, indent=2)
        resume = reviser.revise(resume, job['jd_text'], user_profile, feedback_text, "factuality")
        print(f"  ✓ Revision {fact_iteration} complete")
    
    # PHASE 4: Save Final Resume
    print("\n" + "="*70)
    print("PHASE 4: RENDERING & SAVING")
    print("="*70)
    
    # Save JSON
    saved_json_path = ResumeProvider.save(resume, username, job_id)
    print(f"  ✓ JSON saved to: {saved_json_path}")
    
    # Render to DOCX
    print("\n  Rendering to DOCX...")
    template_path = Path(__file__).parent.parent.parent / "templates" / "Chandan_Resume_Format.docx"
    
    if not template_path.exists():
        print(f"  ⚠️  Template not found: {template_path}")
        print(f"  ⚠️  Skipping DOCX generation")
        saved_docx_path = None
    else:
        renderer = Renderer(str(template_path))
        output_dir = Path(__file__).parent.parent.parent / "output"
        output_dir.mkdir(exist_ok=True)
        docx_output = output_dir / f"{username}_{job_id}.docx"
        saved_docx_path = renderer.render(resume, str(docx_output))
        print(f"  ✓ DOCX saved to: {saved_docx_path}")
    
    # Final Summary
    print("\n" + "="*70)
    print("OPTIMIZATION COMPLETE")
    print("="*70)
    print(f"\nFinal Scores:")
    print(f"  Evaluation: {eval_result['total_score']}/100")
    print(f"  Factuality: {fact_result['factuality_score']}/100")
    print(f"\nOutputs:")
    print(f"  JSON: {saved_json_path}")
    if saved_docx_path:
        print(f"  DOCX: {saved_docx_path}")
    
    return resume, eval_result, fact_result


if __name__ == "__main__":
    try:
        resume, eval_result, fact_result = optimize_resume("chandan", "job1")
        
        # Save results
        with open("final_resume.json", 'w') as f:
            json.dump(resume, f, indent=2)
        
        with open("final_evaluation.json", 'w') as f:
            json.dump(eval_result, f, indent=2)
        
        with open("final_factuality.json", 'w') as f:
            json.dump(fact_result, f, indent=2)
        
        print("\n✓ All results saved to backend/ folder")
        
    except Exception as e:
        print(f"\n❌ PIPELINE FAILED: {e}")
        import traceback
        traceback.print_exc()
