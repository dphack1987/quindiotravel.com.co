"""
Versión mínima de generador de blog
"""

from pathlib import Path

def main():
    base_dir = Path(__file__).parent
    blog_dir = base_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    
    # Crear un artículo simple
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mejor época para visitar Quindío 2026 | Quindío Travel</title>
</head>
<body>
    <h1>Mejor época para visitar Quindío en 2026</h1>
    <p>Guía completa para planificar tu viaje al Eje Cafetero.</p>
    <a href="../index.html">Volver al inicio</a>
</body>
</html>"""
    
    filepath = blog_dir / "mejor-epoca-visitar-quindio-2026.html"
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("Artículo generado exitosamente")

if __name__ == "__main__":
    main()