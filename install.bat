@echo off
title Discord Webhook Utility Installer

:: Check if Python is installed
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and make sure 'python' is in your PATH.
    pause
    exit /b
)

:: Check if pip is installed
pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Pip is not installed. Please install pip before proceeding.
    pause
    exit /b
)

:: Install required Python libraries
echo Installing required Python libraries...
pip install -r requirements.txt

:: Verify that the installation was successful
if %errorlevel% neq 0 (
    echo An error occurred during installation. Please check the error messages and try again.
    pause
    exit /b
)

echo Installation complete! You can now start the application with the start.bat file.
pause
exit /b
