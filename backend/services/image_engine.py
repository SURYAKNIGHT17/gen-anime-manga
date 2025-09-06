"""Image Engine for manga panel generation.
Uses Stable Diffusion for image generation.
"""
import os
import time
import torch
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from compel import Compel
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Global pipeline variable to avoid reloading
_pipeline = None
_compel = None

def _initialize_pipeline():
    """
    Initialize the Stable Diffusion pipeline.
    
    Returns:
        tuple: (pipeline, compel) objects
    """
    global _pipeline, _compel
    
    if _pipeline is None:
        try:
            logger.info("Initializing Stable Diffusion pipeline...")
            
            # Check if CUDA is available
            device = "cuda" if torch.cuda.is_available() else "cpu"
            logger.info(f"Using device: {device}")
            
            # Load the pipeline with optimizations
            model_id = "runwayml/stable-diffusion-v1-5"
            _pipeline = StableDiffusionPipeline.from_pretrained(
                model_id,
                torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            
            # Use DPM++ scheduler for better quality
            _pipeline.scheduler = DPMSolverMultistepScheduler.from_config(_pipeline.scheduler.config)
            
            # Move to device
            _pipeline = _pipeline.to(device)
            
            # Enable memory efficient attention if available
            if hasattr(_pipeline, "enable_xformers_memory_efficient_attention"):
                try:
                    _pipeline.enable_xformers_memory_efficient_attention()
                    logger.info("Enabled xformers memory efficient attention")
                except Exception as e:
                    logger.warning(f"Could not enable xformers: {e}")
            
            # Enable CPU offload for memory efficiency
            if device == "cuda":
                _pipeline.enable_model_cpu_offload()
            
            # Initialize Compel for better prompt handling
            _compel = Compel(tokenizer=_pipeline.tokenizer, text_encoder=_pipeline.text_encoder)
            
            logger.info("Pipeline initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize pipeline: {e}")
            _pipeline = None
            _compel = None
    
    return _pipeline, _compel

def _create_fallback_image(scene_description, characters, style, output_path):
    """
    Create a fallback image when Stable Diffusion is not available.
    
    Args:
        scene_description (str): Description of the scene
        characters (list): List of character descriptions
        style (str): Art style
        output_path (str): Path to save the image
    """
    logger.warning("Creating fallback image - Stable Diffusion not available")
    
    # Create a more sophisticated placeholder
    width, height = 768, 512
    
    # Create a gradient background
    image = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(image)
    
    # Create gradient background
    for y in range(height):
        color_value = int(30 + (y / height) * 50)
        draw.line([(0, y), (width, y)], fill=(color_value, color_value//2, color_value//3))
    
    # Add border
    draw.rectangle([(5, 5), (width-5, height-5)], outline='white', width=3)
    
    # Load font
    try:
        title_font = ImageFont.truetype("arial.ttf", 24)
        text_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
    
    # Add title
    draw.text((20, 20), "MANGA PANEL", fill='white', font=title_font)
    
    # Add scene description (wrapped)
    y_offset = 60
    max_width = width - 40
    words = scene_description.split()
    lines = []
    current_line = []
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        bbox = draw.textbbox((0, 0), test_line, font=text_font)
        if bbox[2] <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
                current_line = [word]
            else:
                lines.append(word)
    
    if current_line:
        lines.append(' '.join(current_line))
    
    for line in lines[:6]:  # Limit to 6 lines
        draw.text((20, y_offset), line, fill='lightgray', font=text_font)
        y_offset += 25
    
    # Add characters info
    if characters:
        y_offset += 20
        draw.text((20, y_offset), f"Characters: {', '.join(characters[:3])}", fill='yellow', font=text_font)
        y_offset += 25
    
    # Add style info
    draw.text((20, y_offset), f"Style: {style}", fill='cyan', font=text_font)
    
    # Add watermark
    draw.text((width-200, height-30), "Generated by AI Manga Creator", fill='gray', font=text_font)
    
    image.save(output_path)
    logger.info(f"Fallback image saved to {output_path}")

def generate_panel(scene_description, characters=None, style="manga"):
    """
    Generate a manga panel based on scene description using Stable Diffusion.
    
    Args:
        scene_description (str): Description of the scene
        characters (list): List of character descriptions
        style (str): Art style (manga, anime, etc.)
        
    Returns:
        str: Path to the generated panel image
    """
    # Create outputs directory if it doesn't exist
    os.makedirs("outputs", exist_ok=True)
    
    # Generate a unique filename
    timestamp = int(time.time())
    filename = f"panel_{timestamp}.png"
    output_path = os.path.join("outputs", filename)
    
    # Initialize pipeline
    pipeline, compel = _initialize_pipeline()
    
    if pipeline is None:
        # Fallback to placeholder image
        _create_fallback_image(scene_description, characters, style, output_path)
        return output_path
    
    try:
        # Construct the prompt
        character_desc = ""
        if characters:
            character_desc = f"featuring {', '.join(characters)}, "
        
        # Enhanced prompt for manga style
        prompt = f"{scene_description}, {character_desc}{style} style, high quality, detailed, dramatic lighting, manga panel, black and white, ink drawing, dynamic composition"
        
        # Negative prompt to avoid unwanted elements
        negative_prompt = "blurry, low quality, distorted, ugly, bad anatomy, extra limbs, text, watermark, signature, copyright, logo, realistic photo"
        
        logger.info(f"Generating image with prompt: {prompt[:100]}...")
        
        # Use Compel for better prompt handling if available
        if compel:
            conditioning = compel.build_conditioning_tensor(prompt)
            negative_conditioning = compel.build_conditioning_tensor(negative_prompt)
            
            # Generate image
            with torch.inference_mode():
                image = pipeline(
                    prompt_embeds=conditioning,
                    negative_prompt_embeds=negative_conditioning,
                    height=512,
                    width=768,
                    num_inference_steps=25,
                    guidance_scale=7.5,
                    generator=torch.Generator().manual_seed(42)
                ).images[0]
        else:
            # Fallback to regular generation
            with torch.inference_mode():
                image = pipeline(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    height=512,
                    width=768,
                    num_inference_steps=25,
                    guidance_scale=7.5,
                    generator=torch.Generator().manual_seed(42)
                ).images[0]
        
        # Save the image
        image.save(output_path)
        logger.info(f"Image generated successfully: {output_path}")
        
        return output_path
        
    except Exception as e:
        logger.error(f"Error generating image: {e}")
        # Fallback to placeholder image
        _create_fallback_image(scene_description, characters, style, output_path)
        return output_path