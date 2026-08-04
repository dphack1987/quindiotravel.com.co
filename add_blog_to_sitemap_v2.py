from pathlib import Path

sitemap_path = Path(__file__).parent / "sitemap.xml"

# Añadir blog.html al sitemap
with open(sitemap_path, 'r', encoding='utf-8') as f:
    content = f.read()

blog_entry = """  <url>
    <loc>https://quindiotravel.com.co/blog.html</loc>
    <lastmod>2026-08-04</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""

if 'blog.html' not in content:
    content = content.replace('</urlset>', f'{blog_entry}\n</urlset>')
    
    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("blog.html añadido al sitemap")
else:
    print("blog.html ya está en el sitemap")