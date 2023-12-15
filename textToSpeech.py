from gtts import gTTS

def TTS(text, fileName, lang='en'):
    gTTS(text, lang=lang).save( "./" + fileName + "/audio.mp3")