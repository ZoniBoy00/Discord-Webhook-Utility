@echo off
title Discord Webhook Utility Installer

:: Check if Python is installed
echo Checking for Python installation...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and ensure it is added to your PATH.
    echo Visit https://www.python.org/downloads/ to download Python.
    pause
    exit /b
)

:: Check if pip is installed
echo Checking for pip installation...
pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip is not installed. Please install pip before proceeding.
    echo Pip is typically installed alongside Python. Refer to https://pip.pypa.io/en/stable/installation/ for help.
    pause
    exit /b
)

:: Install required Python libraries
echo Installing required Python libraries from requirements.txt...
pip install -r requirements.txt

:: Check if the installation succeeded
if %errorlevel% neq 0 (
    echo An error occurred during installation. Please check the error messages and try again.
    echo Ensure you have a stable internet connection and necessary permissions.
    pause
    exit /b
)

echo Installation complete! You can now start the application using the start.bat file.
pause
exit /b
