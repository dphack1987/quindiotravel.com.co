import pdfplumber
import sys

def extract_pdf_text(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                text += page.extract_text() + "\n"
            return text
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    pdf_path = "PORTAFOLIO 2026 QUINDIO TRAVEL (3) (1).pdf"
    text = extract_pdf_text(pdf_path)
    
    # Guardar el texto extraído
    with open("portafolio_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print("Contenido extraído y guardado en portafolio_content.txt")
    print(text[:2000])  # Mostrar primeros 2000 caracteres