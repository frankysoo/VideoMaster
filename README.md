# 🎬 VideoMaster Platform

A powerful web-based platform for automatically adding outro videos to multiple input videos while preserving their original resolution and quality. Perfect for content creators, marketers, and video professionals who need to process multiple videos efficiently.

![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-latest-red.svg)
![FFmpeg](https://img.shields.io/badge/ffmpeg-included-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)
![GitHub stars](https://img.shields.io/github/stars/frankysoo/VideoMaster?style=social)
![GitHub forks](https://img.shields.io/github/forks/frankysoo/VideoMaster?style=social)

## ✨ Features

- **🎯 Perfect Quality Preservation**: Maintains original resolution and quality for both input and outro videos
- **📦 Batch Processing**: Process multiple videos simultaneously with real-time progress tracking
- **🔄 Universal Resolution Support**: Automatically handles any video resolution (720x1280, 1920x1080, 360x640, etc.)
- **⚡ Professional-Grade Processing**: Powered by FFmpeg with optimized encoding settings
- **🌐 Modern Web Interface**: Intuitive drag-and-drop interface with dark/light theme support
- **📦 One-Click Bulk Download**: Download all processed videos in a single ZIP file with one click ⭐ **NEW!**
- **🎨 Beautiful UI**: Responsive design with smooth animations and professional styling
- **💾 Smart File Management**: Automatic cleanup and organized output with professional naming
- **🔧 Configurable Settings**: Multiple quality presets and processing speed options
- **📱 Cross-Platform**: Works on Windows, macOS, and Linux

## 🎉 What's New in Latest Version

### 📦 One-Click Bulk Download Feature
- **🚀 Download All Videos**: Get all processed videos in a single ZIP file
- **⚡ One-Click Convenience**: No need to download videos individually
- **📁 Smart Organization**: Automatically organized ZIP files with descriptive names
- **💾 Memory Efficient**: Creates ZIP files in memory without temporary disk usage
- **📊 Size Information**: Shows total file count and combined size
- **🎯 Perfect for Batch Processing**: Ideal for content creators processing multiple videos

## 🚀 Quick Start

### Prerequisites

1. **Python 3.7+** installed on your system
2. **FFmpeg** installed and accessible (included for Windows users)
3. **Modern web browser** (Chrome, Firefox, Safari, Edge)

### Installation

#### 🚀 Quick Setup (Recommended)
```bash
git clone https://github.com/frankysoo/VideoMaster.git
cd VideoMaster
python setup.py
```

#### 📋 Manual Installation

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/frankysoo/VideoMaster.git
   cd VideoMaster
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg** (Required for video processing)

   **Windows:**
   ```bash
   # Option 1: Using Chocolatey (Recommended)
   choco install ffmpeg

   # Option 2: Manual installation
   # 1. Download from https://ffmpeg.org/download.html
   # 2. Extract to C:\ffmpeg
   # 3. Add C:\ffmpeg\bin to your PATH environment variable
   ```

   **macOS:**
   ```bash
   # Using Homebrew (Recommended)
   brew install ffmpeg
   ```

   **Linux (Ubuntu/Debian):**
   ```bash
   sudo apt update
   sudo apt install ffmpeg
   ```

   **Linux (CentOS/RHEL):**
   ```bash
   sudo yum install ffmpeg
   ```

   **Verify Installation:**
   ```bash
   ffmpeg -version
   ```

4. **Run the platform**

   **Option 1: Using Python script (Cross-platform)**
   ```bash
   python start.py
   ```

   **Option 2: Direct Streamlit command**
   ```bash
   streamlit run VideoMaster_PERFECT.py --server.port=8500
   ```

   **Option 3: Windows batch file**
   ```bash
   START_PERFECT_PLATFORM.bat
   ```

5. **Open your browser** to `http://localhost:8500`

## 📁 Project Structure

```
VideoMaster/
├── VideoMaster_PERFECT.py         # Main application file
├── start.py                      # Cross-platform startup script
├── setup.py                      # Setup and installation script
├── requirements.txt               # Python dependencies
├── README.md                     # This file
├── CHANGELOG.md                  # Version history and changes
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore rules
├── START_PERFECT_PLATFORM.bat   # Windows batch file to start
├── CONTRIBUTING.md               # Contribution guidelines
├── ROADMAP.md                    # Development roadmap
└── .github/                      # GitHub templates and workflows
    ├── workflows/
    │   └── ci.yml               # CI/CD pipeline
    └── ISSUE_TEMPLATE/
        ├── bug_report.md        # Bug report template
        └── feature_request.md   # Feature request template
```

## 🎯 How to Use

1. **Prepare Your Outro**: Create or obtain an outro video in MP4 format
2. **Upload Videos**: Drag and drop your input videos (MP4, MOV, AVI, MKV)
3. **Upload Outro**: Add your outro video that will be appended to each input
4. **Configure Settings**: Choose quality and processing speed
5. **Process**: Click "Process Videos" and watch the real-time progress
6. **Download**: Get all processed videos as a ZIP file

> **Note**: You'll need to provide your own outro video. The platform will automatically scale it to match each input video's resolution while preserving quality.

## 🔧 Technical Details

### Supported Formats
- **Input**: MP4, MOV, AVI, MKV
- **Output**: MP4 (H.264 video, AAC audio)

### Processing Method
- **Zero Quality Loss**: Uses FFmpeg's `-c copy` for perfect preservation
- **Smart Concatenation**: Maintains exact original quality for both videos
- **No Re-encoding**: Direct copy preserves perfect video and audio quality
- **Flexible Output**: Configurable quality settings when re-encoding is needed

### Resolution Handling
- **720x1280 videos** → Outro scaled to 720x1280
- **360x640 videos** → Outro scaled to 360x640
- **Any resolution** → Outro automatically scaled to match

## 🌟 Advanced Features

### Quality Presets
- **High (CRF 18)**: Best quality, larger file size
- **Medium (CRF 23)**: Balanced quality and size (recommended)
- **Fast (CRF 28)**: Smaller files, faster processing

### Processing Speed
- **Fast**: Quick processing, good for testing
- **Medium**: Balanced speed and quality
- **Slow**: Best quality, takes longer

## 🚀 Deployment Options

### Local Development
```bash
streamlit run VideoMaster_PERFECT.py
```

### Production Deployment

**Streamlit Cloud:**
1. Push code to GitHub
2. Connect to Streamlit Cloud
3. Deploy automatically

**Heroku/Railway/Render:**
- Add `ffmpeg` buildpack
- Deploy with requirements.txt

## 🛠️ Customization

### Adding New Features
The platform is built with modular functions:
- `process_video_with_outro()`: Core processing logic
- `get_video_resolution()`: Resolution detection
- `check_ffmpeg()`: FFmpeg availability check

### Styling
Modify the CSS in the `st.markdown()` sections to customize the appearance.

### Processing Options
Add new quality presets or processing options by modifying the selectbox options and corresponding FFmpeg parameters.

## 📊 Performance

- **Processing Speed**: Optimized for speed with zero quality loss
- **Memory Usage**: Minimal footprint with efficient streaming processing
- **Concurrent Users**: Multi-user support with isolated processing environments
- **File Size Limits**: Handles large files efficiently (depends on available disk space)
- **Scalability**: Docker-ready for easy horizontal scaling

## 🔒 Security

- **Temporary Files**: All uploads are stored in temporary directories and automatically cleaned up
- **No Permanent Storage**: Files are not permanently stored on the server
- **Isolated Processing**: Each user session is isolated

## 🐛 Troubleshooting

### Common Issues

**FFmpeg not found:**
- Ensure FFmpeg is installed and in PATH
- On Windows, place ffmpeg.exe in the project directory

**Processing fails:**
- Check video file integrity
- Ensure sufficient disk space
- Try different quality/speed settings

**Slow processing:**
- Use "Fast" speed preset for testing
- Consider video resolution and length
- Check system resources

## 🗺️ Roadmap

We're actively developing VideoMaster Platform into a comprehensive SaaS solution. See our [ROADMAP.md](ROADMAP.md) for detailed upcoming features including:

- 🔐 User Authentication & Subscription System
- ☁️ Cloud Storage Integration
- 📊 Advanced Analytics Dashboard
- 🤖 AI-Powered Video Enhancements
- 📱 Mobile Application

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **🍴 Fork the repository** on GitHub
2. **🌿 Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **💻 Make your changes** and test thoroughly
4. **📝 Commit your changes**: `git commit -m 'Add amazing feature'`
5. **🚀 Push to the branch**: `git push origin feature/amazing-feature`
6. **🔄 Submit a pull request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### 🐛 Found a Bug?
- Open an issue on [GitHub Issues](https://github.com/frankysoo/VideoMaster/issues)
- Include steps to reproduce, expected behavior, and screenshots if applicable

### 💡 Have an Idea?
- Check existing [GitHub Issues](https://github.com/frankysoo/VideoMaster/issues) first
- Open a new issue with the "enhancement" label

## 📄 License

This project is open source. Feel free to use, modify, and distribute.

## 🙏 Acknowledgments

- **FFmpeg**: For powerful video processing capabilities
- **Streamlit**: For the amazing web framework
- **Community**: For feedback and contributions

## 🔗 Links

- **🏠 Repository**: [https://github.com/frankysoo/VideoMaster](https://github.com/frankysoo/VideoMaster)
- **🐛 Issues**: [Report bugs or request features](https://github.com/frankysoo/VideoMaster/issues)
- **📖 Wiki**: [Documentation and guides](https://github.com/frankysoo/VideoMaster/wiki)
- **💬 Discussions**: [Community discussions](https://github.com/frankysoo/VideoMaster/discussions)

## ⭐ Show Your Support

If this project helped you, please consider:
- ⭐ **Starring the repository** on GitHub
- 🍴 **Forking** to contribute
- 📢 **Sharing** with others who might find it useful
- 💝 **Sponsoring** the development

---

**Made with ❤️ for content creators who need professional video processing tools**

[![GitHub stars](https://img.shields.io/github/stars/frankysoo/VideoMaster?style=social)](https://github.com/frankysoo/VideoMaster/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/frankysoo/VideoMaster?style=social)](https://github.com/frankysoo/VideoMaster/network/members)
