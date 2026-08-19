#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from PIL import Image
import json

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

def analyze_png_files():
    """Analizar archivos PNG para decidir conversión o optimización"""
    print("\n" + "="*80)
    print("🔍 ANÁLISIS DE ARCHIVOS PNG")
    print("="*80)
    
    png_files = list(Path(ROOT_PATH).rglob('*.png'))
    # Excluir node_modules
    png_files = [f for f in png_files if 'node_modules' not in str(f)]
    
    print(f"\n📁 Encontrados {len(png_files)} archivos PNG\n")
    
    analysis = {
        'total': len(png_files),
        'with_transparency': [],
        'solid_color': [],
        'large_files': [],
        'logos_icons': []
    }
    
    for i, png_path in enumerate(png_files, 1):
        try:
            size_mb = png_path.stat().st_size / (1024*1024)
            img = Image.open(png_path)
            
            # Información del archivo
            has_alpha = img.mode in ('RGBA', 'LA', 'P')
            width, height = img.size
            
            print(f"{i:2}. {png_path.name}")
            print(f"    Tamaño: {size_mb:.2f} MB | Dimensiones: {width}x{height} | Modo: {img.mode}")
            
            # Clasificar
            is_logo = 'logo' in str(png_path).lower() or 'icon' in str(png_path).lower()
            
            if is_logo or has_alpha:
                print(f"    → ✅ MANTENER (Logo/Ícono con transparencia)")
                analysis['logos_icons'].append({
                    'file': str(png_path),
                    'size_mb': size_mb,
                    'has_alpha': has_alpha
                })
            elif size_mb > 5:
                print(f"    → ⚠️  OPTIMIZAR (Archivo grande)")
                analysis['large_files'].append({
                    'file': str(png_path),
                    'size_mb': size_mb
                })
            elif has_alpha:
                print(f"    → ✅ MANTENER (Con transparencia)")
                analysis['with_transparency'].append({
                    'file': str(png_path),
                    'size_mb': size_mb
                })
            else:
                print(f"    → 🔄 CONVERTIR A JPG (Sin transparencia)")
                analysis['solid_color'].append({
                    'file': str(png_path),
                    'size_mb': size_mb
                })
            
            print()
            
        except Exception as e:
            print(f"    ❌ ERROR: {str(e)}\n")
    
    # Resumen
    print("\n" + "="*80)
    print("📊 RESUMEN DE ANÁLISIS PNG")
    print("="*80)
    print(f"\n✅ Logos/Iconos (MANTENER): {len(analysis['logos_icons'])}")
    print(f"✅ Con transparencia (MANTENER): {len(analysis['with_transparency'])}")
    print(f"⚠️  Archivos grandes (OPTIMIZAR): {len(analysis['large_files'])}")
    print(f"🔄 Convertibles a JPG: {len(analysis['solid_color'])}")
    
    # Guardar análisis
    output_file = Path(ROOT_PATH) / 'png_analysis.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(analysis, f, indent=2, ensure_ascii=False)
    
    print(f"\n📁 Análisis guardado: png_analysis.json")
    print("="*80)

if __name__ == '__main__':
    analyze_png_files()
