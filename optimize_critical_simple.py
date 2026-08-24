#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from PIL import Image
import json
from datetime import datetime

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'
CRITICAL_IMAGES = [
    'assets/images/paisajes/valle-cocora-river-reflection.webp',
    'assets/images/paisajes/palma-cera-sunlight.webp', 
    'assets/images/paisajes/eje-cafetero-sunset-hills.webp',
    'assets/images/paisajes/palm-trees-misty-valley.webp',
    'assets/images/paisajes/valle-cocora-hero-banner.webp',
    'assets/images/paisajes/eje-cafetero-aerial-view.webp',
    'assets/images/paisajes/natural-landscapes-colombia.webp',
]

def optimize_image(img_path):
    try:
        original_size = img_path.stat().st_size / 1024
        img = Image.open(img_path)
        
        print(f"Processing: {img_path.name}")
        print(f"Original: {original_size:.1f}KB, Size: {img.width}x{img.height}")
        
        # Resize if needed
        MAX_WIDTH = 1200
        MAX_HEIGHT = 630
        if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
            aspect = img.width / img.height
            if aspect > MAX_WIDTH / MAX_HEIGHT:
                new_width = MAX_WIDTH
                new_height = int(MAX_WIDTH / aspect)
            else:
                new_height = MAX_HEIGHT
                new_width = int(MAX_HEIGHT * aspect)
            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            print(f"Resized to: {new_width}x{new_height}")
        
        # Save optimized
        img.save(img_path, 'WEBP', quality=80, optimize=True, method=6)
        
        new_size = img_path.stat().st_size / 1024
        reduction = ((original_size - new_size) / original_size) * 100
        
        print(f"Optimized: {new_size:.1f}KB, Reduction: {reduction:.1f}%")
        print(f"Status: {'OK' if new_size < 200 else 'OVER TARGET'}")
        print()
        
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("Critical Image Optimizer for LCP")
    print(f"Path: {ROOT_PATH}")
    print()
    
    root = Path(ROOT_PATH)
    stats = {'optimized': 0, 'errors': 0}
    
    for img_name in CRITICAL_IMAGES:
        img_path = root / img_name
        if img_path.exists():
            if optimize_image(img_path):
                stats['optimized'] += 1
            else:
                stats['errors'] += 1
        else:
            print(f"Not found: {img_name}")
            print()
    
    print(f"Results: {stats['optimized']} optimized, {stats['errors']} errors")

if __name__ == '__main__':
    main()