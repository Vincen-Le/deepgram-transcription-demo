import aiohttp
import json
import asyncio
from transcription_demo import main as transcribe

# Translation demo for pre-recorded audio files

async def main():

    # Await response from Deepgram transcription API
    transcription = await transcribe()
    SOURCE = 'en'
    TARGET = 'es'
    # Await response from iTranslate API with Deepgram transcription input
    translation = await translate(SOURCE, TARGET, transcription)
    print(transcription)
    print(translation)

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
            return result
        
asyncio.run(main())