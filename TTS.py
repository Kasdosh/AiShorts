from gtts import gTTS
import os

def TTS(text, folderName, lang='en'):
    os.makedirs(f"./{folderName}", exist_ok=True)
    gTTS(text, lang=lang).save( "./" + folderName + "/audio.mp3")

if __name__ == "__main__":
    pass