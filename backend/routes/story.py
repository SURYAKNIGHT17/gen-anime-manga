from flask import Blueprint, request, jsonify
from services.nlp_engine import generate_story

story_bp = Blueprint('story', __name__)

@story_bp.route('/generate', methods=['POST'])
def create_story():
    """Generate a story based on user prompt and characters."""
    data = request.json
    if not data or 'prompt' not in data:
        return jsonify({"error": "Missing prompt in request"}), 400
    
    prompt = data.get('prompt')
    characters = data.get('characters', [])
    
    try:
        # Generate story using NLP engine
        story_scenes = generate_story(prompt, characters)
        return jsonify({"status": "success", "scenes": story_scenes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500