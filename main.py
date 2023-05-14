from text_manager import CreateText
from speaker_manager import Speaker

text = CreateText
speaker = Speaker

#final_text = text.create_text_from_pdf("sample.pdf")
final_text = text.create_top_list_from_webpage("https://www.pastemagazine.com/movies/in-theaters/the-10-best-movies-in-theaters-right-now")
print(final_text)
speaker.speaker(final_text, "en")