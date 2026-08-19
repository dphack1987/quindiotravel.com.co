#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from PIL import Image
import json
from datetime import datetime

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'
QUALITY = 85

def convert_png_to_jpg():
    """Convertir PNG sin transparencia a JPG"""
    print("\n" + "="*80)
    print("🔄 CONVERTIENDO PNG → JPG (Sin Transparencia)")
    print("="*80)
    
    # PNG sin transparencia a convertir (según análisis)
    png_to_convert = [
        'chucho2.png',
        '1 (1).png',
        '1 (2).png',
        '1 (3).png',
        '1 (4).png',
        '1 (5).png',
        '1 (6).png'
    ]
    
    stats = {'converted': [], 'errors': []}
    
    # Buscar estos archivos en el proyecto
    root = Path(ROOT_PATH)
    found_files = []
    
    for png_name in png_to_convert:
        for png_path in root.rglob(png_name):
            if 'node_modules' not in str(png_path):
                found_files.append(png_path)
    
    print(f"\n📁 Encontrados {len(found_files)} archivos PNG a convertir\n")
    
    for i, png_path in enumerate(found_files, 1):
        try:
            original_size = png_path.stat().st_size / (1024*1024)
            
            # Abrir imagen
            img = Image.open(png_path)
            
            # Convertir a RGB si es necesario
            if img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    rgb_img.paste(img)
                else:
                    rgb_img.paste(img, mask=img.split()[-1])
                img = rgb_img
            
            # Nuevo nombre con extensión .jpg
            jpg_path = png_path.with_suffix('.jpg')
            
            # Guardar como JPG
            img.save(jpg_path, 'JPEG', quality=QUALITY, optimize=True)
            
            # Eliminar PNG original
            png_path.unlink()
            
            new_size = jpg_path.stat().st_size / (1024*1024)
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"{i}. ✅ {png_path.name} → {jpg_path.name}")
            print(f"   {original_size:.2f}MB → {new_size:.2f}MB ({reduction:.1f}% reducción)")
            
            stats['converted'].append({
                'original': str(png_path),
                'converted': str(jpg_path),
                'original_mb': round(original_size, 2),
                'new_mb': round(new_size, 2),
                'reduction_percent': round(reduction, 1)
            })
            
        except Exception as e:
            print(f"{i}. ❌ ERROR: {str(e)}")
            stats['errors'].append({
                'file': str(png_path),
                'error': str(e)
            })
    
    print(f"\n✅ Conversión completada: {len(stats['converted'])} archivos convertidos")
    print(f"❌ Errores: {len(stats['errors'])}")
    
    # Guardar reporte
    report_file = Path(ROOT_PATH) / 'png_conversion_report.json'
    report_data = {
        'timestamp': datetime.now().isoformat(),
        'converted_count': len(stats['converted']),
        'errors_count': len(stats['errors']),
        'files': stats['converted'],
        'errors': stats['errors']
    }
    
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n📁 Reporte guardado: png_conversion_report.json")
    print("="*80)

if __name__ == '__main__':
    convert_png_to_jpg()
