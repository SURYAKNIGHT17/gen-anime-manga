"""
NLP Engine for story generation.
Simplified version without external AI dependencies.
"""
import os
import random

# Set random seed for reproducibility
random.seed(42)

def generate_story(prompt, characters=None):
    """
    Generate a story based on user prompt and characters.
    
    Args:
        prompt (str): The story prompt from the user
        characters (list): List of character descriptions
        
    Returns:
        list: List of scene dictionaries with text and dialogue
    """
    # In a production environment, we would load a fine-tuned model
    # For this demo, we'll simulate the response
    
    # Placeholder for actual model generation
    # In a real implementation, you would use:
    # generator = pipeline('text-generation', model='gpt2')
    # story = generator(prompt, max_length=1000, num_return_sequences=1)
    
    # Simulate story generation
    character_context = ""
    if characters:
        character_context = "Characters: " + ", ".join(characters)
    
    # Simulate a multi-scene story
    scenes = [
        {
            "scene_id": 1,
            "description": f"Opening scene based on: {prompt}",
            "dialogue": [
                {"character": "Character 1", "text": "This is the beginning of our adventure!"},
                {"character": "Character 2", "text": "I wonder what awaits us..."}
            ]
        },
        {
            "scene_id": 2,
            "description": "The characters encounter their first challenge",
            "dialogue": [
                {"character": "Character 1", "text": "Look out! There's danger ahead!"},
                {"character": "Character 2", "text": "We need to be careful here."}
            ]
        },
        {
            "scene_id": 3,
            "description": "The resolution of the story",
            "dialogue": [
                {"character": "Character 1", "text": "We did it! We overcame the challenge!"},
                {"character": "Character 2", "text": "This is just the beginning of our story."}
            ]
        }
    ]
    
    return scenes