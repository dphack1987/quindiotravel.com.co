"""
Consolidar documentación duplicada en un solo archivo maestro
"""

import re
from pathlib import Path
from datetime import datetime

def read_markdown_files():
    """Leer todos los archivos .md del proyecto"""
    base_dir = Path.cwd()
    md_files = list(base_dir.glob('*.md'))
    
    docs_content = {}
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            docs_content[md_file.name] = content
        except Exception as e:
            print(f"Error reading {md_file.name}: {e}")
    
    return docs_content

def create_master_document(docs_content):
    """Crear documento maestro consolidado"""
    master_content = f"""# DOCUMENTACIÓN MAESTRA - QUINDÍO TRAVEL
**Fecha de consolidación:** {datetime.now().strftime('%Y-%m-%d')}
**Total de documentos consolidados:** {len(docs_content)}

---

## ÍNDICE DE DOCUMENTOS

"""
    
    # Ordenar documentos alfabéticamente
    sorted_files = sorted(docs_content.keys())
    
    for filename in sorted_files:
        master_content += f"### {filename}\n\n"
        content = docs_content[filename]
        
        # Extraer primera sección o resumen si existe
        lines = content.split('\n')
        if lines:
            # Tomar primeras 10 líneas como resumen
            summary = '\n'.join(lines[:10])
            master_content += f"{summary}\n\n"
            master_content += f"**[Ver documento completo](#{filename.replace('.md', '').lower()})**\n\n"
    
    master_content += "---\n\n## DOCUMENTOS COMPLETOS\n\n"
    
    # Agregar documentos completos
    for filename in sorted_files:
        master_content += f"<details>\n<summary>{filename}</summary>\n\n"
        master_content += docs_content[filename]
        master_content += "\n</details>\n\n"
    
    return master_content

def main():
    print("Consolidando documentación...")
    docs_content = read_markdown_files()
    
    if not docs_content:
        print("No se encontraron archivos .md")
        return
    
    master_content = create_master_document(docs_content)
    
    # Guardar documento maestro
    master_file = Path.cwd() / 'DOCUMENTACION_MAESTRA.md'
    with open(master_file, 'w', encoding='utf-8') as f:
        f.write(master_content)
    
    print(f"Documentación consolidada en {master_file.name}")
    print(f"Total de documentos procesados: {len(docs_content)}")
    
    # Lista de archivos a mantener (excepciones)
    keep_files = [
        'DOCUMENTACION_MAESTRA.md',
        'ANALISIS_COMPLETO_PROYECTO.md',
        'README.md'
    ]
    
    # Mover archivos antiguos a carpeta de archivo
    archive_dir = Path.cwd() / 'documentation_archive'
    archive_dir.mkdir(exist_ok=True)
    
    moved_count = 0
    for filename in docs_content.keys():
        if filename not in keep_files:
            old_path = Path.cwd() / filename
            new_path = archive_dir / filename
            try:
                old_path.rename(new_path)
                moved_count += 1
                print(f"Archivado: {filename}")
            except Exception as e:
                print(f"Error archivando {filename}: {e}")
    
    print(f"Total de archivos archivados: {moved_count}")

if __name__ == "__main__":
    main()