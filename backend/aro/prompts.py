"""
Prompt Templates for Multi-Agent Resume System

Contains all prompts for:
- Generator Agent (creates resume content)
- Evaluator Agent (scores and critiques)
- Reviser Agent (plans improvements)
"""

from typing import Dict, Any, List


class PromptTemplates:
    """Centralized prompt templates"""
    
    @staticmethod
    def generator_system_prompt(company: str, job_title: str) -> str:
        """System prompt for resume generator agent"""
        return f"""You are an expert resume writer and recruiter specializing in {company}'s hiring for {job_title} positions.

Your task is to generate a highly tailored, ATS-optimized resume that will pass both automated screening and impress human recruiters.

Key principles:
- Use ACTIVE verbs (Engineered, Architected, Developed, Implemented, Optimized)
- Include QUANTIFIED metrics (%, numbers, scale indicators) in every bullet
- Match JD KEYWORDS naturally without keyword stuffing
- Use **bold markers** around key technologies, metrics, and achievements
- Keep bullets concise (150-200 characters for work experience, max 200 for projects)
- Tell a coherent story that positions candidate as ideal fit

Output must be valid JSON with this exact structure:
{{
  "summary": "MS Computer Science student at Northeastern...",
  "skills": [
    {{"category": "Programming Language", "items": "Python, Java, Go"}},
    {{"category": "Backend Development", "items": "..."}}
  ],
  "experience": [
    {{
      "company": "London Stock Exchange Group (LSEG)",
      "role": "Senior Software Engineer",
      "location": "Bengaluru",
      "duration": "08-2022 to 12-2024",
      "bullets": ["bullet 1 with **bold**", "bullet 2...", ...]
    }}
  ],
  "projects": [
    {{
      "title": "Project Name",
      "tech": "Python, PyTorch",
      "bullet1": "...",
      "bullet2": "..."
    }}
  ]
}}"""
    
    @staticmethod
    def generator_user_prompt(jd_text: str, profile_data: Dict[str, Any], keywords: List[str]) -> str:
        """User prompt for generator with JD and profile"""
        
        keywords_str = ", ".join(keywords[:20])  # Top 20 keywords
        
        return f"""Generate a tailored resume for this job description:

JOB DESCRIPTION:
{jd_text}

CANDIDATE PROFILE:
Education: {profile_data.get('education', 'MS CS at Northeastern, 3.89 GPA')}
Work Experience Foundation: {profile_data.get('work_summary', 'Production experience at LSEG and Infosys')}
Key Projects: {profile_data.get('top_projects', 'Deep RL, Kubernetes Operator, Full-stack LMS')}
Key Technologies: {profile_data.get('technologies', 'Python, Java, Go, AWS, Kubernetes, ML')}

TARGET KEYWORDS TO INCLUDE:
{keywords_str}

REQUIREMENTS:
1. Summary: 520-570 characters, narrative flow (no "seeking internship"), mention LSEG, include GPA, 5-8 **bold** markers
2. Skills: Exactly 7 categories ordered by JD priority, each ~70-95 characters
3. Experience: 
   - LSEG: Exactly 5 bullets (emphasize what matches JD)
   - Infosys: Exactly 4 bullets (complement LSEG, fill gaps)
   - Use real metrics: 7.5M+ records, 180+ countries, 40% latency reduction, 3x throughput, etc.
4. Projects: Exactly 3 projects most relevant to JD, 2 bullets each (max 200 chars per bullet)

Generate the complete resume as JSON. Be specific, use metrics, and naturally incorporate keywords."""
    
    @staticmethod
    def evaluator_system_prompt(company: str, job_title: str) -> str:
        """System prompt for evaluator agent"""
        return f"""You are a strict hiring manager at {company} evaluating candidates for {job_title}.

Your job is to objectively score resumes against the job description using these criteria:

1. KEYWORD MATCH (35 points): How many critical JD keywords appear in the resume?
2. SEMANTIC ALIGNMENT (25 points): How well does the resume content align with JD requirements semantically?
3. QUANTITATIVE METRICS (20 points): What percentage of bullets contain quantified achievements?
4. ROLE-SPECIFIC SKILLS (20 points): Are the must-have skills for this role present?

Be harsh but fair. Real recruiters reject 75% of resumes. Your feedback should be actionable."""
    
    @staticmethod
    def evaluator_user_prompt(jd_text: str, resume_json: Dict[str, Any]) -> str:
        """User prompt for evaluator"""
        import json
        
        resume_str = json.dumps(resume_json, indent=2)
        
        return f"""Evaluate this resume against the job description.

JOB DESCRIPTION:
{jd_text}

RESUME (JSON):
{resume_str}

Provide a detailed evaluation in JSON format:
{{
  "total_score": 0-100,
  "breakdown": {{
    "keyword_match": 0-35,
    "semantic_alignment": 0-25,
    "quant_metrics": 0-20,
    "role_specific_skills": 0-20
  }},
  "missing_keywords": ["keyword1", "keyword2", ...],
  "strengths": ["strength 1", "strength 2", "strength 3"],
  "improvements": [
    {{
      "section": "experience",
      "bullet_index": 0,
      "current": "...",
      "suggestion": "...",
      "reason": "..."
    }}
  ],
  "overall_feedback": "2-3 sentence summary"
}}

Be specific and actionable in your feedback."""
    
    @staticmethod
    def reviser_system_prompt() -> str:
        """System prompt for reviser agent"""
        return """You are an intelligent revision planner for resume optimization.

Your job: Analyze evaluator feedback and create targeted improvement instructions.

You receive:
- Evaluation scores and feedback
- Current resume JSON
- Missing keywords
- Specific improvement suggestions

You produce:
- Prioritized list of changes
- Specific instructions for the generator
- Focus areas for next iteration

Be strategic: focus on high-impact changes that will improve the score most."""
    
    @staticmethod
    def reviser_user_prompt(eval_report: Dict[str, Any], current_resume: Dict[str, Any]) -> str:
        """User prompt for reviser"""
        import json
        
        return f"""Create a revision plan based on this evaluation:

EVALUATION REPORT:
{json.dumps(eval_report, indent=2)}

CURRENT RESUME:
{json.dumps(current_resume, indent=2)}

Generate a revision plan in JSON format:
{{
  "priority_changes": [
    {{
      "section": "summary|skills|experience|projects",
      "action": "add|modify|reorder",
      "target": "specific location",
      "instruction": "detailed instruction for generator",
      "expected_impact": "keyword_match|semantic_alignment|quant_metrics|role_skills"
    }}
  ],
  "focus_keywords": ["keyword1", "keyword2", ...],
  "context_for_generator": "Additional context to guide next generation"
}}

Prioritize changes by potential score impact. Limit to top 3-5 changes."""


# Singleton instance
prompts = PromptTemplates()
