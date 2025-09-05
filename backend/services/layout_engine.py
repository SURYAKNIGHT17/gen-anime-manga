"""
Layout Engine for manga layout and export.
Uses ReportLab for PDF generation and standard libraries for CBZ.
"""
import os
import time
import zipfile
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import Image
import shutil

def create_manga_pdf(panels, title="Manga Creation"):
    """
    Create a PDF with manga panels and dialogue.
    
    Args:
        panels (list): List of panel data with paths and dialogue
        title (str): Title of the manga
        
    Returns:
        str: Path to the generated PDF
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Generate a unique filename
    timestamp = int(time.time())
    filename = f"{title.replace(' ', '_')}_{timestamp}.pdf"
    output_path = os.path.join("outputs", filename)
    
    # Create PDF
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # Add title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(50, height - 50, title)
    
    # Add panels
    y_position = height - 100
    for i, panel in enumerate(panels):
        # Get panel image
        panel_path = panel.get("path")
        if not os.path.exists(panel_path):
            continue
            
        # Add panel image
        img = Image.open(panel_path)
        img_width, img_height = img.size
        
        # Scale image to fit page width with margins
        scale_factor = (width - 100) / img_width
        new_width = img_width * scale_factor
        new_height = img_height * scale_factor
        
        # Check if we need a new page
        if y_position - new_height < 50:
            c.showPage()
            y_position = height - 50
        
        # Draw image
        c.drawImage(panel_path, 50, y_position - new_height, width=new_width, height=new_height)
        
        # Add dialogue
        dialogue = panel.get("dialogue", [])
        dialogue_y = y_position - new_height - 20
        c.setFont("Helvetica", 10)
        for line in dialogue:
            character = line.get("character", "")
            text = line.get("text", "")
            c.drawString(50, dialogue_y, f"{character}: {text}")
            dialogue_y -= 15
            
        y_position = dialogue_y - 20
        
        # Add a new page if needed
        if y_position < 50:
            c.showPage()
            y_position = height - 50
    
    # Save PDF
    c.save()
    
    return output_path

def create_manga_cbz(panels, title="Manga Creation"):
    """
    Create a CBZ (Comic Book ZIP) with manga panels.
    
    Args:
        panels (list): List of panel data with paths
        title (str): Title of the manga
        
    Returns:
        str: Path to the generated CBZ
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Create a temporary directory for the images
    temp_dir = os.path.join("outputs", "temp")
    os.makedirs(temp_dir, exist_ok=True)
    
    # Generate a unique filename
    timestamp = int(time.time())
    filename = f"{title.replace(' ', '_')}_{timestamp}.cbz"
    output_path = os.path.join("outputs", filename)
    
    # Copy panel images to temp directory
    for i, panel in enumerate(panels):
        panel_path = panel.get("path")
        if not os.path.exists(panel_path):
            continue
            
        # Copy image with sequential naming
        dest_path = os.path.join(temp_dir, f"{i:03d}.png")
        shutil.copy(panel_path, dest_path)
    
    # Create ZIP file (CBZ is just a ZIP with a different extension)
    with zipfile.ZipFile(output_path, 'w') as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.basename(file_path))
    
    # Clean up temp directory
    shutil.rmtree(temp_dir)
    
    return output_path