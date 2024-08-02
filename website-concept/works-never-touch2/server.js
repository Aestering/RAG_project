const axios = require('axios');
const qs = require('qs');
let data = qs.stringify({
  'text': 'Hello, world!',
  'target_lang': 'DE',
  'source_lang': '' 
});

let config = {
  method: 'post',
  maxBodyLength: Infinity,
  url: 'https://api-free.deepl.com/v2/translate',
  headers: { 
    'Content-Type': 'application/x-www-form-urlencoded', 
    'Accept': 'application/json', 
    'Authorization': 'DeepL-Auth-Key 037dbd64-30f9-4fdf-b75c-8bb546536181:fx'
  },
  data : data
};

axios.request(config)
.then((response) => {
  console.log(JSON.stringify(response.data));
})
.catch((error) => {
  console.log(error);
});