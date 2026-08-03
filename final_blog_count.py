from pathlib import Path

blog_dir = Path(__file__).parent / "blog"
html_files = list(blog_dir.glob('*.html'))

print(f"Archivos HTML en blog/: {len(html_files)}")
for f in html_files:
    print(f"- {f.name}")