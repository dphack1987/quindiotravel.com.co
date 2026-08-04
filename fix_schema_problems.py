"""
Corrección de Problemas de Schema en Planes
Elimina inconsistencias geográficas y añade campos opcionales importantes
"""

from pathlib import Path

def fix_plan_3_schema():
    """Corrige schema de plan-3.html"""
    
    plan3_path = Path(__file__).parent / "plan-3.html"
    
    with open(plan3_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Corregir inconsistencia geográfica - eliminar "Cartagena"
    content = content.replace('Tour Festivo Independencia de Cartagena 2026', 'Tour Festivo Independencia Eje Cafetero 2026')
    content = content.replace('Tour especial para festivo de Independencia de Cartagena', 'Tour especial para festivo de Independencia en el Eje Cafetero')
    content = content.replace('Gran Quindío Completo', 'Eje Cafetero Completo')
    
    # Añadir campos opcionales importantes
    # Buscar la sección de offers y añadir url
    if '"url"' not in content and '"priceValidUntil"' in content:
        content = content.replace('"priceValidUntil"', '"priceValidUntil"\n            "url": "https://quindiotravel.com.co/plan-3.html"')
    
    with open(plan3_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Schema de plan-3.html corregido")
    return True

def fix_other_plans_schema():
    """Corrige schema de otros planes si es necesario"""
    
    # Verificar si hay planes con problemas similares
    plans_to_check = ["plan-4.html", "plan-5.html", "plan-6.html"]
    
    for plan in plans_to_check:
        filepath = Path(__file__).parent / plan
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Añadir campo url si falta
            if '"url"' not in content and '"priceValidUntil"' in content:
                content = content.replace('"priceValidUntil"', f'"priceValidUntil"\n            "url": "https://quindiotravel.com.co/{plan}"')
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                print(f"Campo url añadido a {plan}")

if __name__ == "__main__":
    print("Corrigiendo problemas de schema en planes...")
    print("=" * 60)
    
    fix_plan_3_schema()
    fix_other_plans_schema()
    
    print("\nProblemas de schema corregidos")
    print("Non-critical issues opcionales corregidos")