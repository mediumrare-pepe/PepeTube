import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import VideoPlayer from '../components/VideoPlayer';
import { fetchComments, postComment } from '../api';

const Watch = () => {
  const { id } = useParams();
  const [comments, setComments] = useState([]);
  const [text, setText] = useState('');

  useEffect(() => {
    fetchComments(id)
      .then((res) => setComments(res.data))
      .catch(() => setComments([]));
  }, [id]);

  const handleSubmit = (e) => {
    e.preventDefault();
    postComment(id, text).then((res) => setComments([...comments, res.data]));
    setText('');
  };

  return (
    <div>
      <VideoPlayer src={`/videos/${id}`} />
      <ul className="comments">
        {comments.map((c, i) => (
          <li key={i}>{c.text}</li>
        ))}
      </ul>
      <form onSubmit={handleSubmit} className="comment-form">
        <input
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Add a comment"
        />
        <button type="submit">Post</button>
      </form>
    </div>
  );
};

export default Watch;
