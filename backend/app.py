from flask import Flask, render_template, send_from_directory, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Security headers
@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Simple API routes for demo
@app.route('/api/story/generate', methods=['POST'])
def generate_story():
    from flask import request
    import story_generator
    
    try:
        # Get request data
        data = request.get_json()
        prompt = data.get('prompt', 'A manga adventure')
        characters = data.get('characters', ['Hero', 'Villain'])
        unhinged = data.get('unhinged', False)  # New parameter for unhinged content
        
        # Ensure characters is a list
        if isinstance(characters, str):
            characters = [characters]
        
        # Generate story using the enhanced story generator module
        story = story_generator.generate_manga_story(prompt, characters, unhinged=unhinged)
        
        return jsonify({
            'success': True,
            'story': story,
            'unhinged': unhinged
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/')
def index():
    return jsonify({"message": "Anime Manga Creator API is running"})

@app.route('/anime')
def anime_page():
    return send_from_directory('static', 'anime.html')

@app.route('/api/generate/panel', methods=['POST'])
def generate_panel():
    from flask import request
    import panel_generator
    
    try:
        # Get request data
        data = request.get_json()
        scene_description = data.get('scene_description', 'A manga scene')
        dialogues = data.get('dialogues', [])
        unhinged = data.get('unhinged', False)
        
        # Generate panel using the enhanced panel generator module
        panel_path, panel_filename = panel_generator.generate_manga_panel(
            scene_description, dialogues, unhinged=unhinged
        )
        
        # Return the correct path format for the frontend
        return jsonify({
            'success': True,
            'panel_path': f'/outputs/{panel_filename}'
        })
    except Exception as e:
        # Fallback to simple error panel
        from PIL import Image, ImageDraw
        import time
        import os
        
        os.makedirs("outputs", exist_ok=True)
        img = Image.new('RGB', (800, 600), color=(255, 200, 200))
        d = ImageDraw.Draw(img)
        d.rectangle([100, 250, 700, 350], fill=(255, 255, 255), outline=(0, 0, 0))
        d.text((400, 300), "Error generating panel", fill=(0, 0, 0))
        
        timestamp = int(time.time())
        filename = f"error_panel_{timestamp}.png"
        filepath = os.path.join("outputs", filename)
        img.save(filepath)
        
        return jsonify({
            'success': False,
            'panel_path': f'/outputs/{filename}',
            'error': str(e)
        })

@app.route('/api/export/pdf', methods=['POST'])
def export_pdf():
    # Create a simple PDF with the manga panels
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    import glob
    import time
    
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Create a PDF file
    timestamp = int(time.time())
    pdf_filename = f"manga_{timestamp}.pdf"
    pdf_path = os.path.join("outputs", pdf_filename)
    
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Your Manga Creation")
    
    # Get all panel images
    panel_files = glob.glob("outputs/panel_*.png")
    
    # If no panels found, create a sample one
    if not panel_files:
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (800, 600), color=(255, 255, 255))
        d = ImageDraw.Draw(img)
        d.text((400, 300), "Sample Manga Panel", fill=(0, 0, 0))
        sample_path = os.path.join("outputs", "sample_panel.png")
        img.save(sample_path)
        panel_files = [sample_path]
    
    # Add panels to PDF
    y_position = height - 150
    for i, panel_file in enumerate(panel_files):
        if y_position < 100:  # Start a new page if needed
            c.showPage()
            y_position = height - 100
        
        # Add panel number
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, y_position, f"Panel {i+1}")
        y_position -= 20
        
        # Add image
        try:
            c.drawImage(panel_file, 100, y_position - 300, width=400, height=300)
        except:
            c.setFont("Helvetica", 12)
            c.drawString(100, y_position - 150, "Image could not be loaded")
        
        y_position -= 350
    
    # Save the PDF
    c.save()
    
    return jsonify({"pdf_path": f"/outputs/{pdf_filename}"})

# Serve generated files
@app.route('/outputs/<path:filename>')
def serve_output(filename):
    return send_from_directory('outputs', filename)

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)