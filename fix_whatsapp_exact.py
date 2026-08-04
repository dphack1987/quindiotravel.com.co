from pathlib import Path

def fix_whatsapp_exact():
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
            
            # Reemplazar específicamente los enlaces de WhatsApp
            old_pattern = f"Plan%20{plan_file.split('-')[1]}%20"
            new_pattern = plan_name.replace(' ', '%20') + '%20'
            content = content.replace(old_pattern, new_pattern)
            
            old_pattern2 = f"Plan%20{plan_file.split('-')[1]}"
            new_pattern2 = plan_name.replace(' ', '%20')
            content = content.replace(old_pattern2, new_pattern2)
            
            with open(plan_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed WhatsApp links: {plan_file} -> {plan_name}")

if __name__ == "__main__":
    fix_whatsapp_exact()