from pathlib import Path

# Optimizar programmatic-pages para Gemini
programmatic_dir = Path(__file__).parent / "programmatic-pages"
programmatic_files = list(programmatic_dir.glob('*.html'))

print(f"Optimizando {len(programmatic_files)} archivos programaticos para Gemini...")

# Schema simple y efectivo para Gemini
simple_gemini_schema = '''    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "Article",
      "author": {
        "@type": "Person",
        "name": "Alvaro Alzate Ortiz",
        "jobTitle": "Operador Turistico Certificado RNT 18152",
        "description": "Operador turistico con mas de 15 anos de experiencia en el Eje Cafetero colombiano"
      },
      "publisher": {
        "@type": "Organization",
        "name": "Quindío Travel",
        "url": "https://quindiotravel.com.co",
        "logo": "https://quindiotravel.com.co/logo_quindio_travel.png"
      },
      "datePublished": "2026-08-03",
      "dateModified": "2026-08-03",
      "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://quindiotravel.com.co/"
      }
    }
    </script>'''

optimized_count = 0

for filepath in programmatic_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Añadir schema simple si no existe
        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{simple_gemini_schema}\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            optimized_count += 1
            if optimized_count <= 5:
                print(f"Schema Gemini añadido: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal archivos programaticos optimizados: {optimized_count}")

# Optimizar blog para Gemini
blog_dir = Path(__file__).parent / "blog"
blog_files = list(blog_dir.glob('*.html'))

print(f"\nOptimizando {len(blog_files)} archivos blog para Gemini...")

blog_optimized_count = 0

for filepath in blog_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Añadir schema simple si no existe
        if '<script type="application/ld+json">' not in content:
            content = content.replace('</head>', f'{simple_gemini_schema}\n</head>')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            blog_optimized_count += 1
            if blog_optimized_count <= 5:
                print(f"Schema Gemini añadido: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal archivos blog optimizados: {blog_optimized_count}")
print(f"\nTotal optimizaciones Gemini: {optimized_count + blog_optimized_count}")
print("Optimizacion Gemini completada")