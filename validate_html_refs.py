#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

def validate_html_references():
    """Validar referencias de archivos en HTML"""
    print("\n" + "="*80)
    print("🔍 VALIDANDO REFERENCIAS EN HTML")
    print("="*80)
    
    # Extensiones de imagen
    img_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif', '.svg')
    
    # Buscar archivos HTML
    html_files = list(Path(ROOT_PATH).rglob('*.html'))
    html_files = [f for f in html_files if 'node_modules' not in str(f)]
    
    print(f"\n📁 Encontrados {len(html_files)} archivos HTML")
    
    issues = {
        'missing_files': [],
        'broken_links': [],
        'fixed': []
    }
    
    # Patrones para buscar referencias HTML y CSS inline.
    patterns = [
        r'src=["\']([^"\']+)["\']',
        r'href=["\']([^"\']+)["\']',
        r'content=["\']([^"\']+)["\']',
        r'data-src=["\']([^"\']+)["\']',
        r'url\(["\']?([^\)"\']+)["\']?\)'
    ]
    
    checked_references = set()

    for html_path in html_files:
        try:
            with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            for pattern in patterns:
                matches = re.findall(pattern, content)
                for match in matches:
                    # Solo revisar referencias a imágenes
                    ref_path = match.strip().split('#', 1)[0].split('?', 1)[0]
                    parsed = urlsplit(ref_path)

                    # Las URLs remotas no son archivos locales del proyecto.
                    if parsed.scheme or ref_path.startswith('//'):
                        continue

                    if not any(parsed.path.lower().endswith(ext) for ext in img_extensions):
                        continue

                    # Resolver rutas relativas y rutas locales que comienzan en /.
                    local_path = parsed.path.lstrip('/')
                    abs_path = (Path(ROOT_PATH) / local_path if ref_path.startswith('/')
                                else html_path.parent / local_path).resolve()
                    reference_key = (str(html_path), ref_path)
                    if reference_key in checked_references:
                        continue
                    checked_references.add(reference_key)
                        
                    if not abs_path.exists():
                        print(f"⚠️  {html_path.name}: Falta archivo '{ref_path}'")
                        issues['missing_files'].append({
                            'html_file': str(html_path),
                            'referenced': ref_path
                        })
        
        except Exception as e:
            print(f"❌ Error en {html_path.name}: {str(e)}")
    
    print(f"\n" + "="*80)
    print("📊 RESUMEN DE VALIDACIÓN")
    print("="*80)
    print(f"⚠️  Referencias faltantes: {len(issues['missing_files'])}")
    
    if issues['missing_files']:
        print("\nArchivos que necesitan ser actualizados:")
        for issue in issues['missing_files'][:10]:
            print(f"  - {issue['referenced']}")

if __name__ == '__main__':
    validate_html_references()
