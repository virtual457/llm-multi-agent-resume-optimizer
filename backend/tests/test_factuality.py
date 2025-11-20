"""
Test Factuality Checker
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.factuality_checker import FactualityChecker
from src.user_data import get_user_data
from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv
import json

load_dotenv()


def test_factuality_checker():
    print("=" * 60)
    print("TESTING FACTUALITY CHECKER")
    print("=" * 60)
    
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
        print(f"   ✓ Loaded resume")
        
        # Load user profile
        print("\n2. Loading user profile...")
        profile = get_user_data("chandan")
        print(f"   ✓ Loaded profile for: {profile['personal']['name']}")
        
        # Create checker
        print("\n3. Creating factuality checker...")
        llm = create_llm_adapter("gemini")
        checker = FactualityChecker(llm, debug=True)
        print("   ✓ Checker created")
        
        # Check factuality
        print("\n4. Checking factuality...")
        result = checker.check(resume, profile)
        print("   ✓ Check complete")
        
        # Print results
        print("\n5. Factuality Results:")
        print(f"\n   Is Factual: {result['is_factual']}")
        print(f"   Factuality Score: {result['factuality_score']}/100")
        
        print(f"\n   Summary Check: {result['summary_check']['is_accurate']}")
        if result['summary_check']['issues']:
            for issue in result['summary_check']['issues']:
                print(f"      - {issue}")
        
        print(f"\n   Experience Check: {result['experience_check']['is_accurate']}")
        if result['experience_check']['issues']:
            for issue in result['experience_check']['issues']:
                print(f"      - {issue}")
        
        print(f"\n   Projects Check: {result['projects_check']['is_accurate']}")
        if result['projects_check']['issues']:
            for issue in result['projects_check']['issues']:
                print(f"      - {issue}")
        
        print(f"\n   Skills Check: {result['skills_check']['is_accurate']}")
        if result['skills_check']['issues']:
            for issue in result['skills_check']['issues']:
                print(f"      - {issue}")
        
        if result['issues']:
            print(f"\n   Overall Issues:")
            for issue in result['issues']:
                print(f"      - {issue}")
        
        # Save to file
        output_file = "test_factuality_output.json"
        with open(output_file, 'w') as f:
            json.dump(result, f, indent=2)
        print(f"\n   ✓ Full output saved to: {output_file}")
        
        print("\n" + "=" * 60)
        print("✓ FACTUALITY CHECK PASSED")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        raise


if __name__ == "__main__":
    test_factuality_checker()
