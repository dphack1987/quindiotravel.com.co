#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

# Imagen actual (problemática)
CURRENT_HERO = 'assets/images/paisajes/natural-landscapes-colombia.webp'

# Imagen alternativa con mejores dimensiones
ALTERNATIVE_HERO = 'assets/images/paisajes/valle-cocora-palmas-cera-sunset.webp'

def optimize_alternative_hero():
    """Optimizar imagen alternativa para usar como hero principal"""
    alt_path = Path(ROOT_PATH) / ALTERNATIVE_HERO
    
    if not alt_path.exists():
        print(f"ERROR: No encontrada {ALTERNATIVE_HERO}")
        return False
    
    try:
        img = Image.open(alt_path)
        current_size = alt_path.stat().st_size / 1024
        
        print(f"Imagen alternativa actual:")
        print(f"  Dimensiones: {img.width}x{img.height}")
        print(f"  Tamaño: {current_size:.1f}KB")
        
        # Optimizar para hero: máximo 1920x1080, calidad alta pero peso razonable
        target_width = 1920
        target_height = 1080
        
        if img.width > target_width or img.height > target_height:
            aspect = img.width / img.height
            if aspect > target_width / target_height:
                new_width = target_width
                new_height = int(target_width / aspect)
            else:
                new_height = target_height
                new_width = int(target_height * aspect)
            
            print(f"Redimensionando: {img.width}x{img.height} → {new_width}x{new_height}")
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Guardar optimizada
        img.save(alt_path, 'WEBP', quality=85, optimize=True, method=6)
        
        new_size = alt_path.stat().st_size / 1024
        reduction = ((current_size - new_size) / current_size) * 100
        
        print(f"Resultado:")
        print(f"  Dimensiones: {img.width}x{img.height}")
        print(f"  Tamaño: {new_size:.1f}KB (era {current_size:.1f}KB)")
        print(f"  Reduccion: {reduction:.1f}%")
        
        return True
        
    except Exception as e:
        print(f"ERROR: {e}")
        return False

def update_html_reference():
    """Actualizar referencia en index.html"""
    html_path = Path(ROOT_PATH) / 'index.html'
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Reemplazar referencia de imagen hero
        old_ref = 'assets/images/paisajes/natural-landscapes-colombia.webp'
        new_ref = 'assets/images/paisajes/valle-cocora-palmas-cera-sunset.webp'
        
        if old_ref in content:
            content = content.replace(old_ref, new_ref)
            
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"\nReferencia actualizada en index.html")
            print(f"  {old_ref} → {new_ref}")
            return True
        else:
            print(f"\nWARNING: No se encontro referencia {old_ref} en index.html")
            return False
            
    except Exception as e:
        print(f"ERROR actualizando HTML: {e}")
        return False

def main():
    print("REEMPLAZO DE IMAGEN HERO PRINCIPAL")
    print("="*60)
    
    print("\n1. Optimizando imagen alternativa...")
    success = optimize_alternative_hero()
    
    if success:
        print("\n2. Actualizando referencia en HTML...")
        update_html_reference()
    
    print("\n" + "="*60)
    print("Proceso completado")
    print("Nueva imagen hero: valle-cocora-palmas-cera-sunset.webp")
    print("Dimensiones optimizadas para background full-width")

if __name__ == '__main__':
    main()