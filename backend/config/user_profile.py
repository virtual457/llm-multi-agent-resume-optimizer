"""
User Profile Loader - Loads candidate data from existing profile files

Reads from: D:\Git\virtual457-projects\job-application-automator\docs\user_profile\
- CHANDAN_PROFILE_MASTER.md
- WORK_EXPERIENCE_DATABASE.md
"""

import os
from pathlib import Path
from typing import Dict, Any


class UserProfileLoader:
    """Loads user profile from existing documentation"""
    
    # Path to existing profile files
    PROFILE_BASE_PATH = Path("D:/Git/virtual457-projects/job-application-automator/docs/user_profile")
    
    @staticmethod
    def load_profile() -> Dict[str, Any]:
        """
        Load complete user profile
        
        Returns structured data for resume generation
        """
        
        # For now, return hardcoded data based on CHANDAN_PROFILE_MASTER.md
        # TODO: Parse markdown files dynamically if needed
        
        return {
            "personal_info": {
                "name": "Chandan Gowda K S",
                "email": "chandan.keelara@gmail.com",
                "phone": "+1 (857) 421-7469",
                "location": "Boston, MA",
                "linkedin": "https://www.linkedin.com/in/chandan-gowda-k-s-765194186/",
                "github": "https://github.com/virtual457",
                "portfolio": "https://virtual457.github.io/"
            },
            
            "education": {
                "ms": {
                    "degree": "MS in Computer Science",
                    "institution": "Northeastern University",
                    "location": "Boston, MA",
                    "gpa": "3.89/4.0",
                    "duration": "01-2025 to 05-2027",
                    "graduation": "May 2027",
                    "status": "Current student (1st year)"
                },
                "be": {
                    "degree": "BE in Computer Science",
                    "institution": "Nitte Meenakshi Institute of Technology (NMIT)",
                    "location": "Bengaluru, India",
                    "gpa": "8.76/10",
                    "duration": "08-2016 to 08-2020"
                }
            },
            
            "work_experience": {
                "lseg": {
                    "company": "London Stock Exchange Group (LSEG)",
                    "role": "Senior Software Engineer",
                    "location": "Bengaluru",
                    "duration": "08-2022 to 12-2024",
                    "description": "Built distributed systems for compliance data processing",
                    "technologies": ["Python", "Java (Micronaut)", "AWS Lambda", "SQS", "API Gateway", "Event-driven architecture", "Microservices"],
                    "metrics": {
                        "records_processed": "7.5M+",
                        "countries_served": "180+",
                        "throughput": "~40 records/second",
                        "data_integrity": "99.9%",
                        "priority_improvement": "35%",
                        "latency_reduction": "40%",
                        "security_improvement": "50%",
                        "engineers_mentored": "5",
                        "teams_collaborated": "7"
                    },
                    "achievements": [
                        "Event-driven data processing pipeline",
                        "Multi-queue priority routing with AWS SQS/Lambda",
                        "Java microservices development",
                        "Performance optimization",
                        "Security hardening with AWS WAF/IAM/TLS",
                        "Mentorship and code reviews",
                        "Cross-functional collaboration",
                        "Zero-downtime migrations",
                        "Workflow automation and orchestration",
                        "RESTful API development"
                    ]
                },
                "infosys": {
                    "company": "Infosys",
                    "role": "Senior Systems Engineer",
                    "location": "Bengaluru",
                    "duration": "10-2020 to 07-2022",
                    "description": "Built Python data processing pipelines and microservices",
                    "technologies": ["Python", "Microservices", "API orchestration", "ETL pipelines", "Database optimization"],
                    "metrics": {
                        "throughput_improvement": "3x",
                        "manual_reduction": "50%",
                        "latency_reduction": "35%",
                        "accuracy_improvement": "20%"
                    },
                    "achievements": [
                        "High-throughput Python data pipelines",
                        "Concurrent execution optimization",
                        "Microservices integration patterns",
                        "Database query optimization",
                        "ETL pipeline efficiency",
                        "Monitoring and error-handling frameworks",
                        "Automation workflows"
                    ]
                }
            },
            
            "top_projects_summary": "Deep RL Agent (PyTorch, 1.5M params), Kubernetes Operator (Go), Full-stack LMS (Next.js/React/Node.js - deployed), Port Management (Django/MySQL), PUBG Data Analysis (4.4M records)",
            
            "key_technologies": "Python, Java, Go, JavaScript, TypeScript, AWS, Kubernetes, Docker, PyTorch, TensorFlow, React, Next.js, MySQL, PostgreSQL, MongoDB",
            
            "certifications": [
                "AWS Certified Cloud Practitioner"
            ],
            
            "publications": [
                "IEEE: Doctor-Patient Assistance System using Artificial Intelligence"
            ]
        }
    
    @staticmethod
    def get_profile_summary() -> str:
        """Get a concise profile summary for prompts"""
        profile = UserProfileLoader.load_profile()
        
        return f"""
MS Computer Science student at Northeastern University (GPA: {profile['education']['ms']['gpa']})
Graduating: {profile['education']['ms']['graduation']}

Work Experience:
1. {profile['work_experience']['lseg']['company']} ({profile['work_experience']['lseg']['duration']})
   - Built distributed systems processing {profile['work_experience']['lseg']['metrics']['records_processed']} records
   - Served {profile['work_experience']['lseg']['metrics']['countries_served']} countries
   - Technologies: {', '.join(profile['work_experience']['lseg']['technologies'][:5])}
   
2. {profile['work_experience']['infosys']['company']} ({profile['work_experience']['infosys']['duration']})
   - Achieved {profile['work_experience']['infosys']['metrics']['throughput_improvement']} throughput improvement
   - Technologies: {', '.join(profile['work_experience']['infosys']['technologies'][:3])}

Top Projects: {profile['top_projects_summary']}
Key Technologies: {profile['key_technologies']}
""".strip()
    
    @staticmethod
    def get_work_metrics() -> Dict[str, Dict[str, str]]:
        """Get work experience metrics for bullet generation"""
        profile = UserProfileLoader.load_profile()
        return {
            "lseg": profile['work_experience']['lseg']['metrics'],
            "infosys": profile['work_experience']['infosys']['metrics']
        }
    
    @staticmethod
    def get_contact_info() -> Dict[str, str]:
        """Get contact information"""
        profile = UserProfileLoader.load_profile()
        return profile['personal_info']


if __name__ == "__main__":
    # Test the loader
    print("="*60)
    print("USER PROFILE LOADER TEST")
    print("="*60)
    
    profile = UserProfileLoader.load_profile()
    
    print("\n📋 Loaded Profile:")
    print(f"   Name: {profile['personal_info']['name']}")
    print(f"   Email: {profile['personal_info']['email']}")
    print(f"   GPA: {profile['education']['ms']['gpa']}")
    
    print("\n💼 Work Experience:")
    print(f"   LSEG: {profile['work_experience']['lseg']['metrics']['records_processed']} records")
    print(f"   Infosys: {profile['work_experience']['infosys']['metrics']['throughput_improvement']} throughput")
    
    print("\n📝 Profile Summary:")
    print(UserProfileLoader.get_profile_summary())
    
    print("\n✅ Profile loaded successfully!")
