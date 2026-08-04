from pathlib import Path

# Implementación directa de lazy loading
index_path = Path(__file__).parent / "index.html"

with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Reemplazar imágenes específicas con lazy loading
replacements = [
    # Imágenes de hoteles (below-the-fold)
    ('<img src="assets/images/alojamientos/finca-hotel-los-girasoles.jpg"', 
     '<img src="assets/images/alojamientos/finca-hotel-los-girasoles.jpg" loading="lazy"'),
    
    ('<img src="assets/images/alojamientos/cabanas-la-esmeralda.jpg"',
     '<img src="assets/images/alojamientos/cabanas-la-esmeralda.jpg" loading="lazy"'),
    
    ('<img src="assets/images/alojamientos/hotel-campestre-cafe-cafe/IMG_0404-scaled.jpg"',
     '<img src="assets/images/alojamientos/hotel-campestre-cafe-cafe/IMG_0404-scaled.jpg" loading="lazy"'),
    
    # Imágenes de atractivos (below-the-fold)
    ('<img src="assets/images/atractivos/parque-del-cafe.jpg"',
     '<img src="assets/images/atractivos/parque-del-cafe.jpg" loading="lazy"'),
    
    ('<img src="assets/images/atractivos/panaca.jpg"',
     '<img src="assets/images/atractivos/panaca.jpg" loading="lazy"'),
    
    ('<img src="assets/images/atractivos/termales-santa-rosa.jpg"',
     '<img src="assets/images/atractivos/termales-santa-rosa.jpg" loading="lazy"'),
]

changes_made = 0
for old, new in replacements:
    if old in content:
        content = content.replace(old, new)
        changes_made += 1
        print(f"Lazy loading añadido: {old[:50]}...")

with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal cambios realizados: {changes_made}")