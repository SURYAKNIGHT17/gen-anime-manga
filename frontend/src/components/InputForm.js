import React, { useState } from 'react';

/**
 * InputForm component for story prompt and character input
 * @param {function} onSubmit - Function to handle form submission
 */
const InputForm = ({ onSubmit }) => {
  const [prompt, setPrompt] = useState('');
  const [characters, setCharacters] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    
    // Split characters by comma
    const characterList = characters
      .split(',')
      .map(char => char.trim())
      .filter(char => char !== '');
    
    // Call the onSubmit function with form data
    await onSubmit({ prompt, characters: characterList });
    setIsLoading(false);
  };

  return (
    <div className="form-container">
      <h2>Create Your Manga</h2>
      <form onSubmit={handleSubmit}>
        <div className="input-group">
          <label className="input-label">Story Prompt</label>
          <textarea
            className="input-field"
            value={prompt}
            onChange={(e) => setPrompt(e.target.value)}
            placeholder="Enter your story idea (e.g., A hero's journey in a cyberpunk world)"
            rows={4}
            required
          />
        </div>
        
        <div className="input-group">
          <label className="input-label">Characters</label>
          <input
            type="text"
            className="input-field"
            value={characters}
            onChange={(e) => setCharacters(e.target.value)}
            placeholder="Enter character names separated by commas (e.g., Cyber ninja, AI companion)"
          />
        </div>
        
        <button 
          type="submit" 
          className="btn btn-primary"
          disabled={isLoading}
        >
          {isLoading ? 'Generating...' : 'Generate Manga'}
        </button>
      </form>
    </div>
  );
};

export default InputForm;