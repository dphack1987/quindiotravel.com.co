from pathlib import Path

def enrich_pages_images():
    paisajes_path = Path(__file__).parent / "assets" / "images" / "paisajes"
    
    image_mapping = {
        "planes.html": ["valle-cocora-hero-banner.jpg", "eje-cafetero-landscape-colombia.jpg", "coffee-plantation-sunset-colombia.jpg"],
        "blog.html": ["eje-cafetero-sunset-hills.jpg", "quindio-mountain-range.jpg", "natural-landscapes-colombia.avif"]
    }
    
    for page_name, images in image_mapping.items():
        page_path = Path(__file__).parent / page_name
        if page_path.exists():
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for img in images:
                if (paisajes_path / img).exists() and img not in content:
                    img_tag = f'<img src="assets/images/paisajes/{img}" alt="{img.replace("-", " ").replace(".jpg", "").replace(".avif", "")}" class="content-image" loading="lazy">'
                    content = content.replace('</section>', f'{img_tag}\n    </section>', 1)
            
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Enriched: {page_name}")

if __name__ == "__main__":
    enrich_pages_images()