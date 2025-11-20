[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<a id="readme-top"></a>

<!-- PROJECT TITLE -->
<div align="center">
  <h3 align="center">🤖 LMARO - LLM Multi-Agent Resume Optimizer</h3>
  <p align="center">
    An AI-powered resume optimization system that uses multiple coordinated LLM agents to generate, evaluate, and iteratively improve resumes tailored to specific job descriptions with factuality verification.
    <br/>
    <a href="#documentation"><strong>Explore the docs »</strong></a>
    <br/><br/>
    <a href="#demo">View Demo</a>
    ·
    <a href="https://github.com/virtual457/llm-multi-agent-resume-optimizer/issues">Report Bug</a>
    ·
    <a href="https://github.com/virtual457/llm-multi-agent-resume-optimizer/issues">Request Feature</a>
  </p>
</div>

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## About The Project

LMARO is an intelligent resume optimization platform that leverages Google's Gemini 2.5 Flash LLM with a multi-agent architecture to create perfectly tailored resumes. The system analyzes job descriptions, matches them against user profiles, and iteratively refines resumes until they achieve 90+ scores in both job alignment and factual accuracy.

### What Makes LMARO Different?

- **Multi-Agent System**: Five specialized agents (Generator, Evaluator, Factuality Checker, Reviser, Renderer) work in coordination
- **Dual Optimization Loop**: Separate evaluation and factuality checking cycles ensure both relevance and accuracy
- **Automated Iteration**: Continues revising until quality thresholds are met (90/100 for both metrics)
- **Real-Time Progress**: Server-Sent Events (SSE) provide live updates during the 30-60 second optimization process
- **Factuality Verification**: Every claim in the resume is verified against the user's actual profile
- **Production Ready**: Complete REST API with comprehensive error handling and retry logic

### Problem Solved

Traditional resume writing is time-consuming and often results in generic documents that don't highlight relevant skills. LMARO automates this process while ensuring:
- Perfect alignment with job requirements
- 100% factual accuracy (no fabricated claims)
- ATS optimization with keyword matching
- Professional formatting in DOCX

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ✨ Key Features

### Backend (FastAPI + Python)
- ✅ **9 REST API Endpoints** - Complete CRUD operations for users, jobs, and resumes
- ✅ **Real-Time SSE Streaming** - Live progress updates during generation
- ✅ **Multi-Agent Pipeline** - Generator → Evaluator → Reviser → Factuality Checker
- ✅ **Dual Scoring System** - Job alignment (35% keyword + 65% LLM) + Factuality verification
- ✅ **Automated Iteration** - Up to 3 revision cycles per optimization phase
- ✅ **DOCX Rendering** - Professional document formatting with templates
- ✅ **Retry Logic** - Handles API rate limits (503 errors) with exponential backoff
- ✅ **Data Persistence** - Structured file-based storage (JSON + DOCX)

### Frontend (Next.js 15 + React 19)
- ✅ **Google Material Design** - Professional UI with Google Sans/Product Sans fonts
- ✅ **Material Icons** - Consistent iconography throughout
- ✅ **Multi-Page Flow** - Landing → Generate → Progress → Results → Preview
- ✅ **Real-Time Progress Modal** - Animated progress tracking with stage indicators
- ✅ **Score Visualization** - Circular progress indicators for both metrics
- ✅ **Resume Preview** - Full-page formatted resume view with print support
- ✅ **Download Options** - JSON and DOCX export capabilities
- ✅ **Mesh Gradient Backgrounds** - Animated floating orbs for visual appeal

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Next.js 15)                    │
│  Landing → Generate Form → SSE Progress Modal → Results → Preview│
└────────────────────────────┬────────────────────────────────────┘
                             │ REST API + SSE
