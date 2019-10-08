from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('diego','pt-br')
tts.write_to_fp(mp3_fp)