#!/usr/bin/env python3
"""
VideoMaster Pro - Professional Platform Launcher
Automatically sets up and launches the video outro platform
"""

import sys
import subprocess
import os
import webbrowser
import time
import platform

def print_banner():
    """Display welcome banner"""
    print("=" * 60)
    print("🎬 VideoMaster Pro - Professional Video Platform")
    print("=" * 60)
    print("🚀 Launching your professional video processing platform...")
    print()

def check_python():
    """Check Python version"""
    print("🔍 Checking Python version...")
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required")
        print(f"   Current version: {sys.version}")
        print("   Please upgrade Python and try again")
        return False
    print(f"✅ Python {sys.version.split()[0]} - OK")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Checking dependencies...")
    
    try:
        import streamlit
        print(f"✅ Streamlit {streamlit.__version__} - Already installed")
        return True
    except ImportError:
        print("📥 Installing Streamlit...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("✅ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies")
            print("   Try running: pip install -r requirements.txt")
            return False

def check_ffmpeg():
    """Check FFmpeg availability"""
    print("🎬 Checking FFmpeg...")
    
    # Check common FFmpeg locations
    ffmpeg_paths = [
        'ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe',
        'ffmpeg.exe',
        'ffmpeg'
    ]
    
    for path in ffmpeg_paths:
        if os.path.exists(path):
            print(f"✅ FFmpeg found at: {path}")
            return True
    
    # Check system PATH
    try:
        result = subprocess.run(['ffmpeg', '-version'], 
                              capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            print("✅ FFmpeg found in system PATH")
            return True
    except:
        pass
    
    print("⚠️  FFmpeg not found")
    print("   The platform will still work, but video processing requires FFmpeg")
    print("   Download from: https://ffmpeg.org/download.html")
    return False

def launch_platform():
    """Launch the Streamlit platform"""
    print("🌐 Starting VideoMaster Pro platform...")
    
    try:
        # Find available port
        port = 8501
        for p in range(8501, 8510):
            try:
                import socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex(('localhost', p))
                sock.close()
                if result != 0:  # Port is available
                    port = p
                    break
            except:
                continue
        
        print(f"🚀 Launching on port {port}...")
        
        # Launch Streamlit
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", 
            "video_outro_platform.py",
            "--server.port", str(port),
            "--server.headless", "false",
            "--theme.base", "light",
            "--theme.primaryColor", "#4f46e5"
        ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Wait for server to start
        print("⏳ Starting server...")
        time.sleep(4)
        
        # Open browser
        url = f"http://localhost:{port}"
        print(f"🌐 Opening browser: {url}")
        webbrowser.open(url)
        
        print()
        print("✨ VideoMaster Pro is now running!")
        print("📱 Platform Features:")
        print("   • Smart AI resolution matching")
        print("   • Batch video processing") 
        print("   • Professional quality output")
        print("   • Secure file handling")
        print()
        print("⌨️  Press Ctrl+C to stop the server")
        print("=" * 60)
        
        # Wait for process
        try:
            process.wait()
        except KeyboardInterrupt:
            print("\n👋 VideoMaster Pro stopped by user")
            process.terminate()
            
    except Exception as e:
        print(f"❌ Error launching platform: {e}")
        print("   Try running manually: streamlit run video_outro_platform.py")

def main():
    """Main launcher function"""
    print_banner()
    
    # Check system requirements
    if not check_python():
        input("Press Enter to exit...")
        return
    
    if not install_dependencies():
        input("Press Enter to exit...")
        return
    
    check_ffmpeg()
    
    print()
    print("🎯 All checks complete! Launching platform...")
    print()
    
    launch_platform()

if __name__ == "__main__":
    main()
