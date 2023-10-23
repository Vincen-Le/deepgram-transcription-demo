import aiohttp
import json
import asyncio
from read_transcript import read_transcript
from clean_text import clean_text

# Translation demo for pre-recorded audio files

async def main():

    # Read transcript from .cha file
    FILEPATH = '../callbank_transcripts/eng/4065.cha'
    transcript = read_transcript(FILEPATH)
    cleaned_transcript = clean_text(transcript)
    SOURCE = 'en'
    TARGET = 'es'
    # Await response from iTranslate API with Deepgram transcription input
    translation = await translate(SOURCE, TARGET, cleaned_transcript)
    print('Transcription: "%s" \n' % (cleaned_transcript))
    print('Translation: %s' % (translation))

# Translation takes source language -> target language

async def translate(source, target, text):
    url = 'https://dev-api.itranslate.com/translation/v2/'
    headers = {
        'Authorization' : '60ce92a0-897c-4925-a79b-ad6cf581b9e7',
        'Content-Type' : 'application/json',
    }
    data = {
        'source' : {'dialect': source, 'text': text},
        'target' : {'dialect': target},
    }


    # POST request made with aiohttp and JSON serialization handled

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            result = await response.json()
            #raw_translation = result["target"]["text"]
            print(result)
            print('\n')
            return result
        
asyncio.run(main())