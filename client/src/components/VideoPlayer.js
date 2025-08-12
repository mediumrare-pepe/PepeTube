import React from 'react';

const VideoPlayer = ({ src }) => (
  <div className="player-container">
    <video controls src={src} />
  </div>
);

export default VideoPlayer;
