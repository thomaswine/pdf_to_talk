from gtts import gTTS
import os

tts = gTTS(text="", lang="en")

filename = "voice.mp3"
tts.save(filename)
os.system(f"start {filename}")