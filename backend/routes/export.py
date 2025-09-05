from flask import Blueprint, request, jsonify, send_file
from services.layout_engine import create_manga_pdf, create_manga_cbz
import os

export_bp = Blueprint('export', __name__)

@export_bp.route('/pdf', methods=['POST'])
def export_pdf():
    """Export manga as PDF."""
    data = request.json
    if not data or 'panels' not in data:
        return jsonify({"error": "Missing panels data in request"}), 400
    
    panels = data.get('panels')
    title = data.get('title', 'Manga Creation')
    
    try:
        # Generate PDF using layout engine
        pdf_path = create_manga_pdf(panels, title)
        return jsonify({"status": "success", "pdf_path": pdf_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@export_bp.route('/cbz', methods=['POST'])
def export_cbz():
    """Export manga as CBZ."""
    data = request.json
    if not data or 'panels' not in data:
        return jsonify({"error": "Missing panels data in request"}), 400
    
    panels = data.get('panels')
    title = data.get('title', 'Manga Creation')
    
    try:
        # Generate CBZ using layout engine
        cbz_path = create_manga_cbz(panels, title)
        return jsonify({"status": "success", "cbz_path": cbz_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@export_bp.route('/download/<format>/<path:filename>', methods=['GET'])
def download_file(format, filename):
    """Download generated manga file."""
    if format not in ['pdf', 'cbz']:
        return jsonify({"error": "Invalid format"}), 400
    
    file_path = os.path.join('outputs', filename)
    if not os.path.exists(file_path):
        return jsonify({"error": "File not found"}), 404
    
    return send_file(file_path, as_attachment=True)