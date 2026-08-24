#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agregar hreflang tags a páginas principales
Extiende la implementación de hreflang a index.html, planes.html, salento.html, etc.
"""

from pathlib import Path
from hreflang_utils import add_hreflang_tags, add_language_detector

# Páginas principales que necesitan hreflang
MAIN_PAGES = [
    'index.html',
    'planes.html', 
    'salento.html',
    'valle-de-cocora.html',
    'parque-del-cafe.html',
    'filandia.html',
]

def process_page(file_path):
    """Procesar una página individual para agregar hreflang"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene hreflang
        if 'hreflang' in content:
            print(f"  SKIP Ya tiene hreflang: {file_path.name}")
            return False
        
        # Obtener nombre relativo
        relative_path = str(file_path.relative_to(Path.cwd())).replace('\\', '/')
        
        # Agregar hreflang tags
        content = add_hreflang_tags(content, relative_path)
        
        # Agregar language detector
        content = add_language_detector(content)
        
        # Guardar cambios
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  OK Procesado: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"  ERROR en {file_path.name}: {e}")
        return False

def main():
    print("Agregando hreflang a paginas principales")
    print("="*60)
    
    base_dir = Path.cwd()
    stats = {'processed': 0, 'skipped': 0, 'errors': 0}
    
    for page_name in MAIN_PAGES:
        page_path = base_dir / page_name
        if page_path.exists():
            result = process_page(page_path)
            if result:
                stats['processed'] += 1
            else:
                stats['skipped'] += 1
        else:
            print(f"  WARNING No encontrada: {page_name}")
            stats['errors'] += 1
    
    print()
    print("="*60)
    print(f"Resultados: {stats['processed']} procesadas, {stats['skipped']} omitidas, {stats['errors']} errores")
    print("="*60)

if __name__ == '__main__':
    main()