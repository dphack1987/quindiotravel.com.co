#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from pathlib import Path
from PIL import Image
import json
from datetime import datetime

# Configuración
ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'
QUALITY_HIGH = 85
QUALITY_MEDIUM = 80
QUALITY_LOW = 75
MAX_WIDTH = 2000
MAX_HEIGHT = 2000
SIZE_THRESHOLD_MB = 5  # Archivos > 5MB a optimizar

class ImageProcessor:
    def __init__(self, root_path):
        self.root = Path(root_path)
        self.stats = {
            'converted': [],
            'optimized': [],
            'errors': [],
            'skipped': []
        }
        
    def convert_jpeg_to_jpg(self):
        """Convertir todos los .jpeg a .jpg"""
        print("\n" + "="*80)
        print("🔄 FASE 1: CONVERTIR .JPEG A .JPG")
        print("="*80)
        
        jpeg_files = list(self.root.rglob('*.jpeg'))
        print(f"\n📁 Encontrados {len(jpeg_files)} archivos .jpeg")
        
        for jpeg_path in jpeg_files:
            # Ignorar node_modules
            if 'node_modules' in str(jpeg_path):
                continue
                
            try:
                # Nuevo nombre con extensión .jpg
                jpg_path = jpeg_path.with_suffix('.jpg')
                
                # Abrir imagen original
                img = Image.open(jpeg_path)
                
                # Convertir a RGB si es necesario (para JPEG)
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                    img = rgb_img
                
                # Guardar como JPG
                img.save(jpg_path, 'JPEG', quality=QUALITY_HIGH, optimize=True)
                
                # Eliminar archivo original
                jpeg_path.unlink()
                
                print(f"   ✅ {jpeg_path.name} → {jpg_path.name}")
                self.stats['converted'].append({
                    'original': str(jpeg_path),
                    'converted': str(jpg_path)
                })
                
            except Exception as e:
                print(f"   ❌ ERROR en {jpeg_path.name}: {str(e)}")
                self.stats['errors'].append({
                    'file': str(jpeg_path),
                    'error': str(e)
                })
        
        print(f"\n✅ Conversión completada: {len(self.stats['converted'])} archivos convertidos")
        
    def optimize_large_images(self):
        """Optimizar imágenes grandes (>5MB)"""
        print("\n" + "="*80)
        print("⚡ FASE 2: OPTIMIZAR ARCHIVOS GRANDES (>5MB)")
        print("="*80)
        
        large_files = []
        
        # Encontrar archivos grandes
        for ext in ['*.jpg', '*.jpeg', '*.png']:
            large_files.extend(self.root.rglob(ext))
        
        # Filtrar por tamaño
        large_files = [f for f in large_files 
                      if f.is_file() 
                      and f.stat().st_size > SIZE_THRESHOLD_MB * 1024 * 1024
                      and 'node_modules' not in str(f)]
        
        print(f"\n📁 Encontrados {len(large_files)} archivos > {SIZE_THRESHOLD_MB}MB")
        
        for img_path in large_files:
            try:
                original_size = img_path.stat().st_size / (1024*1024)
                
                # Abrir imagen
                img = Image.open(img_path)
                
                # Redimensionar si es muy grande
                if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
                    img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
                    print(f"   📐 Redimensionado: {img_path.name}")
                
                # Guardar con compresión
                # Determinar calidad basada en tamaño original
                if original_size > 15:
                    quality = QUALITY_LOW
                elif original_size > 10:
                    quality = QUALITY_MEDIUM
                else:
                    quality = QUALITY_HIGH
                
                # Convertir a RGB si es necesario
                if img.mode in ('RGBA', 'LA', 'P'):
                    rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        rgb_img.paste(Image.new('RGB', img.size, (255, 255, 255)))
                    else:
                        rgb_img.paste(img, mask=img.split()[-1])
                    img = rgb_img
                
                # Guardar optimizado
                img.save(img_path, 'JPEG', quality=quality, optimize=True)
                
                new_size = img_path.stat().st_size / (1024*1024)
                reduction = ((original_size - new_size) / original_size) * 100
                
                print(f"   ✅ {img_path.name}")
                print(f"      {original_size:.2f}MB → {new_size:.2f}MB ({reduction:.1f}% reducción)")
                
                self.stats['optimized'].append({
                    'file': str(img_path),
                    'original_mb': original_size,
                    'new_mb': new_size,
                    'reduction_percent': reduction
                })
                
            except Exception as e:
                print(f"   ❌ ERROR en {img_path.name}: {str(e)}")
                self.stats['errors'].append({
                    'file': str(img_path),
                    'error': str(e)
                })
        
        print(f"\n✅ Optimización completada: {len(self.stats['optimized'])} archivos optimizados")
    
    def generate_report(self):
        """Generar reporte de conversión"""
        print("\n" + "="*80)
        print("📋 REPORTE FINAL")
        print("="*80)
        
        print(f"\n✅ ARCHIVOS CONVERTIDOS (JPEG→JPG): {len(self.stats['converted'])}")
        print(f"✅ ARCHIVOS OPTIMIZADOS: {len(self.stats['optimized'])}")
        print(f"❌ ERRORES: {len(self.stats['errors'])}")
        
        if self.stats['optimized']:
            total_reduction = sum(s['reduction_percent'] for s in self.stats['optimized']) / len(self.stats['optimized'])
            print(f"📊 Reducción promedio: {total_reduction:.1f}%")
        
        # Guardar reporte en JSON
        report_file = self.root / 'conversion_report.json'
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'converted_count': len(self.stats['converted']),
            'optimized_count': len(self.stats['optimized']),
            'errors_count': len(self.stats['errors']),
            'optimized_files': self.stats['optimized'],
            'errors': self.stats['errors']
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Reporte guardado: conversion_report.json")
        print("="*80)

# Ejecutar
if __name__ == '__main__':
    processor = ImageProcessor(ROOT_PATH)
    
    print("\n🚀 INICIANDO CONVERSIÓN Y OPTIMIZACIÓN DE IMÁGENES")
    print(f"📂 Ruta: {ROOT_PATH}\n")
    
    # Fase 1: Convertir JPEG a JPG
    processor.convert_jpeg_to_jpg()
    
    # Fase 2: Optimizar archivos grandes
    processor.optimize_large_images()
    
    # Reporte
    processor.generate_report()
    
    print("\n✨ ¡PROCESO COMPLETADO!")