┌────────────────────────────▼────────────────────────────────────┐
│                    BACKEND (FastAPI + Python)                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              OPTIMIZATION PIPELINE                        │  │
│  │  1. Generator → Initial Resume                           │  │
│  │  2. Evaluator → Score (keyword 35% + LLM 65%)           │  │
│  │  3. Reviser → Improve (if score < 90)                   │  │
│  │  4. Repeat 2-3 (max 3 iterations)                       │  │
│  │  5. Factuality Checker → Verify against profile         │  │
│  │  6. Reviser → Fix inaccuracies (if score < 90)         │  │
│  │  7. Repeat 5-6 (max 3 iterations)                       │  │
│  │  8. Renderer → DOCX output                              │  │
│  └──────────────────────────────────────────────────────────┘  │
│                             ↕                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │            LLM ADAPTER (Gemini 2.5 Flash)                │  │
│  │  • Retry logic for 503 errors                            │  │
│  │  • Token limits: 8K-10K per call                         │  │
│  │  • JSON structured outputs                               │  │
│  └──────────────────────────────────────────────────────────┘  │
│                             ↕                                    │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │               DATA PROVIDERS                              │  │
│  │  • UserProvider: Load user profiles                      │  │
│  │  • JobProvider: Manage job descriptions                  │  │
│  │  • ResumeProvider: Save/load generated resumes           │  │
│  └──────────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────────┘
```

### Data Flow

1. **User Input** → Company, Role, Job Description (via frontend form)
2. **SSE Stream Initiated** → Backend starts optimization pipeline
3. **Generation** → LLM creates initial resume from JD + user profile
4. **Evaluation Loop** → Score → Revise → Re-score (until 90+ or 3 iterations)
5. **Factuality Loop** → Check → Fix → Re-check (until 90+ or 3 iterations)
6. **Rendering** → Convert JSON to formatted DOCX
7. **Results** → Frontend displays scores + download options

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.115.0
- **LLM**: Google Gemini 2.5 Flash (`google-genai` SDK)
- **Document Processing**: `python-docx` for DOCX generation
- **Validation**: Pydantic 2.9.0 for data models
- **Testing**: Pytest (comprehensive test suite)
- **Language**: Python 3.8+

### Frontend
- **Framework**: Next.js 15 (App Router)
- **UI Library**: React 19
- **Styling**: Tailwind CSS 3.4
- **Fonts**: Google Sans, Product Sans (via Google Fonts CDN)
- **Icons**: Material Icons
- **Language**: TypeScript 5

### Infrastructure
- **API Communication**: Server-Sent Events (SSE) for real-time updates
- **Data Storage**: File-based JSON + DOCX (structured in `database/` directory)
- **CORS**: Configured for `localhost:3000`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

### Prerequisites

**Backend:**
- Python 3.8 or higher
- Gemini API key (get from [Google AI Studio](https://makersuite.google.com/app/apikey))

**Frontend:**
- Node.js 18 or higher
- npm or yarn

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/virtual457/llm-multi-agent-resume-optimizer.git
cd llm-multi-agent-resume-optimizer
```

#### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
echo "LLM_PROVIDER=gemini" >> .env

# Copy resume template (required for DOCX generation)
# Place your template at: templates/Chandan_Resume_Format.docx
```

#### 3. Frontend Setup
```bash
cd ../frontend

# Install dependencies
npm install
```

#### 4. Start Both Servers

**Terminal 1 - Backend:**
```bash
cd backend
python main.py
```
Backend runs on: http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```
Frontend runs on: http://localhost:3000

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📖 Usage

### Quick Start

1. **Visit** http://localhost:3000
2. **Click** "Get Started" button
3. **Fill Form**:
   - Company: e.g., "Google"
   - Role: e.g., "Software Engineer Intern"
   - Job Description: Paste complete JD
4. **Generate**: Click "Generate Resume"
5. **Watch Progress**: Modal shows real-time updates (30-60 seconds)
6. **View Results**: See scores (Evaluation + Factuality)
7. **Preview**: Click "Preview Resume" to see formatted output
8. **Download**: Get JSON or DOCX formats

### Sample Job Description

Click "Paste Sample JD" in the form to load a pre-filled example.

### API Testing

Test backend directly:
```bash
# Health check
curl http://localhost:8000/api/health

# Generate resume via API
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "username": "chandan",
    "jd_text": "Software Engineer with Python...",
    "company": "Google",
    "role": "SWE Intern",
    "optimize": true
  }'
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📁 Project Structure

```
llm-multi-agent-resume-optimizer/
├── backend/                    # FastAPI Backend
│   ├── main.py                # FastAPI server entry point
│   ├── src/
│   │   ├── main.py           # Optimization pipeline
│   │   ├── generator.py      # Resume generation agent
│   │   ├── evaluator.py      # JD evaluation agent
│   │   ├── factuality_checker.py  # Accuracy verification
│   │   ├── reviser.py        # Resume improvement agent
│   │   ├── renderer.py       # DOCX conversion
│   │   ├── streaming_pipeline.py  # SSE implementation
│   │   └── providers.py      # Data management
│   ├── api/
│   │   ├── routes.py         # REST endpoints
│   │   ├── models.py         # Pydantic schemas
│   │   └── docs/             # API documentation
│   ├── aro/
│   │   └── llm_adapter.py    # Gemini SDK wrapper
│   ├── database/             # User profiles, jobs, resumes
│   ├── output/               # Generated DOCX files
│   ├── tests/                # Test suite
│   └── README.md            # Backend documentation
│
├── frontend/                  # Next.js Frontend
│   ├── app/
│   │   ├── page.tsx          # Landing page
│   │   ├── generate/         # Form page
│   │   ├── results/          # Results page
│   │   ├── preview/          # Resume preview
│   │   ├── layout.tsx        # Root layout
│   │   └── globals.css       # Google Material Design
│   ├── components/
│   │   ├── GenerationModal.tsx    # Progress tracking
│   │   └── ResumeGenerator.tsx    # Form component
│   └── README.md            # Frontend documentation
│
├── templates/                 # Resume DOCX templates
└── README.md                 # This file
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📚 Documentation

