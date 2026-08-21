import os

def fix_last_5():
    files_to_fix = [
        "blog-mejor-epoca-eje-cafetero.html",
        "index.html",
        "components/head/head.html"
    ]

    replacements = {
        'content="logo_quindio_travel.png"': 'content="assets/images/logo_quindio_travel.png"',
        'content="assets/images/paisajes/eje-cafetero-aerial-view.webp"': 'content="assets/images/paisajes/eje-cafetero-aerial-view.webp"',
        'content="assets/images/paisajes/colombian-coffee-fields.webp"': 'content="assets/images/paisajes/colombian-coffee-fields.webp"',
        'src="logo_quindio_travel.png"': 'src="assets/images/logo_quindio_travel.png"',
        'href="logo_quindio_travel.png"': 'href="assets/images/logo_quindio_travel.png"'
    }

    for file_path in files_to_fix:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)

            if new_content != content:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"✔ Corregido manualmente: {file_path}")

if __name__ == "__main__":
    fix_last_5()