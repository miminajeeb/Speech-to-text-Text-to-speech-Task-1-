from lib2to3.pgen2.grammar import line

url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/c85bf8c9-dcb6-4ee8-b673-e2907fadbbbb'
apikey = 'fEhks9hNZ615lN9wEHOwdGZrqWWS75IN86AOjrZ5C3jz'

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator(apikey)
tts = TextToSpeechV1(authenticator=authenticator)
tts.set_service_url(url)

with open('demofile.txt', 'r') as f:
    text = f.readlines()
text = (line.replace('\n', '') for line in text)
text = ''.join(str(line) for line in text)


with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-US_AllisonV3Voice').get_result()
    audio_file.write(res.content)
