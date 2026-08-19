import os
import re
from pathlib import Path

html_files = [f for f in Path('.').rglob('*.html') if not any(p.startswith('.') for p in f.parts)]
missing = 0
print(f"Analizando {len(html_files)} archivos HTML...\n")

for file in html_files:
    try:
        content = file.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        continue
    
    matches = re.findall(r'(?:src|poster)=["\']([^"\']+)["\']', content)
    for src in matches:
        if src.startswith(('http', '//', 'data:', 'javascript:')) or not src.strip():
            continue
        clean = src.split('?')[0].split('#')[0]
        target = Path('.' + clean).resolve() if clean.startswith('/') else (file.parent / clean).resolve()
        if not target.exists():
            print(f"[FALTA] {file} -> {src}")
            missing += 1

print(f"\nTotal faltantes: {missing}")