# deepgram-transcription-demo

This is a testing repository for the Deepgram transcription model and iTranslate language model.

## Installation

Use the package manager [pip] -> `pip install -r requirements.txt`

## Streaming audio file from audio_files

Run the following command:
`python testing.py -k DEEPGRAM_API_KEY -i ../audio_files/CALLBANK_ID.wav`

## clean_text()

Cleans the pre-loaded transcript from callbank_transcripts for input into testing suite to check WER (word error rate)
