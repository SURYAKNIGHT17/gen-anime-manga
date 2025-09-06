"""NLP Engine for story generation.
Enhanced version with better text processing and AI integration.
"""
import os
import random
import re
import logging
from typing import List, Dict, Optional
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Set random seed for reproducibility
random.seed(42)

class StoryAnalyzer:
    """
    Analyzes and processes story elements for better generation.
    """
    
    def __init__(self):
        # Story genre keywords
        self.genre_keywords = {
            'action': ['fight', 'battle', 'combat', 'war', 'conflict', 'violence', 'chase', 'escape'],
            'romance': ['love', 'relationship', 'heart', 'kiss', 'date', 'romantic', 'passion', 'affection'],
            'mystery': ['mystery', 'detective', 'crime', 'murder', 'investigation', 'clue', 'secret', 'hidden'],
            'fantasy': ['magic', 'wizard', 'dragon', 'spell', 'enchanted', 'mystical', 'supernatural', 'realm'],
            'horror': ['horror', 'scary', 'fear', 'nightmare', 'ghost', 'demon', 'terror', 'haunted'],
            'comedy': ['funny', 'humor', 'joke', 'laugh', 'comedy', 'amusing', 'hilarious', 'witty'],
            'drama': ['emotional', 'tragedy', 'serious', 'dramatic', 'intense', 'conflict', 'struggle'],
            'sci-fi': ['space', 'future', 'technology', 'robot', 'alien', 'cyberpunk', 'dystopian', 'utopian']
        }
        
        # Emotion keywords for dialogue generation
        self.emotion_keywords = {
            'angry': ['furious', 'rage', 'mad', 'irritated', 'annoyed', 'hostile'],
            'sad': ['depressed', 'melancholy', 'sorrowful', 'grief', 'despair', 'heartbroken'],
            'happy': ['joyful', 'cheerful', 'excited', 'delighted', 'euphoric', 'content'],
            'fearful': ['scared', 'terrified', 'anxious', 'worried', 'nervous', 'panicked'],
            'surprised': ['shocked', 'amazed', 'astonished', 'stunned', 'bewildered'],
            'determined': ['resolute', 'focused', 'committed', 'driven', 'persistent']
        }
    
    def analyze_prompt(self, prompt: str) -> Dict:
        """
        Analyze the prompt to extract genre, themes, and emotional tone.
        
        Args:
            prompt (str): The story prompt
            
        Returns:
            dict: Analysis results
        """
        prompt_lower = prompt.lower()
        words = re.findall(r'\b\w+\b', prompt_lower)
        
        # Detect genres
        genre_scores = {}
        for genre, keywords in self.genre_keywords.items():
            score = sum(1 for word in words if word in keywords)
            if score > 0:
                genre_scores[genre] = score
        
        primary_genre = max(genre_scores.keys(), key=genre_scores.get) if genre_scores else 'drama'
        
        # Detect emotions
        emotion_scores = {}
        for emotion, keywords in self.emotion_keywords.items():
            score = sum(1 for word in words if word in keywords)
            if score > 0:
                emotion_scores[emotion] = score
        
        primary_emotion = max(emotion_scores.keys(), key=emotion_scores.get) if emotion_scores else 'neutral'
        
        # Extract key themes
        themes = [word for word in words if len(word) > 4 and word not in ['story', 'about', 'character']]
        
        return {
            'primary_genre': primary_genre,
            'genres': genre_scores,
            'primary_emotion': primary_emotion,
            'emotions': emotion_scores,
            'themes': themes[:5],  # Top 5 themes
            'word_count': len(words)
        }
    
    def generate_character_traits(self, character_name: str, genre: str) -> Dict:
        """
        Generate character traits based on genre.
        
        Args:
            character_name (str): Name of the character
            genre (str): Story genre
            
        Returns:
            dict: Character traits
        """
        genre_traits = {
            'action': ['brave', 'strong', 'determined', 'skilled', 'fearless'],
            'romance': ['charming', 'passionate', 'caring', 'romantic', 'sensitive'],
            'mystery': ['observant', 'intelligent', 'analytical', 'suspicious', 'methodical'],
            'fantasy': ['magical', 'wise', 'mystical', 'powerful', 'ancient'],
            'horror': ['haunted', 'troubled', 'paranoid', 'survivor', 'cursed'],
            'comedy': ['funny', 'witty', 'clumsy', 'optimistic', 'cheerful'],
            'drama': ['complex', 'emotional', 'conflicted', 'deep', 'troubled'],
            'sci-fi': ['technological', 'futuristic', 'logical', 'innovative', 'alien']
        }
        
        traits = random.sample(genre_traits.get(genre, ['interesting', 'unique']), 3)
        
        return {
            'name': character_name,
            'traits': traits,
            'primary_trait': traits[0] if traits else 'mysterious'
        }

