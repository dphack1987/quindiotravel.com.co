from pathlib import Path
import re

def fix_whatsapp_links_aggressive():
    plan_files = [
        "plan-1.html",
        "plan-2.html", 
        "plan-3.html",
        "plan-4.html",
        "plan-5.html",
        "plan-6.html"
    ]
    
    for plan_file in plan_files:
        plan_path = Path(__file__).parent / plan_file
        if plan_path.exists():
            with open(plan_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Eliminar todas las referencias a Plan 1-6 en los links de WhatsApp
            content = re.sub(r'Plan%20\d', 'Plan', content)
            content = re.sub(r'del%20Plan%20\d', 'del%20Plan', content)
            
            with open(plan_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed WhatsApp links: {plan_file}")

if __name__ == "__main__":
    fix_whatsapp_links_aggressive()