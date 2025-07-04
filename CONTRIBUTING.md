# Contributing to VideoMaster Pro

Thank you for your interest in contributing to VideoMaster Pro! We welcome contributions from the community.

## 🚀 Quick Start for Contributors

1. **Fork the repository**
2. **Clone your fork:**
   ```bash
   git clone https://github.com/yourusername/VideoMaster-Pro.git
   cd VideoMaster-Pro
   ```
3. **Create a feature branch:**
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes**
5. **Test your changes:**
   ```bash
   python launch.py
   ```
6. **Commit and push:**
   ```bash
   git add .
   git commit -m "Add your feature description"
   git push origin feature/your-feature-name
   ```
7. **Create a Pull Request**

## 🎯 Ways to Contribute

### 🐛 Bug Reports
- Use the GitHub Issues tab
- Include steps to reproduce
- Provide system information (OS, Python version)
- Include error messages and logs

### ✨ Feature Requests
- Check existing issues first
- Describe the feature clearly
- Explain the use case
- Consider implementation complexity

### 🔧 Code Contributions
- Follow Python PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation if needed

### 📚 Documentation
- Fix typos and grammar
- Improve setup instructions
- Add usage examples
- Translate to other languages

## 🛠️ Development Setup

### Prerequisites
- Python 3.7+
- Git
- Text editor or IDE

### Local Development
```bash
# Clone the repo
git clone https://github.com/yourusername/VideoMaster-Pro.git
cd VideoMaster-Pro

# Install dependencies
pip install -r requirements.txt

# Run the platform
python launch.py
```

### Testing
- Test with various video formats (MP4, MOV, AVI, MKV)
- Test with different resolutions (720p, 1080p, 4K)
- Test batch processing with multiple videos
- Verify download functionality

## 📋 Code Style

### Python Guidelines
- Follow PEP 8
- Use meaningful variable names
- Add docstrings for functions
- Keep functions focused and small
- Use type hints where appropriate

### Example:
```python
def process_video_with_outro(input_path: str, outro_path: str, output_path: str) -> bool:
    """
    Process a video by adding an outro.
    
    Args:
        input_path: Path to input video file
        outro_path: Path to outro video file
        output_path: Path for output video file
        
    Returns:
        bool: True if processing successful, False otherwise
    """
    # Implementation here
    pass
```

## 🎨 UI/UX Guidelines

### Streamlit Best Practices
- Keep the interface clean and intuitive
- Use consistent styling
- Provide clear feedback to users
- Handle errors gracefully
- Optimize for performance

### Design Principles
- **Simplicity**: Easy to use for beginners
- **Performance**: Fast processing and responsive UI
- **Accessibility**: Clear text, good contrast
- **Mobile-friendly**: Works on different screen sizes

## 🧪 Testing Guidelines

### Manual Testing Checklist
- [ ] Platform launches successfully
- [ ] File upload works (drag & drop)
- [ ] Video processing completes without errors
- [ ] Progress tracking displays correctly
- [ ] Download functionality works
- [ ] Batch processing handles multiple files
- [ ] Error handling works for invalid files

### Test Cases
1. **Single video processing**
2. **Batch processing (5+ videos)**
3. **Different video formats**
4. **Various resolutions**
5. **Large file handling (500MB+)**
6. **Network interruption recovery**

## 🚨 Issue Guidelines

### Bug Report Template
```markdown
**Bug Description**
A clear description of the bug.

**Steps to Reproduce**
1. Go to '...'
2. Click on '...'
3. Upload '...'
4. See error

**Expected Behavior**
What you expected to happen.

**Screenshots**
If applicable, add screenshots.

**System Information**
- OS: [e.g. Windows 10, macOS 11.0, Ubuntu 20.04]
- Python Version: [e.g. 3.9.0]
- Browser: [e.g. Chrome 95.0]

**Additional Context**
Any other context about the problem.
```

### Feature Request Template
```markdown
**Feature Description**
A clear description of the feature you'd like to see.

**Use Case**
Explain why this feature would be useful.

**Proposed Solution**
Describe how you think this could be implemented.

**Alternatives Considered**
Other solutions you've considered.

**Additional Context**
Any other context or screenshots.
```

## 🏆 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes for significant contributions
- Special thanks in documentation

## 📞 Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Email**: For security issues or private matters

## 📜 Code of Conduct

### Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## 🎉 Thank You!

Thank you for contributing to VideoMaster Pro! Your contributions help make this project better for everyone.

---

**Happy Coding!** 🚀
