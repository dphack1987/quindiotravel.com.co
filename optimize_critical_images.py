#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Optimizador de Imágenes Críticas para LCP
Enfocado en imágenes que causan problemas de Largest Contentful Paint
"""

from pathlib import Path
from PIL import Image
import json
from datetime import datetime

# Configuración específica para imágenes críticas
ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'
CRITICAL_THRESHOLD_KB = 200  # Optimizar imágenes >200KB
TARGET_SIZE_KB = 150         # Objetivo: máximo 150KB
MAX_WIDTH = 1200            # Ancho máximo para imágenes hero
MAX_HEIGHT = 630            # Alto máximo para imágenes hero
QUALITY = 80               # Calidad alta pero optimizada

# Imágenes críticas específicas a optimizar
CRITICAL_IMAGES = [
    'assets/images/paisajes/valle-cocora-river-reflection.webp',
    'assets/images/paisajes/palma-cera-sunlight.webp', 
    'assets/images/paisajes/eje-cafetero-sunset-hills.webp',
    'assets/images/paisajes/palm-trees-misty-valley.webp',
    'assets/images/paisajes/valle-cocora-hero-banner.webp',
    'assets/images/paisajes/eje-cafetero-aerial-view.webp',
    'assets/images/paisajes/natural-landscapes-colombia.webp',
]

class CriticalImageOptimizer:
    def __init__(self, root_path):
        self.root = Path(root_path)
        self.stats = {'optimized': [], 'errors': [], 'skipped': []}
        
    def optimize_image(self, img_path):
        """Optimizar una imagen individual"""
        try:
            original_size = img_path.stat().st_size / 1024  # KB
            original_size_mb = img_path.stat().st_size / (1024*1024)  # MB
            
            # Abrir imagen
            img = Image.open(img_path)
            original_format = img.format or 'WEBP'
            original_mode = img.mode
            
            print(f"📸 Procesando: {img_path.name}")
            print(f"   Original: {original_size:.1f}KB ({original_size_mb:.2f}MB)")
            print(f"   Formato: {original_format}, Modo: {original_mode}")
            print(f"   Dimensiones: {img.width}x{img.height}")
            
            # Redimensionar si es muy grande
            if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
                aspect = img.width / img.height
                if aspect > MAX_WIDTH / MAX_HEIGHT:
                    new_width = MAX_WIDTH
                    new_height = int(MAX_WIDTH / aspect)
                else:
                    new_height = MAX_HEIGHT
                    new_width = int(MAX_HEIGHT * aspect)
                
                print(f"   Redimensionando: {img.width}x{img.height} → {new_width}x{new_height}")
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Convertir a RGB si es necesario (para JPEG)
            if original_format == 'JPEG' and img.mode in ('RGBA', 'LA', 'P'):
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
                img = rgb_img
                print(f"   Convertido: {original_mode} → RGB")
            
            # Guardar con optimización
            save_format = 'WEBP' if original_format == 'WEBP' else 'JPEG'
            save_kwargs = {
                'format': save_format,
                'quality': QUALITY,
                'optimize': True,
                'method': 6  # Método de compresión agresivo para WebP
            }
            
            if save_format == 'WEBP':
                save_kwargs['lossless'] = False  # Usar compresión con pérdida
                save_kwargs['method'] = 6  # Compresión máxima
            
            img.save(img_path, **save_kwargs)
            
            new_size = img_path.stat().st_size / 1024  # KB
            new_size_mb = img_path.stat().st_size / (1024*1024)  # MB
            reduction = ((original_size - new_size) / original_size) * 100
            
            print(f"   ✅ Optimizado: {new_size:.1f}KB ({new_size_mb:.2f}MB)")
            print(f"   📉 Reducción: {reduction:.1f}%")
            
            # Verificar si cumple objetivo
            if new_size <= TARGET_SIZE_KB:
                print(f"   ✨ Cumple objetivo (<{TARGET_SIZE_KB}KB)")
            else:
                print(f"   ⚠️ Sobre objetivo ({new_size:.1f}KB > {TARGET_SIZE_KB}KB)")
            
            self.stats['optimized'].append({
                'file': str(img_path),
                'original_kb': round(original_size, 1),
                'new_kb': round(new_size, 1),
                'reduction_percent': round(reduction, 1),
                'meets_target': new_size <= TARGET_SIZE_KB
            })
            
            return True
            
        except Exception as e:
            print(f"   ❌ Error: {str(e)}")
            self.stats['errors'].append({
                'file': str(img_path),
                'error': str(e)
            })
            return False
    
    def optimize_critical_images(self):
        """Optimizar imágenes críticas específicas"""
        print("\n" + "="*80)
        print("⚡ OPTIMIZANDO IMÁGENES CRÍTICAS PARA LCP")
        print("="*80)
        print(f"🎯 Objetivo: Reducir imágenes a <{TARGET_SIZE_KB}KB")
        print(f"📏 Dimensiones máximas: {MAX_WIDTH}x{MAX_HEIGHT}")
        print(f"🎨 Calidad: {QUALITY}%")
        print()
        
        for img_name in CRITICAL_IMAGES:
            img_path = self.root / img_name
            if img_path.exists():
                print(f"\n{'─'*60}")
                self.optimize_image(img_path)
            else:
                print(f"⚠️ No encontrada: {img_name}")
                self.stats['skipped'].append(img_name)
    
    def generate_report(self):
        """Generar reporte final"""
        print("\n" + "="*80)
        print("📋 REPORTE FINAL - OPTIMIZACIÓN LCP")
        print("="*80)
        
        print(f"\n✅ IMÁGENES OPTIMIZADAS: {len(self.stats['optimized'])}")
        print(f"❌ ERRORES: {len(self.stats['errors'])}")
        print(f"⏭️ OMITIDAS: {len(self.stats['skipped'])}")
        
        if self.stats['optimized']:
            total_original = sum(s['original_kb'] for s in self.stats['optimized'])
            total_new = sum(s['new_kb'] for s in self.stats['optimized'])
            total_reduction = ((total_original - total_new) / total_original) * 100
            saved = total_original - total_new
            
            meets_target = sum(1 for s in self.stats['optimized'] if s['meets_target'])
            
            print(f"\n📊 ESTADÍSTICAS:")
            print(f"   Tamaño original total: {total_original:.1f}KB ({total_original/1024:.2f}MB)")
            print(f"   Tamaño optimizado total: {total_new:.1f}KB ({total_new/1024:.2f}MB)")
            print(f"   Espacio ahorrado: {saved:.1f}KB ({saved/1024:.2f}MB)")
            print(f"   Reducción total: {total_reduction:.1f}%")
            print(f"   Cumplen objetivo: {meets_target}/{len(self.stats['optimized'])}")
            
            if meets_target < len(self.stats['optimized']):
                print(f"\n⚠️ {len(self.stats['optimized']) - meets_target} imágenes aún sobre objetivo")
        
        # Guardar reporte
        report_file = self.root / 'critical_images_optimization_report.json'
        report_data = {
            'timestamp': datetime.now().isoformat(),
            'target_size_kb': TARGET_SIZE_KB,
            'optimized_count': len(self.stats['optimized']),
            'errors_count': len(self.stats['errors']),
            'skipped_count': len(self.stats['skipped']),
            'optimized_files': self.stats['optimized'],
            'errors': self.stats['errors'],
            'skipped': self.stats['skipped']
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📁 Reporte guardado: {report_file.name}")
        print("="*80)

if __name__ == '__main__':
    print("\n🚀 OPTIMIZADOR DE IMÁGENES CRÍTICAS PARA LCP")
    print(f"📂 Ruta: {ROOT_PATH}\n")
    
    try:
        optimizer = CriticalImageOptimizer(ROOT_PATH)
        optimizer.optimize_critical_images()
        optimizer.generate_report()
        
        print("\n✨ ¡PROCESO COMPLETADO!")
        print("🎯 Impacto esperado: LCP mejorado significativamente")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()