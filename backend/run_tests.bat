@echo off
echo ================================
echo LMARO - Test Suite
echo ================================
echo.

echo [1/3] Testing User Data Loader...
python src\user_data.py
if %errorlevel% neq 0 (
    echo FAILED: User data loader
    exit /b 1
)
echo.

echo [2/3] Testing Generator...
python tests\test_generator.py
if %errorlevel% neq 0 (
    echo FAILED: Generator
    exit /b 1
)
echo.

echo [3/3] Testing Evaluator...
python tests\test_evaluator.py
if %errorlevel% neq 0 (
    echo FAILED: Evaluator
    exit /b 1
)
echo.

echo ================================
echo ALL TESTS PASSED
echo ================================
