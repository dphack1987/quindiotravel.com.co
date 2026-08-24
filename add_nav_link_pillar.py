#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Agregar link a pillar page en navegación principal
Script para agregar link a operador-turistico-quindio.html en navegación
"""

from pathlib import Path
import re

def add_nav_link_to_page(file_path):
    """Agregar link a la nueva pillar page en navegación"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene el link
        if 'operador-turistico-quindio.html' in content:
            return False, "Ya tiene el link"
        
        # Buscar diferentes patrones de navegación
        nav_patterns = [
            r'(<nav class="main-nav">.*?<a href="planes\.html">Planes</a>)',
            r'(<nav class="nav-menu">.*?<a href="planes\.html">Planes</a>)',
            r'(href="planes\.html".*?</a>)'
        ]
        
        new_nav_link = r'\1\n                <a href="operador-turistico-quindio.html">Operador Turístico</a>'
        
        for nav_pattern in nav_patterns:
            new_content = re.sub(nav_pattern, new_nav_link, content, count=1, flags=re.DOTALL)
            if new_content != content:
                break
        
        if new_content == content:
            return False, "No se encontró navegación principal"
        
        # Guardar cambios
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True, "Link agregado exitosamente"
        
    except Exception as e:
        return False, f"Error: {e}"

def main():
    print("Agregando link a pillar page en navegación principal")
    print("="*60)
    
    base_dir = Path.cwd()
    main_pages = ['index.html', 'planes.html', 'salento.html']
    
    stats = {'added': 0, 'skipped': 0, 'errors': 0}
    
    for page in main_pages:
        file_path = base_dir / page
        if not file_path.exists():
            print(f"SKIP {page} - Archivo no encontrado")
            stats['skipped'] += 1
            continue
            
        success, message = add_nav_link_to_page(file_path)
        
        if success:
            print(f"OK {page}")
            stats['added'] += 1
        elif "Ya tiene el link" in message:
            print(f"SKIP {page} - Ya tiene el link")
            stats['skipped'] += 1
        else:
            print(f"ERROR {page} - {message}")
            stats['errors'] += 1
    
    print()
    print("="*60)
    print(f"Resultados: {stats['added']} agregados, {stats['skipped']} omitidos, {stats['errors']} errores")
    print("="*60)

if __name__ == '__main__':
    main()