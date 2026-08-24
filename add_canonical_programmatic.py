#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agregar canonical URLs a páginas programáticas
Implementa canonicalización para evitar duplicate content
"""

from pathlib import Path
import re

def add_canonical_to_page(file_path):
    """Agregar canonical URL a una página individual"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene canonical
        if 'canonical' in content:
            return False, "Ya tiene canonical"
        
        # Generar URL canónica basada en el nombre del archivo
        file_name = file_path.name
        canonical_url = f"https://quindiotravel.com.co/programmatic-pages/{file_name}"
        
        # Buscar el cierre del head </head>
        head_pattern = r'(</head>)'
        
        canonical_tag = f'    <!-- Canonical URL -->\n    <link rel="canonical" href="{canonical_url}">\n\\1'
        
        new_content = re.sub(head_pattern, canonical_tag, content, count=1)
        
        if new_content == content:
            return False, "No se encontró </head>"
        
        # Guardar cambios
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, f"Canonical agregado: {canonical_url}"
        
    except Exception as e:
        return False, f"Error: {e}"

def main():
    print("Agregando canonical URLs a paginas programaticas")
    print("="*60)
    
    base_dir = Path.cwd()
    prog_dir = base_dir / 'programmatic-pages'
    
    if not prog_dir.exists():
        print("ERROR: Directorio programmatic-pages no encontrado")
        return
    
    html_files = list(prog_dir.glob('*.html'))
    print(f"Encontrados {len(html_files)} archivos HTML")
    print()
    
    stats = {'added': 0, 'skipped': 0, 'errors': 0}
    
    for html_file in html_files:
        success, message = add_canonical_to_page(html_file)
        
        if success:
            print(f"OK {html_file.name}")
            stats['added'] += 1
        elif "Ya tiene canonical" in message:
            print(f"SKIP {html_file.name} - Ya tiene canonical")
            stats['skipped'] += 1
        else:
            print(f"ERROR {html_file.name} - {message}")
            stats['errors'] += 1
    
    print()
    print("="*60)
    print(f"Resultados: {stats['added']} agregados, {stats['skipped']} omitidos, {stats['errors']} errores")
    print("="*60)

if __name__ == '__main__':
    main()