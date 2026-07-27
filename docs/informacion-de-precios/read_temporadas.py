import docx2txt
import os

def read_docx_to_file(file_path, output_path):
    try:
        print("Reading: " + os.path.basename(file_path))
        text = docx2txt.process(file_path)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print("Saved to: " + output_path)
        print("Length: " + str(len(text)) + " characters")
        print("\nPREVIEW (first 300 characters):")
        print(text[:300])
        print("\n" + "=" * 80 + "\n")
        
        return True
    except Exception as e:
        print("Error: " + str(e))
        import traceback
        traceback.print_exc()
        return False

# Read all temporada documents
base_path = r"C:\Users\user\Documents\www.quindiotravel.com\docs\informacion-de-precios"

temporada_files = [
    ("TEMPORADA BAJA.docx", "temporada_baja_content.txt"),
    ("TEMPORADA MEDIA  - PUENTES  Y RECESO ESCOLAR 2026.docx", "temporada_media_content.txt"),
    ("TEMPORADA ALTA - 15 DICIEMBRE AL 20 ENERO-2026.docx", "temporada_alta_content.txt")
]

for filename, output_name in temporada_files:
    file_path = os.path.join(base_path, filename)
    output_path = os.path.join(base_path, output_name)
    read_docx_to_file(file_path, output_path)