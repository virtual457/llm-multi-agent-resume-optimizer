# LMARO Backend - Quick Start

## 🚀 Setup (5 minutes)

### 1. Create virtual environment
```bash
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Get Gemini API Key
- Visit: https://makersuite.google.com/app/apikey
- Create API key
- Copy it

### 4. Create .env file
```bash
# Copy example and edit
copy .env.example .env
```

**Edit `.env` and add your key:**
```env
LLM_PROVIDER=gemini
GEMINI_API_KEY=your-key-here
```

---

## 🧪 Test Everything

### Quick Test (Automated)
```bash
test.bat
```

### Manual Tests

**Test 1: LLM Adapter**
```bash
python aro\llm_adapter.py
```

**Test 2: Comprehensive Tests**
```bash
python test_llm.py
```

**Test 3: FastAPI Server**
```bash
python main.py
```

Then open browser:
- http://localhost:8000
- http://localhost:8000/health
- http://localhost:8000/api/test

---

## ✅ What Works Now

- LLM Adapter (Gemini, Anthropic, OpenAI, Mock)
- FastAPI server with CORS
- Basic API endpoints
- Prompt templates

## ❌ What's Next to Build

- Generator Agent
- Evaluator Agent
- Renderer (DOCX generation)
- Iteration loop

---

## 📝 Current Status

**Can test:**
- ✅ Gemini API calls
- ✅ JSON generation
- ✅ FastAPI endpoints

**Can't test yet:**
- ❌ Full resume generation
- ❌ DOCX output
- ❌ Optimization loop

**Ready for:** Building Generator Agent!
