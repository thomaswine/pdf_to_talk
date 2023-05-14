from gtts import gTTS
from PyPDF2 import PdfReader
import os

reader = PdfReader("sample.pdf")
final_text = ""
print(len(reader.pages))

for page_number in range(len(reader.pages)):
    page = reader.pages[page_number]
    pdf_text = page.extract_text()
    final_text += pdf_text
    
print(final_text)

tts = gTTS(text=final_text, lang="en", slow=False)

filename = "voice.mp3"
tts.save(filename)
os.system(f"start {filename}")