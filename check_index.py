import os
import re

def main():
    if not os.path.exists("index.html"):
        print("No se encontró el archivo index.html")
        return

    with open("index.html", "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # Buscar todas las rutas de imágenes en assets/images
    matches = re.findall(r'assets/images/[^\'\"\)\s>]+', content)
    unique_matches = set(matches)

    print(f"--- REVISANDO {len(unique_matches)} REFERENCIAS EN INDEX.HTML ---\n")
    missing = 0
    for img in sorted(unique_matches):
        clean_path = img.split('?')[0].split('#')[0]
        if not os.path.exists(clean_path):
            print(f"[NO EXISTE] {clean_path}")
            missing += 1

    print(f"\nTotal imágenes faltantes o con ruta incorrecta: {missing}")

if __name__ == "__main__":
    main()