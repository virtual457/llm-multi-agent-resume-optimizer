# LLM Multi-Agent Resume Optimizer (LMARO)

**Autonomous resume generation and optimization using multi-agent AI architecture**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org/)

---

## 🎯 Project Overview

LMARO (LLM Multi-Agent Resume Optimizer) is an intelligent system that uses multiple AI agents to automatically generate, evaluate, and iteratively optimize resumes tailored to specific job descriptions. The system employs a **multi-agent architecture** where specialized LLM agents collaborate to produce ATS-optimized, keyword-rich, and professionally formatted resumes.

### Core Value Proposition

- ✅ **Automated Resume Generation** - Create tailored resumes from job descriptions
- ✅ **Multi-Agent Optimization** - Generator, Evaluator, and Reviser agents collaborate
- ✅ **Iterative Improvement** - Continuous refinement until quality threshold met
- ✅ **ATS-Optimized Output** - Keyword matching and semantic alignment scoring
- ✅ **Production-Ready Rendering** - Professional DOCX output with formatting
- ✅ **Full Traceability** - Version control of iterations with scores and diffs

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     React/Next.js Frontend                      │
│            (Job input, iteration viewer, analytics)             │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTP/REST
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Python FastAPI Backend                       │
│                                                                 │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐      │
│  │  Generator   │ → │  Evaluator   │ → │   Reviser    │      │
│  │    Agent     │   │    Agent     │   │    Agent     │      │
│  │   (LLM 1)    │   │   (LLM 2)    │   │   (LLM 3)    │      │
│  └──────────────┘   └──────────────┘   └──────────────┘      │
│         ↓                   ↓                   ↓              │
│  ┌──────────────────────────────────────────────────────┐     │
│  │           LLM Adapter (Pluggable Interface)          │     │
│  │        OpenAI | Anthropic | Local HF | Mock          │     │
│  └──────────────────────────────────────────────────────┘     │
│         ↓                                                      │
│  ┌──────────────────────────────────────────────────────┐     │
│  │    Renderer (python-docx) + Storage + Metrics        │     │
│  └──────────────────────────────────────────────────────┘     │
└─────────────────────────────────────────────────────────────────┘
                             ↓
                    Generated Resume.docx
