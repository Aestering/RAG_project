import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import "../style/Chat.css"

const API_URL = 'http://127.0.0.1:5000';

function Chat() {
  const [question, setQuestion] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const prompt = question.trim();
    if (prompt === '') {
      return;
    }

    const data = {
      prompt: prompt,
    };

    console.log('Sending question:', data);

    try {
      const response = await fetch(API_URL + "/ask_llm", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const data = await response.json();
        console.log('Response from backend:', data.answer);

        setResponse(data.answer);
      } else {
        const error = await response.json();
        console.error(error.error);
        setResponse('An error occurred. Please try again later.');
      }
    } catch (error) {
      console.error(error);
      setResponse('An error occurred. Please try again later.');
    }
  };

  return (
    <div>
      <Navbar />
      <div
        style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          height: '100vh',
          width: '100vw',
        }}
      >
        <h1>RAG Prototype</h1>
        <form
          onSubmit={handleSubmit}
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '1rem',
            maxWidth: '600px',
            width: '100%',
          }}
        >
          <label htmlFor="question">Please upload file first before prompting!</label>
          <textarea
            id="question"
            required
            placeholder='e.g. "Translate from English to Traditional Chinese."'
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            style={{
              width: '100%',
              minHeight: '4rem',
              resize: 'both',
              overflow: 'auto',
              border: 'none',
              outline: 'none',
              fontSize: '1rem',
            }}
          />
          <button type="submit">Submit</button>
        </form>
        <div
          style={{
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '1rem',
            maxWidth: '600px',
            textAlign: 'center',
            width: '100%',
          }}
        >
          <h3>Response:</h3>
          <p>{response}</p>
        </div>
      </div>
    </div>
  );
}

export default Chat;