from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
programmatic_files = list(programmatic_dir.glob('*.html'))

# Procesar solo los primeros 5 archivos para test
test_files = programmatic_files[:5]

print(f"Test con {len(test_files)} archivos")

experience_signal = '''                <div class="eeat-signal">
                    <h3>Experiencia Real y Verificable</h3>
                    <p><strong>15+ años de experiencia:</strong> Como operador turístico certificado RNT 18152, Quindío Travel ha atendido a más de 5,000 viajeros desde 2010.</p>
                </div>'''

enhanced_count = 0

for filepath in test_files:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if 'eeat-signal' not in content:
            content = content.replace(
                '</section>',
                f'{experience_signal}\n            </section>',
                1
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            enhanced_count += 1
            print(f"E-E-A-T añadido: {filepath.name}")
        
    except Exception as e:
        print(f"Error: {filepath.name} - {e}")

print(f"\nTotal mejoras aplicadas: {enhanced_count}")