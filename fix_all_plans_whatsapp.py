from pathlib import Path

def fix_all_plans_whatsapp():
    plan_mapping = {
        "plan-1.html": "Escapada Cafetera de Fin de Semana",
        "plan-2.html": "Aventura Natural en el Eje Cafetero", 
        "plan-3.html": "Experiencia Completa del Eje Cafetero",
        "plan-4.html": "Relax y Aventura en Termales del Eje",
        "plan-5.html": "Experiencia Premium del Eje Cafetero",
        "plan-6.html": "La Experiencia Definitiva del Eje Cafetero"
    }
    
    for plan_file, plan_name in plan_mapping.items():
        plan_path = Path(__file__).parent / plan_file
        if plan_path.exists():
            with open(plan_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Buscar y reemplazar los links de WhatsApp específicos
            import re
            # Patrón para los links de WhatsApp con plan numbers
            pattern = r'wa\.me/573174426044\?text=Hola%20Quind%C3%ADo%20Travel,%20deseo%20cotizar%20el%20Plan%20\d+%20'
            replacement = f'wa.me/573174426044?text=Hola%20Quind%C3%ADo%20Travel,%20deseo%20cotizar%20el%20{plan_name.replace(" ", "%20")}%20'
            content = re.sub(pattern, replacement, content)
            
            pattern2 = r'wa\.me/573174426044\?text=Hola%20Quind%C3%ADo%20Travel,%20por%20favor%20enviarme%20ficha%20t%C3%A9cnica%20y%20disponibilidad%20del%20Plan%20\d+%20'
            replacement2 = f'wa.me/573174426044?text=Hola%20Quind%C3%ADo%20Travel,%20por%20favor%20enviarme%20ficha%20t%C3%A9cnica%20y%20disponibilidad%20del%20{plan_name.replace(" ", "%20")}%20'
            content = re.sub(pattern2, replacement2, content)
            
            with open(plan_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {plan_file} -> {plan_name}")

if __name__ == "__main__":
    fix_all_plans_whatsapp()