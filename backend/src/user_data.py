"""
User Data Loader - Loads user profile from database
"""
import json
from pathlib import Path
from typing import Dict, Any


def get_user_data(username: str = "chandan") -> Dict[str, Any]:
    """
    Load user profile from database
    
    Args:
        username: User folder name in database/
    
    Returns:
        User profile dict
    """
    db_path = Path(__file__).parent.parent / "database" / username / "profile.json"
    
    if not db_path.exists():
        raise FileNotFoundError(f"Profile not found: {db_path}")
    
    with open(db_path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    # Test loading
    profile = get_user_data("chandan")
    print("User:", profile['personal']['name'])
    print("MS GPA:", profile['education']['ms']['gpa'])
    print("Skills:", len(profile['skills']['languages']), "languages")
    print("Projects:", len(profile['projects']))
