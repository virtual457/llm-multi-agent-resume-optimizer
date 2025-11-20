@echo off
REM Quick test script for LMARO

echo ========================================
echo LLM MULTI-AGENT RESUME OPTIMIZER
echo Quick Test Script
echo ========================================
echo.

REM Check if venv exists
if not exist ".venv\" (
    echo Creating virtual environment...
    python -m venv .venv
    echo.
)

REM Activate venv
echo Activating virtual environment...
call .venv\Scripts\activate
echo.

REM Check if dependencies installed
echo Checking dependencies...
pip show fastapi >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Test LLM adapter
echo ========================================
echo TEST 1: LLM Adapter
echo ========================================
python aro\llm_adapter.py
echo.

echo ========================================
echo TEST 2: Starting FastAPI Server
echo ========================================
echo.
echo Server will start at http://localhost:8000
echo.
echo Open browser and test:
echo   - http://localhost:8000 (health check)
echo   - http://localhost:8000/health (detailed health)
echo   - http://localhost:8000/api/test (LLM test)
echo.
echo Press Ctrl+C to stop server
echo.

python main.py
