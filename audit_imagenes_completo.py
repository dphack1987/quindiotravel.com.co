#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from pathlib import Path
from collections import defaultdict

# Extensiones de imagen y video
MEDIA_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp', '.avif', '.gif', '.bmp', '.mp4', '.webm', '.mov', '.avi')

def audit_images(root_path):
    """Auditoría completa de imágenes en el proyecto"""
    
    stats = {
        'total_files': 0,
        'by_extension': defaultdict(int),
        'by_folder': defaultdict(int),
        'by_folder_detail': {},
        'large_files': [],
        'file_list': []
    }
    
    root = Path(root_path)
    
    print("🔍 Escaneando proyecto completo...")
    print(f"Ruta: {root_path}\n")
    
    for fpath in root.rglob('*'):
        if fpath.is_file() and fpath.suffix.lower() in MEDIA_EXTENSIONS:
            # Ignorar node_modules
            if 'node_modules' in str(fpath):
                continue
            
            stats['total_files'] += 1
            ext = fpath.suffix.lower()
            stats['by_extension'][ext] += 1
            
            # Carpeta relativa
            rel_path = fpath.relative_to(root)
            folder = str(rel_path.parent)
            stats['by_folder'][folder] += 1
            
            # Tamaño
            size = fpath.stat().st_size
            stats['file_list'].append({
                'path': str(rel_path),
                'extension': ext,
                'size_mb': round(size / (1024*1024), 2),
                'size_kb': round(size / 1024, 2)
            })
            
            # Archivos > 5MB
            if size > 5 * 1024 * 1024:
                stats['large_files'].append({
                    'path': str(rel_path),
                    'size_mb': round(size / (1024*1024), 2)
                })
    
    return stats

# Ejecutar auditoría
root = r'c:\Users\user\Documents\www.quindiotravel.com'
results = audit_images(root)

print("=" * 80)
print("📊 AUDITORÍA COMPLETA DE IMÁGENES Y VIDEOS")
print("=" * 80)

print(f"\n✅ TOTAL DE ARCHIVOS: {results['total_files']}")

print("\n📁 POR EXTENSIÓN:")
for ext in sorted(results['by_extension'].keys()):
    count = results['by_extension'][ext]
    print(f"   {ext:10} : {count:4} archivos")

print("\n📂 TOP 20 CARPETAS CON MÁS ARCHIVOS:")
sorted_folders = sorted(results['by_folder'].items(), key=lambda x: x[1], reverse=True)
for i, (folder, count) in enumerate(sorted_folders[:20], 1):
    print(f"   {i:2}. {folder:60} : {count:4} archivos")

print(f"\n⚠️  ARCHIVOS GRANDES (>5MB): {len(results['large_files'])}")
for f in results['large_files'][:10]:
    print(f"   {f['path']:70} : {f['size_mb']:.2f} MB")

# Guardar análisis completo en JSON
output_file = os.path.join(root, 'analisis_imagenes_completo.json')
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump({
        'total': results['total_files'],
        'by_extension': dict(results['by_extension']),
        'by_folder': dict(results['by_folder']),
        'large_files': results['large_files'],
        'total_large_files': len(results['large_files'])
    }, f, indent=2, ensure_ascii=False)

print(f"\n✅ Análisis guardado en: analisis_imagenes_completo.json")
print("\n" + "=" * 80)
