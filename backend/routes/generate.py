from flask import Blueprint, request, jsonify
from services.image_engine import generate_panel

generate_bp = Blueprint('generate', __name__)

@generate_bp.route('/panel', methods=['POST'])
def create_panel():
    """Generate a manga panel based on scene description."""
    data = request.json
    if not data or 'scene' not in data:
        return jsonify({"error": "Missing scene description in request"}), 400
    
    scene = data.get('scene')
    characters = data.get('characters', [])
    style = data.get('style', 'manga')
    
    try:
        # Generate panel using image generation engine
        panel_path = generate_panel(scene, characters, style)
        return jsonify({"status": "success", "panel_path": panel_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500