import React from 'react';
import Navbar from '../components/Navbar';

const API_URL = 'http://127.0.0.1:5000';

function Upload() {
  const handleFileSubmit = (e) => {
    e.preventDefault();
    const formData = new FormData(e.target);

    // Send formData to your server using an HTTP request (e.g., axios or fetch).
    // Replace 'YOUR_UPLOAD_API_ENDPOINT' with your actual API endpoint.
    fetch(API_URL + "/upload_file", {
      method: "POST",
      body: formData,
    })

    .then(response => response.json())
    .then(data => {
      console.log('File upload successful:', data);
    })
    .catch(error => {
      console.error('Error uploading the file:', error);
    });
  };

  return (
    <div>
        <Navbar />
        <h1>Upload</h1>
        <div className="container pt-5">
        <form encType="multipart/form-data" onSubmit={handleFileSubmit}>
          <div className="mb-3">
            <label htmlFor="formFile" className="form-label">
              Upload your file
            </label>
            <input
              name="file"
              className="form-control"
              type="file"
              id="formFile"
            />
          </div>
          <div className="form-group">
            <button className="btn btn-primary" type="submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Upload;


