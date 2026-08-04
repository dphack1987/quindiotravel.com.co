from pathlib import Path

index_file = Path(__file__).parent / "index.html"

print("Optimizando index.html para Gemini...")

if index_file.exists():
    with open(index_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Schema optimizado para Gemini con sameAs verificables
    gemini_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://quindiotravel.com.co/#organization",
          "name": "Quindío Travel",
          "url": "https://quindiotravel.com.co",
          "logo": "https://quindiotravel.com.co/logo_quindio_travel.png",
          "description": "Operador turistico certificado RNT 18152 con mas de 15 anos de experiencia en turismo del Eje Cafetero colombiano",
          "sameAs": [
            "https://www.linkedin.com/company/quindiotravel",
            "https://www.facebook.com/quindiotravel",
            "https://www.instagram.com/quindiotravel"
          ],
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+57-317-4426044",
            "contactType": "customer service",
            "availableLanguage": "Spanish"
          },
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Cra 19 21N-79 Bloque 4 Apto 202",
            "addressLocality": "Armenia",
            "addressRegion": "Quindio",
            "addressCountry": "CO"
          },
          "founder": {
            "@id": "https://quindiotravel.com.co/#author"
          },
          "foundingDate": "2010"
        },
        {
          "@type": "Person",
          "@id": "https://quindiotravel.com.co/#author",
          "name": "Alvaro Alzate Ortiz",
          "jobTitle": "Fundador y Operador Turistico",
          "description": "Operador turistico certificado RNT 18152 con mas de 15 anos de experiencia en turismo del Eje Cafetero colombiano",
          "sameAs": [
            "https://www.linkedin.com/in/alvaro-alzate-ortiz"
          ],
          "worksFor": {
            "@id": "https://quindiotravel.com.co/#organization"
          }
        },
        {
          "@type": "TravelAgency",
          "name": "Quindío Travel",
          "description": "Operador turistico especializado en turismo del Eje Cafetero colombiano con planes completos desde $425.000 COP por persona",
          "priceRange": "$$ - $$$",
          "telephone": "+57-317-4426044",
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Cra 19 21N-79 Bloque 4 Apto 202",
            "addressLocality": "Armenia",
            "addressRegion": "Quindio",
            "addressCountry": "CO"
          },
          "areaServed": {
            "@type": "GeoCircle",
            "geoMidpoint": {
              "@type": "GeoCoordinates",
              "latitude": "4.5338",
              "longitude": "-75.6811"
            },
            "geoRadius": "100000"
          }
        }
      ]
    }
    </script>'''
    
    # Encontrar y reemplazar el schema existente
    if '<script type="application/ld+json">' in content:
        start_marker = '<script type="application/ld+json">'
        end_marker = '</script>'
        
        start_pos = content.find(start_marker)
        end_pos = content.find(end_marker, start_pos) + len(end_marker)
        
        if start_pos != -1 and end_pos != -1:
            content = content[:start_pos] + gemini_schema + content[end_pos:]
            
            with open(index_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print("Schema optimizado para Gemini en index.html")
        else:
            print("No se pudo encontrar el bloque schema existente")
    else:
        print("No existe schema JSON-LD en index.html")

print("Optimizacion completada")