@echo off
echo ================================
echo LMARO - Quick Test
echo ================================
echo.

cd backend

echo Testing Generator...
python tests\test_generator.py

if %errorlevel% neq 0 (
    echo.
    echo FAILED - Check error above
    pause
    exit /b 1
)

echo.
echo ================================
echo SUCCESS!
echo ================================
echo.
echo Check: test_generator_output.json
pause
