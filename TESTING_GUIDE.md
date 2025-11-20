# Testing Guide - LLM Multi-Agent Resume Optimizer

**Last Updated:** November 18, 2025
**Current Build:** LLM Adapter + FastAPI Skeleton

---

## 🚀 QUICK START - Test What We've Built

### **Step 1: Setup Python Environment**

```bash
# Navigate to backend directory
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Expected output:** All packages install successfully

---

### **Step 2: Get Gemini API Key**

1. **Go to:** https://makersuite.google.com/app/apikey
2. **Click:** "Create API Key"
3. **Copy** the API key

---

### **Step 3: Configure Environment**

**Create `.env` file in `backend/` folder:**

```bash
# In backend folder, create .env file
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend
```

**Add this to `.env`:**
```env
# LLM Provider
LLM_PROVIDER=gemini

# Gemini API Key (paste your key here)
GEMINI_API_KEY=your-gemini-api-key-here

# Server Settings
HOST=0.0.0.0
PORT=8000
DEBUG=True

# CORS (for frontend when we build it)
CORS_ORIGINS=http://localhost:3000,http://127.0.0.1:3000

# Iteration Settings
MAX_ITERATIONS=5
SCORE_THRESHOLD=85
```

**Replace `your-gemini-api-key-here` with your actual key!**

---

### **Step 4: Test LLM Adapter**

**Run the test script:**

```bash
# Make sure you're in backend folder
cd D:\Git\virtual457-projects\llm-multi-agent-resume-optimizer\backend

# Activate venv
.venv\Scripts\activate

# Test the LLM adapter
python aro/llm_adapter.py
```

**Expected output:**
```
============================================================
LLM ADAPTER TEST
============================================================

1. Testing Mock Adapter...
   ✅ Mock: Mock response #1

2. Testing Gemini...
   ✅ Gemini: Hello from Gemini!

============================================================
Test complete!
```

**What this tests:**
- ✅ Virtual environment works
- ✅ Dependencies installed correctly
- ✅ Gemini API key is valid
- ✅ LLM adapter can call Gemini successfully

**If it fails:**
- Check API key is correct in `.env`
- Verify `google-generativeai` package installed
- Check internet connection

---

### **Step 5: Test FastAPI Server**

**Start the server:**

```bash
# In backend folder with venv activated
python main.py
```

**Expected output:**
```
🚀 Starting LLM Multi-Agent Resume Optimizer
📍 Server: http://0.0.0.0:8000
🔧 Debug mode: True
🤖 LLM Provider: gemini
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**Keep this terminal open!**

---

### **Step 6: Test API Endpoints**

**Open a NEW terminal/browser and test:**

#### **Test 1: Health Check**
**Browser:** Open http://localhost:8000

**Expected response:**
```json
{
  "status": "online",
  "service": "LLM Multi-Agent Resume Optimizer",
  "version": "0.1.0"
}
```

---

#### **Test 2: Detailed Health**
**Browser:** Open http://localhost:8000/health

**Expected response:**
```json
{
  "status": "healthy",
  "llm_provider": "gemini",
  "backend": "operational"
}
```

---

#### **Test 3: LLM Connection Test**
**Browser:** Open http://localhost:8000/api/test

**Expected response:**
```json
{
  "status": "success",
  "provider": "gemini",
  "response": "Hello from the LLM!"
}
```

**What this tests:**
- ✅ FastAPI server running
- ✅ CORS configured
- ✅ Gemini integration works
- ✅ API can call LLM successfully

---

### **Step 7: Test with Python Script**

**Create a test file:** `test_llm.py` in backend folder

```python
"""Quick test of LLM adapter"""
from aro.llm_adapter import create_llm_adapter

# Create Gemini adapter
llm = create_llm_adapter("gemini")

# Test 1: Simple generation
print("Test 1: Simple text generation")
response = llm.generate("Write a one-sentence description of Python", max_tokens=100, temperature=0)
print(f"Response: {response}\n")

# Test 2: JSON generation
print("Test 2: JSON generation")
prompt = """Generate a JSON object with these fields:
{
  "name": "Test Project",
  "tech_stack": ["Python", "FastAPI"],
  "description": "A test project"
}"""

json_response = llm.generate_json(prompt, max_tokens=200)
print(f"JSON Response: {json_response}\n")

print("✅ All tests passed!")
```

