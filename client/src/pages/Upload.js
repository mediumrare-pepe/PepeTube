import React, { useState } from 'react';
import { uploadVideo } from '../api';

const Upload = () => {
  const [title, setTitle] = useState('');
  const [file, setFile] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const data = new FormData();
    data.append('title', title);
    if (file) data.append('file', file);
    uploadVideo(data);
    setTitle('');
    setFile(null);
  };

  return (
    <form onSubmit={handleSubmit} className="upload-form">
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
      />
      <input type="file" onChange={(e) => setFile(e.target.files[0])} />
      <button type="submit">Upload</button>
    </form>
  );
};

export default Upload;
