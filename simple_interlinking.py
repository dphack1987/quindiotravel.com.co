from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"

# Procesar solo el clúster Salento (pilar + 2 relacionadas)
pillar_file = programmatic_dir / "paquetes-salento-2-dias-economicos-2026.html"
related_files = [
    "hoteles-economicos-salento-familias-2026.html",
    "diferencias-salento-filandia-destino-2026.html"
]

print(f"Procesando clúster Salento...")
print(f"Pilar: {pillar_file.name}")
print(f"Relacionadas: {len(related_files)}")

# Añadir enlaces desde pilar a relacionadas
if pillar_file.exists():
    with open(pillar_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    links_section = '''            <section class="related-links">
                <h3>Contenido Relacionado</h3>
                <ul>
                    <li><a href="hoteles-economicos-salento-familias-2026.html">Hoteles Economicos Salento Familias</a></li>
                    <li><a href="diferencias-salento-filandia-destino-2026.html">Diferencias Salento Filandia</a></li>
                </ul>
            </section>'''
    
    if 'related-links' not in content:
        content = content.replace(
            '    <footer class="main-footer">',
            f'{links_section}\n\n    <footer class="main-footer">'
        )
        
        with open(pillar_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Enlaces añadidos a pilar: {pillar_file.name}")

# Añadir backlinks desde relacionadas a pilar
for related_file in related_files:
    related_path = programmatic_dir / related_file
    if related_path.exists():
        with open(related_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        backlink = '                <p><a href="paquetes-salento-2-dias-economicos-2026.html">Volver a: Paquetes Salento 2 Dias Economicos</a></p>'
        
        if 'backlink-to-pillar' not in content:
            content = content.replace(
                '    <footer class="main-footer">',
                f'{backlink}\n\n    <footer class="main-footer">'
            )
            
            with open(related_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"Backlink añadido: {related_file}")

print(f"\nInterlinking de prueba completado")