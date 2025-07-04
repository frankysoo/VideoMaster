@echo off
REM VideoMaster Pro Installation Script for Windows
REM This script automates the installation process

setlocal enabledelayedexpansion

echo.
echo 🎬 VideoMaster Pro Installation Script
echo ======================================
echo.

REM Check if Python is installed
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org/downloads
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

REM Get Python version
for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [SUCCESS] Python %PYTHON_VERSION% found

REM Check Python version (basic check)
for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR=%%a
    set MINOR=%%b
)

if %MAJOR% lss 3 (
    echo [ERROR] Python 3.7+ is required. Found: %PYTHON_VERSION%
    pause
    exit /b 1
)

if %MAJOR% equ 3 if %MINOR% lss 7 (
    echo [ERROR] Python 3.7+ is required. Found: %PYTHON_VERSION%
    pause
    exit /b 1
)

echo.

REM Check if we're in the right directory
if not exist "launch.py" (
    echo [ERROR] launch.py not found
    echo Please run this script from the VideoMaster-Pro directory
    pause
    exit /b 1
)

if not exist "video_outro_platform.py" (
    echo [ERROR] video_outro_platform.py not found
    echo Please run this script from the VideoMaster-Pro directory
    pause
    exit /b 1
)

REM Check FFmpeg
echo [INFO] Checking FFmpeg installation...
ffmpeg -version >nul 2>&1
if %errorlevel% equ 0 (
    echo [SUCCESS] FFmpeg is already installed
) else (
    echo [INFO] FFmpeg not found in system PATH
    if exist "ffmpeg-7.1.1-essentials_build\bin\ffmpeg.exe" (
        echo [SUCCESS] Using bundled FFmpeg installation
    ) else (
        echo [WARNING] FFmpeg not found
        echo The platform includes a bundled FFmpeg installation
        echo If you encounter issues, download FFmpeg from:
        echo https://www.gyan.dev/ffmpeg/builds/
    )
)

echo.

REM Upgrade pip
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo [WARNING] Failed to upgrade pip, continuing anyway...
)

echo.

REM Install dependencies
echo [INFO] Installing Python dependencies...
if not exist "requirements.txt" (
    echo [ERROR] requirements.txt not found
    pause
    exit /b 1
)

python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERROR] Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo [SUCCESS] Dependencies installed successfully

echo.

REM Create desktop shortcut
echo [INFO] Creating desktop shortcut...
set DESKTOP=%USERPROFILE%\Desktop
set CURRENT_DIR=%CD%
set SHORTCUT_PATH=%DESKTOP%\VideoMaster Pro.lnk

REM Create a simple batch file to launch the application
echo @echo off > "%DESKTOP%\VideoMaster Pro.bat"
echo cd /d "%CURRENT_DIR%" >> "%DESKTOP%\VideoMaster Pro.bat"
echo python launch.py >> "%DESKTOP%\VideoMaster Pro.bat"

if exist "%DESKTOP%\VideoMaster Pro.bat" (
    echo [SUCCESS] Desktop shortcut created
) else (
    echo [WARNING] Could not create desktop shortcut
)

echo.

REM Installation complete
echo [SUCCESS] Installation completed successfully!
echo.
echo 🚀 To start VideoMaster Pro:
echo    1. Double-click "VideoMaster Pro.bat" on your desktop
echo    2. Or run: python launch.py
echo.
echo 📚 For help and documentation:
echo    - README.md - Project overview
echo    - SETUP_GUIDE.md - Detailed setup instructions
echo    - examples\ - Sample videos for testing
echo.
echo 🎬 Happy video processing!
echo.

pause
