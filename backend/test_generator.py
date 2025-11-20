"""
Quick Test - Generator Agent

Tests the resume generation with a simple JD
"""

import sys
import os
import json
from dotenv import load_dotenv

# Load environment
load_dotenv()

# Add to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from aro.llm_adapter import create_llm_adapter
from aro.agents.generator import GeneratorAgent, SAMPLE_JD, get_sample_profile


def main():
    """Quick test of generator"""
    
    print("="*60)
    print("QUICK GENERATOR TEST")
    print("="*60)
    
    # Create LLM
    provider = os.getenv("LLM_PROVIDER", "gemini")
    print(f"\nLLM Provider: {provider}")
    
    llm = create_llm_adapter(provider)
    
    # Create generator
    generator = GeneratorAgent(llm)
    
    # Load profile
    print("\nLoading user profile...")
    profile_data = get_sample_profile()
    print("✅ Profile loaded!")
    
    # Generate
    print("\nGenerating resume from sample JD...")
    print("(This will take 10-20 seconds)\n")
    
    resume = generator.generate(
        jd_text=SAMPLE_JD,
        profile_data=profile_data,
        company="Test Company",
        job_title="Software Engineer Intern"
    )
    
    if resume:
        print("\n✅ SUCCESS! Resume generated!")
        print(f"\nSummary preview:")
        print(f"  {resume['summary'][:150]}...")
        
        print(f"\nGenerated {len(resume['skills'])} skill categories")
        print(f"Generated {len(resume['experience'])} work experiences")
        print(f"Generated {len(resume['projects'])} projects")
        
        # Save JSON file
        output_file = "test_generated_resume.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(resume, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Full JSON saved to: {output_file}")
    else:
        print("\n❌ Generation failed!")


if __name__ == "__main__":
    main()
