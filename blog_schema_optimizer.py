from pathlib import Path

blog_dir = Path(__file__).parent / "blog"
html_files = list(blog_dir.glob('*.html'))

print(f"Total archivos blog: {len(html_files)}")

# Schema avanzado con E-E-A-T
schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://quindiotravel.com.co/#organization",
          "name": "Quindío Travel",
          "url": "https://quindiotravel.com.co",
          "logo": "https://quindiotravel.com.co/logo.png",
          "sameAs": [
            "https://www.facebook.com/quindiotravel",
            "https://www.instagram.com/quindiotravel"
          ],
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+57-317-4426044",
            "contactType": "customer service"
          }
        },
        {
          "@type": "Person",
          "@id": "https://quindiotravel.com.co/#author",
          "name": "Álvaro Alzate Ortiz",
          "jobTitle": "Fundador y Operador Turístico",
          "description": "Operador turístico certificado RNT 18152 con más de 15 años de experiencia en turismo del Eje Cafetero",
          "worksFor": {
            "@id": "https://quindiotravel.com.co/#organization"
          }
        },
        {
          "@type": "Article",
          "author": {
            "@id": "https://quindiotravel.com.co/#author"
          },
          "publisher": {
            "@id": "https://quindiotravel.com.co/#organization"
          },
          "datePublished": "2026-08-03",
          "dateModified": "2026-08-03"
        }
      ]
    }
    </script>'''

optimized_count = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Solo agregar schema si no existe
        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{schema}\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            optimized_count += 1
            print(f"Schema añadido: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal artículos optimizados: {optimized_count}")