# Anime Manga Creator

A powerful web application that generates manga stories and panels with AI-enhanced content generation capabilities.

## Features

### 🎨 Story Generation
- Generate 10-15 scene manga stories
- Dynamic character development
- Varied plot points and emotional arcs
- **NEW: Unhinged Mode** - Generate mature, uncensored content with adult themes

### 🖼️ Panel Generation
- Realistic manga-style panels
- Dynamic backgrounds based on scene type
- Character silhouettes and speech bubbles
- Scene-specific visual elements
- **NEW: Enhanced with AI descriptions**

### 📄 PDF Export
- Professional manga layout
- Title page with story summary
- Page numbers and timestamps
- High-quality panel rendering

### 🤖 AI Integration
- OpenAI API integration for enhanced content
- Fallback to local generation
- Customizable content intensity

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd manga_creator
   ```

2. **Install dependencies:**
   ```bash
   pip install flask flask-cors pillow reportlab python-dotenv openai
   ```

3. **Set up environment variables (optional):**
   Create a `.env` file in the backend directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application:**
   ```bash
   cd backend
   python app.py
   ```

5. **Access the application:**
   Open your browser and go to `http://localhost:5000/anime`

## Usage

### Basic Story Generation
1. Enter a story prompt (e.g., "A ninja's quest for revenge")
2. Add character names separated by commas
3. Click "Generate Manga"

### Unhinged Mode ⚠️
1. Check the "🔞 Unhinged Mode" checkbox
2. **Warning:** This generates mature content with:
   - Adult themes and situations
   - Explicit language and swearing
   - Uncensored storylines
   - Unexpected plot twists
3. Confirm the warning dialog
4. Generate your edgy manga content

### Export Options
- Click "Export as PDF" after generation
- Download your complete manga as a PDF file

## What I Implemented

### Step-by-Step Implementation:

1. **Enhanced Story Generator (`story_generator.py`)**
   - Created a comprehensive story generation system
   - Added unhinged mode with adult themes and explicit content
   - Implemented 10-15 scene generation with varied plot points
   - Added emotional depth and character development

2. **OpenAI Integration (`openai_generator.py`)**
   - Built OpenAI API integration for enhanced content generation
   - Added fallback mechanisms for when API is unavailable
   - Implemented unhinged content generation with explicit prompts
   - Created error handling and recovery systems

3. **Enhanced Panel Generator (`panel_generator.py`)**
   - Updated panel generation to use AI-enhanced descriptions
   - Added support for unhinged content visualization
   - Integrated with OpenAI generator for better panel descriptions
   - Maintained fallback to local generation

4. **Updated Backend API (`app.py`)**
   - Modified `/api/story/generate` to support unhinged parameter
   - Updated `/api/generate/panel` to use new panel generator
   - Added comprehensive error handling
   - Integrated all new modules seamlessly

5. **Enhanced Frontend (`anime.html`)**
   - Added "Unhinged Mode" checkbox with warning styling
   - Implemented content warnings and confirmation dialogs
   - Updated API calls to pass unhinged parameter
   - Added visual indicators for mature content

### Key Features Added:
- **Unhinged Content Generation**: Mature themes, explicit language, adult situations
- **AI Enhancement**: OpenAI integration for more creative and unexpected content
- **Content Warnings**: Appropriate warnings and user confirmations
- **Fallback Systems**: Robust error handling with local generation backup
- **Enhanced UI**: Visual indicators and warnings for mature content

## File Structure

```
manga_creator/
├── backend/
│   ├── app.py                 # Main Flask application (UPDATED)
│   ├── story_generator.py     # Enhanced story generation (NEW)
│   ├── panel_generator.py     # Realistic panel generation (NEW)
│   ├── openai_generator.py    # OpenAI API integration (NEW)
│   ├── static/
│   │   └── anime.html         # Frontend interface (UPDATED)
│   └── outputs/               # Generated panels and PDFs
└── README.md                  # Documentation (UPDATED)
```

## Content Warnings

⚠️ **Unhinged Mode generates mature content including:**
- Strong language and profanity
- Adult themes and situations
- Violence and intense scenarios
- Uncensored storylines
- Unexpected and edgy plot developments

**Use responsibly and only if comfortable with explicit content.**

## Technical Implementation Details

### Code Analysis and Corrections Made:

1. **Story Generator Integration**
   - Replaced hardcoded story generation with modular system
   - Added unhinged parameter support throughout the pipeline
   - Implemented comprehensive error handling

2. **Panel Generator Enhancement**
   - Integrated OpenAI descriptions for more realistic panels
   - Added unhinged content support for edgier visuals
   - Maintained backward compatibility with existing system

3. **Frontend Updates**
   - Added mature content warnings and confirmations
   - Updated API calls to include new parameters
   - Enhanced user experience with visual indicators

4. **Error Handling**
   - Comprehensive try-catch blocks throughout
   - Fallback mechanisms for API failures
   - User-friendly error messages

### Testing and Verification:
- Server successfully restarts with new modules
- All API endpoints updated and functional
- Frontend properly handles new parameters
- Error handling tested and working

## License

This project is for educational and entertainment purposes. Use responsibly.

---

**Enjoy creating your unique, unhinged manga stories! 🎌🔞**