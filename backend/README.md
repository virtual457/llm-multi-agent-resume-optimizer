# 🔧 LMARO Backend

FastAPI-based backend with multi-agent LLM pipeline for intelligent resume optimization.

<p align="center">
  <a href="../README.md">← Back to Main README</a>
</p>

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [API Endpoints](#api-endpoints)
- [Core Components](#core-components)
- [Installation](#installation)
- [Configuration](#configuration)
- [Testing](#testing)
- [Development](#development)

## 🎯 Overview

The backend implements a sophisticated multi-agent system where specialized AI agents collaborate to generate, evaluate, and optimize resumes. Built with FastAPI for high performance and Pydantic for data validation.

### Key Capabilities

- **9 REST API Endpoints** with full CRUD operations
- **Server-Sent Events (SSE)** for real-time progress streaming
- **Multi-Agent Pipeline** with 5 specialized agents
- **Dual Optimization Loops** (evaluation + factuality)
- **Retry Logic** for API rate limiting (503 errors)
- **DOCX Rendering** with template support
- **File-Based Storage** with structured data management

## 🏗️ Architecture

### Multi-Agent System

```
User Request
     ↓
┌─────────────────────────┐
│   1. GENERATOR          │ → Creates initial resume from JD + profile
└─────────────────────────┘
     ↓
┌─────────────────────────┐
│   2. EVALUATOR          │ → Scores resume (keyword 35% + LLM 65%)
└─────────────────────────┘
     ↓
    Score < 90?
     ↓ Yes
┌─────────────────────────┐
│   3. REVISER            │ → Improves resume based on feedback
└─────────────────────────┘
     ↓
    Repeat (max 3x)
     ↓
┌─────────────────────────┐
│   4. FACTUALITY CHECKER │ → Verifies claims against profile
└─────────────────────────┘
     ↓
    Score < 90?
     ↓ Yes
┌─────────────────────────┐
│   3. REVISER (again)    │ → Fixes inaccuracies
└─────────────────────────┘
     ↓
    Repeat (max 3x)
     ↓
┌─────────────────────────┐
│   5. RENDERER           │ → Converts JSON to formatted DOCX
└─────────────────────────┘
     ↓
Final Resume (JSON + DOCX)
```

### Data Flow

1. **Input**: Job Description + User Profile
2. **Generation**: LLM creates tailored resume
3. **Evaluation**: Score against JD requirements
4. **Revision**: Improve based on evaluation feedback
5. **Factuality**: Verify all claims are accurate
6. **Rendering**: Format as professional DOCX
7. **Output**: JSON + DOCX files saved to database

## 🌐 API Endpoints

### Base URL
```
http://localhost:8000/api
```

### Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/generate` | Generate optimized resume |
| `POST` | `/generate/stream` | Generate with SSE progress |
| `POST` | `/evaluate` | Evaluate existing resume |
| `POST` | `/factuality` | Check resume factuality |
| `GET` | `/resume/{username}/{job_id}` | Get resume |
| `POST` | `/user/upload` | Upload user profile |
| `POST` | `/job/create` | Create job description |
| `GET` | `/jobs` | List all jobs |
| `GET` | `/resumes/{username}` | List user's resumes |
| `GET` | `/health` | API health check |

### Example: Generate Resume with SSE

```bash
curl -N -X POST http://localhost:8000/api/generate/stream \
  -H "Content-Type: application/json" \
  -d '{
    "username": "chandan",
    "jd_text": "Software Engineer with Python...",
    "company": "Google",
    "role": "SWE Intern",
    "optimize": true
  }'
```

**Response (SSE Stream):**
```
data: {"stage":"setup","message":"Loading profile...","progress":5}

data: {"stage":"generating","message":"Creating resume...","progress":10}

data: {"stage":"evaluating","message":"Scoring...","progress":35}

data: {"stage":"complete","message":"Done!","progress":100,"data":{...}}
```

### Full API Documentation

📖 **[Complete API Reference](./api/docs/API_REFERENCE.md)**

## 🧩 Core Components

### 1. Generator (`src/generator.py`)

Creates initial resume from job description and user profile.

**Input:**
- Job description text
- User profile (JSON)
- Company name
- Role title

**Output:**
- Resume JSON with sections: header, summary, skills, experience, projects

**Key Features:**
- Gemini 2.5 Flash LLM
- 8,000 token limit
- Structured JSON output
- Tailored to JD keywords

### 2. Evaluator (`src/evaluator.py`)

Scores resume against job requirements.

**Scoring System:**
- **35%** - Keyword Match (TF-IDF similarity)
- **65%** - LLM Evaluation (semantic analysis)

**Output:**
- Total score (0-100)
- Section-by-section breakdown
- Detailed feedback for improvement

**Token Limit:** 6,000

### 3. Factuality Checker (`src/factuality_checker.py`)

Verifies every claim against user profile.

**Checks:**
- Dates and durations match
- Projects exist in profile
- Metrics are accurate
- Technologies are verified
- No fabricated achievements

**Output:**
- Factuality score (0-100)
- Issues list by section
- Specific claims flagged

**Token Limit:** 10,000

### 4. Reviser (`src/reviser.py`)

Improves resume based on feedback.

**Revision Types:**
- **Evaluation Revision**: Improve JD alignment
- **Factuality Revision**: Fix inaccuracies

**Input:**
- Current resume
- Feedback (from evaluator or factuality checker)
- User profile
- Job description

**Output:**
- Improved resume JSON

**Token Limit:** 10,000

### 5. Renderer (`src/renderer.py`)

Converts JSON to formatted DOCX.

**Features:**
- Uses custom templates
- Bold text markers (`**text**`)
- Hyperlinks for GitHub/LinkedIn
- Tab alignment
- Professional formatting

**Input:**
- Resume JSON
- Template DOCX path

**Output:**
- Formatted DOCX file

### 6. LLM Adapter (`aro/llm_adapter.py`)

Wrapper for Google Gemini API.

**Features:**
- Retry logic (3 attempts)
- Exponential backoff for 503 errors
- JSON structured outputs
- Error handling

**SDK:** `google-genai` (NEW SDK, not legacy)

**Model:** `gemini-2.5-flash`

### 7. Data Providers (`src/providers.py`)

Manages data storage and retrieval.

**UserProvider:**
- `get(username)` - Load user profile
- Data location: `database/{username}/profile.json`

**JobProvider:**
- `get(job_id)` - Load job description
- `save(job_data)` - Save job
- Data location: `database/jobs/{job_id}.json`

**ResumeProvider:**
- `save(resume, username, job_id)` - Save resume
- `get(username, job_id)` - Load resume
- Data location: `database/resumes/{username}/{job_id}.json`

### 8. Streaming Pipeline (`src/streaming_pipeline.py`)

SSE implementation for real-time progress.

**Yields:**
- Setup stage
- Generation progress
- Evaluation iterations
- Factuality checks
- Rendering status
- Final results

**Progress Tracking:**
- 0-5%: Setup
- 5-25%: Generation
- 25-50%: Evaluation loop
- 50-80%: Factuality loop
- 80-100%: Rendering & saving

## 🚀 Installation

### Prerequisites

- Python 3.8+
- pip
- Gemini API key

### Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cat > .env << EOF
GEMINI_API_KEY=your_api_key_here
LLM_PROVIDER=gemini
EOF
```

### Dependencies

```txt
fastapi==0.115.0
uvicorn==0.30.0
python-docx==1.1.2
pyyaml==6.0.2
google-genai
python-multipart==0.0.12
pydantic==2.9.0
python-dotenv==1.0.1
```

## ⚙️ Configuration

### Environment Variables (`.env`)

```bash
GEMINI_API_KEY=your_api_key_here
LLM_PROVIDER=gemini
```

### Token Limits

Configured in each component:

```python
# Generator
max_tokens=8000

# Evaluator
max_tokens=6000

# Factuality Checker
max_tokens=10000

# Reviser
max_tokens=10000
```

### Optimization Thresholds

```python
# src/streaming_pipeline.py
eval_threshold = 90      # Evaluation score target
fact_threshold = 90      # Factuality score target
max_eval_revisions = 3   # Max evaluation iterations
max_fact_revisions = 3   # Max factuality iterations
```

### Template Location

```
templates/Chandan_Resume_Format.docx
```

Copy your resume template to this location for DOCX generation.

## 🧪 Testing

### Run All Tests

```bash
# API health check
python tests/test_api.py

# Test generator
python tests/test_generator.py

# Test evaluator
python tests/test_evaluator.py

# Test factuality checker
python tests/test_factuality.py
```

### Test Full Pipeline

```bash
python src/main.py
```

**Output:**
- `database/resumes/chandan/job1.json` - Resume JSON
- `output/chandan_job1.docx` - Word document
- `final_resume.json` - Copy in backend/
- `final_evaluation.json` - Evaluation results
- `final_factuality.json` - Factuality results

### Manual API Testing

```bash
# Start server
python main.py

# Health check
curl http://localhost:8000/api/health

# Generate resume
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d @test_request.json
```

## 💻 Development

### Project Structure

```
backend/
├── main.py                 # FastAPI server
├── src/
│   ├── main.py            # CLI pipeline
│   ├── generator.py       # Resume generation
│   ├── evaluator.py       # JD evaluation
│   ├── factuality_checker.py  # Accuracy check
│   ├── reviser.py         # Improvement logic
│   ├── renderer.py        # DOCX conversion
│   ├── streaming_pipeline.py  # SSE implementation
│   └── providers.py       # Data management
├── api/
│   ├── routes.py          # REST endpoints
│   ├── models.py          # Pydantic schemas
│   └── docs/              # API documentation
├── aro/
│   └── llm_adapter.py     # Gemini wrapper
├── database/              # Data storage
│   ├── chandan/
│   │   └── profile.json   # User profile
│   ├── jobs/              # Job descriptions
│   └── resumes/           # Generated resumes
├── output/                # DOCX files
├── tests/                 # Test suite
├── requirements.txt       # Dependencies
└── .env                   # API keys
```

### Adding New Endpoints

1. Define Pydantic model in `api/models.py`
2. Add route in `api/routes.py`
3. Update `API_REFERENCE.md`

### Adding New Agent

1. Create new file in `src/`
2. Implement with LLM adapter
3. Integrate in `src/main.py` pipeline
4. Update `streaming_pipeline.py` for SSE

### Running Server

```bash
# Development
python main.py

# Production
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

**Server runs on:** http://localhost:8000

**API Docs:** http://localhost:8000/docs

## 📊 Performance

### Benchmarks

- **Pipeline Duration**: 30-60 seconds
- **API Response Time**: <100ms (non-generation endpoints)
- **LLM Call Time**: 3-8 seconds per call
- **DOCX Generation**: <1 second
- **Memory Usage**: ~2GB RAM

### Optimization Tips

1. **Reduce Token Limits**: Lower max_tokens for faster responses
2. **Cache LLM Responses**: Store common patterns
3. **Batch Operations**: Group multiple API calls
4. **Use Async**: Parallel LLM calls where possible

## 🐛 Troubleshooting

### Common Issues

**503 Errors from Gemini API:**
- Retry logic handles this automatically (3 attempts)
- Exponential backoff implemented
- Check API quota

**Template Not Found:**
- Ensure template exists at `templates/Chandan_Resume_Format.docx`
- DOCX generation skipped if missing

**Import Errors:**
- Activate virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

**Port Already in Use:**
```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9  # Mac/Linux
netstat -ano | findstr :8000   # Windows
```

## 🔗 Related Documentation

- [Main README](../README.md)
- [Frontend README](../frontend/README.md)
- [API Reference](./api/docs/API_REFERENCE.md)

## 📧 Support

For backend-specific issues:
- Open an issue on GitHub
- Email: chandan.keelara@gmail.com
- Include: Python version, error logs, request/response

<p align="right">(<a href="#readme-top">back to top</a>)</p>
