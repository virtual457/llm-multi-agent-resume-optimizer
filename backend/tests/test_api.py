"""
API Health Check - Test Gemini API before running tests
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aro.llm_adapter import create_llm_adapter
from dotenv import load_dotenv

load_dotenv()


def test_gemini_api():
    """Test if Gemini API is responding"""
    print("\n" + "="*60)
    print("GEMINI API HEALTH CHECK")
    print("="*60)
    
    try:
        print("\n1. Creating LLM adapter...")
        llm = create_llm_adapter("gemini")
        print("   ✓ Adapter created")
        
        print("\n2. Testing simple generation...")
        try:
            response = llm.generate("Say 'API working'", max_tokens=100)
            print(f"   ✓ Response: {response}")
        except Exception as e:
            print(f"   ❌ Simple generation failed")
            print(f"   Error Type: {type(e).__name__}")
            print(f"   Error Message: {str(e)}")
            if "503" in str(e):
                print(f"   Status Code: 503 (Service Unavailable)")
            elif "429" in str(e):
                print(f"   Status Code: 429 (Rate Limit)")
            elif "401" in str(e):
                print(f"   Status Code: 401 (Unauthorized - Check API Key)")
            elif "400" in str(e):
                print(f"   Status Code: 400 (Bad Request)")
            raise
        
        print("\n3. Testing JSON generation...")
        try:
            json_response = llm.generate_json('Return {"status": "ok"}', max_tokens=200)
            print(f"   ✓ JSON Response: {json_response}")
        except Exception as e:
            print(f"   ❌ JSON generation failed")
            print(f"   Error Type: {type(e).__name__}")
            print(f"   Error Message: {str(e)}")
            raise
        
        print("\n" + "="*60)
        print("✓ GEMINI API IS WORKING")
        print("="*60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n" + "="*60)
        print("❌ GEMINI API TEST FAILED")
        print("="*60)
        print(f"\nError Details:")
        print(f"  Type: {type(e).__name__}")
        print(f"  Message: {str(e)}")
        
        # Provide helpful suggestions based on error
        error_str = str(e).lower()
        if "503" in error_str or "overloaded" in error_str or "unavailable" in error_str:
            print(f"\n💡 The API is overloaded right now.")
            print(f"   Wait 5-10 minutes and try again.")
        elif "429" in error_str or "rate limit" in error_str:
            print(f"\n💡 Rate limit exceeded.")
            print(f"   Wait a few minutes before retrying.")
        elif "401" in error_str or "unauthorized" in error_str:
            print(f"\n💡 API key issue.")
            print(f"   Check your GEMINI_API_KEY in .env file.")
        elif "empty response" in error_str:
            print(f"\n💡 API returned empty response (likely overloaded).")
            print(f"   Wait a few minutes and try again.")
        else:
            print(f"\n💡 Unknown error - check the message above.")
        
        print("="*60 + "\n")
        
        # Print full traceback for debugging
        import traceback
        print("Full Traceback:")
        traceback.print_exc()
        
        return False


if __name__ == "__main__":
    success = test_gemini_api()
    sys.exit(0 if success else 1)