def enhance_dialogue(text: str, emotion: str, character_traits: List[str]) -> str:
    """
    Enhance dialogue based on emotion and character traits.
    
    Args:
        text (str): Original dialogue text
        emotion (str): Character's current emotion
        character_traits (list): Character's personality traits
        
    Returns:
        str: Enhanced dialogue
    """
    # Emotion-based modifications
    emotion_modifiers = {
        'angry': ['Damn it!', 'This is ridiculous!', 'I can\'t believe this!'],
        'sad': ['*sighs*', 'I just... I don\'t know anymore.', 'Why does this always happen?'],
        'happy': ['This is amazing!', 'I can\'t contain my excitement!', 'Everything\'s perfect!'],
        'fearful': ['I\'m scared...', 'What if something goes wrong?', 'I have a bad feeling about this.'],
        'surprised': ['What?!', 'I can\'t believe it!', 'That\'s impossible!'],
        'determined': ['I won\'t give up!', 'We can do this!', 'Nothing will stop me!']
    }
    
    # Add emotion-based prefix occasionally
    if random.random() < 0.3 and emotion in emotion_modifiers:
        prefix = random.choice(emotion_modifiers[emotion])
        text = f"{prefix} {text}"
    
    # Trait-based modifications
    if 'witty' in character_traits and random.random() < 0.2:
        text += " *smirks*"
    elif 'serious' in character_traits and random.random() < 0.2:
        text = text.replace('!', '.')
    
    return text

