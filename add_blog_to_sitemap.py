from pathlib import Path

sitemap_path = Path(__file__).parent / "sitemap.xml"

new_blog_pages = [
    "blog/senderismo-rutas-seguras-eje-cafetero-2026.html",
    "blog/gastronomia-autentica-quindio-2026.html",
    "blog/turismo-romantico-luna-miel-2026.html",
    "blog/turismo-accesible-discapacitados-2026.html",
    "blog/turismo-sostenible-eco-2026.html",
    "blog/mejores-fotos-influencers-eje-cafetero-2026.html",
    "blog/turismo-familiar-ninos-2026.html",
    "blog/turismo-solo-soltera-2026.html",
    "blog/conferencias-eventos-quindio-2026.html",
    "blog/ofertas-temporada-agosto-2026.html"
]

with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

added_count = 0
for page in new_blog_pages:
    url = f"https://quindiotravel.com.co/{page}"
    if url not in content:
        entry = f"  <url>\n    <loc>{url}</loc>\n    <lastmod>2026-08-03</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.7</priority>\n  </url>\n"
        content = content.replace('</urlset>', f'{entry}</urlset>')
        added_count += 1
        print(f"Agregado: {page}")

with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nTotal páginas blog agregadas: {added_count}")