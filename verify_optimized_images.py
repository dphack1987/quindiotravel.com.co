#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Verificar calidad y dimensiones de imágenes optimizadas
Asegura que la optimización no causó problemas de visualización
"""

from pathlib import Path
from PIL import Image
import json

# Imágenes optimizadas para verificar
OPTIMIZED_IMAGES = [
    'assets/images/paisajes/valle-cocora-river-reflection.webp',
    'assets/images/paisajes/palma-cera-sunlight.webp', 
    'assets/images/paisajes/eje-cafetero-sunset-hills.webp',
    'assets/images/paisajes/palm-trees-misty-valley.webp',
    'assets/images/paisajes/valle-cocora-hero-banner.webp',
    'assets/images/paisajes/eje-cafetero-aerial-view.webp',
    'assets/images/paisajes/natural-landscapes-colombia.webp',
]

# Contextos donde se usan estas imágenes (del análisis de index.html)
IMAGE_CONTEXTS = {
    'valle-cocora-river-reflection.webp': 'Uso desconocido - verificar',
    'palma-cera-sunlight.webp': 'Hero banner - Planes Especiales Diciembre',
    'eje-cafetero-sunset-hills.webp': 'Uso desconocido - verificar',
    'palm-trees-misty-valley.webp': 'Uso desconocido - verificar',
    'valle-cocora-hero-banner.webp': 'Hero banner - Promociones y popup',
    'eje-cafetero-aerial-view.webp': 'Hero banner - Plan Exclusivo + OG image',
    'natural-landscapes-colombia.webp': 'Hero principal - Background hero section',
}

# Dimensiones mínimas aceptables por contexto
MIN_DIMENSIONS = {
    'hero_principal': (1200, 630),  # Hero principal necesita más resolución
    'hero_banner': (945, 630),     # Hero banners secundarios
    'card': (400, 300),            # Cards y elementos pequeños
    'thumbnail': (200, 150),       # Thumbnails
}

def analyze_image(img_path):
    """Analizar una imagen optimizada"""
    try:
        img = Image.open(img_path)
        file_size = img_path.stat().st_size / 1024  # KB
        
        analysis = {
            'file': img_path.name,
            'dimensions': f"{img.width}x{img.height}",
            'format': img.format,
            'mode': img.mode,
            'size_kb': round(file_size, 1),
            'context': IMAGE_CONTEXTS.get(img_path.name, 'Desconocido'),
            'issues': []
        }
        
        # Verificar dimensiones
        if img.width < 300 or img.height < 200:
            analysis['issues'].append(f"Dimensiones muy pequeñas: {img.width}x{img.height}")
        
        # Verificar si es hero principal
        if 'natural-landscapes-colombia' in img_path.name:
            if img.width < 800 or img.height < 600:
                analysis['issues'].append("Hero principal necesita mejor resolución")
        
        # Verificar calidad básica
        if file_size < 30:
            analysis['issues'].append(f"Tamaño muy pequeño: {file_size:.1f}KB - posible pérdida de calidad")
        
        # Verificar formato
        if img.format != 'WEBP':
            analysis['issues'].append(f"Formato incorrecto: {img.format} (debería ser WEBP)")
        
        return analysis
        
    except Exception as e:
        return {
            'file': img_path.name,
            'error': str(e),
            'issues': [f"Error al analizar: {e}"]
        }

def check_html_references():
    """Verificar referencias a estas imágenes en HTML"""
    base_dir = Path.cwd()
    references = {}
    
    for img_name in OPTIMIZED_IMAGES:
        img_file = Path(img_name).name
        references[img_file] = []
        
        # Buscar en archivos HTML principales
        for html_file in base_dir.glob('*.html'):
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if img_file in content:
                        references[img_file].append(html_file.name)
            except:
                pass
    
    return references

def main():
    print("🔍 VERIFICACIÓN DE IMÁGENES OPTIMIZADAS")
    print("="*80)
    
    base_dir = Path.cwd()
    all_issues = []
    
    print("\n📊 ANÁLISIS DE CALIDAD Y DIMENSIONES")
    print("-"*80)
    
    for img_name in OPTIMIZED_IMAGES:
        img_path = base_dir / img_name
        if img_path.exists():
            analysis = analyze_image(img_path)
            
            print(f"\n📸 {analysis['file']}")
            print(f"   Dimensiones: {analysis['dimensions']}")
            print(f"   Formato: {analysis['format']}, Modo: {analysis['mode']}")
            print(f"   Tamaño: {analysis['size_kb']}KB")
            print(f"   Contexto: {analysis['context']}")
            
            if analysis['issues']:
                print(f"   ⚠️ PROBLEMAS:")
                for issue in analysis['issues']:
                    print(f"      - {issue}")
                    all_issues.append((analysis['file'], issue))
            else:
                print(f"   ✅ Sin problemas detectados")
        else:
            print(f"\n❌ No encontrada: {img_name}")
            all_issues.append((img_name, "Archivo no encontrado"))
    
    print("\n" + "="*80)
    print("🔗 REFERENCIAS EN HTML")
    print("-"*80)
    
    references = check_html_references()
    for img_file, html_files in references.items():
        if html_files:
            print(f"\n📸 {img_file}")
            print(f"   Referenciado en: {', '.join(html_files)}")
        else:
            print(f"\n⚠️ {img_file}")
            print(f"   NO referenciado en HTML principales - podría no usarse")
    
    print("\n" + "="*80)
    print("📋 RESUMEN DE PROBLEMAS")
    print("-"*80)
    
    if all_issues:
        print(f"\n⚠️ Se encontraron {len(all_issues)} problemas:")
        for file, issue in all_issues:
            print(f"   - {file}: {issue}")
    else:
        print("\n✅ No se encontraron problemas")
    
    print("\n" + "="*80)
    
    # Guardar reporte
    from datetime import datetime
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_images': len(OPTIMIZED_IMAGES),
        'issues_found': len(all_issues),
        'detailed_issues': all_issues,
        'html_references': references
    }
    
    with open(base_dir / 'image_verification_report.json', 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print("📁 Reporte guardado: image_verification_report.json")

if __name__ == '__main__':
    main()