```

### Multi-Agent System

**Generator Agent**
- Creates resume sections from JD and candidate profile
- Uses structured prompts for consistency
- Outputs JSON with summary, skills, experience, projects

**Evaluator Agent**
- Scores resume against JD (0-100 scale)
- Provides keyword match, semantic alignment, metrics presence
- Identifies missing keywords and improvement areas

**Reviser Agent**
- Analyzes evaluator feedback
- Generates targeted improvement instructions
- Guides generator for next iteration

---

## 🚀 Features

### Core Features
- **JD Analysis** - Extract keywords and requirements from job descriptions
- **Multi-Agent Collaboration** - Three specialized LLM agents working together
- **Iterative Optimization** - Continuous improvement loop until threshold met
- **Comprehensive Scoring** - Keyword match (35%), semantic alignment (25%), quantitative metrics (20%), role-specific skills (20%)
- **Version Control** - Track all iterations with scores and diffs
- **DOCX Rendering** - Professional Word document output with bold markers and hyperlinks

### Technical Features
- **Pluggable LLM Providers** - OpenAI, Anthropic, local models, or mock
- **Configuration-Driven** - All behavior controlled via YAML
- **Artifact Storage** - Complete iteration history with timestamps
- **Semantic Similarity** - Embedding-based content matching
- **ATS Optimization** - Keyword density and formatting compliance
- **Bold Marker Support** - `**text**` markers for emphasis
- **Hyperlink Generation** - GitHub and contact links

---

## 📁 Project Structure

```
llm-multi-agent-resume-optimizer/
├── backend/                    # Python FastAPI backend
│   ├── aro/                   # Core application
│   │   ├── agents/            # LLM agents
│   │   │   ├── __init__.py
│   │   │   ├── generator.py   # Resume generation agent
│   │   │   ├── evaluator.py   # Scoring and evaluation agent
│   │   │   └── reviser.py     # Improvement planning agent
│   │   ├── __init__.py
│   │   ├── llm_adapter.py     # Pluggable LLM interface
│   │   ├── renderer.py        # DOCX generation (python-docx)
│   │   ├── metrics.py         # Scoring functions
│   │   ├── storage.py         # Artifact versioning
│   │   ├── prompts.py         # Centralized prompt templates
│   │   └── utils.py           # Helper functions
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py          # FastAPI endpoints
│   ├── config/
│   │   └── settings.py        # Application settings
│   ├── main.py                # FastAPI application
│   └── requirements.txt       # Python dependencies
│
├── frontend/                   # Next.js UI
│   ├── app/
│   │   ├── page.tsx           # Landing page
│   │   ├── dashboard/         # Main dashboard
│   │   ├── iterations/        # Iteration viewer
│   │   └── layout.tsx         # Root layout
│   ├── components/
│   │   ├── JDInput.tsx        # Job description input
│   │   ├── IterationViewer.tsx # View iterations
│   │   ├── ScoreCard.tsx      # Score visualization
│   │   └── ConfigPanel.tsx    # Settings configuration
│   ├── lib/
│   │   └── api.ts             # Backend API client
│   ├── package.json
│   └── tsconfig.json
│
├── templates/
│   └── Chandan_Resume_Format.docx  # Resume template
│
├── config/
│   └── current_application.yaml    # Job application config
│
├── docs/
│   ├── architecture.md        # System architecture
│   ├── prompts.md            # Prompt engineering docs
│   └── api.md                # API documentation
│
├── output/                    # Generated artifacts
│   └── [job-timestamp]/
│       └── iteration-[n]/
│           ├── resume.json
│           ├── resume.docx
│           ├── score.json
│           └── diff.patch
│
├── tests/
│   ├── test_generator.py
│   ├── test_evaluator.py
│   ├── test_metrics.py
│   └── test_renderer.py
│
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🛠️ Tech Stack

### Backend
- **Python 3.10+** - Core language
- **FastAPI** - Modern async web framework
- **python-docx** - Word document generation
- **PyYAML** - Configuration management
- **sentence-transformers** - Semantic similarity (optional)
- **LLM Integration** - OpenAI/Anthropic/HuggingFace

### Frontend
- **Next.js 15** - React framework
- **React 19** - UI library
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling
- **Axios** - API communication

### DevOps
- **GitHub Actions** - CI/CD pipeline
- **Docker** (optional) - Containerization
- **Vercel** - Frontend deployment
- **Render/Railway** - Backend deployment

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- LLM API key (OpenAI or Anthropic)

### Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Set environment variables
export ANTHROPIC_API_KEY="your-key-here"  # or OPENAI_API_KEY

# Run backend
python main.py
```

Backend runs at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at `http://localhost:3000`

---

## 📊 How It Works

### 1. Input Phase
- User provides job description
- System loads candidate profile from YAML
- Configures iteration parameters (max iterations, score threshold)

### 2. Generation Loop

```python
iteration = 0
best_score = 0
no_improvement_count = 0

while iteration < max_iterations:
    # Agent 1: Generate resume
    resume_json = generator_agent.generate(jd, profile, context)
    
    # Agent 2: Evaluate resume
    score_report = evaluator_agent.evaluate(jd, resume_json)
    
    # Check for improvement
    if score_report.total_score > best_score:
        best_score = score_report.total_score
        save_iteration(resume_json, score_report)
        no_improvement_count = 0
    else:
        no_improvement_count += 1
    
    # Check stopping conditions
    if best_score >= score_threshold:
        break
    if no_improvement_count >= max_no_improvement:
        break
    
    # Agent 3: Plan revisions
    revision_plan = reviser_agent.plan(score_report)
    context.update(revision_plan)
    
    iteration += 1

# Render best resume to DOCX
renderer.render(best_resume_json, template_path)
```

