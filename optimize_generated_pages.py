"""
Script para automatizar la optimización de breadcrumbs en todas las generated-pages
"""

import os
from pathlib import Path
import re

def add_breadcrumb_to_file(file_path, breadcrumb_name, parent_depth=2):
    """
    Agrega breadcrumb navigation a un archivo HTML
    
    Args:
        file_path: Ruta del archivo HTML
        breadcrumb_name: Nombre del item final del breadcrumb
        parent_depth: Profundidad de directorios para calcular rutas relativas
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar si ya tiene breadcrumb
        if 'breadcrumb-nav' in content.lower():
            print(f"  - Ya tiene breadcrumb: {file_path.name}")
            return False
        
        # Calcular ruta relativa a index.html
        relative_path = '../' * parent_depth
        
        # Buscar el </body> para insertar breadcrumb antes
        body_end_pattern = r'(</body>)'
        
        breadcrumb_html = f'''    <!-- Breadcrumb Navigation -->
    <nav class="breadcrumb-nav" aria-label="Breadcrumb">
        <div class="container">
            <ol class="breadcrumb" itemscope itemtype="https://schema.org/BreadcrumbList">
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="{relative_path}index.html" itemprop="item"><span itemprop="name">Inicio</span></a>
                    <meta itemprop="position" content="1" />
                </li>
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <a href="{relative_path}index.html#hoteles" itemprop="item"><span itemprop="name">Hoteles</span></a>
                    <meta itemprop="position" content="2" />
                </li>
                <li itemprop="itemListElement" itemscope itemtype="https://schema.org/ListItem">
                    <span itemprop="name">{breadcrumb_name}</span>
                    <meta itemprop="position" content="3" />
                </li>
            </ol>
        </div>
    </nav>

</body>'''
        
        # Reemplazar </body> con breadcrumb + </body>
        updated_content = re.sub(body_end_pattern, breadcrumb_html, content)
        
        if updated_content == content:
            print(f"  - No se encontro </body>: {file_path.name}")
            return False
        
        # Guardar archivo actualizado
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"  + Breadcrumb agregado: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"  - Error procesando {file_path.name}: {e}")
        return False

def process_directory(directory_path, parent_depth=2):
    """
    Procesa todos los archivos HTML en un directorio
    
    Args:
        directory_path: Ruta del directorio
        parent_depth: Profundidad de directorios para rutas relativas
    """
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"Directorio no encontrado: {directory_path}")
        return
    
    html_files = list(dir_path.glob('*.html'))
    
    if not html_files:
        print(f"No hay archivos HTML en: {directory_path}")
        return
    
    print(f"\nProcesando {len(html_files)} archivos en {directory_path}:")
    
    success_count = 0
    for html_file in html_files:
        # Generar nombre del breadcrumb basado en el nombre del archivo
        breadcrumb_name = html_file.stem.replace('-', ' ').title()
        
        if add_breadcrumb_to_file(html_file, breadcrumb_name, parent_depth):
            success_count += 1
    
    print(f"{success_count}/{len(html_files)} archivos optimizados")

def main():
    """Función principal"""
    base_dir = Path(__file__).parent
    
    print("Iniciando optimizacion de breadcrumbs en generated-pages")
    print("=" * 60)
    
    # Procesar alojamiento (profundidad 2)
    alojamiento_dir = base_dir / "generated-pages" / "alojamiento"
    process_directory(alojamiento_dir, parent_depth=2)
    
    # Procesar armenia (profundidad 3)
    armenia_dir = base_dir / "generated-pages" / "armenia"
    process_directory(armenia_dir, parent_depth=3)
    
    # Procesar subdirectorios de armenia (profundidad 4)
    armenia_subdirs = ["viajes-aventura", "viajes-bienestar", "viajes-culturales", "viajes-economicos"]
    for subdir in armenia_subdirs:
        sub_dir = base_dir / "generated-pages" / "armenia" / subdir
        if sub_dir.exists():
            process_directory(sub_dir, parent_depth=4)
    
    print("\n" + "=" * 60)
    print("Optimizacion de breadcrumbs completada")

if __name__ == "__main__":
    main()