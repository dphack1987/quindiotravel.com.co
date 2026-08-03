"""
Script para verificar alt text en todas las imágenes del sitio
"""

import re
from pathlib import Path
from collections import defaultdict

def audit_alt_text(file_path):
    """
    Audita alt text en un archivo HTML
    
    Args:
        file_path: Ruta del archivo HTML
        
    Returns:
        Diccionario con análisis de imágenes
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar todas las imágenes
        img_pattern = r'<img[^>]+>'
        images = re.findall(img_pattern, content, re.IGNORECASE)
        
        if not images:
            return {
                'file': file_path.name,
                'total_images': 0,
                'images_with_alt': 0,
                'images_without_alt': 0,
                'issues': []
            }
        
        images_with_alt = 0
        images_without_alt = 0
        issues = []
        
        for img in images:
            # Buscar atributo alt
            alt_match = re.search(r'alt=["\']([^"\']*)["\']', img, re.IGNORECASE)
            
            if alt_match:
                alt_text = alt_match.group(1)
                if alt_text:  # Si tiene contenido
                    images_with_alt += 1
                else:  # Si está vacío alt=""
                    images_without_alt += 1
                    issues.append('Alt vacio')
            else:
                images_without_alt += 1
                issues.append('Sin alt')
        
        # Generar mensaje de issues
        issue_summary = []
        if images_without_alt > 0:
            issue_summary.append(f'{images_without_alt} sin alt')
        
        return {
            'file': file_path.name,
            'total_images': len(images),
            'images_with_alt': images_with_alt,
            'images_without_alt': images_without_alt,
            'percentage_with_alt': (images_with_alt / len(images) * 100) if images else 0,
            'issues': issue_summary
        }
        
    except Exception as e:
        return {
            'file': file_path.name,
            'total_images': 0,
            'images_with_alt': 0,
            'images_without_alt': 0,
            'percentage_with_alt': 0,
            'issues': [f'Error de lectura: {e}']
        }

def analyze_directory(directory_path):
    """
    Analiza todos los archivos HTML en un directorio
    
    Args:
        directory_path: Ruta del directorio
        
    Returns:
        Lista de análisis de imágenes
    """
    dir_path = Path(directory_path)
    
    if not dir_path.exists():
        print(f"Directorio no encontrado: {directory_path}")
        return []
    
    html_files = list(dir_path.glob('*.html'))
    
    if not html_files:
        print(f"No hay archivos HTML en: {directory_path}")
        return []
    
    print(f"\nAnalizando {len(html_files)} archivos en {directory_path}:")
    
    analyses = []
    for html_file in html_files:
        analysis = audit_alt_text(html_file)
        analyses.append(analysis)
        
        if analysis['issues']:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])} ({analysis['total_images']} imagenes)")
        else:
            print(f"  + {analysis['file']}: OK ({analysis['total_images']} imagenes)")
    
    return analyses

def generate_summary(all_analyses):
    """
    Genera resumen del análisis de alt text
    
    Args:
        all_analyses: Lista de todos los análisis
        
    Returns:
        Diccionario con resumen
    """
    total_files = len(all_analyses)
    total_images = sum(a['total_images'] for a in all_analyses)
    total_with_alt = sum(a['images_with_alt'] for a in all_analyses)
    total_without_alt = sum(a['images_without_alt'] for a in all_analyses)
    files_with_issues = sum(1 for a in all_analyses if a['issues'])
    
    return {
        'total_files': total_files,
        'total_images': total_images,
        'total_with_alt': total_with_alt,
        'total_without_alt': total_without_alt,
        'files_with_issues': files_with_issues,
        'percentage_with_alt': (total_with_alt / total_images * 100) if total_images > 0 else 0
    }

def main():
    """Función principal"""
    base_dir = Path(__file__).parent
    
    print("Iniciando verificacion de alt text en imagenes")
    print("=" * 60)
    
    all_analyses = []
    
    # Analizar archivos principales
    main_html_files = list(base_dir.glob('*.html'))
    print(f"\nAnalizando {len(main_html_files)} archivos principales:")
    
    for html_file in main_html_files:
        analysis = audit_alt_text(html_file)
        all_analyses.append(analysis)
        
        if analysis['issues']:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])} ({analysis['total_images']} imagenes)")
        else:
            print(f"  + {analysis['file']}: OK ({analysis['total_images']} imagenes)")
    
    # Generar resumen
    summary = generate_summary(all_analyses)
    
    print("\n" + "=" * 60)
    print("RESUMEN DE AUDITORIA")
    print("=" * 60)
    print(f"Total archivos analizados: {summary['total_files']}")
    print(f"Total imagenes: {summary['total_images']}")
    print(f"Imagenes con alt: {summary['total_with_alt']} ({summary['percentage_with_alt']:.1f}%)")
    print(f"Imagenes sin alt: {summary['total_without_alt']}")
    print(f"Archivos con problemas: {summary['files_with_issues']}")
    
    # Mostrar archivos con problemas
    files_with_problems = [a for a in all_analyses if a['issues']]
    if files_with_problems:
        print("\nARCHIVOS CON PROBLEMAS:")
        for analysis in files_with_problems:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])} ({analysis['total_images']} imagenes)")
    
    print("\nVerificacion de alt text completada")

if __name__ == "__main__":
    main()