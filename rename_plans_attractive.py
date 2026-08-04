"""
Renombrar Planes con Nombres Atractivos para Turistas
Elimina números y crea nombres más emocionales y turísticos
"""

from pathlib import Path

# Nombres nuevos atractivos para planes
attractive_names = {
    "plan-1.html": {
        "old_name": "Plan 1: Vive El Eje Cafetero Temático",
        "new_name": "Escapada Cafetera de Fin de Semana",
        "old_title": "Plan 2 Días 1 Noche Eje Cafetero: Parque del Café y PANACA",
        "new_title": "Escapada Cafetera de Fin de Semana: Parque del Café y PANACA"
    },
    "plan-2.html": {
        "old_name": "Plan 2: Naturaleza y Diversión Cafetera",
        "new_name": "Aventura Natural en el Eje Cafetero",
        "old_title": "Plan 3 Días 2 Noches Eje Cafetero: Naturaleza y Diversión",
        "new_title": "Aventura Natural en el Eje Cafetero: 3 Días de Experiencia"
    },
    "plan-3.html": {
        "old_name": "Plan 3: La Experiencia Completa del Eje",
        "new_name": "Experiencia Completa del Eje Cafetero",
        "old_title": "Plan 4 Días 3 Noches Eje Cafetero: Experiencia Completa",
        "new_title": "Experiencia Completa del Eje Cafetero: 4 Días de Aventura"
    },
    "plan-4.html": {
        "old_name": "Plan 4: Aventura y Relax Termal",
        "new_name": "Relax y Aventura en Termales del Eje",
        "old_title": "Plan 4 Días 3 Noches Eje Cafetero: Aventura y Relax Termal",
        "new_title": "Relax y Aventura en Termales del Eje: 4 Días de Bienestar"
    },
    "plan-5.html": {
        "old_name": "Plan 5: Experiencia Premium VIP",
        "new_name": "Experiencia Premium del Eje Cafetero",
        "old_title": "Plan 5 Días 4 Noches Eje Cafetero: Experiencia Premium VIP",
        "new_title": "Experiencia Premium del Eje Cafetero: 5 Días de Lujo"
    },
    "plan-6.html": {
        "old_name": "Plan 6: Experiencia Definitiva Premium",
        "new_name": "La Experiencia Definitiva del Eje Cafetero",
        "old_title": "Plan 5 Días 4 Noches Eje Cafetero: Experiencia Definitiva Premium",
        "new_title": "La Experiencia Definitiva del Eje Cafetero: 5 Días Inolvidables"
    }
}

def rename_plan_attractive(plan_file):
    """Renombra un plan con nombre atractivo"""
    
    plan_path = Path(__file__).parent / plan_file
    
    if not plan_path.exists():
        print(f"Archivo {plan_file} no encontrado")
        return False
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    names = attractive_names.get(plan_file)
    if not names:
        print(f"No hay configuración para {plan_file}")
        return False
    
    # Reemplazar nombres en schema
    content = content.replace(f'"{names["old_name"]}"', f'"{names["new_name"]}"')
    
    # Reemplazar títulos
    content = content.replace(f'<title>{names["old_title"]}', f'<title>{names["new_title"]}')
    content = content.replace(f'<meta property="og:title" content="{names["old_title"]}', f'<meta property="og:title" content="{names["new_title"]}')
    content = content.replace(f'<meta name="twitter:title" content="{names["old_title"]}', f'<meta name="twitter:title" content="{names["new_title"]}')
    
    # Corregir inconsistencias geográficas en plan-3.html
    if plan_file == "plan-3.html":
        content = content.replace('Tour Festivo Independencia de Cartagena 2026', 'Tour Festivo Independencia Eje Cafetero 2026')
        content = content.replace('Tour especial para festivo de Independencia de Cartagena', 'Tour especial para festivo de Independencia en el Eje Cafetero')
        content = content.replace('Gran Quindío Completo', 'Eje Cafetero Completo')
    
    with open(plan_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] {plan_file} renombrado: {names['old_name']} -> {names['new_name']}")
    return True

if __name__ == "__main__":
    print("Renombrando planes con nombres atractivos para turistas...")
    print("=" * 70)
    
    for plan_file in attractive_names.keys():
        rename_plan_attractive(plan_file)
    
    print("\n" + "=" * 70)
    print("[OK] Todos los planes han sido renombrados con nombres atractivos")
    print("[OK] Inconsistencias geograficas corregidas")
    print("[OK] Numeros eliminados de los nombres de planes")