"""
Data Providers - Centralized data management

Handles storage and retrieval of:
- User profiles
- Job descriptions
- Generated resumes
"""
import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime


class Config:
    """Centralized configuration"""
    BASE_DIR = Path(__file__).parent.parent / "database"
    USERS_DIR = BASE_DIR  # users are in database/username/
    JOBS_DIR = BASE_DIR / "jobs"
    RESUMES_DIR = BASE_DIR / "resumes"


class UserProvider:
    """Manages user profile data"""
    
    @staticmethod
    def get(username: str = "chandan") -> Dict[str, Any]:
        """Load user profile"""
        path = Config.USERS_DIR / username / "profile.json"
        
        if not path.exists():
            raise FileNotFoundError(f"User profile not found: {path}")
        
        with open(path, 'r') as f:
            return json.load(f)


class JobProvider:
    """Manages job description data"""
    
    @staticmethod
    def get(job_id: str = "job1") -> Dict[str, Any]:
        """Load job description"""
        path = Config.JOBS_DIR / f"{job_id}.json"
        
        if not path.exists():
            raise FileNotFoundError(f"Job not found: {path}")
        
        with open(path, 'r') as f:
            return json.load(f)


class ResumeProvider:
    """Manages generated resume storage and retrieval"""
    
    @staticmethod
    def save(
        resume_json: Dict[str, Any], 
        username: str = "chandan",
        job_id: str = "job1"
    ) -> str:
        """
        Save generated resume (overwrites existing)
        
        Args:
            resume_json: Resume data
            username: User identifier
            job_id: Job identifier
        
        Returns:
            Saved file path
        """
        # Create directory: resumes/username/
        resume_dir = Config.RESUMES_DIR / username
        resume_dir.mkdir(parents=True, exist_ok=True)
        
        # Single file per job: job1.json, job2.json, etc.
        filepath = resume_dir / f"{job_id}.json"
        
        # Add metadata
        resume_with_metadata = {
            "metadata": {
                "username": username,
                "job_id": job_id,
                "updated_at": datetime.now().isoformat()
            },
            "resume": resume_json
        }
        
        # Save (overwrites)
        with open(filepath, 'w') as f:
            json.dump(resume_with_metadata, f, indent=2)
        
        return str(filepath)
    
    @staticmethod
    def get(
        username: str = "chandan",
        job_id: str = "job1"
    ) -> Dict[str, Any]:
        """
        Load generated resume
        
        Args:
            username: User identifier
            job_id: Job identifier
        
        Returns:
            Resume data (without metadata)
        """
        filepath = Config.RESUMES_DIR / username / f"{job_id}.json"
        
        if not filepath.exists():
            raise FileNotFoundError(f"Resume not found: {filepath}")
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        return data['resume']
    
    @staticmethod
    def exists(username: str = "chandan", job_id: str = "job1") -> bool:
        """Check if resume exists"""
        filepath = Config.RESUMES_DIR / username / f"{job_id}.json"
        return filepath.exists()


# Convenience functions (backward compatibility)
def get_user_data(username: str = "chandan") -> Dict[str, Any]:
    """Load user profile"""
    return UserProvider.get(username)


def get_job_data(job_id: str = "job1") -> Dict[str, Any]:
    """Load job description"""
    return JobProvider.get(job_id)


if __name__ == "__main__":
    # Test providers
    print("Testing Data Providers...")
    
    # Test user provider
    print("\n1. User Provider:")
    user = UserProvider.get("chandan")
    print(f"   ✓ Loaded: {user['personal']['name']}")
    
    # Test job provider
    print("\n2. Job Provider:")
    job = JobProvider.get("job1")
    print(f"   ✓ Loaded: {job['company']} - {job['role']}")
    
    # Test resume provider (save)
    print("\n3. Resume Provider (Save):")
    sample_resume = {"test": "data", "summary": "Test summary"}
    path = ResumeProvider.save(sample_resume, "chandan", "job1")
    print(f"   ✓ Saved to: {path}")
    
    # Test resume provider (load)
    print("\n4. Resume Provider (Load):")
    loaded = ResumeProvider.get("chandan", "job1")
    print(f"   ✓ Loaded: {loaded}")
    
    # Test exists
    print("\n5. Resume Provider (Exists):")
    exists = ResumeProvider.exists("chandan", "job1")
    print(f"   ✓ Exists: {exists}")
    
    print("\n✓ All providers working!")
