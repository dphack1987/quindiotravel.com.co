import xml.etree.ElementTree as ET
import re
from pathlib import Path
import sys

# Ruta al archivo document.xml (relativa al script)
script_dir = Path(__file__).parent
xml_file = script_dir / 'extraido' / 'word' / 'document.xml'

# Validar que el archivo existe
if not xml_file.exists():
    print(f"Error: El archivo XML no existe: {xml_file}")
    print("Por favor verifica que la estructura de archivos sea correcta:")
    print(f"  {script_dir}/")
    print(f"    extraido/")
    print(f"      word/")
    print(f"        document.xml")
    sys.exit(1)

# Parsear el XML
tree = ET.parse(xml_file)
root = tree.getroot()

# Namespace de Word
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Extraer todo el texto
text_content = []

# Buscar todos los elementos de texto
for elem in root.iter():
    # Verificar si es un elemento de texto de Word
    if elem.tag.endswith('}t'):
        if elem.text:
            text_content.append(elem.text)
    # Verificar si es un tabulador
    elif elem.tag.endswith('}tab'):
        text_content.append('\t')
    # Verificar si es un salto de línea
    elif elem.tag.endswith('}br'):
        text_content.append('\n')
    # Verificar si es un párrafo
    elif elem.tag.endswith('}p'):
        text_content.append('\n\n')

# Unir todo el texto
full_text = ''.join(text_content)

# Limpiar espacios múltiples
full_text = re.sub(r'\n\s*\n', '\n\n', full_text)
full_text = re.sub(r'[ \t]+', ' ', full_text)

# Guardar en archivo de texto (en el mismo directorio del script)
output_file = script_dir / 'texto-extraido.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Texto extraído exitosamente en texto-extraido.txt")
print(f"Total de caracteres: {len(full_text)}")
print(f"Archivo guardado en: {output_file}")