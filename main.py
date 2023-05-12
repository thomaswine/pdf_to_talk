from gtts import gTTS
from PyPDF2 import PdfReader
import os

reader = PdfReader("sample.pdf")

print(len(reader.pages))

page = reader.pages[0]

pdf_text = page.extract_text()

print(pdf_text) 

#file = open("sample_pdf.pdf", "r").read().replace("\n", " ")

tts = gTTS(text=pdf_text, lang="fr")

filename = "voice.mp3"
tts.save(filename)
os.system(f"start {filename}")