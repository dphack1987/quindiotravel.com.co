#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

# Imagen hero principal necesita dimensiones para background full-width
HERO_IMAGE = 'assets/images/paisajes/natural-landscapes-colombia.webp'

# Dimensiones apropiadas para hero background (móvil hasta desktop 4K)
HERO_DIMENSIONS = {
    'mobile': (375, 667),      # Móvil estándar
    'tablet': (768, 1024),     # Tablet
    'desktop': (1920, 1080),   # Desktop HD
    'large': (2560, 1440),     # Desktop 2K
    'ultra': (3840, 2160)      # Desktop 4K
}

def fix_hero_image():
    """Re-optimizar imagen hero con dimensiones apropiadas"""
    hero_path = Path(ROOT_PATH) / HERO_IMAGE
    
    if not hero_path.exists():
        print(f"ERROR: No encontrada {HERO_IMAGE}")
        return False
    
    try:
        # Abrir imagen actual
        img = Image.open(hero_path)
        current_size = hero_path.stat().st_size / 1024
        
        print(f"Imagen hero actual:")
        print(f"  Dimensiones: {img.width}x{img.height}")
        print(f"  Tamaño: {current_size:.1f}KB")
        print(f"  Formato: {img.format}")
        
        # Para hero background, necesitamos como mínimo 1920px de ancho
        # pero mantener el peso bajo. Usaremos 1600x900 como balance
        target_width = 1600
        target_height = 900
        
        if img.width < target_width or img.height < target_height:
            print(f"\nWARNING: Dimensiones actuales demasiado pequeñas para hero background")
            print(f"  Mínimo recomendado: {target_width}x{target_height}")
            print(f"  Actuales: {img.width}x{img.height}")
            
            # No podemos mejorar la calidad sin el original, pero podemos
            # avisar del problema
            print(f"\n⚠️ La imagen necesita ser reemplazada con versión de mayor resolución")
            print(f"   Recomendación: Usar imagen original de al menos 1920x1080px")
            return False
        
        # Si las dimensiones son adecuadas, solo optimizar compresión
        print(f"\nDimensiones adecuadas para hero background")
        print(f"Optimizando compresión manteniendo dimensiones...")
        
        # Re-guardar con compresión agresiva pero manteniendo dimensiones
        img.save(hero_path, 'WEBP', quality=85, optimize=True, method=6)
        
        new_size = hero_path.stat().st_size / 1024
        reduction = ((current_size - new_size) / current_size) * 100
        
        print(f"\nResultado:")
        print(f"  Dimensiones: {img.width}x{img.height} (sin cambio)")
        print(f"  Tamaño: {new_size:.1f}KB (era {current_size:.1f}KB)")
        print(f"  Reducción: {reduction:.1f}%")
        
        if new_size < 200:
            print(f"  ✅ Cumple objetivo (<200KB)")
        else:
            print(f"  ⚠️ Sobre objetivo ({new_size:.1f}KB > 200KB)")
        
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def main():
    print("CORRECCIÓN DE IMAGEN HERO PRINCIPAL")
    print("="*60)
    
    success = fix_hero_image()
    
    print("\n" + "="*60)
    if success:
        print("Imagen hero optimizada correctamente")
    else:
        print("La imagen hero necesita ser reemplazada con versión de mayor resolución")

if __name__ == '__main__':
    main()