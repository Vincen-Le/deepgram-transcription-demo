# deepgram-transcription-demo

This is a testing repository for the Deepgram transcription model and iTranslate language model.

## Installation

Use the package manager [pip] -> `pip install -r requirements.txt`

## Streaming audio file from audio_files

Run the following command:
`python testing.py -k DEEPGRAM_API_KEY -i ../audio_files/CALLBANK_ID.wav`

## clean_text(input)

Cleans the pre-loaded transcript from callbank_transcripts for input into testing suite to check WER (word error rate)

## read_transcript(FILEPATH_CHA)

Reads corresponding callbank transcript from callbank_transcripts; Matches the inputted callbank audio file

## testing.py

Main livestream testing suite

## testing.py commands

- `-k` or `--key`: Insert DEEPGRAM_API_KEY for authorization
- `-i` or `--input`: Input "mic" to stream from mic, FILEPATH to WAV file, or URL to direct audio stream; Defaults to "4065.wav"
- `-m` or `--model`: Which model to make request against (i.e. `--model phonecall`); Defaults to general
- `-t` or `--tier`: Which model tier to make request against; Defaults to nova
- `-ts` or `--timestamps`: Whether to include timestamps to printed streamed transcript; Defaults to False
- `-f` or `--format`: Format for output where "text" is plaintext, "VTT," or "SRT" which will save to directory
- `-tr` or `--translate`: Translate from source to target language (i.e. `--translate en es`); Defaults to empty language input array

## translation live stream demo

1. `cd live_stream`
2. `python testing.py -k DEEPGRAM_API_KEY`
