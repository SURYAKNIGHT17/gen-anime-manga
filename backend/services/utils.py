"""
Utility functions for the manga creator application.
"""
import os
import time
import json
from datetime import datetime

def sanitize_filename(filename):
    """
    Sanitize a filename to ensure it's safe for file system operations.
    
    Args:
        filename (str): The filename to sanitize
        
    Returns:
        str: Sanitized filename
    """
    # Replace invalid characters
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def generate_unique_id():
    """
    Generate a unique ID based on timestamp.
    
    Returns:
        str: Unique ID
    """
    return f"{int(time.time())}_{os.getpid()}"

def save_project_metadata(project_id, title, scenes, output_dir="outputs"):
    """
    Save project metadata to a JSON file.
    
    Args:
        project_id (str): Unique project ID
        title (str): Project title
        scenes (list): List of scene data
        output_dir (str): Directory to save metadata
        
    Returns:
        str: Path to the metadata file
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Create metadata
    metadata = {
        "project_id": project_id,
        "title": title,
        "created_at": datetime.now().isoformat(),
        "scenes": scenes
    }
    
    # Save metadata to file
    filename = f"{sanitize_filename(title)}_{project_id}.json"
    file_path = os.path.join(output_dir, filename)
    
    with open(file_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return file_path

def load_project_metadata(project_id, output_dir="outputs"):
    """
    Load project metadata from a JSON file.
    
    Args:
        project_id (str): Unique project ID
        output_dir (str): Directory where metadata is stored
        
    Returns:
        dict: Project metadata or None if not found
    """
    # Find metadata file
    for filename in os.listdir(output_dir):
        if filename.endswith(f"{project_id}.json"):
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'r') as f:
                return json.load(f)
    
    return None