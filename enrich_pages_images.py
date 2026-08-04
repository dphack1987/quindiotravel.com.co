from pathlib import Path

def add_images_to_pages():
    index = Path(__file__).parent / "index.html"
    salento = Path(__file__).parent / "salento.html"
    filandia = Path(__file__).parent / "filandia.html"
    
    paisajes = [
        "valle-cocora-hero-banner.jpg",
        "valle-cocora-palmas-cera-sunset.jpg",
        "eje-cafetero-landscape-colombia.jpg",
        "coffee-plantation-sunset-colombia.jpg",
        "palm-trees-mountains-background.jpg"
    ]
    
    for page in [index, salento, filandia]:
        if page.exists():
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Añadir imágenes en header o hero section
            for img in paisajes:
                if img not in content:
                    img_tag = f'<img src="assets/images/paisajes/{img}" alt="{img}" class="section-image">'
                    content = content.replace('<section class="hero"', f'<div class="image-gallery">{img_tag}</div>\n    <section class="hero"')
            
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {page.name}")

if __name__ == "__main__":
    add_images_to_pages()