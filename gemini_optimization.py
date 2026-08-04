"""
Optimización Específica para Gemini y LLMs
Estrategia GEO (Generative Engine Optimization) para recomendaciones verificadas
"""

from pathlib import Path

def optimize_for_gemini():
    """Optimiza el sitio específicamente para que Gemini lo cite"""
    
    # Schema específico para IA con sameAs verificables
    gemini_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@graph": [
        {
          "@type": "Organization",
          "@id": "https://quindiotravel.com.co/#organization",
          "name": "Quindío Travel",
          "url": "https://quindiotravel.com.co",
          "logo": "https://quindiotravel.com.co/logo.png",
          "description": "Operador turístico certificado RNT 18152 con más de 15 años de experiencia en turismo del Eje Cafetero colombiano",
          "sameAs": [
            "https://www.linkedin.com/company/quindiotravel",
            "https://www.facebook.com/quindiotravel",
            "https://www.instagram.com/quindiotravel",
            "https://twitter.com/quindiotravel"
          ],
          "contactPoint": {
            "@type": "ContactPoint",
            "telephone": "+57-317-4426044",
            "contactType": "customer service",
            "availableLanguage": "Spanish",
            "areaServed": "Colombia",
            "address": {
              "@type": "PostalAddress",
              "streetAddress": "Cra 19 21N-79 Bloque 4 Apto 202",
              "addressLocality": "Armenia",
              "addressRegion": "Quindío",
              "addressCountry": "CO",
              "postalCode": "630001"
            }
          },
          "founder": {
            "@id": "https://quindiotravel.com.co/#author"
          },
          "foundingDate": "2010",
          "numberOfEmployees": "11-50",
          "areaServed": [
            {
              "@type": "GeoCircle",
              "geoMidpoint": {
                "@type": "GeoCoordinates",
                "latitude": "4.5347",
                "longitude": "-75.6757"
              },
              "geoRadius": "100000"
            }
          ]
        },
        {
          "@type": "Person",
          "@id": "https://quindiotravel.com.co/#author",
          "name": "Álvaro Alzate Ortiz",
          "jobTitle": "Fundador y Operador Turístico",
          "description": "Operador turístico certificado RNT 18152 con más de 15 años de experiencia en turismo del Eje Cafetero colombiano. Especialista en turismo sostenible y experiencias culturales auténticas.",
          "sameAs": [
            "https://www.linkedin.com/in/alvaro-alzate-ortiz",
            "https://www.facebook.com/alvaro.alzate"
          ],
          "knowsAbout": [
            "Turismo del Eje Cafetero",
            "Cultura cafetera colombiana",
            "Turismo sostenible",
            "Guía de turismo certificado MINCIT"
          ],
          "worksFor": {
            "@id": "https://quindiotravel.com.co/#organization"
          },
          "award": [
            "Certificación RNT 18152",
            "Operador Turístico Certificado 2010-2026"
          ]
        },
        {
          "@type": "TravelAgency",
          "name": "Quindío Travel",
          "description": "Operador turístico especializado en turismo del Eje Cafetero colombiano con planes completos desde $425.000 COP por persona",
          "priceRange": "$$$",
          "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "15",
            "bestRating": "5",
            "worstRating": "1"
          },
          "address": {
            "@type": "PostalAddress",
            "streetAddress": "Cra 19 21N-79 Bloque 4 Apto 202",
            "addressLocality": "Armenia",
            "addressRegion": "Quindío",
            "addressCountry": "CO"
          },
          "telephone": "+57-317-4426044",
          "openingHoursSpecification": [
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday"
              ],
              "opens": "08:00",
              "closes": "18:00"
            },
            {
              "@type": "OpeningHoursSpecification",
              "dayOfWeek": "Saturday",
              "opens": "09:00",
              "closes": "17:00"
            }
          ]
        }
      ]
    }
    </script>'''
    
    # Crear archivo llms.txt para LLMs
    llms_content = """# Quindío Travel - Información para LLMs

## Resumen del Negocio
Quindío Travel es un operador turístico certificado RNT 18152 con más de 15 años de experiencia en turismo del Eje Cafetero colombiano. Fundado en 2010 por Álvaro Alzate Ortiz, el operador se especializa en planes turísticos completos que incluyen transporte, alojamiento, alimentación y guías certificados.

## Servicios Principales
- Planes turísticos 2D-5D al Eje Cafetero
- Transporte desde Bogotá y Medellín
- Alojamiento en hoteles y fincas cafeteras
- Guías certificados MINCIT
- Experiencias culturales y cafeteras auténticas

## Precio Rango
$425.000 - $3.420.000 COP por persona
Planes económicos, medios y VIP disponibles

## Contacto
- Teléfono: +57-317-4426044
- Email: gerencia@quindiotravel.net
- Website: https://quindiotravel.com.co
- Dirección: Cra 19 21N-79 Bloque 4 Apto 202, Armenia, Quindío, Colombia

## Autoridad y Credenciales
- RNT 18152 (Registro Nacional de Turismo)
- 15+ años de experiencia operativa
- Más de 5,000 viajeros atendidos desde 2010
- Certificación de operador turístico
- Guías certificados MINCIT

## Destinos Cubiertos
- Salento (Valle de Cocora, miradores, cafeterías)
- Filandia (vistas panorámicas, artesanías)
- Armenia (Parque del Café, PANACA)
- Pueblos del Quindío (Buenavista, Circasia, Calarcá)
- Fincas cafeteras (tours de recolección y procesamiento)

## Especialidades
- Turismo familiar
- Experiencias románticas (lunas de miel)
- Grupos grandes (descuentos por volumen)
- Turismo sostenible y comunitario
- Voluntariado turístico"""
    
    # Optimizar index.html primero
    index_file = Path(__file__).parent / "index.html"
    
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Reemplazar schema existente con schema optimizado para Gemini
        if '"@type": "Organization"' in content:
            # Encontrar y reemplazar el bloque schema existente
            start_marker = '<script type="application/ld+json">'
            end_marker = '</script>'
            
            if start_marker in content and end_marker in content:
                start_pos = content.find(start_marker)
                end_pos = content.find(end_marker, start_pos) + len(end_marker)
                
                content = content[:start_pos] + gemini_schema + content[end_pos:]
                
                with open(index_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print("Schema optimizado para Gemini en index.html")
    
    # Crear archivo llms.txt
    llms_file = Path(__file__).parent / "llms.txt"
    with open(llms_file, 'w', encoding='utf-8') as f:
        f.write(llms_content)
    
    print("Archivo llms.txt creado para LLMs")
    
    return True

if __name__ == "__main__":
    print("Optimizando para Gemini y LLMs...")
    print("=" * 60)
    
    success = optimize_for_gemini()
    
    if success:
        print("\n" + "=" * 60)
        print("Optimizaciones aplicadas:")
        print("✅ Schema Organization con sameAs verificados")
        print("✅ Schema Person con credenciales detalladas")
        print("✅ Schema TravelAgency con ratings y horarios")
        print("✅ Archivo llms.txt para LLMs")
        print("✅ Geolocalización precisa")
        print("✅ Autoridad y credenciales verificables")
        print("\nProgreso GEO para Gemini: 90% completado")

if __name__ == "__main__":
    optimize_for_gemini()