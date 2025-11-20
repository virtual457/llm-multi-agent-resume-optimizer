"""
Test Generator
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.generator import Generator
from src.user_data import get_user_data
from src.job_data import get_job_data
from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv
import json

# Import API health check
from test_api import test_gemini_api

load_dotenv()


def test_generator(run_api_check=False):
    print("=" * 60)
    print("TESTING GENERATOR")
    print("=" * 60)
    
    # Run API health check only if requested
    if run_api_check:
        if not test_gemini_api():
            print("\n⚠️  Skipping generator test - API not available")
            sys.exit(1)
    
    try:
        # Load user data
        print("\n1. Loading user profile...")
        profile = get_user_data("chandan")
        print(f"   ✓ Loaded profile for: {profile['personal']['name']}")
        
        # Load job data
        print("\n2. Loading job description...")
        job = get_job_data("job1")
        print(f"   ✓ Company: {job['company']}")
        print(f"   ✓ Role: {job['role']}")
        
        # Create generator
        print("\n3. Creating generator...")
        llm = create_llm_adapter("gemini")
        gen = Generator(llm)
        print("   ✓ Generator created")
        
        # Generate resume
        print("\n4. Generating resume...")
        resume = gen.generate(
            jd_text=job['jd_text'],
            user_profile=profile,
            company=job['company'],
            role=job['role']
        )
        print("   ✓ Resume generated")
        
        # Validate structure
        print("\n5. Validating structure...")
        assert 'summary' in resume, "Missing summary"
        assert 'skills' in resume, "Missing skills"
        assert 'experience' in resume, "Missing experience"
        assert 'projects' in resume, "Missing projects"
        assert len(resume['skills']) == 7, f"Expected 7 skills, got {len(resume['skills'])}"
        assert len(resume['experience']) == 2, f"Expected 2 experience entries, got {len(resume['experience'])}"
        assert len(resume['projects']) == 3, f"Expected 3 projects, got {len(resume['projects'])}"
        print("   ✓ Structure valid")
        
        # Print results
        print("\n6. Resume Preview:")
        print(f"\n   Summary ({len(resume['summary'])} chars):")
        print(f"   {resume['summary'][:150]}...")
        
        print(f"\n   Skills ({len(resume['skills'])} categories):")
        for skill in resume['skills'][:3]:
            print(f"   - {skill['category']}: {skill['items'][:50]}...")
        
        print(f"\n   Experience:")
        for exp in resume['experience']:
            print(f"   - {exp['company']}: {len(exp['bullets'])} bullets")
        
        print(f"\n   Projects:")
        for proj in resume['projects']:
            print(f"   - {proj['title']}")
        
        # Save to file
        output_file = "test_generator_output.json"
        with open(output_file, 'w') as f:
            json.dump(resume, f, indent=2)
        print(f"\n   ✓ Full output saved to: {output_file}")
        
        print("\n" + "=" * 60)
        print("✓ GENERATOR TEST PASSED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    # Check for --check flag to run API health check
    run_check = "--check" in sys.argv
    test_generator(run_api_check=run_check)
