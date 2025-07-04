# 🎬 FFmpeg Setup for VideoMaster Pro

## What is FFmpeg?
FFmpeg is a powerful, open-source multimedia framework that can decode, encode, transcode, mux, demux, stream, filter, and play almost any video or audio format. VideoMaster Pro uses FFmpeg as its core video processing engine.

## Installation Options

### 🪟 Windows Installation

#### Option 1: Portable Installation (Recommended)
1. **Download FFmpeg Essentials Build:**
   - Go to: https://www.gyan.dev/ffmpeg/builds/
   - Download: `ffmpeg-release-essentials.zip`
   - Extract to your VideoMaster Pro folder
   - Rename folder to: `ffmpeg-7.1.1-essentials_build`

2. **Verify Installation:**
   - The platform will automatically detect FFmpeg
   - You should see "FFmpeg Engine Ready" in the platform

#### Option 2: System Installation
1. **Download Full Build:**
   - Go to: https://ffmpeg.org/download.html#build-windows
   - Download the latest release
   - Extract to `C:\ffmpeg\`

2. **Add to PATH:**
   - Open System Properties → Advanced → Environment Variables
   - Add `C:\ffmpeg\bin` to your PATH variable
   - Restart command prompt

### 🍎 macOS Installation

#### Using Homebrew (Easiest):
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg
brew install ffmpeg
```

#### Manual Installation:
1. **Download:**
   - Go to: https://evermeet.cx/ffmpeg/
   - Download the latest FFmpeg build
   - Extract the binary

2. **Install:**
   ```bash
   # Move to system directory
   sudo mv ffmpeg /usr/local/bin/
   
   # Make executable
   sudo chmod +x /usr/local/bin/ffmpeg
   ```

### 🐧 Linux Installation

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

#### CentOS/RHEL/Fedora:
```bash
# CentOS/RHEL
sudo yum install epel-release
sudo yum install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

#### Arch Linux:
```bash
sudo pacman -S ffmpeg
```

## Verification

### Test FFmpeg Installation:
```bash
ffmpeg -version
```

You should see output similar to:
```
ffmpeg version 4.4.2 Copyright (c) 2000-2021 the FFmpeg developers
built with gcc 9 (Ubuntu 9.4.0-1ubuntu1~20.04.1)
configuration: --prefix=/usr --extra-version=0ubuntu0.20.04.1 ...
```

### Test in VideoMaster Pro:
1. Launch the platform: `python launch.py`
2. Check the "System Status" section
3. Look for "✅ FFmpeg Engine Ready"

## Troubleshooting

### Common Issues:

**"FFmpeg not found" on Windows:**
- Ensure FFmpeg is in the project folder as `ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe`
- Or add FFmpeg to your system PATH
- Restart command prompt after PATH changes

**"Permission denied" on macOS/Linux:**
- Use `sudo` when moving files to system directories
- Ensure execute permissions: `chmod +x /path/to/ffmpeg`

**"Command not found" after installation:**
- Restart your terminal/command prompt
- Check PATH variable includes FFmpeg location
- Try absolute path to FFmpeg binary

### Advanced Configuration:

**Custom FFmpeg Location:**
If you have FFmpeg installed in a custom location, the platform will check these paths in order:
1. `ffmpeg-7.1.1-essentials_build/bin/ffmpeg.exe` (Windows)
2. `ffmpeg.exe` (Windows, current directory)
3. `ffmpeg` (System PATH)
4. `/usr/bin/ffmpeg` (Linux/macOS)
5. `/usr/local/bin/ffmpeg` (macOS)

**Performance Optimization:**
- FFmpeg will automatically use available CPU cores
- For faster processing, ensure sufficient RAM (8GB+ recommended)
- SSD storage significantly improves processing speed

## FFmpeg Features Used by VideoMaster Pro

### Video Processing:
- **Scaling**: Automatic resolution matching between input and outro videos
- **Concatenation**: Seamless joining of input video + outro
- **Encoding**: H.264 video compression with AAC audio
- **Quality Control**: CRF-based quality settings (18-28 range)

### Supported Formats:
- **Input**: MP4, MOV, AVI, MKV, and more
- **Output**: MP4 with H.264 video and AAC audio
- **Codecs**: Automatic codec detection and conversion

### Quality Presets:
- **High Quality**: CRF 18 (larger files, best quality)
- **Medium Quality**: CRF 23 (balanced size/quality)
- **Fast Processing**: CRF 28 (smaller files, faster processing)

## Building from Source (Advanced)

If you need to compile FFmpeg from source:

### Prerequisites:
- C compiler (GCC, Clang, or MSVC)
- Make/CMake build system
- Various codec libraries (optional)

### Basic Build:
```bash
# Download source
wget https://ffmpeg.org/releases/ffmpeg-4.4.2.tar.xz
tar -xf ffmpeg-4.4.2.tar.xz
cd ffmpeg-4.4.2

# Configure and build
./configure --prefix=/usr/local
make -j$(nproc)
sudo make install
```

### With Additional Codecs:
```bash
./configure \
  --prefix=/usr/local \
  --enable-libx264 \
  --enable-libx265 \
  --enable-libvpx \
  --enable-libfdk-aac \
  --enable-gpl \
  --enable-nonfree
```

## License Information

FFmpeg is licensed under the LGPL or GPL depending on configuration:
- **LGPL**: Basic functionality, suitable for commercial use
- **GPL**: With additional codecs, requires GPL compliance

VideoMaster Pro uses FFmpeg in a way that's compatible with both licenses.

## Performance Tips

### For Best Performance:
1. **Use SSD storage** for input/output files
2. **Ensure sufficient RAM** (8GB+ recommended)
3. **Close unnecessary applications** during processing
4. **Use appropriate quality settings** for your needs
5. **Process in batches** rather than all at once

### Hardware Acceleration:
FFmpeg supports hardware acceleration on supported systems:
- **NVIDIA**: NVENC/NVDEC
- **Intel**: Quick Sync Video
- **AMD**: VCE/VCN

Note: VideoMaster Pro uses software encoding for maximum compatibility.

---

**Need Help?** Check the main SETUP_GUIDE.md for additional troubleshooting steps.
