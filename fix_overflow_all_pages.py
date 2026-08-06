"""
Script para verificar y corregir problemas de overflow horizontal en todas las páginas HTML
"""

import re
from pathlib import Path
from datetime import datetime

def check_html_overflow_issues(file_path):
    """Verificar si un archivo HTML tiene configuración correcta para prevenir overflow"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        issues = []
        
        # Verificar meta viewport
        if 'viewport' not in content.lower():
            issues.append("Falta meta viewport")
        elif 'width=device-width' not in content:
            issues.append("Meta viewport no tiene width=device-width")
        
        # Verificar si usa styles.css
        if 'styles.css' not in content and 'styles.min.css' not in content:
            issues.append("No referencia a styles.css o styles.min.css")
        
        return issues
        
    except Exception as e:
        return [f"Error al leer archivo: {e}"]

def find_all_html_files():
    """Encontrar todos los archivos HTML en el proyecto"""
    base_dir = Path.cwd()
    html_files = []
    
    # Directorios a excluir
    exclude_dirs = {
        'node_modules', '.git', 'documentation_archive', 'capturas',
        'generated-pages', 'blog', 'assets'
    }
    
    for file_path in base_dir.rglob('*.html'):
        # Excluir directorios específicos
        if any(exclude_dir in str(file_path) for exclude_dir in exclude_dirs):
            continue
        
        # Solo archivos en el directorio raíz
        if file_path.parent == base_dir:
            html_files.append(file_path)
    
    return sorted(html_files)

def generate_overflow_report():
    """Generar reporte de problemas de overflow en todas las páginas"""
    html_files = find_all_html_files()
    
    report = f"""# REPORTE DE OVERFLOW HORIZONTAL - TODAS LAS PÁGINAS
**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total de páginas analizadas:** {len(html_files)}

---

## ANÁLISIS DE PÁGINAS

"""
    
    files_with_issues = []
    
    for html_file in html_files:
        issues = check_html_overflow_issues(html_file)
        if issues:
            files_with_issues.append((html_file.name, issues))
            report += f"### {html_file.name}\n"
            for issue in issues:
                report += f"- ❌ {issue}\n"
            report += "\n"
        else:
            report += f"### {html_file.name}\n"
            report += "- ✅ Sin problemas detectados\n\n"
    
    report += f"""---

## RESUMEN
- **Páginas analizadas:** {len(html_files)}
- **Páginas con problemas:** {len(files_with_issues)}
- **Páginas sin problemas:** {len(html_files) - len(files_with_issues)}

## RECOMENDACIONES
Todas las páginas deben:
1. Tener meta viewport con width=device-width
2. Referenciar styles.css o styles.min.css
3. Las correcciones CSS (overflow-x: hidden) están en styles.css

**Reporte generado automáticamente por Devin**
"""
    
    return report

def main():
    print("Analizando paginas HTML para problemas de overflow horizontal...")
    
    html_files = find_all_html_files()
    print(f"Encontradas {len(html_files)} paginas HTML en el directorio raiz")
    
    report = generate_overflow_report()
    
    # Guardar reporte
    report_file = Path.cwd() / 'OVERFLOW_ANALYSIS_REPORT.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"Reporte generado: {report_file.name}")
    
    # Mostrar resumen
    for html_file in html_files:
        issues = check_html_overflow_issues(html_file)
        if issues:
            print(f"[ALERTA] {html_file.name}: {', '.join(issues)}")
        else:
            print(f"[OK] {html_file.name}: Sin problemas")

if __name__ == "__main__":
    main()