import React from 'react';
import axios from 'axios';

const App = () => {
  const apiUrl = 'https://jsonplaceholder.typicode.com/posts'; // Example API URL

  const login_api = "http://127.0.0.1:5000/login"
  const students_api = "http://127.0.0.1:5000/students"
  var access_token
  const handlePost = () => {
    axios
      .post(login_api, {
        username: 'divine',
        password: 'divine'
      })
      .then((response) => {
        console.log('POST response:', response.data);
        access_token = response.data.access_token
      })
      .catch((error) => {
        console.error('Error during POST request:', error);
      });
  };

  const handleGet = () => {
    axios
      .get(students_api,{
        headers: {
          Authorization: 'Bearer ' + access_token
        }
      })
      .then((response) => {
        console.log('GET response:', response.data);
      })
      .catch((error) => {
        console.error('Error during GET request:', error);
      });
  };

  const handlePut = () => {
    axios
      .put(`${apiUrl}/1`, {
        id: 1,
        title: 'foo',
        body: 'bar',
        userId: 1,
      })
      .then((response) => {
        console.log('PUT response:', response.data);
      })
      .catch((error) => {
        console.error('Error during PUT request:', error);
      });
  };

  const handleDelete = () => {
    axios
      .delete(`${apiUrl}/1`)
      .then((response) => {
        console.log('DELETE response:', response.status); // 200 means success
      })
      .catch((error) => {
        console.error('Error during DELETE request:', error);
      });
  };

  return (
    <div>
      <h1>React Axios Example</h1>
      <button onClick={handlePost}>POST</button>
      <button onClick={handleGet}>GET</button>
      <button onClick={handlePut}>PUT</button>
      <button onClick={handleDelete}>DELETE</button>
    </div>
  );
};

export default App;
