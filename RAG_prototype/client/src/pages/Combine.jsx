import React, { useState } from 'react';


import "../style/Combine.css"
import Navbar from '../components/Navbar';

const API_URL = 'http://127.0.0.1:5000';

const Combine = () => {
  const [text, setText] = useState('');
  const [sourceLang, setSourceLang] = useState('');
  const [targetLang, setTargetLang] = useState('');
  const [translatedText, setTranslatedText] = useState('');
  
  const [response, setResponse] = useState('');

  const handleInputChange = (e) => {
    setText(e.target.value);
  };

  const handleTranslate = async (e) => {
    e.preventDefault();
    try {
        const response = await fetch(API_URL + "/translate",{
            method: "POST",
            
            headers: {
                "Content-Type": "application/json",
            },

            body:JSON.stringify({
                text,
                source_lang: sourceLang,
                target_lang: targetLang,
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error ${response.status}`);
        }

        const data = await response.json();
        setTranslatedText(data.translated_text)

    } catch (error) {
        console.error("Error:", error);
    }
  };

  const handleSwapLanguages = () => {
    
    if (targetLang === "EN-GB" || targetLang === "EN-US") {
        if (sourceLang === "ZH") {
            setSourceLang("EN");
            setTargetLang("ZH-HANT");
        } else if (sourceLang !== "ZH") {
            setSourceLang("EN");
            setTargetLang(sourceLang);
        }
    } else if (targetLang === "ZH-HANT" || targetLang === "ZH-HANS") {
        if (sourceLang === "EN") {
            setSourceLang("ZH");
            setTargetLang("EN-GB");
        } else if (sourceLang !== "EN") {
            setSourceLang("ZH");
            setTargetLang(sourceLang);
        }
    } else {
        setSourceLang(targetLang);
        setTargetLang(sourceLang);
    }    
  };




  const handleRAG = async (e) => {
    e.preventDefault();
 
    const prompt = text
    if (prompt === '') {
      return;
    }


    const data = {
      prompt: (`Can you translate this text [${prompt}] from ${sourceLang} to ${targetLang}`),
      /* prompt: (`Please enhance the translation of this source text [${prompt}] with RAG data [${translatedText}]`), */
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
        <div className="translation-app">
            <h1>RAG Translation App</h1>
            <div className="input-output-container">
            <div className="input-container">
                <label htmlFor="source-language">Source Language:</label>
                <select id="source-language" value={sourceLang} onChange={(e) => setSourceLang(e.target.value)}>
                <option value="EN">English</option>
                <option value="ZH">Chinese</option>
                <option value="JA">Japanese</option>
                <option value="KO">Korean</option>
                </select>
                <textarea
                id="input-text"
                value={text}
                onChange={handleInputChange}
                placeholder="Enter text to translate..."
                ></textarea>
            </div>
            <div className="output-container">
                <label htmlFor="target-language">Target Language:</label>
                <select id="target-language" value={targetLang} onChange={(e) => setTargetLang(e.target.value)}>
                <option value="EN-GB">English (UK)</option>
                <option value="EN-US">English (US)</option>
                <option value="ZH-HANT">Traditional Chinese</option>
                <option value="ZH-HANS">Simplified Chinese</option>
                <option value="JA">Japanese</option>
                <option value="KO">Korean</option>
                </select>
                <textarea id="output-text" value={translatedText} readOnly placeholder="Translated text will appear here"></textarea>
            </div>
            </div>

            <h3>RAG assisted translation:</h3>
            <p>{response}</p>

            <div className="button-container">
            <button onClick={handleTranslate}>Translate</button>
            <button onClick={handleSwapLanguages}>Swap</button>
            <button onClick={handleRAG}>Enable RAG</button>
            </div>

            

        </div>
    </div>
  );
};

export default Combine;