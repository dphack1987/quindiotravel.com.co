import docx2txt
from pathlib import Path
import sys

def read_docx_simple(file_path):
    try:
        # Convertir a Path y validar que existe
        file_path = Path(file_path)
        if not file_path.exists():
            print(f"Error: El archivo no existe: {file_path}")
            return False
        
        print("Opening file: " + str(file_path))
        text = docx2txt.process(str(file_path))
        
        # Guardar en archivo con nombre dinámico basado en el input
        output_file = file_path.parent / f"{file_path.stem}_content.txt"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(text)
        
        print("Content saved to: " + output_file)
        print("Length of content: " + str(len(text)) + " characters")
        
        # Print first 500 characters as preview
        print("\nPREVIEW (first 500 characters):")
        print(text[:500])
        
        return True
    except Exception as e:
        print("Error reading file: " + str(e))
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    # Usar ruta relativa al directorio del script
    script_dir = Path(__file__).parent
    file_path = script_dir / "Pagina www.quindiotravel.com.co.docx"
    
    # Si no existe el archivo específico, mostrar ayuda
    if not file_path.exists():
        print("Uso: python read_docx_simple.py [ruta_archivo]")
        print("Por defecto busca: Pagina www.quindiotravel.com.co.docx")
        print(f"Directorio actual: {script_dir}")
        
        # Intentar usar argumento de línea de comandos si se proporciona
        if len(sys.argv) > 1:
            file_path = Path(sys.argv[1])
        else:
            print("Por favor proporciona la ruta del archivo .docx como argumento")
            sys.exit(1)
    
    read_docx_simple(file_path)