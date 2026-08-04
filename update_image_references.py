"""
Actualizar Referencias de Imágenes Renombradas
Actualiza rutas de imágenes en index.html con nuevos nombres descriptivos
"""

from pathlib import Path
import sys
import io

# Configurar encoding para Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def update_image_references():
    """Actualiza referencias de imágenes en index.html"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mapeo de nombres viejos a nuevos
    image_mapping = {
        "foto_hero1.jpg": "valle-cocora-hero-banner.jpg",
        "foto-jeep.jpg": "jeep-willys-eje-cafetero.jpg",
        "landscape-with-palm-trees-foreground-mountains-background.jpg": "palm-trees-mountains-background.jpg",
        "10834.jpg": "valle-cocora-palmas-cera-sunset.jpg",
        "56855.jpg": "eje-cafetero-landscape-colombia.jpg"
    }
    
    updated_count = 0
    
    for old_name, new_name in image_mapping.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            print(f"[OK] Actualizado: {old_name} -> {new_name}")
            updated_count += 1
        else:
            print(f"[SKIP] No encontrado: {old_name}")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\nTotal actualizaciones: {updated_count}")
    return updated_count

if __name__ == "__main__":
    print("Actualizando referencias de imágenes renombradas...")
    print("=" * 70)
    
    update_image_references()
    
    print("\n" + "=" * 70)
    print("Actualización de referencias completada")