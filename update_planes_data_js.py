"""
Actualizar planes-data.js con Nombres Atractivos
Actualiza el archivo JavaScript que contiene los datos de los planes
"""

from pathlib import Path

planes_data_path = Path(__file__).parent / "assets" / "js" / "planes-data.js"

# Mapeo de nombres viejos a nuevos
name_replacements = {
    "Plan 1: Vive El Eje Cafetero Temático": "Escapada Cafetera de Fin de Semana",
    "Plan 2: Naturaleza y Diversión Cafetera": "Aventura Natural en el Eje Cafetero",
    "Plan 3: La Experiencia Completa del Eje": "Experiencia Completa del Eje Cafetero",
    "Plan 4: Aventura y Relax Termal": "Relax y Aventura en Termales del Eje",
    "Plan 5: Tradición y Raíces de la Arriería": "Experiencia Premium del Eje Cafetero",
    "Plan 6: Gran Quindío Integral": "La Experiencia Definitiva del Eje Cafetero"
}

def update_planes_data():
    """Actualiza planes-data.js con nombres nuevos"""
    
    if not planes_data_path.exists():
        print("planes-data.js no encontrado")
        return False
    
    with open(planes_data_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar nombres
    changes_made = 0
    for old_name, new_name in name_replacements.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            changes_made += 1
            print(f"[OK] {old_name} -> {new_name}")
    
    if changes_made > 0:
        with open(planes_data_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"\n[OK] Total cambios: {changes_made}")
        return True
    else:
        print("[INFO] No se encontraron nombres viejos para reemplazar")
        return False

if __name__ == "__main__":
    print("Actualizando planes-data.js con nombres atractivos...")
    print("=" * 70)
    
    update_planes_data()
    
    print("\n" + "=" * 70)
    print("[OK] planes-data.js actualizado con nombres atractivos")