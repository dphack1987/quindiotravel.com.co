from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"

# Procesar clúster Filandia
pillar_file = programmatic_dir / "mejor-epoca-visitar-filandia-2026.html"
related_files = [
    "diferencias-salento-filandia-destino-2026.html",
    "vistas-panoramicas-filandia-2026.html",
    "mejores-miradores-filandia-2026.html",
    "mirador-filandia-360-grados-2026.html",
    "compras-artesania-filandia-2026.html"
]

print(f"Procesando clúster FILANDIA...")
print(f"Pilar: {pillar_file.name}")
print(f"Relacionadas: {len(related_files)}")

# Añadir enlaces desde pilar a relacionadas
if pillar_file.exists():
    with open(pillar_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links_html = ""
    for related_file in related_files:
        related_path = programmatic_dir / related_file
        if related_path.exists():
            title = related_file.replace("-", " ").replace(".html", "").title()
            links_html += f'                    <li><a href="{related_file}">{title}</a></li>\n'
    
    if 'related-links' not in content:
        links_section = f'''            <section class="related-links">
                <h3>Contenido Relacionado - Filandia</h3>
                <ul class="related-links-list">
{links_html}                </ul>
            </section>'''
        
        content = content.replace(
            '    <footer class="main-footer">',
            f'{links_section}\n\n    <footer class="main-footer">'
        )
        
        with open(pillar_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Enlaces añadidos a pilar: {pillar_file.name}")

# Añadir backlinks desde relacionadas a pilar
pillar_title = "Mejor Epoca Visitar Filandia 2026"
backlink = f'                <p><a href="mejor-epoca-visitar-filandia-2026.html">Volver a: {pillar_title}</a></p>'

for related_file in related_files:
    related_path = programmatic_dir / related_file
    if related_path.exists():
        with open(related_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'backlink-to-pillar' not in content:
            content = content.replace(
                '    <footer class="main-footer">',
                f'{backlink}\n\n    <footer class="main-footer">'
            )
            
            with open(related_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ Backlink añadido: {related_file}")

print(f"\nClúster FILANDIA completado")