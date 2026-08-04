from pathlib import Path

project_root = Path(__file__).parent

# Archivos principales que deben estar en sitemap
main_files = [
    "index.html",
    "planes.html", 
    "blog.html",
    "salento.html",
    "filandia.html",
    "armenia.html",
    "hotel-campestre-cafe-cafe.html",
    "finca-hotel-la-dorada.html",
    "cabanas-la-esmeralda.html",
    "finca-hotel-los-girasoles.html",
    "hotel-campestre-la-tata.html",
    "hotel-campestre-las-camelias.html",
    "hotel-de-la-vega.html"
]

print("Checking main files in sitemap...")

sitemap_path = project_root / "sitemap.xml"
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

for filename in main_files:
    if filename in sitemap_content:
        print(f"[OK] {filename} in sitemap")
    else:
        print(f"[MISSING] {filename} not in sitemap")