from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
programmatic_files = list(programmatic_dir.glob('*.html'))

print(f"Total archivos a procesar: {len(programmatic_files)}")

experience_section = '''            <section class="eeat-section">
                <h2>Experiencia Real y Autoridad en el Eje Cafetero</h2>
                <p><strong>15+ años de experiencia:</strong> Como operador turístico certificado RNT 18152, Quindío Travel ha atendido a más de 5,000 viajeros desde 2010, con experiencia comprobable en turismo del Eje Cafetero colombiano.</p>
                <p><strong>Certificación oficial:</strong> RNT 18152 - Registro Nacional de Turismo Colombia, garantía de profesionalismo y cumplimiento de normativas turísticas.</p>
                <p><strong>Conocimiento local:</strong> Operadores nativos del Quindío con conocimiento profundo de la cultura, geografía y tradiciones del Eje Cafetero.</p>
            </section>'''

enhanced_count = 0

for filepath in programmatic_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'eeat-section' not in content:
            # Insertar antes del footer
            content = content.replace(
                '    <footer class="main-footer">',
                f'{experience_section}\n\n    <footer class="main-footer">'
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            enhanced_count += 1
            print(f"E-E-A-T añadido: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal mejoras aplicadas: {enhanced_count}")