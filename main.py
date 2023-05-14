from text_manager import CreateText
from speaker_manager import Speaker

text = CreateText
speaker = Speaker

input = int(input("What do you want to heart?"))

if input == 1:
    final_text = text.create_text_from_pdf("sample.pdf")
elif input == 2:
    #final_text = text.create_top_list_from_webpage("https://www.pastemagazine.com/movies/in-theaters/the-10-best-movies-in-theaters-right-now")
    final_text = text.create_top_list_from_webpage("https://www.pastemagazine.com/movies/netflix/popular-on-netflix-daily-top-10")

print(final_text)
speaker.speaker(final_text, "en")