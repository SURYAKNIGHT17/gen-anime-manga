import React, { useState } from 'react';

/**
 * DownloadButton component for exporting manga as PDF/CBZ
 * @param {array} panels - Array of panel objects
 * @param {string} title - Title of the manga
 */
const DownloadButton = ({ panels, title }) => {
  const [isLoading, setIsLoading] = useState(false);
  const [format, setFormat] = useState('pdf');

  // Don't render if no panels
  if (!panels || panels.length === 0) {
    return null;
  }

  const handleDownload = async () => {
    setIsLoading(true);
    
    try {
      // Prepare data for API request
      const data = {
        panels: panels.map(panel => ({
          path: panel.imagePath,
          dialogue: panel.dialogue || []
        })),
        title: title || 'My Manga'
      };
      
      // Call the appropriate API endpoint based on format
      const endpoint = format === 'pdf' ? '/api/export/pdf' : '/api/export/cbz';
      
      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
      
      if (!response.ok) {
        throw new Error('Failed to generate file');
      }
      
      const result = await response.json();
      
      // Trigger download
      if (result.status === 'success') {
        const downloadUrl = `/api/export/download/${format}/${result[`${format}_path`].split('/').pop()}`;
        window.open(downloadUrl, '_blank');
      }
    } catch (error) {
      console.error('Download error:', error);
      alert('Failed to download manga. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="download-container">
      <div>
        <select 
          value={format} 
          onChange={(e) => setFormat(e.target.value)}
          className="input-field"
          style={{ marginRight: '10px', width: 'auto' }}
        >
          <option value="pdf">PDF</option>
          <option value="cbz">CBZ (Comic Book)</option>
        </select>
        
        <button 
          onClick={handleDownload} 
          className="btn btn-download"
          disabled={isLoading}
        >
          {isLoading ? 'Generating...' : `Download as ${format.toUpperCase()}`}
        </button>
      </div>
    </div>
  );
};

export default DownloadButton;