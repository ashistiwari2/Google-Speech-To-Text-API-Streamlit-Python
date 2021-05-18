# -*- coding: utf-8 -*-
"""
Speech to Text, Proiect PSA

"""

from google.cloud import speech
import os
import io
import wave

def generate_transcript(language_code="ro-RO"):
    
    # Creates google client
    client = speech.SpeechClient()

    # Full path of the audio file, Replace with your file name
    file_name = os.path.join(os.path.dirname(__file__),"cache/recording.wav")
    wav_file = wave.Wave_read(file_name)
    ch = wav_file.getnchannels()

    #Loads the audio file into memory
    with io.open(file_name, "rb") as audio_file:
        content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        audio_channel_count=ch,
        language_code=language_code,
    )

    # Sends the request to google to transcribe the audio
    response = client.recognize(request={"config": config, "audio": audio})

    return response
    