#!/usr/bin/env python3
"""
Script para analizar discrepancias entre páginas existentes y sitemap actual
"""
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

# Forzar salida inmediata
sys.stdout.reconfigure(line_buffering=True)

def get_sitemap_urls(sitemap_path):
    """Extrae todas las URLs del sitemap.xml"""
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        urls = set()
        
        for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
            url_text = url.text
            # Eliminar el dominio base para comparar con archivos locales
            if url_text.startswith('https://quindiotravel.com.co/'):
                clean_url = url_text.replace('https://quindiotravel.com.co/', '')
                if clean_url == '':
                    clean_url = 'index.html'
                urls.add(clean_url)
            elif url_text == 'https://quindiotravel.com.co':
                urls.add('index.html')
        
        return urls
    except Exception as e:
        print(f"Error leyendo sitemap: {e}")
        return set()

def get_html_files(root_dir):
    """Encuentra todos los archivos HTML en el directorio y subdirectorios"""
    html_files = set()
    html_details = defaultdict(list)
    
    for root, dirs, files in os.walk(root_dir):
        # Ignorar directorios que no deben estar en el sitemap
        if any(skip in root for skip in ['.git', '__pycache__', '.devin', 'node_modules', 'tmp', 'backup']):
            continue
            
        for file in files:
            if file.endswith('.html'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, root_dir)
                
                # Convertir a formato URL (usar / en lugar de \)
                relative_path = relative_path.replace('\\', '/')
                
                # Ignorar archivos en directorios que no deben indexarse
                if any(skip in relative_path for skip in ['assets/', 'docs/', 'js/', 'logos_aliados/', 
                                                           'competitive-engine/', 'don-chucho-backend/',
                                                           'outreach_data/', 'directories_data/',
                                                           'pseo-engine/', 'sitemaps/', 'social_media_content/',
                                                           'programmatic-pages/', 'blog/']):
                    # Estos se manejan por separado
                    html_details['excluded'].append(relative_path)
                    continue
                
                html_files.add(relative_path)
                html_details['included'].append(relative_path)
    
    return html_files, html_details

def get_blog_files():
    """Obtiene archivos del blog"""
    blog_dir = Path('blog')
    blog_files = set()
    
    if blog_dir.exists():
        for file in blog_dir.glob('*.html'):
            if file.name != 'test.html':  # Excluir archivos de prueba
                blog_files.add(f"blog/{file.name}")
    
    return blog_files

def get_programmatic_files():
    """Obtiene archivos programáticos"""
    prog_dir = Path('programmatic-pages')
    prog_files = set()
    
    if prog_dir.exists():
        for file in prog_dir.glob('*.html'):
            prog_files.add(f"programmatic-pages/{file.name}")
    
    return prog_files

def get_generated_pages():
    """Obtiene páginas en generated-pages"""
    gen_dir = Path('generated-pages')
    gen_files = set()
    
    if gen_dir.exists():
        for root, dirs, files in os.walk(gen_dir):
            for file in files:
                if file.endswith('.html'):
                    full_path = Path(root) / file
                    relative_path = full_path.relative_to(gen_dir)
                    relative_path_str = str(relative_path).replace('\\', '/')
                    gen_files.add(f"generated-pages/{relative_path_str}")
    
    return gen_files

def get_attraction_pages():
    """Obtiene páginas de atracciones individuales"""
    attraction_files = set()
    
    # Directorios de atracciones específicos
    attraction_dirs = [
        'parque-del-cafe',
        'panaca',
        'recuca',
        'mariposario',
        'termales-de-santa-rosa',
        'quinti-patas-arriba'
    ]
    
    for dir_name in attraction_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists():
            for file in dir_path.glob('*.html'):
                attraction_files.add(f"{dir_name}/{file.name}")
    
    return attraction_files

