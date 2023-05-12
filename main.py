from gtts import gTTS
import os

file = open("sample.txt", "r").read().replace("\n", " ")

tts = gTTS(text=str(file), lang="fr")

filename = "voice.mp3"
tts.save(filename)
os.system(f"start {filename}")