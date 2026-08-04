from pathlib import Path

def enrich_pages_strategically():
    paisajes_path = Path(__file__).parent / "assets" / "images" / "paisajes"
    available_images = list(paisajes_path.glob("*.jpg")) + list(paisajes_path.glob("*.jfif")) + list(paisajes_path.glob("*.avif"))
    
    image_mapping = {
        "salento.html": ["valle-cocora-hero-banner.jpg", "valle-cocora-palmas-cera-sunset.jpg", "quindio-traditional-town.jfif"],
        "filandia.html": ["filandia-colonial-architecture.jfif", "eje-cafetero-landscape-colombia.jpg", "palm-trees-mountains-background.jpg"],
        "index.html": ["valle-cocora-hero-banner.jpg", "eje-cafetero-landscape-colombia.jpg", "coffee-plantation-sunset-colombia.jpg"]
    }
    
    for page_name, images in image_mapping.items():
        page_path = Path(__file__).parent / page_name
        if page_path.exists():
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for img in images:
                if (paisajes_path / img).exists() and img not in content:
                    img_tag = f'<img src="assets/images/paisajes/{img}" alt="{img.replace("-", " ").replace(".jpg", "")}" class="content-image" loading="lazy">'
                    content = content.replace('</section>', f'{img_tag}\n    </section>', 1)
            
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Enriched: {page_name}")

if __name__ == "__main__":
    enrich_pages_strategically()