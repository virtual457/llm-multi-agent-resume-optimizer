"""
Test Evaluator
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.evaluator import Evaluator
from src.job_data import get_job_data
from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv
import json

# Import API health check
from test_api import test_gemini_api

load_dotenv()


def test_evaluator(run_api_check=False):
    print("=" * 60)
    print("TESTING EVALUATOR")
    print("=" * 60)
    
    # Run API health check only if requested
    if run_api_check:
        if not test_gemini_api():
            print("\n⚠️  Skipping evaluator test - API not available")
            sys.exit(1)
    
    try:
        # Load generated resume
        print("\n1. Loading generated resume...")
        resume_file = "test_generator_output.json"
        if not os.path.exists(resume_file):
            print(f"   ❌ {resume_file} not found!")
            print("   Run generator test first: python tests/test_generator.py")
            return
        
        with open(resume_file, 'r') as f:
            resume = json.load(f)
        print(f"   ✓ Loaded resume from {resume_file}")
        
        # Load job data
        print("\n2. Loading job description...")
        job = get_job_data("job1")
        print(f"   ✓ Company: {job['company']}")
        print(f"   ✓ Role: {job['role']}")
        
        # Create evaluator with DEBUG enabled
        print("\n3. Creating evaluator...")
        llm = create_llm_adapter("gemini")
        evaluator = Evaluator(llm, debug=True)
        print("   ✓ Evaluator created")
        
        # Evaluate resume
        print("\n4. Evaluating resume against JD...")
        result = evaluator.evaluate(resume, job['jd_text'])
        print("   ✓ Evaluation complete")
        
        # Validate structure
        print("\n5. Validating result...")
        assert 'total_score' in result, "Missing total_score"
        assert 'keyword_score' in result, "Missing keyword_score"
        assert 'llm_score' in result, "Missing llm_score"
        assert 'feedback' in result, "Missing feedback"
        assert 0 <= result['total_score'] <= 100, "Invalid total_score"
        assert 0 <= result['keyword_score'] <= 35, "Invalid keyword_score"
        assert 0 <= result['llm_score'] <= 65, "Invalid llm_score"
        print("   ✓ Result structure valid")
        
        # Print results
        print("\n6. Evaluation Results:")
        print(f"\n   Total Score: {result['total_score']}/100")
        print(f"   Keyword Score: {result['keyword_score']}/35")
        print(f"   LLM Score: {result['llm_score']}/65")
        print(f"\n   Feedback:")
        print(f"   {result['feedback']}")
        
        # Save to file
        output_file = "test_evaluator_output.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n   ✓ Full output saved to: {output_file}")
        
        print("\n" + "=" * 60)
        print("✓ EVALUATOR TEST PASSED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    # Check for --check flag to run API health check
    run_check = "--check" in sys.argv
    test_evaluator(run_api_check=run_check)
