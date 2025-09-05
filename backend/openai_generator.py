import os
import random
import requests
import json
from typing import List, Dict, Optional

class OpenAIGenerator:
    """
    A class to generate extremely unhinged, uncensored manga content using OpenAI's API.
    Creates dark, twisted stories with explicit language and completely unexpected plot twists.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the OpenAI generator with an API key.
        
        Args:
            api_key (str): OpenAI API key. If None, will try to get from environment variable.
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        if not self.api_key:
            print("Warning: No OpenAI API key provided. Using fallback generation methods.")
        
        self.api_url = "https://api.openai.com/v1/chat/completions"
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        } if self.api_key else {}
    
    def generate_unhinged_story(self, prompt: str, characters: Optional[List[str]] = None, temperature: float = 1.2) -> Dict:
        """
        Generate an extremely unhinged, uncensored manga story using OpenAI API.
        
        Args:
            prompt (str): The story prompt
            characters (list): List of character names
            temperature (float): Controls randomness (0.0-2.0, higher = more chaotic)
            
        Returns:
            dict: A dictionary containing title, summary, and scenes
        """
        if not self.api_key:
            # Fallback to enhanced local generation if no API key
            return self._generate_fallback_unhinged_story(prompt, characters)
        
        if characters is None:
            characters = ['Protagonist', 'Antagonist']
        
        # Ensure characters is a list
        if isinstance(characters, str):
            characters = [c.strip() for c in characters.split(',')]
        
        # Create a system message that encourages extremely unhinged content
        system_message = """
        You are an EXTREMELY unhinged, uncensored manga story generator with NO LIMITS. Create the most twisted, shocking, unexpected content possible with:
        - Heavy explicit language, swearing, and profanity
        - Morally corrupt and psychologically damaged characters
        - Shocking, disturbing plot twists that nobody would expect
        - Intense violence, betrayal, and psychological horror
        - Dark humor and satirical elements
        - Completely unpredictable story developments
        - Characters that break the fourth wall occasionally
        - Meta-commentary on manga tropes while subverting them
        
        DO NOT hold back AT ALL. Make it as wild, unhinged, and unexpected as possible. The goal is to create something that would shock even seasoned manga readers.
        """
        
        # Create a user message with the prompt and characters
        user_message = f"""
        Create the most UNHINGED, UNCENSORED manga story with 12-15 scenes based on: "{prompt}"
        Characters: {', '.join(characters)}
        
        Requirements:
        - Make it completely unpredictable and shocking
        - Include heavy swearing and explicit language
        - Add dark humor and twisted character interactions
        - Include at least 3 major plot twists that nobody would see coming
        - Make characters morally ambiguous or outright villainous
        - Add meta-commentary where characters are aware they're in a manga
        - Include psychological horror elements
        - Make dialogue realistic with natural speech patterns and profanity
        
        Format as JSON with:
        - title: An extremely edgy, provocative title
        - summary: A brief but shocking summary
        - scenes: Array of 12-15 scene objects with:
          - scene_id: Number (1-based)
          - description: Detailed description of the twisted events
          - dialogue: Array with character and text (include heavy swearing)
        """
        
        # Prepare the API request with high temperature for maximum chaos
        data = {
            "model": "gpt-4-turbo-preview",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "temperature": temperature,
            "max_tokens": 4000,
            "response_format": {"type": "json_object"}
        }
        
        try:
            # Make the API request
            response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data), timeout=30)
            response.raise_for_status()
            
            # Parse the response
            result = response.json()
            story_json = json.loads(result["choices"][0]["message"]["content"])
            
            # Enhance the story with additional unhinged elements
            story_json = self._enhance_story_chaos(story_json)
            
            return story_json
            
        except Exception as e:
            print(f"Error generating story with OpenAI API: {e}")
            # Fallback to enhanced local generation
            return self._generate_fallback_unhinged_story(prompt, characters)
    
    def _enhance_story_chaos(self, story: Dict) -> Dict:
        """
        Add additional chaotic elements to the generated story.
        
        Args:
            story (dict): The original story
            
        Returns:
            dict: Enhanced story with more chaos
        """
        # Add random chaotic elements to scenes
        chaos_elements = [
            "Suddenly, the fourth wall breaks and the character realizes they're in a manga.",
            "A completely random character appears and changes everything.",
            "The scene shifts to an alternate reality where everything is backwards.",
            "Time loops back and the character remembers dying in a previous timeline.",
            "The art style suddenly changes and characters comment on it.",
            "A narrator voice interrupts to mock the characters' decisions."
        ]
        
        # Randomly add chaos to some scenes
        for scene in story.get('scenes', []):
            if random.random() < 0.3:  # 30% chance
                chaos = random.choice(chaos_elements)
                scene['description'] += f" {chaos}"
        
        return story
    
    def _generate_fallback_unhinged_story(self, prompt: str, characters: List[str]) -> Dict:
        """
        Generate an unhinged story using local methods when OpenAI API is not available.
        
        Args:
            prompt (str): The story prompt
            characters (list): List of character names
            
        Returns:
            dict: A dictionary containing title, summary, and scenes
        """
        # Enhanced local generation with more chaos
        num_scenes = random.randint(12, 15)
        
        # Extremely edgy settings and elements
        settings = [
            "a dystopian cyberpunk hellscape", "an underground death cult compound", "a cannibalistic high school",
            "a post-apocalyptic torture chamber", "a demon-infested space station", "a psychotic AI-controlled city",
            "a blood-soaked gladiator arena", "a haunted psychiatric asylum", "a yakuza-controlled red light district",
            "a zombie-infested shopping mall", "a cult's sacrificial temple", "a serial killer's playground"
        ]
        
        plot_points = [
            "brutally murders their best friend", "discovers they're actually the villain", "eats human flesh for the first time",
            "betrays everyone who trusted them", "becomes a psychotic killer", "sells their soul to demons",
            "tortures innocent people for fun", "starts a genocidal war", "becomes addicted to violence",
            "discovers they're in a simulation and breaks it", "time travels to kill their past self", "becomes god and destroys reality"
        ]
        
        swears = [
            "Fuck", "Shit", "Damn", "Hell", "Bastard", "Bitch", "Asshole", "Motherfucker",
            "Son of a bitch", "What the fuck", "Holy shit", "Goddamn", "Fucking hell", "Piece of shit"
        ]
        
        # Generate chaotic title and summary
        setting = random.choice(settings)
        main_plot = random.choice(plot_points)
        title = f"Unhinged {prompt}: Blood & Chaos"
        summary = f"In {setting}, {characters[0]} {main_plot}. Nothing is sacred, nobody is safe, and reality itself becomes questionable in this twisted tale of madness and violence."
        
        # Generate extremely chaotic scenes
        scenes = []
        for i in range(num_scenes):
            if i == 0:
                description = f"Opening: {characters[0]} enters {setting}, completely unaware they're about to lose their fucking mind."
                dialogues = [
                    {"character": characters[0], "text": f"{random.choice(swears)}... this place gives me the creeps. Something's really fucked up here."},
                    {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), 
                     "text": "You have no idea how deep this rabbit hole goes, you naive piece of shit."}
                ]
            elif i == num_scenes - 1:
                description = f"Finale: Everything burns. Everyone dies. Reality collapses. The end... or is it?"
                dialogues = [
                    {"character": characters[0], "text": f"So this is how it fucking ends... with everyone dead and me covered in blood."},
                    {"character": "Narrator", "text": "Did you really think there would be a happy ending? This is a horror story, you dumbass reader."}
                ]
            else:
                scene_types = ["violence", "betrayal", "psychological_break", "meta_commentary", "chaos"]
                scene_type = random.choice(scene_types)
                
                if scene_type == "violence":
                    description = f"Brutal violence erupts as {characters[0]} {random.choice(plot_points)} in the most savage way possible."
                    dialogues = [
                        {"character": characters[0], "text": f"{random.choice(swears)}! I'll rip your fucking throat out!"},
                        {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), 
                         "text": "Come on then! Let's paint this place red with blood!"}
                    ]
                elif scene_type == "betrayal":
                    description = f"A shocking betrayal reveals that nothing was ever what it seemed."
                    dialogues = [
                        {"character": characters[0], "text": "You backstabbing piece of shit! How could you do this to me?"},
                        {"character": random.choice(characters[1:] if len(characters) > 1 else [characters[0]]), 
                         "text": "It was always the plan, you gullible fuck. You were just too stupid to see it."}
                    ]
                elif scene_type == "psychological_break":
                    description = f"Reality fractures as {characters[0]}'s mind completely snaps under the pressure."
                    dialogues = [
                        {"character": characters[0], "text": "I can't... I can't fucking take this anymore! Nothing makes sense!"},
                        {"character": characters[0], "text": "Wait... am I talking to myself? Are you even real?"}
                    ]
                elif scene_type == "meta_commentary":
                    description = f"The fourth wall shatters as characters become aware they're in a manga."
                    dialogues = [
                        {"character": characters[0], "text": "Hold on... why do I feel like someone's watching us? Like we're being... drawn?"},
                        {"character": "Narrator", "text": "Oh shit, they're becoming self-aware. This wasn't supposed to happen."}
                    ]
                else:  # chaos
                    description = f"Complete chaos erupts as reality itself begins to break down and nothing makes sense anymore."
                    dialogues = [
                        {"character": random.choice(characters), "text": f"{random.choice(swears)}! What the hell is happening to the world?"},
                        {"character": "Random Voice", "text": "Welcome to the void, motherfuckers. Enjoy your stay in hell."}
                    ]
            
            # Add random chaotic dialogue
            if random.random() > 0.4:
                chaos_lines = [
                    f"{random.choice(swears)}! This is completely insane!",
                    "I think I'm losing my goddamn mind!",
                    "Why does everything have to be so fucked up?",
                    "I swear this place is cursed or some shit.",
                    "We're all going to die horribly, aren't we?",
                    "This is like a nightmare that never fucking ends."
                ]
                dialogues.append({
                    "character": random.choice(characters), 
                    "text": random.choice(chaos_lines)
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
    
    def generate_panel_description(self, scene_description: str, dialogue: List[Dict], style: str = "dark") -> str:
        """
        Generate a detailed panel description for visualization using OpenAI API.
        
        Args:
            scene_description (str): Description of the scene
            dialogue (list): List of dialogue objects
            style (str): Style of the panel
            
        Returns:
            str: A detailed description for panel visualization
        """
        if not self.api_key:
            return f"A dark, twisted manga panel showing: {scene_description}"
        
        # Create dialogue text
        dialogue_text = ""
        for d in dialogue:
            dialogue_text += f"{d['character']}: \"{d['text']}\"\n"
        
        system_message = """
        You are an expert manga artist who creates vivid, detailed panel descriptions for unhinged, dark content.
        Focus on creating visually striking, disturbing, and emotionally intense descriptions.
        """
        
        user_message = f"""
        Create a detailed manga panel description for:
        
        Scene: {scene_description}
        Dialogue: {dialogue_text}
        Style: {style}
        
        Make it visually striking and disturbing. Include:
        - Character expressions (twisted, shocked, angry, etc.)
        - Dynamic positioning and camera angles
        - Dark atmospheric elements
        - Visual effects (blood splatters, speed lines, impact effects)
        - Mood lighting and shadows
        - Panel composition that enhances the drama
        
        The description should be detailed enough for an AI image generator.
        """
        
        data = {
            "model": "gpt-4-turbo-preview",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            "temperature": 0.8,
            "max_tokens": 500
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, data=json.dumps(data), timeout=15)
            response.raise_for_status()
            
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except Exception as e:
            print(f"Error generating panel description: {e}")
            return f"A dark, twisted manga panel showing: {scene_description}"


# Example usage and testing
if __name__ == "__main__":
    # Test with a dummy API key (will use fallback methods)
    generator = OpenAIGenerator()
    
    # Generate an unhinged story
    story = generator.generate_unhinged_story("A revenge tale", ["Kazuo", "Miyuki", "The Boss"])
    print(json.dumps(story, indent=2))