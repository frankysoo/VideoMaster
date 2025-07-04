#!/usr/bin/env python3
"""
🎬 VideoMaster Platform Setup
============================

Setup script for VideoMaster Platform installation and configuration.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ is required")
        print(f"   Current version: {sys.version}")
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_dependencies():
    """Install required Python dependencies"""
    print("📦 Installing Python dependencies...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def check_ffmpeg():
    """Check if FFmpeg is available"""
    # Check if ffmpeg.exe exists in current directory (Windows)
    if os.path.exists('ffmpeg.exe'):
        print("✅ FFmpeg found in project directory")
        return True
    
    # Check if ffmpeg is in PATH
    if shutil.which('ffmpeg'):
        print("✅ FFmpeg found in system PATH")
        return True
    
    print("⚠️  FFmpeg not found")
    return False

def install_ffmpeg():
    """Install FFmpeg if needed"""
    if check_ffmpeg():
        return True
    
    print("📥 FFmpeg installation required...")
    
    if os.name == 'nt':  # Windows
        print("🪟 For Windows users:")
        print("   Option 1: Run 'choco install ffmpeg' (if you have Chocolatey)")
        print("   Option 2: Download from https://ffmpeg.org/download.html")
        print("   Option 3: The application will guide you through installation")
    elif sys.platform == 'darwin':  # macOS
        print("🍎 For macOS users:")
        print("   Run: brew install ffmpeg")
    else:  # Linux
        print("🐧 For Linux users:")
        print("   Ubuntu/Debian: sudo apt install ffmpeg")
        print("   CentOS/RHEL: sudo yum install ffmpeg")
    
    return False

def verify_installation():
    """Verify that everything is set up correctly"""
    print("\n🔍 Verifying installation...")
    
    # Check main application file
    if not Path("VideoMaster_PERFECT.py").exists():
        print("❌ VideoMaster_PERFECT.py not found")
        return False
    
    # Check dependencies
    try:
        import streamlit
        print("✅ Streamlit available")
    except ImportError:
        print("❌ Streamlit not available")
        return False
    
    # Check FFmpeg
    if not check_ffmpeg():
        print("⚠️  FFmpeg not available (will be handled by the application)")
    
    return True

def main():
    """Main setup function"""
    print("🎬 VideoMaster Platform Setup")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("VideoMaster_PERFECT.py").exists():
        print("❌ VideoMaster_PERFECT.py not found")
        print("   Please run this script from the VideoMaster project directory")
        sys.exit(1)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Check/install FFmpeg
    ffmpeg_available = install_ffmpeg()
    
    # Verify installation
    if not verify_installation():
        print("\n❌ Setup verification failed")
        sys.exit(1)
    
    # Success message
    print("\n🎉 Setup completed successfully!")
    print("\n🚀 To start VideoMaster Platform:")
    print("   python start.py")
    print("   or")
    print("   streamlit run VideoMaster_PERFECT.py --server.port=8500")
    
    if not ffmpeg_available:
        print("\n⚠️  Note: FFmpeg installation may be required")
        print("   The application will guide you through this process")
    
    print("\n🌐 The platform will be available at: http://localhost:8500")

if __name__ == "__main__":
    main()