**Run it:**
```bash
python test_llm.py
```

**Expected output:**
```
Test 1: Simple text generation
Response: Python is a high-level, interpreted programming language known for its simplicity and readability.

Test 2: JSON generation
JSON Response: {'name': 'Test Project', 'tech_stack': ['Python', 'FastAPI'], 'description': 'A test project'}

✅ All tests passed!
```

---

## 🔧 WHAT YOU CAN TEST RIGHT NOW

### **Available Components:**

1. **✅ LLM Adapter**
   - Test file: `aro/llm_adapter.py`
   - Can call Gemini for text generation
   - Can call Gemini for JSON generation
   - Has mock mode for free testing

2. **✅ Prompts**
   - File: `aro/prompts.py`
   - Generator prompts defined
   - Evaluator prompts defined
   - Reviser prompts defined

3. **✅ FastAPI Server**
   - File: `main.py`, `api/routes.py`
   - Server boots and runs
   - Basic endpoints work
   - Health checks functional

---

## 🚫 WHAT DOESN'T WORK YET

**Not implemented:**
- ❌ `/api/generate` - Returns mock data (agent not built)
- ❌ `/api/evaluate` - Returns mock data (agent not built)
- ❌ Renderer - Can't create DOCX yet
- ❌ Iteration loop - No optimization yet

---

## 🎯 NEXT TESTING MILESTONE

**After we build Generator Agent:**

You'll be able to test:
```bash
# Call the generation endpoint
curl -X POST http://localhost:8000/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "jd_text": "Software Engineer role requiring Python...",
    "profile_data": {"education": "MS CS"}
  }'
```

And get back a complete resume JSON!

---

## 📋 TESTING CHECKLIST

Run through these tests to verify everything works:

### **Setup Tests:**
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip list` shows all packages)
- [ ] `.env` file created with GEMINI_API_KEY
- [ ] Can activate venv without errors

### **LLM Adapter Tests:**
- [ ] `python aro/llm_adapter.py` runs successfully
- [ ] Mock adapter works
- [ ] Gemini adapter returns text
- [ ] No API errors

### **FastAPI Server Tests:**
- [ ] `python main.py` starts server
- [ ] http://localhost:8000 returns JSON
- [ ] http://localhost:8000/health shows "gemini" provider
- [ ] http://localhost:8000/api/test returns Gemini response
- [ ] No Python errors in terminal

### **Integration Test:**
- [ ] Can call Gemini from Python script
- [ ] Can get JSON response from Gemini
- [ ] Response parsing works correctly

---

## 🐛 TROUBLESHOOTING

### **Issue: "GEMINI_API_KEY not found"**
**Solution:** 
- Check `.env` file exists in `backend/` folder
- Verify API key is correct (no extra spaces)
- Make sure you're running from backend folder

### **Issue: "Module not found: google.generativeai"**
**Solution:**
```bash
pip install google-generativeai
```

### **Issue: "Port 8000 already in use"**
**Solution:**
- Kill other process using port 8000
- Or change PORT in `.env` to 8001

### **Issue: Gemini API error**
**Solution:**
- Verify API key is valid
- Check you have quota remaining
- Try using mock adapter instead: `LLM_PROVIDER=mock`

---

## 📊 TESTING WORKFLOW

**As we build each component, test it immediately:**

```
Build Component → Unit Test → Integration Test → Manual Test → Commit
```

**Example for Generator Agent (next to build):**

1. **Write code:** `aro/agents/generator.py`
2. **Unit test:** Test with mock LLM
3. **Integration test:** Test with real Gemini
4. **Manual test:** Call via API endpoint
5. **Verify:** Check generated JSON structure
6. **Commit:** Save working code

---

## 🎯 READY TO START?

**You can start testing NOW with:**

1. **Setup environment** (5 minutes)
2. **Get Gemini API key** (2 minutes)
3. **Run all tests above** (5 minutes)
4. **Verify everything works** ✓

**Then I'll build the Generator Agent and you can test actual resume generation!**

**Total setup time: ~15 minutes**

---

**Let me know when you've completed the setup and all tests pass!** 🚀
