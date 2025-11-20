"""
Generator Agent - Creates tailored resume content from JD and profile

This agent uses LLM to generate resume JSON with:
- Summary
- Skills (7 categories)
- Work Experience (LSEG 5 bullets, Infosys 4 bullets)
- Projects (3 projects with 2 bullets each)
"""

import sys
import os
from typing import Dict, Any, List, Optional
import json
import re

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from aro.llm_adapter import LLMAdapter, create_llm_adapter
from aro.prompts import prompts
from config.user_profile import UserProfileLoader


class GeneratorAgent:
    """Agent responsible for generating resume content"""
    
    def __init__(self, llm: LLMAdapter):
        """
        Initialize generator agent
        
        Args:
            llm: LLM adapter instance
        """
        self.llm = llm
        self.generation_count = 0
    
    def extract_keywords(self, jd_text: str, top_n: int = 30) -> List[str]:
        """
        Extract key technical terms and requirements from JD
        
        Args:
            jd_text: Job description text
            top_n: Number of top keywords to extract
        
        Returns:
            List of keywords
        """
        # Common tech keywords to look for
        tech_patterns = [
            # Languages
            r'\b(Python|Java|JavaScript|TypeScript|Go|C\+\+|C#|SQL|Ruby|Rust|Kotlin|Swift)\b',
            # Frameworks
            r'\b(React|Next\.js|Django|Flask|FastAPI|Spring|Node\.js|Express|Angular|Vue)\b',
            # Cloud
            r'\b(AWS|Azure|GCP|Kubernetes|Docker|Lambda|EC2|S3|SQS)\b',
            # Databases
            r'\b(MySQL|PostgreSQL|MongoDB|Redis|DynamoDB|SQL Server)\b',
            # ML/AI
            r'\b(Machine Learning|Deep Learning|PyTorch|TensorFlow|Neural Networks|AI|LLM|GPT)\b',
            # Practices
            r'\b(Microservices|REST API|GraphQL|CI/CD|Agile|DevOps|TDD|Git)\b',
            # General
            r'\b(Distributed Systems|Big Data|ETL|Data Pipeline|Event-Driven)\b'
        ]
        
        keywords = set()
        text_upper = jd_text
        
        for pattern in tech_patterns:
            matches = re.findall(pattern, text_upper, re.IGNORECASE)
            keywords.update(matches)
        
        # Also extract requirement-like phrases
        requirement_lines = [line.strip() for line in jd_text.split('\n') 
                            if any(word in line.lower() for word in ['experience', 'proficiency', 'knowledge', 'skills'])]
        
        for line in requirement_lines[:10]:  # Top 10 requirement lines
            words = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', line)
            keywords.update([w for w in words if len(w) > 3])
        
        return list(keywords)[:top_n]
    
    def generate(
        self, 
        jd_text: str, 
        profile_data: Dict[str, Any],
        company: str = "Target Company",
        job_title: str = "Software Engineer",
        iteration_context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Generate tailored resume content
        
        Args:
            jd_text: Full job description text
            profile_data: Candidate profile information
            company: Company name
            job_title: Job title
            iteration_context: Context from previous iterations (for refinement)
        
        Returns:
            Resume JSON with all sections
        """
        self.generation_count += 1
        
        print(f"\n🤖 Generator Agent - Iteration {self.generation_count}")
        print(f"   Company: {company}")
        print(f"   Role: {job_title}")
        
        # Extract keywords from JD
        print("   📊 Extracting keywords from JD...")
        keywords = self.extract_keywords(jd_text, top_n=25)
        print(f"   ✅ Found {len(keywords)} keywords: {', '.join(keywords[:10])}...")
        
        # Build prompt
        print("   📝 Building generation prompt...")
        system_prompt = prompts.generator_system_prompt(company, job_title)
        user_prompt = prompts.generator_user_prompt(jd_text, profile_data, keywords)
        
        # Add iteration context if refinement
        if iteration_context:
            user_prompt += f"\n\nREVISION INSTRUCTIONS:\n{iteration_context.get('context_for_generator', '')}"
        
        # Combine system and user prompts
        full_prompt = f"{system_prompt}\n\n{user_prompt}"
        
        # Call LLM
        print("   🧠 Calling LLM to generate resume...")
        try:
            resume_json = self.llm.generate_json(full_prompt, max_tokens=8000)
            print(f"   ✅ Resume generated successfully!")
            
            # Validate structure
            self._validate_resume_structure(resume_json)
            print(f"   ✅ Structure validation passed!")
            
            return resume_json
            
        except json.JSONDecodeError as e:
            print(f"   ❌ JSON parsing error: {e}")
            raise
        except Exception as e:
            print(f"   ❌ Generation error: {e}")
            raise
    
    def _validate_resume_structure(self, resume_json: Dict[str, Any]) -> bool:
        """
        Validate that resume JSON has required structure
        
        Args:
            resume_json: Generated resume JSON
        
        Returns:
            True if valid
        
        Raises:
            ValueError if invalid structure
        """
        required_fields = ['summary', 'skills', 'experience', 'projects']
        
        for field in required_fields:
            if field not in resume_json:
                raise ValueError(f"Missing required field: {field}")
        
        # Validate skills
        if not isinstance(resume_json['skills'], list):
            raise ValueError("Skills must be a list")
        
        if len(resume_json['skills']) != 7:
            print(f"   ⚠️  Warning: Expected 7 skill categories, got {len(resume_json['skills'])}")
        
        # Validate experience
        if not isinstance(resume_json['experience'], list):
            raise ValueError("Experience must be a list")
        
        if len(resume_json['experience']) != 2:
            raise ValueError(f"Expected 2 experience entries (LSEG + Infosys), got {len(resume_json['experience'])}")
        
        # Check LSEG has 5 bullets
        lseg = resume_json['experience'][0]
        if len(lseg.get('bullets', [])) != 5:
            print(f"   ⚠️  Warning: LSEG should have 5 bullets, got {len(lseg.get('bullets', []))}")
        
        # Check Infosys has 4 bullets
        infosys = resume_json['experience'][1]
        if len(infosys.get('bullets', [])) != 4:
            print(f"   ⚠️  Warning: Infosys should have 4 bullets, got {len(infosys.get('bullets', []))}")
        
        # Validate projects
        if not isinstance(resume_json['projects'], list):
            raise ValueError("Projects must be a list")
        
        if len(resume_json['projects']) != 3:
            print(f"   ⚠️  Warning: Expected 3 projects, got {len(resume_json['projects'])}")
        
        return True
    
    def get_stats(self) -> Dict[str, Any]:
        """Get generation statistics"""
        return {
            "total_generations": self.generation_count
        }


# Sample JD for testing
SAMPLE_JD = """
Software Engineer Intern - Backend Systems

We're looking for a software engineering intern to work on backend systems, distributed architectures, and cloud infrastructure.

Requirements:
- Strong programming skills in Python, Java, or Go
- Experience with distributed systems and microservices
- Knowledge of cloud platforms (AWS, Kubernetes, Docker)
- Understanding of databases (SQL, NoSQL)
- Machine learning experience is a plus

Responsibilities:
- Build scalable backend services
- Develop RESTful APIs
- Work with big data processing pipelines
- Collaborate with cross-functional teams
"""

# Get sample profile from loader
def get_sample_profile():
    """Get profile data from UserProfileLoader"""
    profile = UserProfileLoader.load_profile()
    return {
        "education": f"{profile['education']['ms']['degree']}, {profile['education']['ms']['institution']} ({profile['education']['ms']['gpa']})",
        "work_summary": f"Production experience at {profile['work_experience']['lseg']['company']} and {profile['work_experience']['infosys']['company']}",
        "top_projects": profile['top_projects_summary'],
        "technologies": profile['key_technologies']
    }


def test_generator():
    """Test the generator agent"""
    print("\n" + "="*60)
    print("GENERATOR AGENT TEST")
    print("="*60)
    
    # Load environment
    from dotenv import load_dotenv
    load_dotenv()
    
    # Create LLM adapter
    provider = os.getenv("LLM_PROVIDER", "mock")
    print(f"\nUsing LLM provider: {provider}")
    
    llm = create_llm_adapter(provider)
    
    # Create generator agent
    generator = GeneratorAgent(llm)
    
    # Load profile from config
    print("\n📂 Loading user profile from config...")
    profile_data = get_sample_profile()
    print("   ✅ Profile loaded!")
    
    # Generate resume
    print("\n🚀 Generating resume for sample JD...")
    
    try:
        resume_json = generator.generate(
            jd_text=SAMPLE_JD,
            profile_data=SAMPLE_PROFILE,
            company="Test Company",
            job_title="Software Engineer Intern"
        )
        
        print("\n" + "="*60)
        print("✅ GENERATION SUCCESSFUL!")
        print("="*60)
        
        print("\n📄 Generated Resume Summary:")
        print(f"   Summary length: {len(resume_json.get('summary', ''))} chars")
        print(f"   Skill categories: {len(resume_json.get('skills', []))}")
        print(f"   Experience entries: {len(resume_json.get('experience', []))}")
        print(f"   Projects: {len(resume_json.get('projects', []))}")
        
        # Show summary
        print(f"\n📝 Summary:\n   {resume_json.get('summary', 'N/A')}")
        
        # Show first skill category
        if resume_json.get('skills'):
            print(f"\n🔧 First skill category:")
            skill = resume_json['skills'][0]
            print(f"   {skill.get('category', 'N/A')}: {skill.get('items', 'N/A')}")
        
        # Show first LSEG bullet
        if resume_json.get('experience'):
            lseg = resume_json['experience'][0]
            print(f"\n💼 LSEG first bullet:")
            if lseg.get('bullets'):
                print(f"   {lseg['bullets'][0]}")
        
        # Show first project
        if resume_json.get('projects'):
            project = resume_json['projects'][0]
            print(f"\n🚀 First project: {project.get('title', 'N/A')}")
            print(f"   Tech: {project.get('tech', 'N/A')}")
            print(f"   Bullet: {project.get('bullet1', 'N/A')}")
        
        # Save to file for inspection
        output_file = "test_generated_resume.json"
        with open(output_file, 'w') as f:
            json.dump(resume_json, f, indent=2)
        
        print(f"\n💾 Full JSON saved to: {output_file}")
        print("\n🎉 Generator Agent is working!")
        
        return resume_json
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    test_generator()
