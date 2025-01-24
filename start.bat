@echo off
title Discord Webhook Utility

:: Ensure Python is installed
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH. Please install Python and ensure 'python' is in your PATH.
    pause
    exit /b
)

:: Start the Python script
echo Starting Discord Webhook Utility...
python webhook_utility.py

:: Handle errors
if %errorlevel% neq 0 (
    echo An error occurred while running the application. Please check the error messages and try again.
    pause
    exit /b
)

pause
exit /b
