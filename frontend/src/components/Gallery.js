import React from 'react';

/**
 * Gallery component to display generated manga panels
 * @param {array} panels - Array of panel objects with image paths and dialogue
 */
const Gallery = ({ panels }) => {
  if (!panels || panels.length === 0) {
    return null;
  }

  return (
    <div className="gallery">
      <h2>Your Manga</h2>
      {panels.map((panel, index) => (
        <div key={index} className="panel">
          <img 
            src={panel.imagePath} 
            alt={`Panel ${index + 1}`} 
            className="panel-image" 
          />
          
          {panel.dialogue && panel.dialogue.length > 0 && (
            <div className="dialogue">
              {panel.dialogue.map((line, i) => (
                <p key={i}>
                  <strong>{line.character}:</strong> {line.text}
                </p>
              ))}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default Gallery;