"""
Actualizar Meta Tags de Planes con Nombres Atractivos
Actualiza og:title y twitter:title con nombres nuevos
"""

from pathlib import Path

# Nombres nuevos para meta tags
meta_tags_updates = {
    "plan-1.html": {
        "old_og_title": 'Plan 2D/1N Vive Eje Cafetero Temático 2026 | Quindío Travel',
        "new_og_title": 'Escapada Cafetera de Fin de Semana 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 2D/1N Vive Eje Cafetero 2026',
        "new_twitter_title": 'Escapada Cafetera de Fin de Semana 2026'
    },
    "plan-2.html": {
        "old_og_title": 'Plan 3D/2N Naturaleza y Diversión Cafetera 2026 | Quindío Travel',
        "new_og_title": 'Aventura Natural en el Eje Cafetero 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 3D/2N Naturaleza y Diversión Cafetera 2026',
        "new_twitter_title": 'Aventura Natural en el Eje Cafetero 2026'
    },
    "plan-3.html": {
        "old_og_title": 'Plan 4D/3N La Experiencia Completa del Eje 2026 | Quindío Travel',
        "new_og_title": 'Experiencia Completa del Eje Cafetero 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 4D/3N La Experiencia Completa del Eje 2026',
        "new_twitter_title": 'Experiencia Completa del Eje Cafetero 2026'
    },
    "plan-4.html": {
        "old_og_title": 'Plan 4D/3N Aventura y Relax Termal 2026 | Quindío Travel',
        "new_og_title": 'Relax y Aventura en Termales del Eje 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 4D/3N Aventura y Relax Termal 2026',
        "new_twitter_title": 'Relax y Aventura en Termales del Eje 2026'
    },
    "plan-5.html": {
        "old_og_title": 'Plan 5D/4N Experiencia Premium VIP 2026 | Quindío Travel',
        "new_og_title": 'Experiencia Premium del Eje Cafetero 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 5D/4N Experiencia Premium VIP 2026',
        "new_twitter_title": 'Experiencia Premium del Eje Cafetero 2026'
    },
    "plan-6.html": {
        "old_og_title": 'Plan 5D/4N Experiencia Definitiva Premium 2026 | Quindío Travel',
        "new_og_title": 'La Experiencia Definitiva del Eje Cafetero 2026 | Quindío Travel',
        "old_twitter_title": 'Plan 5D/4N Experiencia Definitiva Premium 2026',
        "new_twitter_title": 'La Experiencia Definitiva del Eje Cafetero 2026'
    }
}

def update_meta_tags(plan_file):
    """Actualiza meta tags de un plan"""
    
    plan_path = Path(__file__).parent / plan_file
    
    if not plan_path.exists():
        print(f"Archivo {plan_file} no encontrado")
        return False
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updates = meta_tags_updates.get(plan_file)
    if not updates:
        print(f"No hay configuración para {plan_file}")
        return False
    
    # Actualizar og:title
    content = content.replace(f'<meta property="og:title" content="{updates["old_og_title"]}"', 
                            f'<meta property="og:title" content="{updates["new_og_title"]}"')
    
    # Actualizar twitter:title
    content = content.replace(f'<meta name="twitter:title" content="{updates["old_twitter_title"]}"', 
                            f'<meta name="twitter:title" content="{updates["new_twitter_title"]}"')
    
    with open(plan_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"[OK] {plan_file} meta tags actualizados")
    return True

if __name__ == "__main__":
    print("Actualizando meta tags de planes con nombres atractivos...")
    print("=" * 70)
    
    for plan_file in meta_tags_updates.keys():
        update_meta_tags(plan_file)
    
    print("\n" + "=" * 70)
    print("[OK] Todos los meta tags han sido actualizados con nombres atractivos")