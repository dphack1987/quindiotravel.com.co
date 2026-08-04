"""
Actualizar Secciones FAQ en Planes HTML
Actualiza preguntas en FAQ con nombres nuevos de planes
"""

from pathlib import Path

# Mapeo de nombres viejos a nuevos para FAQ
faq_replacements = {
    "Plan 1: Vive El Eje Cafetero Temático": "Escapada Cafetera de Fin de Semana",
    "Plan 2: Naturaleza y Diversión Cafetera": "Aventura Natural en el Eje Cafetero",
    "Plan 3: La Experiencia Completa del Eje": "Experiencia Completa del Eje Cafetero",
    "Plan 4: Aventura y Relax Termal": "Relax y Aventura en Termales del Eje",
    "Plan 5: Tradición y Raíces de la Arriería": "Experiencia Premium del Eje Cafetero",
    "Plan 6: Gran Quindío Integral": "La Experiencia Definitiva del Eje Cafetero"
}

# Simplificado para reemplazar solo "Plan 1:", "Plan 2:", etc.
simple_replacements = {
    "Plan 1:": "Escapada Cafetera de Fin de Semana",
    "Plan 2:": "Aventura Natural en el Eje Cafetero",
    "Plan 3:": "Experiencia Completa del Eje Cafetero",
    "Plan 4:": "Relax y Aventura en Termales del Eje",
    "Plan 5:": "Experiencia Premium del Eje Cafetero",
    "Plan 6:": "La Experiencia Definitiva del Eje Cafetero"
}

def update_faq_in_plan(plan_file):
    """Actualiza FAQ en un archivo de plan"""
    
    plan_path = Path(__file__).parent / plan_file
    
    if not plan_path.exists():
        print(f"Archivo {plan_file} no encontrado")
        return False
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar nombres en FAQ
    changes_made = 0
    for old_name, new_name in simple_replacements.items():
        if old_name in content:
            content = content.replace(old_name, new_name)
            changes_made += 1
    
    if changes_made > 0:
        with open(plan_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] {plan_file} FAQ actualizado ({changes_made} cambios)")
        return True
    else:
        print(f"[INFO] {plan_file} no requiere cambios en FAQ")
        return False

if __name__ == "__main__":
    print("Actualizando secciones FAQ en planes HTML...")
    print("=" * 70)
    
    plan_files = ["plan-1.html", "plan-2.html", "plan-3.html", "plan-4.html", "plan-5.html", "plan-6.html"]
    
    total_changes = 0
    for plan_file in plan_files:
        if update_faq_in_plan(plan_file):
            total_changes += 1
    
    print("\n" + "=" * 70)
    print(f"[OK] Total archivos actualizados: {total_changes}")
    print("[OK] Secciones FAQ actualizadas con nombres atractivos")