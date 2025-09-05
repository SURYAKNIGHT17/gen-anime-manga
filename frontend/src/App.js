import React, { useState } from 'react';
import BackgroundVideo from './components/BackgroundVideo';
import InputForm from './components/InputForm';
import Gallery from './components/Gallery';
import DownloadButton from './components/DownloadButton';
import './styles/app.css';

/**
 * Main App component for the Manga Creator application
 */
function App() {
  const [panels, setPanels] = useState([]);
  const [title, setTitle] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  /**
   * Handle form submission and generate manga
   * @param {object} formData - Form data with prompt and characters
   */
  const handleSubmit = async (formData) => {
    setIsLoading(true);
    
    try {
      // Step 1: Generate story
      const storyResponse = await fetch('/api/story/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });
      
      if (!storyResponse.ok) {
        throw new Error('Failed to generate story');
      }
      
      const storyData = await storyResponse.json();
      
      // Step 2: Generate panels for each scene
      const generatedPanels = [];
      
      for (const scene of storyData.scenes) {
        const panelResponse = await fetch('/api/generate/panel', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            scene: scene.description,
            characters: formData.characters,
            style: 'manga'
          })
        });
        
        if (!panelResponse.ok) {
          throw new Error('Failed to generate panel');
        }
        
        const panelData = await panelResponse.json();
        
        generatedPanels.push({
          imagePath: panelData.panel_path,
          dialogue: scene.dialogue
        });
      }
      
      // Update state with generated panels
      setPanels(generatedPanels);
      setTitle(formData.prompt);
    } catch (error) {
      console.error('Error generating manga:', error);
      alert('Failed to generate manga. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <BackgroundVideo />
      
      <div className="container">
        <header>
          <h1>Anime Manga Creator</h1>
          <p>Create your own manga with AI-powered story and image generation</p>
        </header>
        
        <InputForm onSubmit={handleSubmit} />
        
        {isLoading && (
          <div className="loading">
            <p>Generating your manga... Please wait.</p>
          </div>
        )}
        
        <Gallery panels={panels} />
        
        <DownloadButton panels={panels} title={title} />
      </div>
    </div>
  );
}

export default App;