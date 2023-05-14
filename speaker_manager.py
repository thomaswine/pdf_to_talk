from gtts import gTTS
import os

class Speaker:
    
    def speaker(final_text, language):
        tts = gTTS(text=final_text, lang=language, slow=False)

        filename = "voice.mp3"
        tts.save(filename)
        os.system(f"start {filename}")