# Structure Created

## Directory Layout
```
backend/
├── src/
│   ├── generator.py       # Generate resume from JD
│   ├── evaluator.py       # Score resume against JD
│   ├── user_data.py       # Load user profile
│   └── main.py            # Complete pipeline
├── tests/
│   ├── test_generator.py  # Test generator
│   └── test_evaluator.py  # Test evaluator
├── database/
│   └── chandan/
│       └── profile.json   # Your complete profile
└── run_tests.bat          # Run all tests

```

## Components

### 1. User Profile (database/chandan/profile.json)
- Complete profile from job-application-automator
- Structured JSON with personal, education, work, skills, projects
- Loaded via `get_user_data("chandan")`

### 2. Generator (src/generator.py)
- Takes: JD + user profile + company + role
- Returns: Resume JSON
- Uses LLM to generate tailored content

### 3. Evaluator (src/evaluator.py)
- Takes: Resume JSON + JD
- Returns: Score (0-100) with breakdown
- Keyword matching (35 pts) + LLM eval (65 pts)

### 4. Main Pipeline (src/main.py)
- Combines generator + evaluator
- Iterates to improve score
- Returns best resume

## Run Tests

```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
run_tests.bat
```

Or individually:
```bash
# Test user data loader
python src\user_data.py

# Test generator
python tests\test_generator.py

# Test evaluator
python tests\test_evaluator.py

# Run full pipeline
python src\main.py
```

## What's Decoupled

- ✅ Generator: Standalone module
- ✅ Evaluator: Standalone module  
- ✅ User data: Separate database folder
- ✅ Tests: Separate tests folder
- ✅ Each component can run independently
