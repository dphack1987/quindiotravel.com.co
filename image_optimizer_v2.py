#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path
from PIL import Image
import json
from datetime import datetime

# Configuración
ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'
QUALITY = 75
MAX_WIDTH = 1800
MAX_HEIGHT = 1800
SIZE_THRESHOLD_MB = 5

class ImageOptimizer:
    def __init__(self, root_path):
        self.root = Path(root_path)
        self.stats = {'optimized': [], 'errors': [], 'skipped': []}
        
    def optimize_large_images(self):
        """Optimizar imágenes grandes (>5MB) - Versión mejorada"""
        print("\n" + "="*80)
        print("⚡ OPTIMIZANDO ARCHIVOS GRANDES (>5MB)")
        print("="*80)
        
        large_files = []
        
        # Encontrar archivos grandes
        for ext in ['*.jpg', '*.png']:
            large_files.extend(self.root.rglob(ext))
        
        # Filtrar por tamaño
        large_files = [f for f in large_files 
                      if f.is_file() 
                      and f.stat().st_size > SIZE_THRESHOLD_MB * 1024 * 1024
                      and 'node_modules' not in str(f)]
        
        print(f"\n📁 Encontrados {len(large_files)} archivos > {SIZE_THRESHOLD_MB}MB\n")
        
        for i, img_path in enumerate(large_files, 1):
            try:
                original_size = img_path.stat().st_size / (1024*1024)
                
                # Abrir imagen
                img = Image.open(img_path)
                original_format = img.format
                
                # Redimensionar si es muy grande
                if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
                    aspect = img.width / img.height
                    if aspect > MAX_WIDTH / MAX_HEIGHT:
                        new_width = MAX_WIDTH
                        new_height = int(MAX_WIDTH / aspect)
                    else:
                        new_height = MAX_HEIGHT
                        new_width = int(MAX_HEIGHT * aspect)
                    
                    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Convertir a RGB si es necesario
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = rgb_img
                
                # Guardar optimizado
                img.save(img_path, 'JPEG', quality=QUALITY, optimize=True)
                
                new_size = img_path.stat().st_size / (1024*1024)
                reduction = ((original_size - new_size) / original_size) * 100
                
                print(f"{i:2}. ✅ {img_path.name}")
                print(f"    {original_size:.2f}MB → {new_size:.2f}MB ({reduction:.1f}% reducción)")
                
                self.stats['optimized'].append({
                    'file': str(img_path),
                    'original_mb': round(original_size, 2),
                    'new_mb': round(new_size, 2),
                    'reduction_percent': round(reduction, 1)
                })
                
            except Exception as e:
                print(f"{i:2}. ❌ {img_path.name}: {str(e)}")
                self.stats['errors'].append({
                    'file': str(img_path),
                    'error': str(e)
                })
        
        print(f"\n✅ Optimización completada: {len(self.stats['optimized'])} archivos optimizados")
        print(f"❌ Errores: {len(self.stats['errors'])}")
    
    def generate_report(self):
        """Generar reporte final"""
        print("\n" + "="*80)
        print("📋 REPORTE FINAL")
        print("="*80)
        
        print(f"\n✅ ARCHIVOS OPTIMIZADOS: {len(self.stats['optimized'])}")
        print(f"❌ ERRORES: {len(self.stats['errors'])}")
        
        if self.stats['optimized']:
            total_reduction = sum(s['reduction_percent'] for s in self.stats['optimized']) / len(self.stats['optimized'])
            total_original = sum(s['original_mb'] for s in self.stats['optimized'])
            total_new = sum(s['new_mb'] for s in self.stats['optimized'])
            saved = total_original - total_new
            
            print(f"\n📊 ESTADÍSTICAS:")
            print(f"   Tamaño original: {total_original:.2f} MB")
            print(f"   Tamaño optimizado: {total_new:.2f} MB")
            print(f"   Espacio ahorrado: {saved:.2f} MB")
            print(f"   Reducción promedio: {total_reduction:.1f}%")
        
        # Guardar reporte
        report_file = self.root / 'optimization_report.json'
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'optimized_count': len(self.stats['optimized']),
            'errors_count': len(self.stats['errors']),
            'optimized_files': self.stats['optimized'],
            'errors': self.stats['errors']
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Reporte guardado: optimization_report.json")
        print("="*80)

if __name__ == '__main__':
    optimizer = ImageOptimizer(ROOT_PATH)
    print("\n🚀 OPTIMIZADOR DE IMÁGENES (VERSIÓN MEJORADA)")
    print(f"📂 Ruta: {ROOT_PATH}\n")
    
    optimizer.optimize_large_images()
    optimizer.generate_report()
    
    print("\n✨ ¡PROCESO COMPLETADO!")