### Detailed Guides

- **[Backend Documentation](./backend/README.md)** - API endpoints, pipeline details, testing
- **[Frontend Documentation](./frontend/README.md)** - UI components, routing, styling
- **[API Reference](./backend/api/docs/API_REFERENCE.md)** - Complete API specification

### Key Concepts

**Evaluation Scoring:**
- **35% Keyword Match**: TF-IDF similarity between resume and JD
- **65% LLM Evaluation**: Semantic understanding of job fit
- **Threshold**: 90/100 required to pass

**Factuality Checking:**
- Verifies all claims against user profile
- Checks metrics, dates, project existence
- Flags fabricated achievements
- **Threshold**: 90/100 required

**Revision Strategy:**
- Max 3 iterations per phase (evaluation + factuality)
- Each iteration uses detailed feedback from previous check
- Stops early if threshold is met

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🗺️ Roadmap

- [x] Multi-agent backend pipeline
- [x] Real-time SSE progress streaming
- [x] Google Material Design frontend
- [x] Resume preview with print support
- [x] Dual scoring system (evaluation + factuality)
- [x] DOCX rendering with templates
- [ ] User authentication and accounts
- [ ] Resume history and versioning
- [ ] Multiple resume templates
- [ ] Cover letter generation
- [ ] LinkedIn profile optimization
- [ ] ATS compatibility checker
- [ ] A/B testing for resume variations
- [ ] Analytics dashboard
- [ ] Mobile app (React Native)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Areas for contribution:
- Additional LLM providers (OpenAI, Anthropic)
- Enhanced evaluation metrics
- Resume template designs
- UI/UX improvements
- Test coverage expansion

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📧 Contact

Chandan Gowda K S – chandan.keelara@gmail.com

Project Link: https://github.com/virtual457/llm-multi-agent-resume-optimizer

Portfolio: https://virtual457.github.io

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🙏 Acknowledgments

- Google Gemini AI for LLM capabilities
- FastAPI team for excellent framework
- Next.js team for React framework
- Material Design for UI guidelines
- Open source community

Other portfolio projects:
- [Dino Game Deep RL](https://github.com/virtual457/dino-game) - Autonomous game-playing AI
- [Calendly Clone](https://github.com/virtual457/Calendly) - Enterprise scheduling platform
- [Orion PaaS](https://github.com/virtual457/Orion-platform) - Kubernetes-based platform
- [Face Recognition System](https://github.com/virtual457/Recognition-and-Validation-of-Faces-using-Machine-Learning-and-Image-Processing)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/virtual457/llm-multi-agent-resume-optimizer.svg?style=for-the-badge
[forks-shield]: https://img.shields.io/github/forks/virtual457/llm-multi-agent-resume-optimizer.svg?style=for-the-badge
[stars-shield]: https://img.shields.io/github/stars/virtual457/llm-multi-agent-resume-optimizer.svg?style=for-the-badge
[issues-shield]: https://img.shields.io/github/issues/virtual457/llm-multi-agent-resume-optimizer.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/virtual457/llm-multi-agent-resume-optimizer.svg?style=for-the-badge
[contributors-url]: https://github.com/virtual457/llm-multi-agent-resume-optimizer/graphs/contributors
[forks-url]: https://github.com/virtual457/llm-multi-agent-resume-optimizer/network/members
[stars-url]: https://github.com/virtual457/llm-multi-agent-resume-optimizer/stargazers
[issues-url]: https://github.com/virtual457/llm-multi-agent-resume-optimizer/issues
[license-url]: https://github.com/virtual457/llm-multi-agent-resume-optimizer/blob/master/LICENSE