def generate_story(prompt: str, characters: Optional[List[str]] = None) -> List[Dict]:
    """
    Generate an enhanced story based on user prompt and characters.
    
    Args:
        prompt (str): The story prompt from the user
        characters (list): List of character names
        
    Returns:
        list: List of scene dictionaries with enhanced text and dialogue
    """
    logger.info(f"Generating story for prompt: {prompt[:50]}...")
    
    # Initialize analyzer
    analyzer = StoryAnalyzer()
    
    # Analyze the prompt
    analysis = analyzer.analyze_prompt(prompt)
    logger.info(f"Detected genre: {analysis['primary_genre']}, emotion: {analysis['primary_emotion']}")
    
    # Set up characters
    if not characters:
        characters = ['Protagonist', 'Deuteragonist']
    elif isinstance(characters, str):
        characters = [c.strip() for c in characters.split(',')]
    
    # Generate character profiles
    character_profiles = {}
    for char in characters:
        character_profiles[char] = analyzer.generate_character_traits(char, analysis['primary_genre'])
    
    # Generate story structure based on genre
    genre = analysis['primary_genre']
    num_scenes = random.randint(8, 12)
    
    # Genre-specific story templates
    story_templates = {
        'action': {
            'opening': 'A tense situation unfolds',
            'rising': 'The conflict escalates dramatically',
            'climax': 'An intense battle determines the outcome',
            'resolution': 'The dust settles and consequences are revealed'
        },
        'romance': {
            'opening': 'Two characters meet under interesting circumstances',
            'rising': 'Their relationship develops with complications',
            'climax': 'A moment of truth tests their bond',
            'resolution': 'Their feelings are finally resolved'
        },
        'mystery': {
            'opening': 'A puzzling event occurs',
            'rising': 'Clues are discovered and suspects emerge',
            'climax': 'The truth is dramatically revealed',
            'resolution': 'Justice is served and mysteries are solved'
        },
        'fantasy': {
            'opening': 'A magical world is introduced',
            'rising': 'Ancient powers awaken and quests begin',
            'climax': 'Epic magical confrontation',
            'resolution': 'The realm\'s fate is decided'
        }
    }
    
    template = story_templates.get(genre, story_templates['action'])
    
    # Generate scenes
    scenes = []
    for i in range(num_scenes):
        scene_type = 'opening' if i == 0 else 'resolution' if i == num_scenes - 1 else 'rising' if i < num_scenes * 0.7 else 'climax'
        
        # Generate scene description
        if scene_type in template:
            base_description = template[scene_type]
        else:
            base_description = "The story continues to unfold"
        
        description = f"{base_description} as {prompt} develops further. {random.choice(analysis['themes']) if analysis['themes'] else 'The plot'} becomes central to the narrative."
        
        # Generate dialogue
        dialogue = []
        num_dialogues = random.randint(2, 4)
        
        for j in range(num_dialogues):
            speaker = random.choice(characters)
            char_profile = character_profiles[speaker]
            
            # Generate contextual dialogue based on scene and character
            dialogue_options = {
                'opening': [
                    f"Something about this {random.choice(analysis['themes']) if analysis['themes'] else 'situation'} feels different.",
                    "I have a feeling our lives are about to change.",
                    "This is either the beginning of something great or terrible."
                ],
                'rising': [
                    "Things are getting more complicated than I expected.",
                    "We need to be careful about our next move.",
                    "I'm starting to understand what's really happening here."
                ],
                'climax': [
                    "This is it - everything comes down to this moment!",
                    "I won't let everything we've worked for be destroyed!",
                    "The truth changes everything!"
                ],
                'resolution': [
                    "Finally, we can see the bigger picture.",
                    "This ending is just a new beginning.",
                    "We've learned so much from this experience."
                ]
            }
            
            base_text = random.choice(dialogue_options.get(scene_type, dialogue_options['rising']))
            enhanced_text = enhance_dialogue(base_text, analysis['primary_emotion'], char_profile['traits'])
            
            dialogue.append({
                "character": speaker,
                "text": enhanced_text
            })
        
        scenes.append({
            "scene_id": i + 1,
            "description": description,
            "dialogue": dialogue,
            "scene_type": scene_type,
            "genre": genre
        })
    
    logger.info(f"Generated {len(scenes)} scenes for {genre} story")
    return scenes

def extract_keywords(text: str) -> List[str]:
    """
    Extract important keywords from text for better processing.
    
    Args:
        text (str): Input text
        
    Returns:
        list: List of important keywords
    """
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
    
    # Extract words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out stop words and short words
    keywords = [word for word in words if word not in stop_words and len(word) > 3]
    
    # Return most common keywords
    word_counts = Counter(keywords)
    return [word for word, count in word_counts.most_common(10)]

def analyze_sentiment(text: str) -> str:
    """
    Simple sentiment analysis for text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Sentiment (positive, negative, neutral)
    """
    positive_words = ['good', 'great', 'excellent', 'amazing', 'wonderful', 'fantastic', 'love', 'like', 'happy', 'joy', 'success', 'win', 'victory']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'hate', 'dislike', 'sad', 'angry', 'fear', 'fail', 'loss', 'defeat', 'wrong']
    
    words = re.findall(r'\b\w+\b', text.lower())
    
    positive_score = sum(1 for word in words if word in positive_words)
    negative_score = sum(1 for word in words if word in negative_words)
    
    if positive_score > negative_score:
        return 'positive'
    elif negative_score > positive_score:
        return 'negative'
    else:
        return 'neutral'