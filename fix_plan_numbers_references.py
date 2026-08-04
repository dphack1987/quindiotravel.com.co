from pathlib import Path

def fix_plan_numbers():
    plan_files = [
        "plan-1.html",
        "plan-2.html", 
        "plan-3.html",
        "plan-4.html",
        "plan-5.html",
        "plan-6.html"
    ]
    
    new_names = [
        "Escapada Cafetera de Fin de Semana",
        "Aventura Natural en el Eje Cafetero",
        "Experiencia Completa del Eje Cafetero",
        "Relax y Aventura en Termales del Eje",
        "Experiencia Premium del Eje Cafetero",
        "La Experiencia Definitiva del Eje Cafetero"
    ]
    
    for i, plan_file in enumerate(plan_files):
        plan_path = Path(__file__).parent / plan_file
        if plan_path.exists():
            with open(plan_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Reemplazar referencias a Plan 1, Plan 2, etc.
            content = content.replace(f"Plan {i+1}", new_names[i])
            content = content.replace(f"Plan {i+1}:", new_names[i] + ":")
            content = content.replace(f"Plan{i+1}", new_names[i])
            
            with open(plan_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed: {plan_file}")

if __name__ == "__main__":
    fix_plan_numbers()