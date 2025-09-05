import random
from typing import List, Dict
from openai_generator import OpenAIGenerator

def generate_manga_story(prompt: str = "A mysterious adventure", characters: List[str] = None, unhinged: bool = False) -> Dict:
    """
    Generate a manga story with 10-15 scenes.
    
    Args:
        prompt (str): The story prompt
        characters (list): List of character names
        unhinged (bool): Whether to generate unhinged, uncensored content
        
    Returns:
        dict: A dictionary containing title, summary, and scenes
    """
    if characters is None:
        characters = ['Protagonist', 'Antagonist']
    
    # Ensure characters is a list
    if isinstance(characters, str):
        characters = [c.strip() for c in characters.split(',')]
    
    # Use OpenAI generator for unhinged content
    if unhinged:
        try:
            openai_gen = OpenAIGenerator()
            return openai_gen.generate_unhinged_story(prompt, characters)
        except Exception as e:
            print(f"Error with OpenAI generator: {e}")
            # Fall back to enhanced local generation
            return _generate_enhanced_local_story(prompt, characters, unhinged=True)
    else:
        return _generate_enhanced_local_story(prompt, characters, unhinged=False)

def _generate_enhanced_local_story(prompt: str, characters: List[str], unhinged: bool = False) -> Dict:
    """
    Generate a story using enhanced local methods.
    
    Args:
        prompt (str): The story prompt
        characters (list): List of character names
        unhinged (bool): Whether to make content more edgy
        
    Returns:
        dict: A dictionary containing title, summary, and scenes
    """
    num_scenes = random.randint(10, 15)
    
    if unhinged:
        # Enhanced edgy content for local generation
        settings = [
            "a dystopian underground facility", "a blood-soaked battlefield", "a corrupt corporate tower",
            "a lawless wasteland", "a twisted psychological experiment", "a criminal underworld",
            "a post-apocalyptic city", "a dark web of conspiracies", "a violent gang territory",
            "a morally bankrupt institution", "a hellish nightmare realm", "a savage survival arena"
        ]
        
        plot_points = [
            "brutally confronts their demons", "makes a morally questionable choice", "betrays someone close",
            "discovers a horrifying truth", "commits an unforgivable act", "loses their humanity",
            "embraces their dark side", "destroys everything they love", "becomes the villain",
            "breaks every rule", "crosses the point of no return", "faces ultimate corruption"
        ]
        
        emotions = [
            "ruthlessly determined", "psychologically broken", "violently angry", "desperately hopeful",
            "dangerously unstable", "morally conflicted", "coldly calculating", "deeply traumatized",
            "savagely vengeful", "completely unhinged", "darkly amused", "brutally honest"
        ]
        
        swears = [
            "damn", "hell", "shit", "fuck", "bastard", "bitch", "asshole", "motherfucker",
            "son of a bitch", "what the fuck", "holy shit", "goddamn", "fucking hell", "piece of shit"
        ]
        
        # Generate edgy title and summary
        setting = random.choice(settings)
        main_plot = random.choice(plot_points)
        title = f"{prompt}: {random.choice(['Blood & Betrayal', 'Chaos Unleashed', 'Dark Descent', 'Savage Truth', 'Broken Souls'])}"
        summary = f"In {setting}, {characters[0]} {main_plot}. A brutal tale where morality is a luxury and survival demands sacrifice."
        
        # Enhanced dialogue templates for edgy content
        dialogue_templates = {
            "ruthlessly determined": ["I'll do whatever it takes, no matter who gets hurt.", "Mercy is a weakness I can't afford."],
            "psychologically broken": ["I can't tell what's real anymore...", "The voices won't stop..."],
            "violently angry": ["I'll tear this whole place apart!", "Someone's going to pay for this!"],
            "desperately hopeful": ["There has to be another way... please...", "I refuse to believe it's hopeless."],
            "dangerously unstable": ["Haha... this is getting interesting...", "Let's see how far we can push this."],
            "morally conflicted": ["Is this who I've become?", "When did I stop caring about right and wrong?"]
        }
        
    else:
        # Original enhanced story elements for regular content
        settings = [
            "a mysterious academy", "an ancient temple", "a futuristic city", "a haunted mansion",
            "a magical forest", "an underground laboratory", "a floating island", "a cyberpunk district",
            "a desert oasis", "a mountain peak", "a space station", "a medieval castle"
        ]
        
        plot_points = [
            "discovers a hidden power", "faces their greatest fear", "betrays a trusted ally",
            "uncovers a dark secret", "makes an impossible choice", "confronts their past",
            "saves an enemy", "loses everything", "gains new allies", "breaks an ancient curse",
            "travels through time", "enters another dimension"
        ]
        
        emotions = [
            "determined", "conflicted", "angry", "hopeful", "desperate", "confused",
            "triumphant", "sorrowful", "fearful", "excited", "nostalgic", "vengeful"
        ]
        
        # Generate dynamic title and summary
        setting = random.choice(settings)
        main_plot = random.choice(plot_points)
        title = f"Chronicles of {prompt}: {random.choice(['Awakening', 'Destiny', 'Legacy', 'Revolution', 'Eclipse'])}"
        summary = f"In {setting}, {characters[0]} {main_plot}. A tale of courage, mystery, and the bonds that define us."
        
        # Regular dialogue templates
        dialogue_templates = {
            "determined": ["I won't give up, no matter what!", "This is what I've been training for."],
            "conflicted": ["I don't know what's right anymore...", "How can I choose between them?"],
            "angry": ["You've gone too far this time!", "I'll make you pay for what you've done!"],
            "hopeful": ["Maybe there's still a chance...", "I believe we can find another way."],
            "desperate": ["Please, there has to be something we can do!", "I'm running out of options..."],
            "fearful": ["What if we're too late?", "I've never been so scared in my life..."]
        }
    
    # Generate varied scenes
    scenes = []
    for i in range(num_scenes):
        if i == 0:
            # Opening scene
            if unhinged:
                description = f"Opening: {characters[0]} enters {setting}, unaware they're about to descend into hell."
                dialogues = [
                    {"character": characters[0], "text": f"Something's seriously {random.choice(['fucked up', 'wrong', 'off'])} with this place..."},
                    {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), "text": "You have no idea what you've gotten yourself into, you naive bastard."}
                ]
            else:
                description = f"Opening: {characters[0]} arrives at {setting}, sensing that their life is about to change forever."
                dialogues = [
                    {"character": characters[0], "text": "Something feels different about this place... like it's been waiting for me."},
                    {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), "text": "You're more perceptive than I thought. Welcome to your destiny."}
                ]
        elif i == num_scenes - 1:
            # Final scene
            if unhinged:
                description = f"Finale: The brutal truth is revealed and {characters[0]} must choose between their soul and survival."
                dialogues = [
                    {"character": characters[0], "text": f"So this is what I've become... a {random.choice(['monster', 'killer', 'piece of shit'])}."},
                    {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), "text": "Welcome to reality, asshole. Now you understand the price of power."}
                ]
            else:
                description = f"Finale: The truth is revealed and {characters[0]} must make the ultimate choice that will determine everyone's fate."
                dialogues = [
                    {"character": characters[0], "text": "Now I understand... everything led to this moment."},
                    {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), "text": "The choice is yours. What kind of future will you create?"}
                ]
        else:
            # Middle scenes with variety
            current_emotion = random.choice(emotions)
            current_plot = random.choice(plot_points)
            description = f"Scene {i+1}: Feeling {current_emotion}, {characters[0]} {current_plot} while navigating the challenges ahead."
            
            # Generate contextual dialogue
            main_dialogue = random.choice(dialogue_templates.get(current_emotion, ["Let's see what happens next."]))
            
            # Add swearing to unhinged dialogue
            if unhinged and random.random() > 0.5:
                swear = random.choice(swears)
                if not any(s in main_dialogue.lower() for s in ['damn', 'hell', 'shit', 'fuck']):
                    main_dialogue = f"{swear.capitalize()}, {main_dialogue.lower()}"
            
            if unhinged:
                response_options = [
                    "The game is rigged, but we're still playing like idiots.",
                    "Morality is a luxury we can't fucking afford.",
                    "Everyone has a breaking point, and we're way past ours.",
                    "Trust is the first casualty of this shitshow.",
                    "Sometimes the hero and villain are the same damn person.",
                    "We're all going to hell, might as well enjoy the ride.",
                    "Survival makes monsters of us all."
                ]
            else:
                response_options = [
                    "The path ahead won't be easy, but we'll face it together.",
                    "Every challenge makes us stronger.",
                    "Hope is what keeps us going.",
                    "We'll find a way, we always do.",
                    "Together, we can overcome anything."
                ]
            
            dialogues = [
                {"character": characters[0], "text": main_dialogue},
                {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), "text": random.choice(response_options)}
            ]
            
            # Add occasional third dialogue for more depth
            if random.random() > 0.6:
                if unhinged:
                    extra_lines = [
                        "The line between hero and villain is thinner than you think.",
                        "Everyone's got blood on their hands now.",
                        "Survival changes people in fucked up ways.",
                        "The system is broken, and we're the damn glitch.",
                        "Sometimes the only way out is through hell itself.",
                        "We've crossed lines we can never uncross.",
                        "This world doesn't give a shit about good intentions."
                    ]
                else:
                    extra_lines = [
                        "The stakes have never been higher.",
                        "Everything we've worked for depends on this.",
                        "I can feel the power growing stronger.",
                        "The enemy is closer than we thought.",
                        "Time is running out."
                    ]
                dialogues.append({
                    "character": random.choice(characters), 
                    "text": random.choice(extra_lines)
                })
        
        scenes.append({
            "scene_id": i + 1,
            "description": description,
            "dialogue": dialogues
        })
    
    return {
        "title": title,
        "summary": summary,
        "scenes": scenes
    }

# Test function
if __name__ == "__main__":
    # Test regular story
    print("=== REGULAR STORY ===")
    regular_story = generate_manga_story("A revenge tale", ["Kazuo", "Miyuki"], unhinged=False)
    print(f"Title: {regular_story['title']}")
    print(f"Summary: {regular_story['summary']}")
    print(f"Scenes: {len(regular_story['scenes'])}")
    
    print("\n=== UNHINGED STORY ===")
    unhinged_story = generate_manga_story("A revenge tale", ["Kazuo", "Miyuki"], unhinged=True)
    print(f"Title: {unhinged_story['title']}")
    print(f"Summary: {unhinged_story['summary']}")
    print(f"Scenes: {len(unhinged_story['scenes'])}")