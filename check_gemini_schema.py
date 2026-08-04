from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
blog_dir = Path(__file__).parent / "blog"

programmatic_files = list(programmatic_dir.glob('*.html'))
blog_files = list(blog_dir.glob('*.html'))

print("Verificando schema compatible con Gemini...")

# Verificar schema en archivos programaticos
with_schema_programmatic = 0
without_schema_programmatic = 0

for filepath in programmatic_files[:10]:  # Solo verificar primeros 10
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script type="application/ld+json">' in content:
        with_schema_programmatic += 1
        print(f"Con schema: {filepath.name}")
    else:
        without_schema_programmatic += 1

print(f"\nProgrammatic: {with_schema_programmatic} con schema, {without_schema_programmatic} sin schema")

# Verificar schema en archivos blog
with_schema_blog = 0
without_schema_blog = 0

for filepath in blog_files[:5]:  # Solo verificar primeros 5
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<script type="application/ld+json">' in content:
        with_schema_blog += 1
        print(f"Con schema: {filepath.name}")
    else:
        without_schema_blog += 1

print(f"\nBlog: {with_schema_blog} con schema, {without_schema_blog} sin schema")