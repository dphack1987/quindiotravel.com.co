#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image

OPTIMIZED_IMAGES = [
    'assets/images/paisajes/valle-cocora-river-reflection.webp',
    'assets/images/paisajes/palma-cera-sunlight.webp', 
    'assets/images/paisajes/eje-cafetero-sunset-hills.webp',
    'assets/images/paisajes/palm-trees-misty-valley.webp',
    'assets/images/paisajes/valle-cocora-hero-banner.webp',
    'assets/images/paisajes/eje-cafetero-aerial-view.webp',
    'assets/images/paisajes/valle-cocora-palmas-cera-sunset.webp',  # Nueva hero principal
]

def main():
    print("Verificacion simple de imagenes optimizadas")
    base_dir = Path.cwd()
    
    for img_name in OPTIMIZED_IMAGES:
        img_path = base_dir / img_name
        if img_path.exists():
            try:
                img = Image.open(img_path)
                size_kb = img_path.stat().st_size / 1024
                print(f"OK {img_path.name}: {img.width}x{img.height}, {size_kb:.1f}KB")
            except Exception as e:
                print(f"ERROR {img_path.name}: {e}")
        else:
            print(f"ERROR {img_path.name}: No encontrada")

if __name__ == '__main__':
    main()