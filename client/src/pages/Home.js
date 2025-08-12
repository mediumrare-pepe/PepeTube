import React, { useEffect, useState } from 'react';
import VideoCard from '../components/VideoCard';

const Home = () => {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    setVideos([
      { id: 1, title: 'Sample Video', thumbnail: 'https://via.placeholder.com/300x180' },
      { id: 2, title: 'Another Video', thumbnail: 'https://via.placeholder.com/300x180' }
    ]);
  }, []);

  return (
    <div className="video-grid">
      {videos.map((v) => (
        <VideoCard key={v.id} video={v} />
      ))}
    </div>
  );
};

export default Home;
