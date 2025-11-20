"""
Job Data Loader - Loads job descriptions from database
"""
import json
from pathlib import Path
from typing import Dict, Any


def get_job_data(job_id: str = "job1") -> Dict[str, Any]:
    """
    Load job description from database
    
    Args:
        job_id: Job file name in database/jobs/
    
    Returns:
        Job data dict with company, role, jd_text
    """
    db_path = Path(__file__).parent.parent / "database" / "jobs" / f"{job_id}.json"
    
    if not db_path.exists():
        raise FileNotFoundError(f"Job not found: {db_path}")
    
    with open(db_path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    # Test loading
    job = get_job_data("job1")
    print("Company:", job['company'])
    print("Role:", job['role'])
    print("JD length:", len(job['jd_text']), "chars")
