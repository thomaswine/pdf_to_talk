from PyPDF2 import PdfReader

class CreateText:
    
    def create_text_from_pdf(file_name):
        reader = PdfReader(file_name)
        final_text = ""

        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            pdf_text = page.extract_text()
            final_text += pdf_text
        
        return final_text