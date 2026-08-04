from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"

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

# Archivos nuevos programáticos para optimizar
new_files = [
    "experiencias-romanticas-parejas-2026.html",
    "turismo-gastronomico-aroma-cafe-2026.html",
    "senderismo-avanzado-quindio-2026.html",
    "birdwatching-eje-cafetero-2026.html",
    "noches-estrellas-cocora-2026.html",
    "artesania-tradicional-quindio-2026.html",
    "mujeres-empresarias-cafe-2026.html",
    "cultura-paisa-musica-2026.html",
    "fotografia-avanzada-palmas-2026.html",
    "rutas-moto-turismo-2026.html"
]

for filename in new_files:
    filepath = programmatic_dir / filename
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