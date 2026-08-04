"""
Corregir Inconsistencias Geográficas en Event Schema
Tour Festivo Todos los Santos debe ser del Eje Cafetero, no Santa Rosa de Cabal
"""

from pathlib import Path

def fix_event_schema_geography():
    """Corrige ubicación geográfica en schema de eventos"""
    
    # Buscar y corregir eventos con ubicación incorrecta
    files_to_check = ["plan-4.html", "plan-5.html", "plan-6.html"]
    
    for plan_file in files_to_check:
        filepath = Path(__file__).parent / plan_file
        if filepath.exists():
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Corregir ubicación de Santa Rosa de Cabal a Eje Cafetero
            content = content.replace('Santa Rosa de Cabal', 'Armenia')
            content = content.replace('Risaralda', 'Quindío')
            content = content.replace('Termales Santa Rosa y Eje Cafetero', 'Termales Santa Rosa y Eje Cafetero')
            
            # Corregir coordenadas si están incorrectas
            if '4.8667' in content and '-75.6167' in content:
                content = content.replace('4.8667', '4.5338')
                content = content.replace('-75.6167', '-75.6811')
            
            # Añadir campo url en offers si falta
            if '"url"' not in content and '"priceValidUntil"' in content:
                content = content.replace('"priceValidUntil"', f'"priceValidUntil"\n            "url": "https://quindiotravel.com.co/{plan_file}"')
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"[OK] {plan_file} geografia corregida")

if __name__ == "__main__":
    print("Corrigiendo inconsistencias geograficas en schema de eventos...")
    print("=" * 70)
    
    fix_event_schema_geography()
    
    print("\n" + "=" * 70)
    print("[OK] Inconsistencias geograficas corregidas")
    print("[OK] Coordenadas actualizadas al Eje Cafetero")
    print("[OK] Campo url añadido en offers")