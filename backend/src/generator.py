"""
Generator - Creates resume JSON from JD and user profile
"""
import json
from typing import Dict, Any
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aro.llm_adapter import LLMAdapter


class Generator:
    def __init__(self, llm: LLMAdapter):
        self.llm = llm
    
    def generate(self, jd_text: str, user_profile: Dict[str, Any], company: str, role: str) -> Dict[str, Any]:
        """
        Generate resume JSON from JD and user profile
        
        Args:
            jd_text: Job description
            user_profile: User data dict
            company: Company name
            role: Role title
        
        Returns:
            Resume JSON with summary, skills, experience, projects
        """
        prompt = self._build_prompt(jd_text, user_profile, company, role)
        resume_json = self.llm.generate_json(prompt, max_tokens=8000)
        return resume_json
    
    def _build_prompt(self, jd_text: str, user_profile: Dict[str, Any], company: str, role: str) -> str:
        """Build generation prompt for LLM"""
        
        # Convert profile to simple string for prompt
        profile_str = json.dumps(user_profile, indent=2)
        
        prompt = f"""You are an expert resume writer. Generate a tailored resume JSON for this role.

ROLE: {role} at {company}

JOB DESCRIPTION:
{jd_text}

USER PROFILE:
{profile_str}

INSTRUCTIONS:
1. Summary: 520-570 characters with **bold** markers
2. Skills: Exactly 7 categories, 70-95 characters each
3. Experience: 
   - LSEG: 5 bullets (150-200 chars, **bold** markers)
   - Infosys: 4 bullets (150-200 chars, **bold** markers)
4. Projects: 3 most relevant, 2 bullets each (max 200 chars, **bold**)

OUTPUT FORMAT (JSON only, no markdown):
{{
  "header": {{"title": "Role | MS CS @ Northeastern | Keywords"}},
  "summary": "...",
  "skills": [
    {{"category": "Languages", "items": "Python, Java, Go, ..."}},
    ...6 more categories
  ],
  "experience": [
    {{
      "company": "London Stock Exchange Group (LSEG)",
      "role": "Software Engineer",
      "location": "Bengaluru",
      "duration": "08-2022 to 12-2024",
      "bullets": ["bullet1", "bullet2", "bullet3", "bullet4", "bullet5"]
    }},
    {{
      "company": "Infosys",
      "role": "Software Engineer",
      "location": "Bengaluru",
      "duration": "10-2020 to 07-2022",
      "bullets": ["bullet1", "bullet2", "bullet3", "bullet4"]
    }}
  ],
  "projects": [
    {{
      "title": "ProjectName",
      "tech": "Tech1, Tech2, Tech3",
      "bullet1": "...",
      "bullet2": "..."
    }},
    {{...}},
    {{...}}
  ]
}}

Return ONLY valid JSON."""
        
        return prompt
