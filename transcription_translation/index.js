require('dotenv').config();
const fetch = require('cross-fetch');
const { Deepgram } = require('@deepgram/sdk');
const deepgram = new Deepgram(process.env.DG_KEY);

// Translation function sourced from Deepgram tutorial

async function translate(source, target, text) {
  const url = 'https://dev-api.itranslate.com/translation/v2/';
  const headers = {
    Authorization: '60ce92a0-897c-4925-a79b-ad6cf581b9e7',
    'Content-Type': 'application/json',
  };
  const data = {
    source: { dialect: source, text: text },
    target: { dialect: target },
  };

  const result = await fetch(url, {
    method: 'POST',
    headers,
    body: JSON.stringify(data),
  }).then((r) => r.json());

  return result;
}

//translation test

translate('en', 'es', 'Hello world').then((data) => console.log(data));
