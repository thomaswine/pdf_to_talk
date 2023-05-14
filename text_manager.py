from PyPDF2 import PdfReader
from bs4 import BeautifulSoup
import requests

class CreateText:
    
    def create_text_from_pdf(file_name):
        reader = PdfReader(file_name)
        final_text = ""

        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            pdf_text = page.extract_text()
            final_text += pdf_text
        
        return(final_text)
    
    def create_top_list_from_webpage(page_url):
        response = requests.get(page_url)
        webpage = response.text
        soup = BeautifulSoup(webpage, "html.parser")
        
        movies_list = ""
        
        all_movies = soup.find_all(name="big")
        
        for movie in all_movies:
            movie_title = movie.getText()
            movies_list += f"{movie_title}\n"
        
        return(movies_list)
        
        