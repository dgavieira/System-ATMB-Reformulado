from gtts import gTTS
import os
tts = gTTS(text='Good morning', lang='en')
tts2 = gTTS(text='Diego', lang='pt-br')
tts3 = gTTS(text="Esse é o Sistema Educativo de Musicografia Braile. Seja bem vindo!",lang='pt-br')
tts.save("good.mp3")
tts2.save("diego.mp3")
tts3.save("systematmb.mp3")