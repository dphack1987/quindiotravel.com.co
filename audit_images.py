import os
import re

def audit_image_references():
    root_dir = "."
    image_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.svg', '.avif')
    
    # 1. Obtener inventario de imágenes reales en disco (normalizadas en minúsculas para comparar)
    real_files = {}
    for dirpath, _, filenames in os.walk(os.path.join(root_dir, "assets")):
        for f in filenames:
            if f.lower().endswith(image_extensions):
                full_path = os.path.normpath(os.path.join(dirpath, f))
                # Guardar ruta relativa desde la raíz en minúsculas
                real_files[full_path.lower().replace("\\", "/")] = full_path

    print(f"Total imágenes en disco (assets): {len(real_files)}\n")

    # Regex para capturar rutas de imágenes en src="..." o url(...)
    regex = re.compile(r'(?:src|href|url)\s*=\s*["\']?([^"\'\s>]+\.(?:jpg|jpeg|png|webp|svg|avif))', re.IGNORECASE)

    missing_count = 0
    fixed_matches = []

    # 2. Analizar cada archivo HTML
    for dirpath, _, filenames in os.walk(root_dir):
        if '.git' in dirpath:
            continue
        for file in filenames:
            if file.endswith(".html"):
                html_path = os.path.normpath(os.path.join(dirpath, file))
                rel_dir = os.path.relpath(dirpath, root_dir)

                try:
                    with open(html_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()

                    matches = regex.findall(content)
                    for raw_src in set(matches):
                        # Limpiar la ruta para resolverla desde la raíz
                        clean_src = raw_src.strip()
                        if clean_src.startswith("http"):
                            continue # Ignorar URLs externas

                        # Resolver ruta según el nivel del HTML
                        if rel_dir == ".":
                            target_path = clean_src
                        else:
                            target_path = os.path.normpath(os.path.join(rel_dir, clean_src))

                        target_path_norm = target_path.replace("\\", "/").lower()

                        # Verificar si existe exactamente
                        if target_path_norm not in real_files:
                            missing_count += 1
                            
                            # Buscar sugerencia (mismo nombre distinta extensión)
                            base_name = os.path.splitext(target_path_norm)[0]
                            possible_fix = [rf for rf in real_files if rf.startswith(base_name)]

                            print(f"[NO ENCONTRADA] En: {html_path}")
                            print(f"  Llamada original: {clean_src}")
                            if possible_fix:
                                suggested = real_files[possible_fix[0]]
                                print(f"  --> SUGERENCIA EN DISCO: {suggested}")
                            else:
                                print("  --> NO EXISTE NINGÚN ARCHIVO SIMILAR EN ASSETS")
                            print("-" * 50)

                except Exception as e:
                    print(f"Error procesando {html_path}: {e}")

    print(f"\nResumen: Se encontraron {missing_count} referencias a imágenes rotas.")

if __name__ == "__main__":
    audit_image_references()