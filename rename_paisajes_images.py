"""
Renombrar Imágenes de Paisajes con Nombres Descriptivos
Elimina números de planes y usa keywords SEO descriptivas
"""

from pathlib import Path
import shutil

def rename_paisajes_images():
    """Renombra imágenes de paisajes con nombres descriptivos"""
    
    paisajes_path = Path(__file__).parent / "assets" / "images" / "paisajes"
    
    # Mapeo de nombres actuales a nombres descriptivos (sin números de planes)
    rename_mapping = {
        "10834.jpg": "valle-cocora-palmas-cera-sunset.jpg",
        "360_F_1993830573_bL6hcmQxqtnes4BIPHaux9ZdrOii20bm.jpg": "valle-cocora-morning-mist.jpg",
        "56855.jpg": "eje-cafetero-landscape-colombia.jpg",
        "D5VTOP7OQ5EYDJZUEMFDPXZ22E.jpg": "coffee-plantation-sunset-colombia.jpg",
        "depositphotos_517177072-stock-photo-salento-colombia-july-2021-beautiful.jpg": "salento-colombia-beautiful-town.jpg",
        "depositphotos_604446036-stock-photo-views-cocora-valley-its-tall.jpg": "valle-cocora-tall-palms.jpg",
        "foto_hero1.jpg": "valle-cocora-hero-banner.jpg",
        "foto-jeep.jpg": "jeep-willys-eje-cafetero.jpg",
        "high-angle-shot-beautiful-tree-covered-mountain-valleys-cloudy-sky.jpg": "eje-cafetero-mountain-valleys-cloudy.jpg",
        "images (1).jfif": "quindio-traditional-town.jfif",
        "images (2).jfif": "filandia-colonial-architecture.jfif",
        "images (5).jfif": "armenia-city-view.jfif",
        "images.jfif": "salento-colorful-houses.jfif",
        "istockphoto-1347870326-612x612.jpg": "coffee-beans-colombia-closeup.jpg",
        "landscape-with-palm-trees-foreground-mountains-background.jpg": "palm-trees-mountains-background.jpg",
        "MICE Paisaje  - 140 Foto Sebastian Sanint.ssanint (1).jpg": "eje-cafetero-aerial-view.jpg",
        "montanas-region-quindio-colombia_926199-3851242.jpg": "quindio-mountains-colombia.jpg",
        "paisajes-naturales-colombia_782077-226.avif": "natural-landscapes-colombia.avif",
        "pexels-brooke-laven-238543175-14762491.jpg": "coffee-plantation-green.jpg",
        "pexels-deniss-bojanini-174298580-13371168.jpg": "valle-cocora-river-reflection.jpg",
        "pexels-edgar-rodrigo-235374482-28405101.jpg": "palma-cera-sunlight.jpg",
        "pexels-imagenesclau-36459595.jpg": "eje-cafetero-green-mountains.jpg",
        "pexels-jess-londono-47825207-15699623.jpg": "coffee-region-cloudy-sky.jpg",
        "pexels-juan-diavanera-2150627805-33185965.jpg": "colombian-coffee-fields.jpg",
        "pexels-mateodavilah-13566752.jpg": "eje-cafetero-sunset-hills.jpg",
        "pexels-pepelpro-17073858.jpg": "quindio-mountain-range.jpg",
        "pexels-sebasvargas0220-6758257.jpg": "coffee-nature-panorama.jpg",
        "pexels-yuraforrat-12769582.jpg": "palm-trees-misty-valley.jpg"
    }
    
    renamed_count = 0
    skipped_count = 0
    
    for old_name, new_name in rename_mapping.items():
        old_path = paisajes_path / old_name
        new_path = paisajes_path / new_name
        
        if old_path.exists():
            try:
                shutil.move(old_path, new_path)
                print(f"[OK] Renombrado: {old_name} → {new_name}")
                renamed_count += 1
            except Exception as e:
                print(f"[ERROR] No se pudo renombrar {old_name}: {e}")
                skipped_count += 1
        else:
            print(f"[SKIP] Archivo no encontrado: {old_name}")
            skipped_count += 1
    
    print(f"\nResumen:")
    print(f"Renombrados: {renamed_count}")
    print(f"Saltados: {skipped_count}")
    
    return renamed_count

if __name__ == "__main__":
    print("Renombrando imágenes de paisajes con nombres descriptivos...")
    print("=" * 70)
    
    rename_paisajes_images()
    
    print("\n" + "=" * 70)
    print("Renombrado completado")