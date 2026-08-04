from pathlib import Path

blog_dir = Path(__file__).parent / "blog"

# Schema para añadir manualmente
schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "author": {
        "@type": "Person",
        "name": "Alvaro Alzate Ortiz",
        "jobTitle": "Operador Turistico Certificado RNT 18152"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Quindío Travel"
      },
      "datePublished": "2026-08-03"
    }
    </script>'''

# Archivos nuevos para optimizar
new_files = [
    "senderismo-rutas-seguras-eje-cafetero-2026.html",
    "turismo-romantico-luna-miel-2026.html",
    "turismo-accesible-discapacitados-2026.html",
    "turismo-sostenible-eco-2026.html",
    "mejores-fotos-influencers-eje-cafetero-2026.html",
    "turismo-familiar-ninos-2026.html",
    "turismo-solo-soltera-2026.html"
]

for filename in new_files:
    filepath = blog_dir / filename
    if filepath.exists():
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '</head>' in content and '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{schema}\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Schema añadido: {filename}")
        else:
            print(f"Ya tiene schema: {filename}")
    else:
        print(f"No existe: {filename}")