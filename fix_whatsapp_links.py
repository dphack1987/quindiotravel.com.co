from pathlib import Path

def fix_whatsapp_links():
    plan_files = [
        ("plan-1.html", "Escapada Cafetera de Fin de Semana"),
        ("plan-2.html", "Aventura Natural en el Eje Cafetero"), 
        ("plan-3.html", "Experiencia Completa del Eje Cafetero"),
        ("plan-4.html", "Relax y Aventura en Termales del Eje"),
        ("plan-5.html", "Experiencia Premium del Eje Cafetero"),
        ("plan-6.html", "La Experiencia Definitiva del Eje Cafetero")
    ]
    
    for plan_file, plan_name in plan_files:
        plan_path = Path(__file__).parent / plan_file
        if plan_path.exists():
            with open(plan_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Reemplazar referencias a Plan 1, Plan 2, etc. con nombres atractivos en links de WhatsApp
            import re
            content = re.sub(r'Plan%20\d', plan_name.replace(' ', '%20'), content)
            content = re.sub(r'del%20Plan%20\d', 'del%20' + plan_name.replace(' ', '%20'), content)
            
            with open(plan_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed WhatsApp links: {plan_file} -> {plan_name}")

if __name__ == "__main__":
    fix_whatsapp_links()