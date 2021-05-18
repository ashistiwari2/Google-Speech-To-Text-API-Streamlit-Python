# Streamlit App integrating Google Speech-To-Text API in Python

## Authors:
[Sergiu Craioveanu](https://github.com/the-sergiu)
[Paraschiva Mihai](https://github.com/ParaschivaMihai)
## Description
Intuitive Streamlit App written in Python which converts a wavefile into text through Google Speech-to-Text API text generation capabilities. Requires a credentials JSON file obtained using the steps described [here](https://www.hellocodeclub.com/python-speech-recognition-create-program-with-google-api/).

Languages available: English, Romanian.

## Setup
1. Clone Repo (duh)
2. Use a Google Account to obtain the credentials json, as per the link above.
3. (Optional) Create a credentials folder.

To connect to the Google Speech-To-Text API, we require an OS environment variable which specifies the path for the configured credentials (a .json file).

**Linux**:
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/serj/Desktop/Google-Speech-To-Text-API-Python-App/credentials/key-file.json"
```

4. Also, requirements should be installed using:
```
pip install -r requirements.txt
```
Python version used: Python 3.7

## Running the app

To run the app, navigate to the **src/** folder within the repo, and simply run (after successfully completing the above steps):

```
streamlit run interface.py
```

## App Display

If you uploaded your own wave file containing speech, this is how the app might look.


![App pic](misc/running_app.PNG)

## Misc

We also included our own samples within the **sound_samples** directory, both in Romanian and English.

