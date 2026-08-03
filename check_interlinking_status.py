from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
html_files = list(programmatic_dir.glob('*.html'))

print(f"Total archivos: {len(html_files)}")

with_links = 0
without_links = 0

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'related-links' in content:
        with_links += 1
    else:
        without_links += 1
        print(f"Sin links: {filepath.name}")

print(f"\nCon enlaces: {with_links}")
print(f"Sin enlaces: {without_links}")