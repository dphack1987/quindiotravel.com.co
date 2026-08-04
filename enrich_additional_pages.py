from pathlib import Path

def enrich_additional_pages():
    paisajes_path = Path(__file__).parent / "assets" / "images" / "paisajes"
    available_images = list(paisajes_path.glob("*.jpg")) + list(paisajes_path.glob("*.jfif")) + list(paisajes_path.glob("*.avif"))
    
    image_mapping = {
        "armenia.html": ["armenia-city-view.jfif", "eje-cafetero-green-mountains.jpg", "coffee-nature-panorama.jpg"],
        "plan-1.html": ["valle-cocora-hero-banner.jpg", "eje-cafetero-sunset-hills.jpg", "coffee-plantation-green.jpg"],
        "plan-2.html": ["palm-trees-misty-valley.jpg", "valle-cocora-river-reflection.jpg", "colombian-coffee-fields.jpg"],
        "plan-3.html": ["eje-cafetero-aerial-view.jpg", "quindio-mountain-range.jpg", "eje-cafetero-mountain-valleys-cloudy.jpg"],
        "plan-4.html": ["coffee-region-cloudy-sky.jpg", "palm-trees-mountains-background.jpg", "palma-cera-sunlight.jpg"],
        "plan-5.html": ["eje-cafetero-green-mountains.jpg", "coffee-nature-panorama.jpg", "quindio-mountains-colombia.jpg"],
        "plan-6.html": ["natural-landscapes-colombia.avif", "eje-cafetero-landscape-colombia.jpg", "coffee-plantation-sunset-colombia.jpg"]
    }
    
    for page_name, images in image_mapping.items():
        page_path = Path(__file__).parent / page_name
        if page_path.exists():
            with open(page_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            for img in images:
                if (paisajes_path / img).exists() and img not in content:
                    img_tag = f'<img src="assets/images/paisajes/{img}" alt="{img.replace("-", " ").replace(".jpg", "").replace(".jfif", "").replace(".avif", "")}" class="content-image" loading="lazy">'
                    content = content.replace('</section>', f'{img_tag}\n    </section>', 1)
            
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Enriched: {page_name}")
        else:
            print(f"Skip: {page_name} not found")

if __name__ == "__main__":
    enrich_additional_pages()