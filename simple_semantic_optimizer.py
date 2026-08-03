from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
html_files = list(programmatic_dir.glob('*.html'))

print(f"Total archivos a optimizar: {len(html_files)}")

optimized_count = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Schema avanzado
        schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Organization",
      "name": "Quindío Travel",
      "url": "https://quindiotravel.com.co",
      "logo": "https://quindiotravel.com.co/logo.png",
      "contactPoint": {
        "@type": "ContactPoint",
        "telephone": "+57-317-4426044",
        "contactType": "customer service"
      }
    }
    </script>'''
        
        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{schema}\n</head>')
        
        # FAQ schema
        faq_schema = '''    <script type="application/ld+json">
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Cuál es el mejor momento para visitar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "La mejor época depende de tus preferencias: temporada baja (enero-marzo) para mejores precios, temporada alta (diciembre-enero) para mejor clima."
          }
        }
      ]
    }
    </script>'''
        
        if '"@type": "FAQPage"' not in content:
            content = content.replace('</head>', f'{faq_schema}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        optimized_count += 1
        print(f"Optimizado: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal optimizados: {optimized_count}")