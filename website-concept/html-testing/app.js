translateBtn.addEventListener("click", () => {
    let text = fromText.value.trim(),
      translateFrom = selectTag[0].value,
      translateTo = selectTag[1].value;
  
    if (!text) return;
  
    toText.setAttribute("placeholder", "Translating...");
  
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
    myHeaders.append("Accept", "application/json");
    myHeaders.append("Authorization", "037dbd64-30f9-4fdf-b75c-8bb546536181:fx"); // Replace with your actual DeepL API key
  
    const urlencoded = new URLSearchParams();
    urlencoded.append("text", text);
    urlencoded.append("target_lang", "DE");
    urlencoded.append("source_lang", "");
  
    const requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: urlencoded,
      redirect: "follow",
    };
  
    fetch("https://api-free.deepl.com/v2/translate", requestOptions)
      .then((response) => response.json())
      .then((data) => {
        const outputText = document.getElementById("output-text");
        outputText.value = result.translations[0].text;
      })
      .catch((error) => console.error(error));
        
});


    
