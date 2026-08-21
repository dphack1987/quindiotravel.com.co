import os
import re

def check_everything():
    root_dir = "."
    missing_count = 0
    total_refs = 0

    print("--- INICIANDO AUDITORÍA EN HTML, JS Y COMPONENTES ---\n")

    for dirpath, _, filenames in os.walk(root_dir):
        if '.git' in dirpath:
            continue
            
        for file in filenames:
            if file.endswith((".html", ".js")):
                filepath = os.path.join(dirpath, file)
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                # Buscar cualquier coincidencia que apunte a assets
                matches = re.findall(r'(?:src|href|url|content|src\s*:\s*)["\']?([^"\'\)\s>]+\.(?:png|jpg|jpeg|webp|svg))', content, re.IGNORECASE)
                
                for img_path in set(matches):
                    if "assets/" in img_path or "images/" in img_path:
                        total_refs += 1
                        
                        # Limpiar variables o rutas HTTP completas
                        clean_path = img_path.replace("https://quindiotravel.com.co/", "").split('?')[0]
                        if clean_path.startswith("/"):
                            clean_path = clean_path[1:]
                            
                        if not os.path.exists(clean_path):
                            print(f"[FALTA EN DISCO] En: {filepath}")
                            print(f"   └── Ruta llamada: {img_path}\n")
                            missing_count += 1

    print(f"Resultados: {total_refs} imágenes analizadas. {missing_count} no existen realmente en la ruta llamada.")

if __name__ == "__main__":
    check_everything()