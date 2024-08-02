const express = require('express');
const axios = require('axios');
const qs = require('qs');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/translate', async (req, res) => {
  const { text, target_lang, source_lang } = req.body;

  try {
    const response = await axios.post(
      'https://api-free.deepl.com/v2/translate',
      qs.stringify({
        text,
        target_lang,
        source_lang,
      }),
      {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          'Accept': 'application/json',
          'Authorization': 'DeepL-Auth-Key 037dbd64-30f9-4fdf-b75c-8bb546536181:fx',
        },
      }
    );

    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});