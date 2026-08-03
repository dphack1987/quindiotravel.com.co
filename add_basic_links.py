from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
html_files = list(programmatic_dir.glob('*.html'))

print(f"Procesando {len(html_files)} archivos para agregar enlaces básicos...")

# Enlaces básicos para todas las páginas
basic_links = '''            <section class="related-links">
                <h3>Contenido Relacionado</h3>
                <ul>
                    <li><a href="paquetes-salento-2-dias-economicos-2026.html">Paquetes Salento 2 Dias Economicos</a></li>
                    <li><a href="tour-eje-cafetero-sin-transporte-2026.html">Tour Eje Cafetero Sin Transporte</a></li>
                    <li><a href="hoteles-cerca-parque-cafe-2026.html">Hoteles Cerca Parque Cafe</a></li>
                    <li><a href="experiencias-cafeteras-autenticas-quindio-2026.html">Experiencias Cafeteras</a></li>
                </ul>
            </section>'''

added_count = 0

for filepath in html_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'related-links' not in content:
            content = content.replace(
                '    <footer class="main-footer">',
                f'{basic_links}\n\n    <footer class="main-footer">'
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            added_count += 1
            print(f"✅ Enlaces añadidos: {filepath.name}")
        
    except Exception as e:
        print(f"❌ Error: {filepath.name} - {e}")

print(f"\nTotal enlaces añadidos: {added_count}")
print(f"Total archivos procesados: {len(html_files)}")