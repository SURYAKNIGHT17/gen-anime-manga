import React, { useState, useEffect } from 'react';
import '../styles/app.css';

/**
 * BackgroundVideo component that randomly selects and plays an anime video clip
 * as a fullscreen background
 */
const BackgroundVideo = () => {
  // For demo purposes, we'll use a placeholder array of video names
  // In a real implementation, these would be actual video files in the public/videos folder
  const videoClips = ['clip1.mp4', 'clip2.mp4', 'clip3.mp4', 'clip4.mp4', 'clip5.mp4'];
  
  // Randomly select a video clip
  const [randomClip, setRandomClip] = useState('');
  
  useEffect(() => {
    // Select a random clip when component mounts
    const randomIndex = Math.floor(Math.random() * videoClips.length);
    setRandomClip(videoClips[randomIndex]);
  }, []);
  
  // If no clip is selected yet, return null
  if (!randomClip) return null;
  
  return (
    <div className="video-container">
      <video autoPlay muted loop className="bg-video">
        <source src={`/videos/${randomClip}`} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    </div>
  );
};

export default BackgroundVideo;