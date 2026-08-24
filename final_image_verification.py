#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image

# Imágenes optimizadas finales
OPTIMIZED_IMAGES = {
    'assets/images/paisajes/valle-cocora-river-reflection.webp': {'expected_dims': (343, 630), 'context': 'Uso desconocido'},
    'assets/images/paisajes/palma-cera-sunlight.webp': {'expected_dims': (472, 630), 'context': 'Hero banner - Planes Especiales'},
    'assets/images/paisajes/eje-cafetero-sunset-hills.webp': {'expected_dims': (472, 630), 'context': 'Uso desconocido'},
    'assets/images/paisajes/palm-trees-misty-valley.webp': {'expected_dims': (420, 630), 'context': 'Uso desconocido'},
    'assets/images/paisajes/valle-cocora-hero-banner.webp': {'expected_dims': (945, 630), 'context': 'Hero banner - Promociones'},
    'assets/images/paisajes/eje-cafetero-aerial-view.webp': {'expected_dims': (958, 630), 'context': 'Hero banner - Plan Exclusivo'},
    'assets/images/paisajes/valle-cocora-palmas-cera-sunset.webp': {'expected_dims': (1400, 933), 'context': 'HERO PRINCIPAL - Background'},
}

def main():
    print("VERIFICACION FINAL DE IMAGENES OPTIMIZADAS")
    print("="*70)
    
    base_dir = Path.cwd()
    all_ok = True
    
    for img_path, expected in OPTIMIZED_IMAGES.items():
        full_path = base_dir / img_path
        if full_path.exists():
            try:
                img = Image.open(full_path)
                size_kb = full_path.stat().st_size / 1024
                expected_dims = expected['expected_dims']
                context = expected['context']
                
                # Verificar dimensiones
                dims_ok = (img.width, img.height) == expected_dims
                
                # Verificar tamaño
                size_ok = size_kb < 200
                
                status = "OK" if dims_ok and size_ok else "WARNING"
                
                print(f"\n{status} {Path(img_path).name}")
                print(f"  Contexto: {context}")
                print(f"  Dimensiones: {img.width}x{img.height} (esperado: {expected_dims[0]}x{expected_dims[1]})")
                print(f"  Tamaño: {size_kb:.1f}KB")
                
                if not dims_ok:
                    print(f"  WARNING: Dimensiones incorrectas")
                    all_ok = False
                if not size_ok:
                    print(f"  WARNING: Tamaño sobre 200KB")
                    all_ok = False
                    
            except Exception as e:
                print(f"\nERROR {Path(img_path).name}: {e}")
                all_ok = False
        else:
            print(f"\nERROR {Path(img_path).name}: No encontrada")
            all_ok = False
    
    print("\n" + "="*70)
    if all_ok:
        print("RESULTADO: Todas las imagenes verificadas correctamente")
    else:
        print("RESULTADO: Se encontraron problemas que requieren atencion")
    print("="*70)

if __name__ == '__main__':
    main()