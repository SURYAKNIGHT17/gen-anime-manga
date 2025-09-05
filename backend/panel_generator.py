import random
import os
from PIL import Image, ImageDraw, ImageFont
import time
import math
from openai_generator import OpenAIGenerator

def generate_manga_panel(scene_description, dialogues, unhinged=False):
    """
    Generate a manga panel based on scene description and dialogues
    """
    # Try to enhance the panel description using OpenAI if available
    try:
        openai_gen = OpenAIGenerator()
        enhanced_description = openai_gen.generate_panel_description(scene_description, unhinged=unhinged)
        if enhanced_description:
            scene_description = enhanced_description
    except Exception as e:
        print(f"OpenAI enhancement failed, using original description: {e}")
    
    # Create a more realistic manga panel
    width, height = 800, 600
    
    # Choose panel style based on scene content
    if "action" in scene_description.lower():
        # Action scenes have dynamic backgrounds
        panel = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(panel)
        
        # Draw speed lines for action scenes
        for _ in range(50):
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            draw.line([(x1, y1), (x2, y2)], fill=(0, 0, 0), width=1)
            
    elif "dialogue" in scene_description.lower():
        # Dialogue scenes have simpler backgrounds
        panel = Image.new('RGB', (width, height), color=(240, 240, 240))
        draw = ImageDraw.Draw(panel)
        
    else:
        # Standard scene with manga-style elements
        panel = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(panel)
        
        # Add manga-style background elements
        for _ in range(10):
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = x1 + random.randint(50, 200), y1 + random.randint(50, 200)
            fill_color = (random.randint(220, 250), random.randint(220, 250), random.randint(220, 250))
            draw.rectangle([x1, y1, x2, y2], fill=fill_color)
    
    # Add character silhouettes
    num_characters = min(len(dialogues) if dialogues else 2, 3)
    for i in range(num_characters):
        # Character position
        if num_characters == 1:
            x = width // 2
        else:
            x = width // (num_characters + 1) * (i + 1)
        
        # Draw character silhouette
        y = height - 150
        draw.ellipse((x - 30, y - 100, x + 30, y - 40), fill=(0, 0, 0))  # Head
        draw.rectangle((x - 40, y - 40, x + 40, y + 100), fill=(0, 0, 0))  # Body
    
    # Add speech bubbles for dialogues
    if dialogues:
        font = ImageFont.load_default()
        for i, dialogue in enumerate(dialogues[:3]):
            if isinstance(dialogue, dict):
                text = dialogue.get('text', '')
                character = dialogue.get('character', 'Character')
                
                # Position speech bubbles
                bubble_x = width // 4 + (i * width // 4)
                bubble_y = 100 + (i * 50)
                
                # Draw speech bubble
                bubble_width = min(len(text) * 8, 300)
                draw.ellipse((bubble_x - bubble_width//2, bubble_y - 40, 
                             bubble_x + bubble_width//2, bubble_y + 40), 
                             outline=(0, 0, 0), fill=(255, 255, 255), width=2)
                
                # Draw text
                draw.text((bubble_x - bubble_width//2 + 10, bubble_y - 10), 
                         f"{character}: {text}", fill=(0, 0, 0), font=font)
    
    # Add panel border
    draw.rectangle([(0, 0), (width-1, height-1)], outline=(0, 0, 0), width=3)
    
    # Add scene description as caption
    caption_font = ImageFont.load_default()
    caption_text = scene_description[:50] + "..." if len(scene_description) > 50 else scene_description
    draw.rectangle([(10, height-30), (width-10, height-5)], fill=(255, 255, 255), outline=(0, 0, 0))
    draw.text((15, height-25), caption_text, fill=(0, 0, 0), font=caption_font)
    
    # Save the panel
    os.makedirs('outputs', exist_ok=True)
    timestamp = int(time.time())
    panel_filename = f"panel_{timestamp}.png"
    panel_path = os.path.join('outputs', panel_filename)
    panel.save(panel_path)
    
    return panel_path, panel_filename