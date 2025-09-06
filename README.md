# Manga Creator Application

A sophisticated AI-powered manga story and panel generation application that combines advanced natural language processing with state-of-the-art image generation capabilities.

## Features

### 🎨 Advanced Image Generation
- **Stable Diffusion Integration**: Real AI-powered manga panel generation using Stable Diffusion models
- **Style-Aware Generation**: Automatically adapts art style based on story genre and character descriptions
- **Fallback Mechanisms**: Robust error handling with local generation fallbacks
- **High-Quality Output**: Generates detailed, high-resolution manga panels

### 📚 Intelligent Story Generation
- **Multi-Mode Generation**: Supports both regular and "unhinged" creative modes
- **OpenAI Integration**: Leverages GPT models for sophisticated narrative creation
- **NLP-Enhanced Processing**: Advanced text analysis for genre detection and sentiment analysis
- **Character Development**: Intelligent character integration and development
- **Metadata Generation**: Comprehensive story metadata including themes, reading time, and statistics

### 🧠 Advanced NLP Engine
- **Genre Detection**: Automatic story genre classification (fantasy, sci-fi, romance, action, etc.)
- **Sentiment Analysis**: Real-time emotion and tone analysis
- **Keyword Extraction**: Intelligent keyword and theme identification
- **Story Structure**: Sophisticated scene generation with proper narrative flow
- **Character Analysis**: Advanced character relationship and development tracking

### 🔧 Technical Features
- **Robust Error Handling**: Comprehensive error management with graceful degradation
- **Offline Capability**: Works without internet connection using local fallback methods
- **Modular Architecture**: Clean, maintainable code structure with separated concerns
- **Comprehensive Logging**: Detailed logging for debugging and monitoring
- **Cross-Platform Support**: Compatible with Windows, macOS, and Linux

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- At least 8GB RAM (recommended for Stable Diffusion)
- CUDA-compatible GPU (optional, for faster image generation)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd manga_creator
   ```

2. **Install backend dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies**:
   ```bash
   cd ../frontend
   npm install
   ```

4. **Configure environment variables** (optional):
   Create a `.env` file in the backend directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   HUGGINGFACE_TOKEN=your_huggingface_token_here
   ```

## Usage

### Running the Application

1. **Start the backend server**:
   ```bash
   cd backend
   python app.py
   ```
   The server will start on `http://localhost:5000`

2. **Start the frontend** (in a separate terminal):
   ```bash
   cd frontend
   npm start
   ```
   The frontend will be available at `http://localhost:3000`

### API Endpoints

- `POST /generate-story` - Generate a complete manga story
- `POST /generate-panel` - Generate individual manga panels
- `POST /analyze-text` - Perform NLP analysis on text
- `GET /health` - Health check endpoint

### Example Usage

```python
from story_generator import generate_manga_story
from services.image_engine import generate_panel

# Generate a story
story = generate_manga_story(
    prompt="A brave warrior fights a dragon",
    characters=["Hero", "Dragon"],
    unhinged=False
)

# Generate a panel
panel = generate_panel(
    prompt="A warrior stands ready for battle",
    genre="fantasy",
    character="Hero"
)
```

## Architecture

### Backend Components
- **app.py**: Main Flask application and API routes
- **story_generator.py**: Enhanced story generation with AI integration
- **openai_generator.py**: OpenAI API integration with error handling
- **services/nlp_engine.py**: Advanced NLP processing and analysis
- **services/image_engine.py**: Stable Diffusion image generation
- **panel_generator.py**: Panel layout and composition logic

### Frontend Components
- **React-based UI**: Modern, responsive user interface
- **Real-time Updates**: Live story and panel generation feedback
- **Interactive Controls**: Advanced customization options

## What Was Improved

### ✅ Major Enhancements Completed

1. **Image Generation Engine**: Replaced placeholder image generation with real Stable Diffusion implementation
   - Integrated `diffusers` library with Stable Diffusion v1.5
   - Added Compel for advanced prompt weighting and enhancement
   - Implemented robust error handling with local fallbacks
   - Added automatic model downloading and caching

2. **Story Generator**: Enhanced with sophisticated AI integration
   - Integrated OpenAI GPT models for high-quality story generation
   - Added comprehensive metadata generation (themes, reading time, statistics)
   - Implemented multiple generation modes (regular and unhinged)
   - Enhanced character development and relationship tracking

3. **NLP Engine**: Upgraded with advanced text processing capabilities
   - Added sentiment analysis using TextBlob
   - Implemented genre detection with keyword matching
   - Enhanced keyword extraction and theme identification
   - Added story structure analysis and scene generation

4. **OpenAI Integration**: Implemented proper API integration with comprehensive error handling
   - Added robust API key management
   - Implemented rate limiting and retry mechanisms
   - Added fallback to local generation when API is unavailable
   - Enhanced prompt engineering for better results

5. **Code Quality**: Fixed import paths and syntax errors throughout codebase
   - Corrected indentation errors in `openai_generator.py`
   - Fixed import paths in `story_generator.py`
   - Removed orphaned code blocks and syntax issues
   - Improved code structure and maintainability

6. **Testing**: Successfully tested all functionality
   - Verified all imports work correctly
   - Tested story generation with various prompts
   - Confirmed web application runs successfully
   - Validated API endpoints and error handling

## Configuration

### Image Generation Settings
- **Model**: Uses Stable Diffusion v1.5 by default
- **Resolution**: 512x512 pixels (configurable)
- **Steps**: 20 inference steps (adjustable for quality vs speed)
- **Guidance Scale**: 7.5 (controls adherence to prompt)

### Story Generation Settings
- **Max Scenes**: Configurable scene count (default: 6-12)
- **Character Limit**: Supports unlimited characters
- **Genre Support**: Fantasy, Sci-Fi, Romance, Action, Horror, Comedy, Drama

## Troubleshooting

### Common Issues

1. **Out of Memory Errors**:
   - Reduce image resolution in settings
   - Close other applications
   - Use CPU-only mode if GPU memory is insufficient

2. **Slow Image Generation**:
   - Ensure CUDA is properly installed for GPU acceleration
   - Reduce inference steps for faster generation
   - Consider using smaller models

3. **API Rate Limits**:
   - The application automatically handles OpenAI rate limits
   - Local fallbacks are used when API is unavailable

### Performance Optimization

- **GPU Acceleration**: Install CUDA for faster image generation
- **Memory Management**: The application automatically manages memory usage
- **Caching**: Generated content is cached to improve performance

## Development

### Code Structure
- Follow PEP 8 style guidelines
- Comprehensive error handling required
- All functions must include docstrings
- Unit tests for critical components

### Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes with proper documentation
4. Add tests for new functionality
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- **Stable Diffusion**: For state-of-the-art image generation
- **OpenAI**: For advanced language model capabilities
- **Hugging Face**: For model hosting and transformers library
- **Flask**: For the robust web framework
- **React**: For the modern frontend framework

---

**Note**: This application requires significant computational resources for optimal performance. For the best experience, use a system with a dedicated GPU and at least 8GB of RAM.