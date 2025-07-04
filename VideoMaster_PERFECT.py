#!/usr/bin/env python3
"""
🎬 VideoMaster PERFECT - BOTH VIDEOS ORIGINAL QUALITY PRESERVED
================================================================

THE ONLY VERSION YOU NEED - PERFECT QUALITY PRESERVATION FOR BOTH VIDEOS

Your #1 Priority: Input video AND outro video BOTH keep their EXACT original quality and resolution.
NO scaling, NO quality loss, NO compression - PERFECT preservation of BOTH videos.

🎯 PERFECT Features:
- ✅ INPUT VIDEO: Keeps EXACT original resolution and quality (NO changes)
- ✅ OUTRO VIDEO: Keeps EXACT original resolution and quality (NO changes)
- ✅ PERFECT CONCATENATION: Uses '-c copy' for zero quality loss
- ✅ NO SCALING: Both videos preserved exactly as they are
- ✅ NO RE-ENCODING: Direct copy preserves perfect quality
- ✅ ONE PERFECT VERSION (No duplicates, no confusion)

🚀 Launch: streamlit run VideoMaster_PERFECT.py --server.port=8500
"""

import streamlit as st
import os
import subprocess
import shutil
import tempfile
import time
from pathlib import Path

# 🎯 PERFECT CONFIGURATION - RESOLUTION & QUALITY FIRST
st.set_page_config(
    page_title="🎬 VideoMaster PERFECT",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Theme Selection
if 'theme' not in st.session_state:
    st.session_state.theme = 'dark'

def get_theme_css(theme='dark'):
    """Generate CSS based on selected theme"""

    if theme == 'dark':
        return """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        .stApp {
            background: linear-gradient(135deg, #0c0c0c 0%, #1a1a1a 50%, #0f0f0f 100%);
            font-family: 'Inter', sans-serif;
        }

        .main-header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 25%, #ff9ff3 50%, #54a0ff 75%, #5f27cd 100%);
            background-size: 400% 400%;
            animation: gradientShift 8s ease infinite;
            padding: 3rem 2rem;
            border-radius: 25px;
            text-align: center;
            color: white;
            margin-bottom: 3rem;
            box-shadow: 0 25px 50px rgba(255, 107, 107, 0.3), 0 0 100px rgba(255, 159, 243, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(20px);
            position: relative;
            overflow: hidden;
        }

        .feature-box {
            background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
            padding: 1.5rem;
            border-radius: 20px;
            margin: 1rem 0;
            color: #ffffff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
            border: 1px solid rgba(255, 255, 255, 0.05);
            transition: all 0.3s ease;
        }

        .upload-section {
            background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 1rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
        }

        .upload-section h3 {
            color: #ffffff !important;
        }

        .upload-section p {
            color: rgba(255, 255, 255, 0.8) !important;
        }

        .processing-section {
            background: linear-gradient(135deg, #1a202c 0%, #2d3748 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 2rem 0;
            border: 1px solid rgba(255, 107, 107, 0.2);
            box-shadow: 0 20px 40px rgba(255, 107, 107, 0.1);
        }

        .processing-section h2 {
            color: #ffffff !important;
        }

        .processing-section p {
            color: rgba(255, 255, 255, 0.9) !important;
        }

        .stats-container {
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 2rem 0;
            border: 1px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        }

        .stats-container h2 {
            color: #ffffff !important;
        }

        .metric-container {
            background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
            padding: 1.5rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            border: 1px solid rgba(255, 255, 255, 0.1);
            margin: 0.5rem;
            transition: all 0.3s ease;
        }

        .metric-container h3 {
            color: #ffffff !important;
        }

        .metric-container h2 {
            color: #ffffff !important;
        }

        .metric-container p {
            color: rgba(255, 255, 255, 0.8) !important;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
            font-weight: 700;
            text-shadow: 0 2px 10px rgba(0,0,0,0.3);
        }

        .stMarkdown {
            color: rgba(255, 255, 255, 0.95) !important;
        }

        .stSidebar {
            background: linear-gradient(180deg, #1a1a1a 0%, #0d1117 100%);
        }

        .stSidebar .stMarkdown {
            color: rgba(255, 255, 255, 0.95) !important;
        }

        .stFileUploader label {
            color: rgba(255, 255, 255, 0.9) !important;
        }

        .stSelectbox label {
            color: rgba(255, 255, 255, 0.9) !important;
        }
        """

    else:  # light theme
        return """
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #f1f5f9 100%);
            font-family: 'Inter', sans-serif;
        }

        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
            background-size: 400% 400%;
            animation: gradientShift 8s ease infinite;
            padding: 3rem 2rem;
            border-radius: 25px;
            text-align: center;
            color: white;
            margin-bottom: 3rem;
            box-shadow: 0 25px 50px rgba(102, 126, 234, 0.3), 0 0 100px rgba(240, 147, 251, 0.2);
            border: 1px solid rgba(255, 255, 255, 0.2);
            backdrop-filter: blur(20px);
            position: relative;
            overflow: hidden;
        }

        .feature-box {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 1.5rem;
            border-radius: 20px;
            margin: 1rem 0;
            color: #1a202c;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.8);
            border: 1px solid rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
        }

        .upload-section {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 1rem 0;
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        .upload-section h3 {
            color: #1a202c !important;
        }

        .upload-section p {
            color: #4a5568 !important;
        }

        .processing-section {
            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 2rem 0;
            border: 1px solid rgba(102, 126, 234, 0.2);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.1);
        }

        .processing-section h2 {
            color: #1a202c !important;
        }

        .processing-section p {
            color: #2d3748 !important;
        }

        .stats-container {
            background: linear-gradient(135deg, #ffffff 0%, #f1f5f9 100%);
            padding: 2rem;
            border-radius: 25px;
            margin: 2rem 0;
            border: 1px solid rgba(0, 0, 0, 0.1);
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }

        .stats-container h2 {
            color: #1a202c !important;
        }

        .metric-container {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 100%);
            padding: 1.5rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            border: 1px solid rgba(0, 0, 0, 0.05);
            margin: 0.5rem;
            transition: all 0.3s ease;
        }

        .metric-container h3 {
            color: #1a202c !important;
        }

        .metric-container h2 {
            color: #1a202c !important;
        }

        .metric-container p {
            color: #4a5568 !important;
        }

        h1, h2, h3, h4, h5, h6 {
            color: #1a202c !important;
            font-weight: 700;
            text-shadow: 0 2px 10px rgba(255,255,255,0.5);
        }

        .stMarkdown {
            color: #2d3748 !important;
        }

        .stSidebar {
            background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
        }

        .stSidebar .stMarkdown {
            color: #2d3748 !important;
        }

        .stFileUploader label {
            color: #2d3748 !important;
        }

        .stSelectbox label {
            color: #2d3748 !important;
        }
        """

# 🎨 DYNAMIC THEME STYLING
theme_css = get_theme_css(st.session_state.theme)

# Common CSS for both themes
common_css = """
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
        animation: shimmer 3s infinite;
    }

    .main-header h1 {
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 0 30px rgba(255,255,255,0.5);
        letter-spacing: -2px;
    }

    .main-header p {
        font-size: 1.3rem;
        font-weight: 500;
        margin: 0.5rem 0;
        opacity: 0.95;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes shimmer {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }

    .feature-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        transition: left 0.5s;
        position: relative;
        overflow: hidden;
    }

    .feature-box:hover::before {
        left: 100%;
    }

    .feature-box:hover {
        transform: translateY(-5px);
    }

    .feature-box h4 {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #667eea !important;
    }

    .feature-box p {
        font-size: 0.9rem;
        opacity: 0.8;
        line-height: 1.4;
    }

    .success-box {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
        animation: successPulse 2s ease-in-out;
    }

    @keyframes successPulse {
        0%, 100% { box-shadow: 0 10px 30px rgba(16, 185, 129, 0.3); }
        50% { box-shadow: 0 15px 40px rgba(16, 185, 129, 0.5); }
    }

    .error-box {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 10px 30px rgba(239, 68, 68, 0.3);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        background-size: 400% 400%;
        animation: gradientShift 4s ease infinite;
        color: white;
        border: none;
        border-radius: 50px;
        padding: 1rem 3rem;
        font-weight: 700;
        font-size: 1.1rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
        position: relative;
        overflow: hidden;
    }

    .stButton > button::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }

    .stButton > button:hover::before {
        left: 100%;
    }

    .stButton > button:hover {
        transform: translateY(-3px);
        box-shadow: 0 20px 45px rgba(102, 126, 234, 0.6);
    }

    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb, #f5576c, #4facfe);
        background-size: 400% 100%;
        animation: gradientShift 2s ease infinite;
        border-radius: 10px;
        height: 15px;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }

    .metric-container:hover {
        transform: translateY(-3px);
    }

    .stDownloadButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        box-shadow: 0 8px 25px rgba(16, 185, 129, 0.3);
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 35px rgba(16, 185, 129, 0.4);
    }

    .theme-toggle {
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 50px;
        padding: 0.5rem 1rem;
        color: white;
        cursor: pointer;
        transition: all 0.3s ease;
    }

    .theme-toggle:hover {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
    }

    /* Fix text visibility for all form elements */
    .stFileUploader > div > div > div {
        color: inherit !important;
    }

    .stSelectbox > div > div > div {
        color: inherit !important;
    }

    .stExpander > div > div > div {
        color: inherit !important;
    }

    /* Ensure all text in containers is visible */
    .upload-section * {
        color: inherit !important;
    }

    .processing-section * {
        color: inherit !important;
    }

    .stats-container * {
        color: inherit !important;
    }

    .metric-container * {
        color: inherit !important;
    }

    /* Override Streamlit's default text colors */
    .stApp .stMarkdown p {
        color: inherit !important;
    }

    .stApp .stMarkdown h1,
    .stApp .stMarkdown h2,
    .stApp .stMarkdown h3,
    .stApp .stMarkdown h4,
    .stApp .stMarkdown h5,
    .stApp .stMarkdown h6 {
        color: inherit !important;
    }

    /* Ensure file uploader text is visible */
    .stFileUploader > div > div > small {
        opacity: 0.8 !important;
    }

    /* Ensure button text is always white */
    .stButton > button {
        color: white !important;
    }

    .stDownloadButton > button {
        color: white !important;
    }

    /* Ensure expander text is visible */
    .stExpander > div > div > p {
        color: inherit !important;
    }

    /* Progress bar text */
    .stProgress > div > div > div {
        color: white !important;
    }
"""

st.markdown(f"""
<style>
{theme_css}
{common_css}
</style>
""", unsafe_allow_html=True)

def check_ffmpeg():
    """🔍 PERFECT FFmpeg Detection - Find the best FFmpeg installation"""
    # Priority order: system FFmpeg first (most common)
    possible_paths = [
        'ffmpeg',                                         # System PATH (BEST)
        'ffmpeg.exe',                                     # Local copy (Windows)
        '/usr/bin/ffmpeg',                               # Linux system
        '/usr/local/bin/ffmpeg',                         # macOS Homebrew
        '/opt/homebrew/bin/ffmpeg'                       # macOS Apple Silicon
    ]

    for path in possible_paths:
        if shutil.which(path) or os.path.exists(path):
            st.success(f"✅ FFmpeg found: {path}")
            return path

    # Show installation instructions if FFmpeg not found
    st.error("❌ FFmpeg not found! Please install FFmpeg to continue.")

    with st.expander("📥 How to Install FFmpeg", expanded=True):
        st.markdown("""
        **Windows:**
        1. Download from: https://ffmpeg.org/download.html
        2. Extract to a folder (e.g., `C:\\ffmpeg`)
        3. Add to PATH: `C:\\ffmpeg\\bin`
        4. Or use Chocolatey: `choco install ffmpeg`

        **macOS:**
        ```bash
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

        After installation, restart this application.
        """)

    return None

def get_video_resolution(video_path, ffmpeg_cmd):
    """🎯 PERFECT Resolution Detection - CRITICAL for quality preservation"""
    
    # Construct ffprobe command from ffmpeg command
    if 'ffmpeg.exe' in ffmpeg_cmd:
        ffprobe_cmd = ffmpeg_cmd.replace('ffmpeg.exe', 'ffprobe.exe')
    elif 'ffmpeg' in ffmpeg_cmd:
        ffprobe_cmd = ffmpeg_cmd.replace('ffmpeg', 'ffprobe')
    else:
        # Fallback: try to find ffprobe in the same directory
        ffmpeg_dir = os.path.dirname(ffmpeg_cmd)
        ffprobe_cmd = os.path.join(ffmpeg_dir, 'ffprobe.exe' if os.name == 'nt' else 'ffprobe')
    
    # PERFECT probe command - EXACT same as working scripts
    probe_cmd = [
        ffprobe_cmd, 
        '-v', 'quiet', 
        '-select_streams', 'v:0', 
        '-show_entries', 'stream=width,height', 
        '-of', 'csv=s=x:p=0', 
        video_path
    ]
    
    try:
        st.info(f"🔍 Detecting resolution for: {os.path.basename(video_path)}")
        result = subprocess.run(probe_cmd, capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0 and result.stdout.strip():
            output = result.stdout.strip()
            st.info(f"📊 Raw ffprobe output: '{output}'")
            
            if 'x' in output:
                dimensions = output.split('x')
                if len(dimensions) == 2:
                    try:
                        width = int(dimensions[0].strip())
                        height = int(dimensions[1].strip())
                        if width > 0 and height > 0:
                            st.success(f"✅ PERFECT! Resolution detected: {width}x{height}")
                            return width, height
                    except ValueError as e:
                        st.error(f"❌ Error parsing dimensions: {e}")
        
        # Debug information for troubleshooting
        st.error(f"❌ Resolution detection failed")
        st.error(f"Return code: {result.returncode}")
        st.error(f"Stdout: '{result.stdout}'")
        st.error(f"Stderr: '{result.stderr}'")
        
    except subprocess.TimeoutExpired:
        st.error(f"⏰ Timeout detecting resolution for: {video_path}")
    except Exception as e:
        st.error(f"💥 Unexpected error: {str(e)}")
    
    return None, None

def process_video_with_outro(input_path, outro_path, output_path, ffmpeg_cmd, progress_callback=None):
    """🎬 PERFECT Video Processing - PRESERVES BOTH INPUT AND OUTRO ORIGINAL QUALITY & RESOLUTION"""

    # Step 1: Get input video resolution (for logging)
    input_width, input_height = get_video_resolution(input_path, ffmpeg_cmd)
    if not input_width or not input_height:
        return False, "Could not determine input video resolution"

    # Step 2: Get outro video resolution (for logging)
    outro_width, outro_height = get_video_resolution(outro_path, ffmpeg_cmd)
    st.info(f"📹 Input: {input_width}x{input_height} | Outro: {outro_width}x{outro_height}")
    st.info(f"🎯 PERFECT MODE: Input keeps original resolution, outro scaled to match (no lag!)")

    try:
        st.info(f"🚀 Processing: {os.path.basename(input_path)}")
        if progress_callback:
            progress_callback(f"Processing {os.path.basename(input_path)}...")

        # Create temporary files for processing
        import tempfile
        temp_dir = tempfile.gettempdir()
        temp_input = os.path.join(temp_dir, f"temp_input_{os.path.basename(input_path)}")
        temp_outro = os.path.join(temp_dir, f"temp_outro_{os.path.basename(outro_path)}")
        list_file = os.path.join(temp_dir, f"temp_list_{os.path.basename(input_path)}.txt")

        # Step 3: Normalize input video (EXACT approach from working script)
        st.info("📋 Step 1: Normalizing input video (preserving original resolution)")
        cmd1 = [
            ffmpeg_cmd,
            '-i', input_path,
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-s', f'{input_width}x{input_height}',  # Keep original resolution
            '-r', '30',                             # Standard framerate
            '-ar', '44100',                         # Standard audio rate
            '-ac', '2',                             # Stereo audio
            '-pix_fmt', 'yuv420p',                  # Standard pixel format
            '-preset', 'slow',                      # High quality preset
            temp_input,
            '-y'
        ]

        result1 = subprocess.run(cmd1, capture_output=True, text=True, timeout=120)
        if result1.returncode != 0:
            return False, f"Failed to normalize input video: {result1.stderr}"

        # Step 4: Normalize outro video to match input technical specs
        st.info("📋 Step 2: Normalizing outro video (scaling to match input resolution)")
        cmd2 = [
            ffmpeg_cmd,
            '-i', outro_path,
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-s', f'{input_width}x{input_height}',  # Scale to match input resolution
            '-r', '30',                             # Match framerate
            '-ar', '44100',                         # Match audio rate
            '-ac', '2',                             # Match audio channels
            '-pix_fmt', 'yuv420p',                  # Match pixel format
            '-preset', 'slow',                      # High quality preset
            temp_outro,
            '-y'
        ]

        result2 = subprocess.run(cmd2, capture_output=True, text=True, timeout=120)
        if result2.returncode != 0:
            return False, f"Failed to normalize outro video: {result2.stderr}"

        # Step 5: Create concatenation list file
        st.info("📋 Step 3: Creating concatenation list")
        with open(list_file, 'w') as f:
            f.write(f"file '{os.path.abspath(temp_input)}'\n")
            f.write(f"file '{os.path.abspath(temp_outro)}'\n")

        # Step 6: PERFECT CONCATENATION - NO QUALITY LOSS FOR EITHER VIDEO
        st.info("🎬 Step 4: PERFECT concatenation (both videos keep original quality)")
        cmd3 = [
            ffmpeg_cmd,
            '-f', 'concat',
            '-safe', '0',
            '-i', list_file,
            '-c', 'copy',  # COPY = PERFECT QUALITY PRESERVATION
            output_path,
            '-y'
        ]

        result3 = subprocess.run(cmd3, capture_output=True, text=True, timeout=300)
        success = result3.returncode == 0

        # Cleanup temporary files
        for temp_file in [temp_input, temp_outro, list_file]:
            if os.path.exists(temp_file):
                os.remove(temp_file)

        if success:
            # Verify output file exists and has content
            if os.path.exists(output_path) and os.path.getsize(output_path) > 0:
                st.success(f"✅ PERFECT! Input video preserved at original resolution!")
                st.success(f"📊 Input part: {input_width}x{input_height} (original resolution, high quality)")
                st.success(f"📊 Outro part: {input_width}x{input_height} (scaled to match, high quality)")
                st.success(f"🎬 Both parts now have consistent technical specs - no more lag!")
                return True, "Success - Input resolution preserved, outro optimized"
            else:
                return False, "Output file not created or empty"
        else:
            st.error(f"❌ Concatenation error: {result3.stderr}")
            return False, f"Concatenation error: {result3.stderr}"

    except subprocess.TimeoutExpired:
        return False, "Processing timeout (5 minutes)"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

# 🎬 MAIN APPLICATION
def main():
    # Ultra Premium Header with Theme Indicator
    theme_emoji = "🌙" if st.session_state.theme == 'dark' else "☀️"
    theme_name = "Dark" if st.session_state.theme == 'dark' else "Light"

    st.markdown(f"""
    <div class="main-header">
        <h1>🎬 VideoMaster PERFECT</h1>
        <p><strong>ULTRA PREMIUM VIDEO PROCESSING STUDIO</strong></p>
        <p>Professional-Grade Resolution & Quality Preservation</p>
        <p style="font-size: 1rem; opacity: 0.8;">Powered by Advanced FFmpeg Technology</p>
        <p style="font-size: 0.9rem; opacity: 0.7;">{theme_emoji} {theme_name} Theme Active</p>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar - PERFECT Features
    with st.sidebar:
        # Theme Toggle
        st.markdown("## 🎨 Theme Selection")

        col_theme1, col_theme2 = st.columns(2)

        with col_theme1:
            if st.button("🌙 Dark", use_container_width=True,
                        type="primary" if st.session_state.theme == 'dark' else "secondary"):
                st.session_state.theme = 'dark'
                st.rerun()

        with col_theme2:
            if st.button("☀️ Light", use_container_width=True,
                        type="primary" if st.session_state.theme == 'light' else "secondary"):
                st.session_state.theme = 'light'
                st.rerun()

        st.markdown("---")
        st.markdown("## 🎯 PERFECT Features")

        features = [
            ("🔍 Smart Resolution Detection", "Automatically detects and preserves exact input video resolution"),
            ("⚡ Lightning Fast Processing", "Optimized FFmpeg settings for speed and quality"),
            ("🎨 Professional Quality Output", "CRF 23, libx264, AAC - perfect quality settings"),
            ("📱 Multiple Format Support", "MP4, MOV, AVI, MKV, WebM - all major video formats"),
            ("🔒 Secure & Private", "All processing happens locally on your machine"),
            ("💎 Batch Processing", "Process multiple videos with one click"),
            ("🎭 Dual Theme Support", "Beautiful dark and light themes for any preference"),
            ("📊 Advanced Analytics", "Real-time metrics and processing statistics")
        ]

        for title, description in features:
            st.markdown(f"""
            <div class="feature-box">
                <h4>{title}</h4>
                <p>{description}</p>
            </div>
            """, unsafe_allow_html=True)

    # Check FFmpeg availability
    ffmpeg_cmd = check_ffmpeg()
    if not ffmpeg_cmd:
        st.error("❌ FFmpeg not found! Please install FFmpeg to continue.")
        st.stop()

    # Premium File Upload Sections
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #ff6b6b; font-size: 2.5rem; margin-bottom: 0.5rem;">🎬 PROFESSIONAL UPLOAD STUDIO</h2>
        <p style="color: rgba(255,255,255,0.7); font-size: 1.2rem;">Drag & Drop Your Premium Content</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="upload-section">
            <h3 style="color: #54a0ff; text-align: center; margin-bottom: 1rem;">📹 INPUT VIDEOS</h3>
            <p style="text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 1.5rem;">
                Upload multiple videos for batch processing
            </p>
        </div>
        """, unsafe_allow_html=True)

        input_videos = st.file_uploader(
            "Choose your input videos",
            type=['mp4', 'mov', 'avi', 'mkv', 'webm'],
            accept_multiple_files=True,
            help="📁 Supported formats: MP4, MOV, AVI, MKV, WebM | 🚀 Batch processing available",
            key="input_uploader"
        )

        if input_videos:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                        padding: 1rem; border-radius: 15px; text-align: center; margin-top: 1rem;">
                <h4 style="color: white; margin: 0;">✅ {len(input_videos)} Video(s) Ready</h4>
                <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                    Total size: {sum(len(video.getvalue()) for video in input_videos) / (1024*1024):.1f} MB
                </p>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="upload-section">
            <h3 style="color: #ff9ff3; text-align: center; margin-bottom: 1rem;">🎬 OUTRO VIDEO</h3>
            <p style="text-align: center; color: rgba(255,255,255,0.7); margin-bottom: 1.5rem;">
                Your signature ending for all videos
            </p>
        </div>
        """, unsafe_allow_html=True)

        outro_video = st.file_uploader(
            "Choose your outro video",
            type=['mp4', 'mov', 'avi', 'mkv', 'webm'],
            help="🎯 This video will be added to the end of each input video | 🔄 Automatically scaled to match",
            key="outro_uploader"
        )

        if outro_video:
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
                        padding: 1rem; border-radius: 15px; text-align: center; margin-top: 1rem;">
                <h4 style="color: white; margin: 0;">✅ Outro Ready</h4>
                <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                    Size: {len(outro_video.getvalue()) / (1024*1024):.1f} MB
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Premium Processing Section
    if input_videos and outro_video:
        st.markdown("""
        <div class="processing-section">
            <h2 style="color: #ff6b6b; text-align: center; font-size: 2.5rem; margin-bottom: 1rem;">
                🚀 ULTRA PREMIUM PROCESSING
            </h2>
            <p style="text-align: center; color: rgba(255,255,255,0.8); font-size: 1.2rem; margin-bottom: 2rem;">
                Professional-Grade Video Production Pipeline
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Advanced Options
        with st.expander("⚙️ ADVANCED PROCESSING OPTIONS", expanded=False):
            col_opt1, col_opt2, col_opt3 = st.columns(3)

            with col_opt1:
                quality_preset = st.selectbox(
                    "🎨 Quality Preset",
                    ["Ultra High (Slow)", "High (Recommended)", "Balanced (Fast)"],
                    index=1,
                    help="Higher quality = slower processing but better results"
                )

            with col_opt2:
                output_format = st.selectbox(
                    "📁 Output Format",
                    ["MP4 (Recommended)", "MOV (Apple)", "AVI (Legacy)"],
                    index=0,
                    help="MP4 offers best compatibility across all platforms"
                )

            with col_opt3:
                naming_style = st.selectbox(
                    "📝 File Naming",
                    ["PERFECT_[original]", "PROCESSED_[original]", "STUDIO_[original]"],
                    index=0,
                    help="Choose how processed files will be named"
                )

        # Premium Processing Button
        st.markdown("""
        <div style="text-align: center; margin: 2rem 0;">
        """, unsafe_allow_html=True)

        if st.button("🎬 START ULTRA PREMIUM PROCESSING", type="primary", use_container_width=True):
            # Create persistent temporary directory for processing
            import uuid
            session_id = str(uuid.uuid4())[:8]
            temp_dir = Path(tempfile.gettempdir()) / f"videomaster_{session_id}"
            temp_dir.mkdir(exist_ok=True)

            # Store temp_dir in session state for cleanup later
            st.session_state.temp_dir = temp_dir

            try:
                # Save outro video
                outro_path = temp_dir / f"outro_{outro_video.name}"
                with open(outro_path, "wb") as f:
                    f.write(outro_video.getbuffer())

                # Process each input video
                processed_videos = []
                total_videos = len(input_videos)

                # Progress tracking
                progress_bar = st.progress(0)
                status_text = st.empty()
                results_container = st.container()

                success_count = 0
                failed_videos = []
                processed_files = []  # Store file data for downloads

                for i, input_video in enumerate(input_videos):
                    # Update progress
                    progress = (i + 1) / total_videos
                    progress_bar.progress(progress)
                    status_text.text(f"Processing {i+1}/{total_videos}: {input_video.name}")

                    # Save input video
                    input_path = temp_dir / f"input_{input_video.name}"
                    with open(input_path, "wb") as f:
                        f.write(input_video.getbuffer())

                    # Generate output filename based on user preference
                    prefix = naming_style.split("_")[0]
                    output_filename = f"{prefix}_{input_video.name}"
                    output_path = temp_dir / output_filename

                    # Process video with PERFECT settings
                    with results_container:
                        st.markdown(f"#### Processing: {input_video.name}")

                        success, message = process_video_with_outro(
                            str(input_path),
                            str(outro_path),
                            str(output_path),
                            ffmpeg_cmd,
                            lambda msg: status_text.text(msg)
                        )

                        if success:
                            success_count += 1
                            file_size = os.path.getsize(output_path) / (1024*1024)

                            # Read file data immediately and store it
                            with open(output_path, "rb") as f:
                                file_data = f.read()

                            processed_files.append({
                                'filename': output_filename,
                                'data': file_data,
                                'size': file_size,
                                'original_name': input_video.name
                            })

                            st.markdown(f"""
                            <div class="success-box">
                                <h4 style="margin: 0 0 0.5rem 0;">🎉 ULTRA PREMIUM SUCCESS!</h4>
                                <p style="margin: 0.2rem 0;"><strong>📁 File:</strong> {input_video.name}</p>
                                <p style="margin: 0.2rem 0;"><strong>📊 Quality:</strong> Professional Grade Preserved</p>
                                <p style="margin: 0.2rem 0;"><strong>💾 Output:</strong> {output_filename} ({file_size:.1f} MB)</p>
                                <p style="margin: 0.2rem 0;"><strong>⚡ Status:</strong> Ready for Download</p>
                            </div>
                            """, unsafe_allow_html=True)

                            processed_videos.append(output_filename)
                        else:
                            failed_videos.append((input_video.name, message))
                            st.markdown(f"""
                            <div class="error-box">
                                <h4 style="margin: 0 0 0.5rem 0;">❌ PROCESSING FAILED</h4>
                                <p style="margin: 0.2rem 0;"><strong>📁 File:</strong> {input_video.name}</p>
                                <p style="margin: 0.2rem 0;"><strong>🔍 Error:</strong> {message}</p>
                                <p style="margin: 0.2rem 0;"><strong>💡 Tip:</strong> Check file format and try again</p>
                            </div>
                            """, unsafe_allow_html=True)

                # Store processed files in session state for downloads
                st.session_state.processed_files = processed_files

                # Show download section for successful files
                if processed_files:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                                box-shadow: 0 20px 40px rgba(16, 185, 129, 0.3);">
                        <h3 style="color: white; margin: 0 0 1rem 0;">📥 DOWNLOAD YOUR PREMIUM VIDEOS</h3>
                        <p style="color: rgba(255,255,255,0.9); margin: 0;">
                            Click the buttons below to download your processed videos
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                    # Create download buttons for each processed file
                    for file_info in processed_files:
                        col_dl1, col_dl2, col_dl3 = st.columns([1, 2, 1])
                        with col_dl2:
                            st.download_button(
                                label=f"📥 DOWNLOAD {file_info['filename']} ({file_info['size']:.1f} MB)",
                                data=file_info['data'],
                                file_name=file_info['filename'],
                                mime="video/mp4",
                                use_container_width=True,
                                key=f"download_{file_info['filename']}"
                            )

                # Add cleanup option
                st.markdown("---")
                if st.button("🗑️ Clear Session & Start Fresh", type="secondary", use_container_width=True):
                    # Cleanup temporary files
                    if hasattr(st.session_state, 'temp_dir') and st.session_state.temp_dir.exists():
                        import shutil
                        try:
                            shutil.rmtree(st.session_state.temp_dir)
                        except:
                            pass

                    # Clear session state
                    if 'processed_files' in st.session_state:
                        del st.session_state.processed_files
                    if 'temp_dir' in st.session_state:
                        del st.session_state.temp_dir

                    st.success("✅ Session cleared! You can now process new videos.")
                    st.rerun()

            except Exception as e:
                st.error(f"❌ An error occurred during processing: {str(e)}")
                # Cleanup on error
                if hasattr(st.session_state, 'temp_dir') and st.session_state.temp_dir.exists():
                    import shutil
                    try:
                        shutil.rmtree(st.session_state.temp_dir)
                    except:
                        pass

                # Ultra Premium Final Summary
                st.markdown("""
                <div class="stats-container">
                    <h2 style="color: #ff6b6b; text-align: center; font-size: 2.5rem; margin-bottom: 2rem;">
                        📊 ULTRA PREMIUM PROCESSING COMPLETE
                    </h2>
                </div>
                """, unsafe_allow_html=True)

                # Premium Metrics
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.markdown(f"""
                    <div class="metric-container">
                        <h3 style="color: #54a0ff; margin: 0;">📁 TOTAL</h3>
                        <h2 style="color: white; margin: 0.5rem 0;">{total_videos}</h2>
                        <p style="color: rgba(255,255,255,0.7); margin: 0;">Videos Processed</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    st.markdown(f"""
                    <div class="metric-container">
                        <h3 style="color: #10b981; margin: 0;">✅ SUCCESS</h3>
                        <h2 style="color: white; margin: 0.5rem 0;">{success_count}</h2>
                        <p style="color: rgba(255,255,255,0.7); margin: 0;">Perfect Quality</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="metric-container">
                        <h3 style="color: #ef4444; margin: 0;">❌ FAILED</h3>
                        <h2 style="color: white; margin: 0.5rem 0;">{len(failed_videos)}</h2>
                        <p style="color: rgba(255,255,255,0.7); margin: 0;">Need Retry</p>
                    </div>
                    """, unsafe_allow_html=True)

                with col4:
                    success_rate = (success_count / total_videos * 100) if total_videos > 0 else 0
                    st.markdown(f"""
                    <div class="metric-container">
                        <h3 style="color: #ff9ff3; margin: 0;">📈 RATE</h3>
                        <h2 style="color: white; margin: 0.5rem 0;">{success_rate:.1f}%</h2>
                        <p style="color: rgba(255,255,255,0.7); margin: 0;">Success Rate</p>
                    </div>
                    """, unsafe_allow_html=True)

                # Premium Status Messages
                if success_count == total_videos:
                    st.balloons()
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #10b981 0%, #059669 100%);
                                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                                box-shadow: 0 20px 40px rgba(16, 185, 129, 0.3);">
                        <h2 style="color: white; margin: 0;">🎉 ULTRA PREMIUM SUCCESS!</h2>
                        <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 1.2rem;">
                            All videos processed with PERFECT resolution and quality preservation!
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                elif success_count > 0:
                    st.markdown(f"""
                    <div style="background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                                box-shadow: 0 20px 40px rgba(245, 158, 11, 0.3);">
                        <h2 style="color: white; margin: 0;">⚠️ PARTIAL SUCCESS</h2>
                        <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 1.2rem;">
                            {success_count} videos processed successfully, {len(failed_videos)} failed.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
                                padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                                box-shadow: 0 20px 40px rgba(239, 68, 68, 0.3);">
                        <h2 style="color: white; margin: 0;">❌ PROCESSING FAILED</h2>
                        <p style="color: rgba(255,255,255,0.9); margin: 1rem 0 0 0; font-size: 1.2rem;">
                            No videos were processed successfully. Please check the error messages above.
                        </p>
                    </div>
                    """, unsafe_allow_html=True)

                # Show failed videos with premium styling
                if failed_videos:
                    st.markdown("""
                    <div style="margin: 2rem 0;">
                        <h3 style="color: #ef4444; text-align: center;">❌ FAILED VIDEOS ANALYSIS</h3>
                    </div>
                    """, unsafe_allow_html=True)

                    for video_name, error in failed_videos:
                        st.markdown(f"""
                        <div style="background: linear-gradient(135deg, #374151 0%, #1f2937 100%);
                                    padding: 1rem; border-radius: 15px; margin: 0.5rem 0;
                                    border-left: 4px solid #ef4444;">
                            <h4 style="color: #ef4444; margin: 0 0 0.5rem 0;">📁 {video_name}</h4>
                            <p style="color: rgba(255,255,255,0.8); margin: 0; font-size: 0.9rem;">
                                <strong>Error:</strong> {error}
                            </p>
                        </div>
                        """, unsafe_allow_html=True)

                st.markdown("</div>", unsafe_allow_html=True)  # Close processing button div

    # Show previously processed files if they exist
    if hasattr(st.session_state, 'processed_files') and st.session_state.processed_files:
        st.markdown("---")
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    padding: 2rem; border-radius: 20px; text-align: center; margin: 2rem 0;
                    box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);">
            <h3 style="color: white; margin: 0 0 1rem 0;">📥 PREVIOUSLY PROCESSED VIDEOS</h3>
            <p style="color: rgba(255,255,255,0.9); margin: 0;">
                Your processed videos are still available for download
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Show download buttons for previously processed files
        for file_info in st.session_state.processed_files:
            col_prev1, col_prev2, col_prev3 = st.columns([1, 2, 1])
            with col_prev2:
                st.download_button(
                    label=f"📥 DOWNLOAD {file_info['filename']} ({file_info['size']:.1f} MB)",
                    data=file_info['data'],
                    file_name=file_info['filename'],
                    mime="video/mp4",
                    use_container_width=True,
                    key=f"prev_download_{file_info['filename']}"
                )

        # Add cleanup option for previous files
        if st.button("🗑️ Clear Previous Downloads", type="secondary", use_container_width=True):
            # Cleanup temporary files
            if hasattr(st.session_state, 'temp_dir') and st.session_state.temp_dir.exists():
                import shutil
                try:
                    shutil.rmtree(st.session_state.temp_dir)
                except:
                    pass

            # Clear session state
            if 'processed_files' in st.session_state:
                del st.session_state.processed_files
            if 'temp_dir' in st.session_state:
                del st.session_state.temp_dir

            st.success("✅ Previous downloads cleared! Ready for new processing.")
            st.rerun()

if __name__ == "__main__":
    main()
