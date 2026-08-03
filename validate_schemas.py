"""
Script para validar que los bloques de datos estructurados esten correctamente cerrados
"""

import re

def validate_schemas(file_path):
    """
    Valida que los bloques de datos estructurados esten correctamente cerrados
    
    Args:
        file_path: Ruta del archivo HTML
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar todos los bloques script de application/ld+json
    script_pattern = r'<script type="application/ld\+json">(.*?)</script>'
    script_blocks = re.findall(script_pattern, content, re.DOTALL)
    
    print(f"Encontrados {len(script_blocks)} bloques de datos estructurados")
    print("=" * 60)
    
    errors = []
    for i, block in enumerate(script_blocks, 1):
        # Contar llaves y corchetes
        open_braces = block.count('{')
        close_braces = block.count('}')
        open_brackets = block.count('[')
        close_brackets = block.count(']')
        
        brace_balance = open_braces - close_braces
        bracket_balance = open_brackets - close_brackets
        
        if brace_balance != 0 or bracket_balance != 0:
            errors.append(f"Bloque {i}: Llaves={brace_balance}, Corchetes={bracket_balance}")
        
        print(f"Bloque {i}: {len(block)} caracteres, Llaves: {open_braces}/{close_braces}, Corchetes: {open_brackets}/{close_brackets}")
    
    print("=" * 60)
    
    if errors:
        print("ERRORES ENCONTRADOS:")
        for error in errors:
            print(f"  - {error}")
        return False
    else:
        print("Todos los bloques estan correctamente cerrados")
        return True

if __name__ == "__main__":
    validate_schemas("index.html")