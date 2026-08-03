from pathlib import Path

programmatic_dir = Path(__file__).parent / "programmatic-pages"
html_files = list(programmatic_dir.glob('*.html'))

print(f"Total páginas programáticas: {len(html_files)}")