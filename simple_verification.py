from pathlib import Path

project_root = Path(__file__).parent

# Count HTML files
html_files = list(project_root.glob("*.html"))
blog_files = list(project_root.glob("blog/*.html"))
programmatic_files = list(project_root.glob("programmatic-pages/*.html"))
plan_files = list(project_root.glob("plan-*.html"))

print("HTML Files Count:")
print(f"Root: {len(html_files)}")
print(f"Blog: {len(blog_files)}")
print(f"Programmatic: {len(programmatic_files)}")
print(f"Plans: {len(plan_files)}")
print(f"Total: {len(html_files) + len(blog_files) + len(programmatic_files) + len(plan_files)}")

# Key files verification
key_files = ["index.html", "planes.html", "blog.html", "sitemap.xml", "robots.txt"]
print("\nKey Files:")
for filename in key_files:
    exists = (project_root / filename).exists()
    print(f"{filename}: {'OK' if exists else 'MISSING'}")

# Sitemap verification
sitemap = project_root / "sitemap.xml"
if sitemap.exists():
    with open(sitemap, 'r', encoding='utf-8') as f:
        content = f.read()
    url_count = content.count("<url>")
    has_anchor = "#hoteles" in content
    print(f"\nSitemap URLs: {url_count}")
    print(f"Has anchor: {has_anchor}")

# Robots.txt verification
robots = project_root / "robots.txt"
if robots.exists():
    with open(robots, 'r', encoding='utf-8') as f:
        content = f.read()
    has_crawl_delay = "Crawl-delay" in content
    print(f"Robots.txt has crawl-delay: {has_crawl_delay}")