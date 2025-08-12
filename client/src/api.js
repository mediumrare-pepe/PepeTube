import axios from 'axios';

const API = axios.create({ baseURL: '/api' });

export const login = (credentials) => API.post('/auth/login', credentials);
export const uploadVideo = (data) =>
  API.post('/videos', data, {
    headers: { 'Content-Type': 'multipart/form-data' },
  });
export const fetchComments = (videoId) =>
  API.get(`/videos/${videoId}/comments`);
export const postComment = (videoId, text) =>
  API.post(`/videos/${videoId}/comments`, { text });

export default API;
