from text_manager import CreateText
from speaker_manager import Speaker


text = CreateText
speaker = Speaker

final_text = text.create_text_from_pdf("sample.pdf")
speaker.speaker(final_text, "en")
