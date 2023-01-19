import streamlit as st
import numpy as np
import pandas as pd
import os
import shutil
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from speech_to_text import generate_transcript
st.write(os.listdir())

# Stergem tot din folder-ul de cache
folder = 'src/cache/'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        st.warning('Failed to delete %s. Reason: %s' % (file_path, e))
        print('Failed to delete %s. Reason: %s' % (file_path, e))

### Aplicatia ###
language = st.radio('Language: ', ('Română', 'English'))

if language == 'English':
    st.title("Speech-to-Text using Google API")
    st.write("By Craioveanu Sergiu and Paraschiva Mihai")
    language_code = "en-US"
elif language == 'Română':
    st.title("Speech-to-Text folosind Google API")
    st.write("De Craioveanu Sergiu si Paraschiva Mihai")
    language_code = "ro-RO"

# st.image('../img.png', use_column_width='always')

# Incarcam fisierul
if language == 'English':   
    st.markdown("# Select a waveform file:")
    uploaded_file = st.file_uploader("Pick a wave file.", type='wav') 
elif language == 'Română':
    st.markdown("# Selecteaza un fisier Waveform")
    uploaded_file = st.file_uploader("Alege un fisier de tip wav.", type='wav') 

if uploaded_file is None:
    if language == 'English':   
        st.info("Please pick a wave file.")
        st.stop()
    elif language == 'Română':
        st.info("Va rugam sa incarcati un fisier wav.")
        st.stop()


# Dispunem posibilitatea de a asculta fisierul audio
if language == 'English':   
    st.markdown("# Listen to file")
elif language == 'Română':
    st.markdown("# Asculta fisierul")

st.audio(uploaded_file, format='audio/ogg')

# Generam byte data din fisierul uploadat cu posibilitatea de a-l stoca local
bytes_data = uploaded_file.getvalue()
with open('src/cache/recording.wav', mode='bx') as f:
    f.write(bytes_data)

# Generam transcript/Speech to text-ul efectiv
response = generate_transcript(language_code)

if language == 'English':   
    st.markdown("# Generated text:")
elif language == 'Română':
    st.markdown("# Textul generat:")

for result in response.results:
    st.text_area("Text","{}".format(result.alternatives[0].transcript))




