"""
Quick Test Script - Test LLM Adapter with different providers

Usage:
    python test_llm.py              # Uses .env LLM_PROVIDER
    python test_llm.py mock         # Force mock mode
    python test_llm.py gemini       # Force Gemini
"""

import sys
import os
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Add aro to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aro.llm_adapter import create_llm_adapter


def test_text_generation(llm, provider_name):
    """Test simple text generation"""
    print(f"\n{'='*60}")
    print(f"TEST 1: Text Generation ({provider_name})")
    print(f"{'='*60}")
    
    prompt = "Write a one-sentence description of Python programming language"
    
    print(f"Prompt: {prompt}")
    print("Generating...\n")
    
    try:
        response = llm.generate(prompt, max_tokens=100, temperature=0)
        print(f"✅ Response: {response}\n")
        return True
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return False


def test_json_generation(llm, provider_name):
    """Test JSON generation"""
    print(f"\n{'='*60}")
    print(f"TEST 2: JSON Generation ({provider_name})")
    print(f"{'='*60}")
    
    prompt = """Generate a JSON object representing a software engineer with these fields:
{
  "name": "John Doe",
  "skills": ["Python", "Java", "AWS"],
  "years_experience": 3,
  "current_role": "Software Engineer"
}

Generate a different example person."""
    
    print("Generating JSON...\n")
    
    try:
        response = llm.generate_json(prompt, max_tokens=200)
        print(f"✅ JSON Response:")
        import json
        print(json.dumps(response, indent=2))
        print()
        return True
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return False


def test_resume_generation(llm, provider_name):
    """Test resume-like JSON generation"""
    print(f"\n{'='*60}")
    print(f"TEST 3: Resume JSON Generation ({provider_name})")
    print(f"{'='*60}")
    
    prompt = """Generate a minimal resume JSON with this structure:
{
  "summary": "Software engineer with Python experience...",
  "skills": [
    {"category": "Programming", "items": "Python, Java"},
    {"category": "Backend", "items": "REST APIs, Microservices"}
  ],
  "projects": [
    {
      "title": "Example Project",
      "tech": "Python, FastAPI",
      "bullet1": "Built API with FastAPI",
      "bullet2": "Achieved 100 req/sec"
    }
  ]
}

Make up a realistic software engineer resume."""
    
    print("Generating resume JSON...\n")
    
    try:
        response = llm.generate_json(prompt, max_tokens=1000)
        print(f"✅ Resume JSON:")
        import json
        print(json.dumps(response, indent=2))
        
        # Validate structure
        assert "summary" in response, "Missing summary"
        assert "skills" in response, "Missing skills"
        assert "projects" in response, "Missing projects"
        
        print(f"\n✅ Structure validation passed!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}\n")
        return False


def main():
    """Run all tests"""
    
    # Determine provider
    if len(sys.argv) > 1:
        provider = sys.argv[1]
    else:
        provider = os.getenv("LLM_PROVIDER", "mock")
    
    print(f"\n{'='*60}")
    print(f"LLM ADAPTER COMPREHENSIVE TEST")
    print(f"Provider: {provider.upper()}")
    print(f"{'='*60}")
    
    # Create adapter
    try:
        llm = create_llm_adapter(provider)
        print(f"✅ LLM adapter created successfully\n")
    except Exception as e:
        print(f"❌ Failed to create adapter: {e}")
        print("\nMake sure:")
        print("  1. .env file exists with GEMINI_API_KEY")
        print("  2. API key is valid")
        print("  3. Dependencies installed (pip install -r requirements.txt)")
        return
    
    # Run tests
    results = []
    results.append(("Text Generation", test_text_generation(llm, provider)))
    results.append(("JSON Generation", test_json_generation(llm, provider)))
    results.append(("Resume JSON", test_resume_generation(llm, provider)))
    
    # Summary
    print(f"\n{'='*60}")
    print("TEST SUMMARY")
    print(f"{'='*60}")
    
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    passed_count = sum(1 for _, passed in results if passed)
    total_count = len(results)
    
    print(f"\nResults: {passed_count}/{total_count} tests passed")
    
    if passed_count == total_count:
        print("\n🎉 All tests passed! LLM adapter is working perfectly!")
        print("\n✅ Ready to build Generator Agent next!")
    else:
        print("\n⚠️  Some tests failed. Fix issues before proceeding.")


if __name__ == "__main__":
    main()
