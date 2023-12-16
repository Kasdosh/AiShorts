import speech_recognition as sr
import os
from pydub import AudioSegment

# Convert mp3 file to wav
def MP3_TO_WAV(srcPath):
    sound = AudioSegment.from_mp3(srcPath)
    sound.export(srcPath.split("audio.")[0]+"audio.wav", format="wav")

def STT(folderName):
    mp3_path = f"./{folderName}/audio.mp3"
    wav_path = f"./{folderName}/audio.wav"
    MP3_TO_WAV(mp3_path)
    silence_time_stamps = get_silence_points(wav_path)
    slice_audio(folderName, silence_time_stamps)
    

def get_silence_points(srcPath):
    silence_points = []
    # Load audio
    audio = AudioSegment.from_file(srcPath)
    # Duration of the audio in milliseconds
    duration = len(audio)
    # Analyze dB level for each millisecond
    last = ""
    for i in range(duration):
        millisecond_audio = audio[i:i+1]
        db_level = millisecond_audio.dBFS
        if last != db_level and db_level == float('-inf'):
            silence_points.append(i)
        last = db_level
    return silence_points

def slice_audio(folderName, silence_points):
    os.makedirs(f"./{folderName}/fragments", exist_ok=True)
    audio = AudioSegment.from_file(f"./{folderName}/audio.wav")
    last = 0
    for time_stamp in silence_points:
        if time_stamp - last > 300:
            audio[last:time_stamp].export(f"./{folderName}/fragments/{last}-{time_stamp}.mp3", format="mp3")
        last = time_stamp


if __name__ == "__main__":
    pass