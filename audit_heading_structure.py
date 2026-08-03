"""
Script para auditar la estructura de encabezados (H1-H6) en todas las páginas HTML
"""

import re
from pathlib import Path
from collections import defaultdict

def audit_heading_structure(file_path):
    """
    Audita la estructura de encabezados en un archivo HTML
    
    Args:
        file_path: Ruta del archivo HTML
        
    Returns:
        Diccionario con análisis de encabezados
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Buscar todos los encabezados
        heading_pattern = r'<h([1-6])[^>]*>(.*?)</h\1>'
        headings = re.findall(heading_pattern, content, re.IGNORECASE | re.DOTALL)
        
        if not headings:
            return {
                'file': file_path.name,
                'has_h1': False,
                'h1_count': 0,
                'total_headings': 0,
                'heading_structure': [],
                'issues': ['No hay encabezados']
            }
        
        heading_structure = []
        h1_count = 0
        last_level = 0
        
        for level, text in headings:
            level = int(level)
            # Limpiar el texto del encabezado
            clean_text = re.sub(r'<[^>]+>', '', text).strip()
            
            heading_structure.append({
                'level': level,
                'text': clean_text[:50] + '...' if len(clean_text) > 50 else clean_text
            })
            
            if level == 1:
                h1_count += 1
            
            # Verificar saltos de nivel
            if last_level > 0 and level > last_level + 1:
                pass  # Salto de nivel detectado
            
            last_level = level
        
        issues = []
        
        # Verificar si hay H1
        has_h1 = h1_count > 0
        
        if not has_h1:
            issues.append('No hay H1')
        elif h1_count > 1:
            issues.append(f'Hay {h1_count} H1 (debería haber solo 1)')
        
        # Verificar estructura lógica
        if heading_structure:
            first_heading = heading_structure[0]['level']
            if first_heading != 1:
                issues.append(f'El primer encabezado es H{first_heading}, debería ser H1')
        
        return {
            'file': file_path.name,
            'has_h1': has_h1,
            'h1_count': h1_count,
            'total_headings': len(heading_structure),
            'heading_structure': heading_structure,
            'issues': issues
        }
        
    except Exception as e:
        return {
            'file': file_path.name,
            'has_h1': False,
            'h1_count': 0,
            'total_headings': 0,
            'heading_structure': [],
            'issues': [f'Error de lectura: {e}']
        }

def analyze_directory(directory_path):
    """
    Analiza todos los archivos HTML en un directorio
    
    Args:
        directory_path: Ruta del directorio
        
    Returns:
        Lista de análisis de encabezados
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
        analysis = audit_heading_structure(html_file)
        analyses.append(analysis)
        
        if analysis['issues']:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])}")
        else:
            print(f"  + {analysis['file']}: OK")
    
    return analyses

def generate_summary(all_analyses):
    """
    Genera resumen del análisis de encabezados
    
    Args:
        all_analyses: Lista de todos los análisis
        
    Returns:
        Diccionario con resumen
    """
    total_files = len(all_analyses)
    files_with_h1 = sum(1 for a in all_analyses if a['has_h1'])
    files_with_issues = sum(1 for a in all_analyses if a['issues'])
    files_multiple_h1 = sum(1 for a in all_analyses if a['h1_count'] > 1)
    
    return {
        'total_files': total_files,
        'files_with_h1': files_with_h1,
        'files_without_h1': total_files - files_with_h1,
        'files_with_issues': files_with_issues,
        'files_multiple_h1': files_multiple_h1,
        'percentage_with_h1': (files_with_h1 / total_files * 100) if total_files > 0 else 0
    }

def main():
    """Función principal"""
    base_dir = Path(__file__).parent
    
    print("Iniciando auditoria de estructura de encabezados")
    print("=" * 60)
    
    all_analyses = []
    
    # Analizar archivos principales
    main_html_files = list(base_dir.glob('*.html'))
    print(f"\nAnalizando {len(main_html_files)} archivos principales:")
    
    for html_file in main_html_files:
        analysis = audit_heading_structure(html_file)
        all_analyses.append(analysis)
        
        if analysis['issues']:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])}")
        else:
            print(f"  + {analysis['file']}: OK")
    
    # Generar resumen solo de archivos principales
    summary = generate_summary(all_analyses)
    
    print("\n" + "=" * 60)
    print("RESUMEN DE AUDITORIA")
    print("=" * 60)
    print(f"Total archivos analizados: {summary['total_files']}")
    print(f"Archivos con H1: {summary['files_with_h1']} ({summary['percentage_with_h1']:.1f}%)")
    print(f"Archivos sin H1: {summary['files_without_h1']}")
    print(f"Archivos con problemas: {summary['files_with_issues']}")
    print(f"Archivos con multiples H1: {summary['files_multiple_h1']}")
    
    # Mostrar archivos con problemas
    files_with_problems = [a for a in all_analyses if a['issues']]
    if files_with_problems:
        print("\nARCHIVOS CON PROBLEMAS:")
        for analysis in files_with_problems:
            print(f"  - {analysis['file']}: {', '.join(analysis['issues'])}")
    
    print("\nAuditoria de estructura de encabezados completada")

if __name__ == "__main__":
    main()