def main():
    base_dir = Path('.')
    sitemap_path = base_dir / 'sitemap.xml'
    
    print("=" * 80, flush=True)
    print("ANÁLISIS DE DISCREPANCIAS ENTRE PÁGINAS EXISTENTES Y SITEMAP", flush=True)
    print("=" * 80, flush=True)
    
    # 1. Obtener URLs del sitemap actual
    print("\n1. Leyendo sitemap.xml actual...")
    sitemap_urls = get_sitemap_urls(sitemap_path)
    print(f"   URLs en sitemap: {len(sitemap_urls)}")
    
    # 2. Obtener archivos HTML principales
    print("\n2. Buscando archivos HTML principales...")
    html_files, html_details = get_html_files(base_dir)
    print(f"   Archivos HTML principales: {len(html_files)}")
    
    # 3. Obtener archivos del blog
    print("\n3. Buscando archivos del blog...")
    blog_files = get_blog_files()
    print(f"   Archivos del blog: {len(blog_files)}")
    
    # 4. Obtener archivos programáticos
    print("\n4. Buscando archivos programáticos...")
    prog_files = get_programmatic_files()
    print(f"   Archivos programáticos: {len(prog_files)}")
    
    # 5. Obtener generated-pages
    print("\n5. Buscando archivos en generated-pages...")
    gen_files = get_generated_pages()
    print(f"   Archivos en generated-pages: {len(gen_files)}")
    
    # 6. Obtener páginas de atracciones
    print("\n6. Buscando páginas de atracciones...")
    attraction_files = get_attraction_pages()
    print(f"   Páginas de atracciones: {len(attraction_files)}")
    
    # 7. Unir todos los archivos HTML existentes
    all_html_files = html_files | blog_files | prog_files | gen_files | attraction_files
    print(f"\n   TOTAL ARCHIVOS HTML: {len(all_html_files)}")
    
    # 8. Encontrar archivos faltantes en el sitemap
    print("\n7. Buscando archivos faltantes en el sitemap...")
    missing_files = all_html_files - sitemap_urls
    print(f"   Archivos faltantes: {len(missing_files)}")
    
    # 9. Encontrar URLs en sitemap que no existen como archivos
    print("\n8. Buscando URLs en sitemap sin archivo correspondiente...")
    extra_urls = sitemap_urls - all_html_files
    print(f"   URLs extra en sitemap: {len(extra_urls)}")
    
    # 10. Clasificar archivos faltantes
    print("\n" + "=" * 80)
    print("CLASIFICACIÓN DE ARCHIVOS FALTANTES")
    print("=" * 80)
    
    missing_by_type = defaultdict(list)
    for file in sorted(missing_files):
        if file.startswith('blog/'):
            missing_by_type['blog'].append(file)
        elif file.startswith('programmatic-pages/'):
            missing_by_type['programmatic'].append(file)
        elif file.startswith('generated-pages/'):
            missing_by_type['generated'].append(file)
        elif file.startswith('parque-del-cafe/') or file.startswith('panaca/') or \
             file.startswith('recuca/') or file.startswith('mariposario/') or \
             file.startswith('termales-de-santa-rosa/') or file.startswith('quinti-patas-arriba/'):
            missing_by_type['attractions'].append(file)
        else:
            missing_by_type['main'].append(file)
    
    for category, files in missing_by_type.items():
        print(f"\n{category.upper()} ({len(files)} archivos):")
        for file in files[:10]:  # Mostrar primeros 10
            print(f"  - {file}")
        if len(files) > 10:
            print(f"  ... y {len(files) - 10} más")
    
    # 11. Mostrar URLs extra
    if extra_urls:
        print("\n" + "=" * 80)
        print("URLS EN SITEMAP SIN ARCHIVO CORRESPONDIENTE")
        print("=" * 80)
        for url in sorted(extra_urls)[:20]:
            print(f"  - {url}")
        if len(extra_urls) > 20:
            print(f"  ... y {len(extra_urls) - 20} más")
    
    # 12. Generar reporte
    print("\n" + "=" * 80)
    print("RESUMEN")
    print("=" * 80)
    print(f"Total archivos HTML existentes: {len(all_html_files)}")
    print(f"Total URLs en sitemap: {len(sitemap_urls)}")
    print(f"Archivos faltantes en sitemap: {len(missing_files)}")
    print(f"URLs extra en sitemap: {len(extra_urls)}")
    print(f"Porcentaje de completitud: {((len(sitemap_urls) / len(all_html_files)) * 100):.1f}%")
    
    # 13. Guardar lista de archivos faltantes
    with open('missing_files.txt', 'w') as f:
        for file in sorted(missing_files):
            f.write(f"{file}\n")
    
    print(f"\nLista de archivos faltantes guardada en: missing_files.txt")
    
    return missing_files, all_html_files, sitemap_urls

if __name__ == '__main__':
    missing_files, all_html_files, sitemap_urls = main()
