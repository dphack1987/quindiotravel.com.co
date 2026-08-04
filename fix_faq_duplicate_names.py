"""
Corregir Nombres Duplicados en FAQ
Elimina nombres duplicados creados por el reemplazo
"""

from pathlib import Path

faq_fixes = {
    "plan-1.html": {
        "duplicate": "¿Qué incluye el Escapada Cafetera de Fin de Semana Vive El Eje Cafetero Temático?",
        "correct": "¿Qué incluye la Escapada Cafetera de Fin de Semana?"
    },
    "plan-2.html": {
        "duplicate": "¿Qué incluye el Aventura Natural en el Eje Cafetero Naturaleza y Diversión Cafetera?",
        "correct": "¿Qué incluye la Aventura Natural en el Eje Cafetero?"
    },
    "plan-3.html": {
        "duplicate": "¿Qué incluye el Experiencia Completa del Eje Cafetero La Experiencia Completa del Eje?",
        "correct": "¿Qué incluye la Experiencia Completa del Eje Cafetero?"
    },
    "plan-4.html": {
        "duplicate": "¿Qué incluye el Relax y Aventura en Termales del Eje Aventura y Relax Termal?",
        "correct": "¿Qué incluye el Relax y Aventura en Termales del Eje?"
    },
    "plan-5.html": {
        "duplicate": "¿Qué incluye el Experiencia Premium del Eje Cafetero Tradición y Raíces de la Arriería?",
        "correct": "¿Qué incluye la Experiencia Premium del Eje Cafetero?"
    },
    "plan-6.html": {
        "duplicate": "¿Qué incluye el La Experiencia Definitiva del Eje Cafetero Gran Quindío Integral?",
        "correct": "¿Qué incluye la Experiencia Definitiva del Eje Cafetero?"
    }
}

def fix_faq_duplicate(plan_file):
    """Corrige nombres duplicados en FAQ"""
    
    plan_path = Path(__file__).parent / plan_file
    
    if not plan_path.exists():
        print(f"Archivo {plan_file} no encontrado")
        return False
    
    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixes = faq_fixes.get(plan_file)
    if not fixes:
        print(f"No hay configuración para {plan_file}")
        return False
    
    if fixes["duplicate"] in content:
        content = content.replace(fixes["duplicate"], fixes["correct"])
        
        with open(plan_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"[OK] {plan_file} FAQ duplicado corregido")
        return True
    else:
        print(f"[INFO] {plan_file} no requiere corrección")
        return False

if __name__ == "__main__":
    print("Corrigiendo nombres duplicados en FAQ...")
    print("=" * 70)
    
    for plan_file in faq_fixes.keys():
        fix_faq_duplicate(plan_file)
    
    print("\n" + "=" * 70)
    print("[OK] Nombres duplicados en FAQ corregidos")