### 3. Scoring System

**Composite Score (0-100):**
- **Keyword Match (35%)** - JD keywords present in resume
- **Semantic Alignment (25%)** - Embedding similarity between JD and resume
- **Quantitative Metrics (20%)** - Presence of numbers/percentages
- **Role-Specific Skills (20%)** - Critical skills for the role

### 4. Output
- Final resume as DOCX
- All iterations saved with scores
- Diff patches showing changes
- JSON metadata for analysis

---

## 🎨 API Endpoints

### Generation
```http
POST /api/generate
Content-Type: application/json

{
  "jd_text": "Job description...",
  "profile": { ... },
  "settings": {
    "max_iterations": 5,
    "score_threshold": 85
  }
}
```

### Evaluation
```http
POST /api/evaluate
Content-Type: application/json

{
  "jd_text": "...",
  "resume_json": { ... }
}
```

### Render
```http
POST /api/render
Content-Type: application/json

{
  "resume_json": { ... },
  "format": "docx"
}
```

---

## 📈 Development Roadmap

### MVP (Week 1-2)
- [x] Project structure
- [ ] LLM adapter with mock/real providers
- [ ] Generator agent with prompts
- [ ] Evaluator agent with scoring
- [ ] Basic iteration loop
- [ ] DOCX renderer (reuse existing code)
- [ ] CLI interface

### Enhancement (Week 3-4)
- [ ] Reviser agent
- [ ] Semantic similarity scoring
- [ ] Artifact versioning and storage
- [ ] Diff generation
- [ ] Next.js frontend
- [ ] Real-time progress updates

### Production (Week 5-6)
- [ ] Comprehensive testing
- [ ] CI/CD pipeline
- [ ] Documentation
- [ ] Error handling and validation
- [ ] Rate limiting and caching
- [ ] Deployment scripts

---

## 🔐 Security & Best Practices

- **API Keys** - Environment variables only, never committed
- **Input Validation** - Sanitize JD text and profile data
- **Rate Limiting** - Prevent API abuse
- **Caching** - Reduce LLM costs through response caching
- **Logging** - Comprehensive audit trail
- **PII Protection** - Strip sensitive data from logs

---

## 🧪 Testing Strategy

### Unit Tests
- YAML parsing and validation
- Keyword matching algorithms
- DOCX rendering logic
- Scoring functions

### Integration Tests
- Generator + Evaluator pipeline
- Full iteration loop with mocked LLMs
- API endpoint responses

### End-to-End Tests
- Complete generation for sample JDs
- Human evaluation of outputs
- Regression tests for DOCX formatting

---

## 📚 Documentation

- [Architecture Overview](docs/architecture.md)
- [Prompt Engineering Guide](docs/prompts.md)
- [API Reference](docs/api.md)
- [Deployment Guide](docs/deployment.md)

---

## 🤝 Contributing

This is a personal project for Chandan Gowda K S's job application automation. However, suggestions and improvements are welcome!

---

## 📝 License

MIT License - See [LICENSE](LICENSE) for details

---

## 👤 Author

**Chandan Gowda K S**

- 📧 Email: chandan.keelara@gmail.com
- 💼 LinkedIn: [linkedin.com/in/chandan-gowda-k-s-765194186](https://www.linkedin.com/in/chandan-gowda-k-s-765194186/)
- 🐙 GitHub: [@virtual457](https://github.com/virtual457)
- 🌐 Portfolio: [virtual457.github.io](https://virtual457.github.io)

---

## 🎓 Project Purpose

This project serves dual purposes:
1. **Practical Tool** - Automate and optimize job application resumes
2. **Portfolio Showcase** - Demonstrate expertise in:
   - Multi-agent AI systems
   - LLM integration and prompt engineering
   - Full-stack development (Python + Next.js)
   - System architecture and design
   - Production-quality software engineering

**Built as part of Northeastern University MS Computer Science program (2025-2027)**

---

**Status:** 🚧 Active Development - MVP Target: December 2025
