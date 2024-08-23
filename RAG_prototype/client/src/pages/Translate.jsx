import React, { useState } from 'react';
import Navbar from '../components/Navbar';
import "../style/Translate.css";

const API_URL = 'http://127.0.0.1:5000';


function Translator() {
  const [text, setText] = useState('');
  const [sourceLang, setSourceLang] = useState('EN');
  const [targetLang, setTargetLang] = useState('EN-GB');
  const [translatedText, setTranslatedText] = useState('');

  const handleSubmit2 = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(API_URL + '/translate', {
        method: 'POST',

        headers: {
            'Content-Type': 'application/json',
          },

        body: JSON.stringify({
          text,
          source_lang: sourceLang,
          target_lang: targetLang,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error ${response.status}`);
      }

      const data = await response.json();
      setTranslatedText(data.translated_text);
      
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
        <Navbar />
      <h1>DeepL Text Translator</h1>
      <form onSubmit={handleSubmit2}>
        <label htmlFor="text">Text to translate:</label>
        <textarea
          name="text"
          id="text"
          rows="5"
          value={text}
          onChange={(e) => setText(e.target.value)}
        ></textarea>
        <br />
        <label htmlFor="source_lang">Source language:</label>
        <select
          name="source_lang"
          id="source_lang"
          value={sourceLang}
          onChange={(e) => setSourceLang(e.target.value)}
        >
          <option value="EN">English</option>
          <option value="ZH">Chinese</option>
          <option value="JA">Japanese</option>
          <option value="KO">Korean</option>
          {/* Add more language options as needed */}
        </select>
        <br />
        <label htmlFor="target_lang">Target language:</label>
        <select
          name="target_lang"
          id="target_lang"
          value={targetLang}
          onChange={(e) => setTargetLang(e.target.value)}
        >
          <option value="EN-GB">English (UK)</option>
          <option value="EN-US">English (US)</option>
          <option value="ZH-HANT">Traditional Chinese</option>
          <option value="ZH-HANS">Simplified Chinese</option>
          <option value="JA">Japanese</option>
          <option value="KO">Korean</option>
          {/* Add more language options as needed */}
        </select>
        <br />
        <button type="submit">Translate</button>
      </form>

      {translatedText && (
        <div>
          <h2>Translated Text:</h2>
          <p>{translatedText}</p>
        </div>
      )}
    </div>
  );
};

export default Translator;