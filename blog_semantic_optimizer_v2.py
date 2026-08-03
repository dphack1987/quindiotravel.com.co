from pathlib import Path

blog_dir = Path(__file__).parent / "blog"
html_files = list(blog_dir.glob('*.html'))

print(f"Total archivos blog a optimizar: {len(html_files)}")

optimized_count = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
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
        
        # Solo agregar schema si no existe
        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{schema}\n</head>')
        
        # FAQ schema específico para cada tema
        faq_schema = '''    <script type="application/ld+json">
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "¿Cuánto cuesta un viaje al Eje Cafetero?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Los precios varían desde $425.000 COP para planes económicos hasta $3.420.000 COP para planes VIP. Cotiza gratis tu plan personalizado."
          }
        },
        {
          "@type": "Question",
          "name": "¿Es seguro viajar al Eje Cafetero?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Sí, el Eje Cafetero es una de las regiones más seguras de Colombia para turismo. Como operadores locales certificados RNT 18152, garantizamos seguridad en todos nuestros viajes."
          }
        },
        {
          "@type": "Question",
          "name": "¿Cuál es la mejor época para visitar?",
          "acceptedAnswer": {
            "@type": "Answer",
            "text": "Temporada baja (enero-marzo) para mejores precios, temporada alta (diciembre-enero) para mejor clima y festividades."
          }
        }
      ]
    }
    </script>'''
        
        # Solo agregar FAQ si no existe
        if '"@type": "FAQPage"' not in content:
            content = content.replace('</head>', f'{faq_schema}\n</head>')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        optimized_count += 1
        print(f"Optimizado: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal artículos optimizados: {optimized_count}")