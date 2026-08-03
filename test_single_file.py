from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"

# Probar con un solo archivo
test_file = programmatic_dir / "mejor-epoca-visitar-filandia-2026.html"

print(f"Archivo de prueba: {test_file.exists()}")
print(f"Ruta: {test_file}")

if test_file.exists():
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"Longitud del contenido: {len(content)}")
    print(f"Contiene 'related-links': {'related-links' in content}")
    
    # Simple test de reemplazo
    if 'related-links' not in content:
        test_section = '            <section class="related-links"><p>TEST</p></section>'
        content = content.replace(
            '    <footer class="main-footer">',
            f'{test_section}\n\n    <footer class="main-footer">'
        )
        
        with open(test_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Test de reemplazo exitoso")
else:
    print("❌ Archivo no encontrado")