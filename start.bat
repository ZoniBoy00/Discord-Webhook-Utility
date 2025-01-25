@echo off
title Discord Webhook Utility

:: Check if Python is installed
echo Verifying Python installation...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in your PATH. Please install Python and ensure it is added to your PATH.
    echo Visit https://www.python.org/downloads/ to download Python.
    pause
    exit /b
)

:: Check if the Python script exists
if not exist "webhook_utility.py" (
    echo Error: webhook_utility.py file not found in the current directory.
    echo Please ensure the file exists and try again.
    pause
    exit /b
)

:: Start the Python script
echo Starting Discord Webhook Utility...
python webhook_utility.py

:: Check if the Python script ran successfully
if %errorlevel% neq 0 (
    echo An error occurred while running the application.
    echo Please check the Python script for any issues and ensure all dependencies are installed.
    pause
    exit /b
)

echo The application has exited successfully.
pause
exit /b
