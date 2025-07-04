#!/bin/bash

# VideoMaster Pro Installation Script for Linux/macOS
# This script automates the installation process

set -e  # Exit on any error

echo "🎬 VideoMaster Pro Installation Script"
echo "======================================"
echo ""

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if Python is installed
check_python() {
    print_status "Checking Python installation..."
    
    if command -v python3 &> /dev/null; then
        PYTHON_CMD="python3"
    elif command -v python &> /dev/null; then
        PYTHON_CMD="python"
    else
        print_error "Python is not installed. Please install Python 3.7+ first."
        echo "Visit: https://python.org/downloads"
        exit 1
    fi
    
    # Check Python version
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2)
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d'.' -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d'.' -f2)
    
    if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
        print_error "Python 3.7+ is required. Found: $PYTHON_VERSION"
        exit 1
    fi
    
    print_success "Python $PYTHON_VERSION found"
}

# Install FFmpeg
install_ffmpeg() {
    print_status "Checking FFmpeg installation..."
    
    if command -v ffmpeg &> /dev/null; then
        print_success "FFmpeg is already installed"
        return
    fi
    
    print_warning "FFmpeg not found. Attempting to install..."
    
    # Detect OS and install FFmpeg
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        if command -v apt-get &> /dev/null; then
            print_status "Installing FFmpeg using apt-get..."
            sudo apt-get update
            sudo apt-get install -y ffmpeg
        elif command -v yum &> /dev/null; then
            print_status "Installing FFmpeg using yum..."
            sudo yum install -y epel-release
            sudo yum install -y ffmpeg
        elif command -v dnf &> /dev/null; then
            print_status "Installing FFmpeg using dnf..."
            sudo dnf install -y ffmpeg
        elif command -v pacman &> /dev/null; then
            print_status "Installing FFmpeg using pacman..."
            sudo pacman -S ffmpeg
        else
            print_warning "Could not detect package manager. Please install FFmpeg manually."
            print_status "Visit: https://ffmpeg.org/download.html"
        fi
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        if command -v brew &> /dev/null; then
            print_status "Installing FFmpeg using Homebrew..."
            brew install ffmpeg
        else
            print_warning "Homebrew not found. Please install FFmpeg manually."
            print_status "Install Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
            print_status "Then run: brew install ffmpeg"
        fi
    else
        print_warning "Unsupported OS. Please install FFmpeg manually."
        print_status "Visit: https://ffmpeg.org/download.html"
    fi
    
    # Verify installation
    if command -v ffmpeg &> /dev/null; then
        print_success "FFmpeg installed successfully"
    else
        print_warning "FFmpeg installation may have failed. The bundled version will be used."
    fi
}

# Install Python dependencies
install_dependencies() {
    print_status "Installing Python dependencies..."
    
    # Upgrade pip first
    $PYTHON_CMD -m pip install --upgrade pip
    
    # Install requirements
    if [ -f "requirements.txt" ]; then
        $PYTHON_CMD -m pip install -r requirements.txt
        print_success "Dependencies installed successfully"
    else
        print_error "requirements.txt not found"
        exit 1
    fi
}

# Create desktop shortcut (Linux only)
create_shortcut() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        print_status "Creating desktop shortcut..."
        
        DESKTOP_FILE="$HOME/Desktop/VideoMaster-Pro.desktop"
        CURRENT_DIR=$(pwd)
        
        cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=VideoMaster Pro
Comment=Professional Video Outro Platform
Exec=$PYTHON_CMD $CURRENT_DIR/launch.py
Icon=$CURRENT_DIR/icon.png
Terminal=false
Categories=AudioVideo;Video;
EOF
        
        chmod +x "$DESKTOP_FILE"
        print_success "Desktop shortcut created"
    fi
}

# Main installation process
main() {
    echo "Starting VideoMaster Pro installation..."
    echo ""
    
    # Check if we're in the right directory
    if [ ! -f "launch.py" ] || [ ! -f "video_outro_platform.py" ]; then
        print_error "Please run this script from the VideoMaster-Pro directory"
        exit 1
    fi
    
    # Run installation steps
    check_python
    echo ""
    
    install_ffmpeg
    echo ""
    
    install_dependencies
    echo ""
    
    create_shortcut
    echo ""
    
    print_success "Installation completed successfully!"
    echo ""
    echo "🚀 To start VideoMaster Pro, run:"
    echo "   $PYTHON_CMD launch.py"
    echo ""
    echo "📚 For help and documentation:"
    echo "   - README.md - Project overview"
    echo "   - SETUP_GUIDE.md - Detailed setup instructions"
    echo "   - examples/ - Sample videos for testing"
    echo ""
    echo "🎬 Happy video processing!"
}

# Run main function
main
