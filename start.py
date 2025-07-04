#!/usr/bin/env python3
"""
🎬 VideoMaster PERFECT - Simple Startup Script
==============================================

Cross-platform startup script for VideoMaster PERFECT Platform.
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """Check if required dependencies are installed"""
    try:
        import streamlit
        print("✅ Streamlit is available")
        return True
    except ImportError:
        print("❌ Streamlit not found. Installing dependencies...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            return False

def main():
    """Main startup function"""
    print("🎬 VideoMaster PERFECT Platform")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not Path("VideoMaster_PERFECT.py").exists():
        print("❌ VideoMaster_PERFECT.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Check dependencies
    if not check_dependencies():
        sys.exit(1)
    
    print("🚀 Starting VideoMaster PERFECT Platform...")
    print("🌐 Platform will open at: http://localhost:8500")
    print("💡 Press Ctrl+C to stop the server")
    print()
    
    try:
        # Start Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "VideoMaster_PERFECT.py",
            "--server.port=8500",
            "--browser.gatherUsageStats=false"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Shutting down VideoMaster Platform...")
        print("✅ Thank you for using VideoMaster PERFECT! ✨")
    except Exception as e:
        print(f"❌ Error starting platform: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
