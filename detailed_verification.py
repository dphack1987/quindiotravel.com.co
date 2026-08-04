from pathlib import Path

project_root = Path(__file__).parent

print("DETAILED PROJECT VERIFICATION")
print("=" * 70)

# 1. Count HTML files by category
html_files = list(project_root.glob("*.html"))
blog_files = list(project_root.glob("blog/*.html"))
programmatic_files = list(project_root.glob("programmatic-pages/*.html"))
plan_files = list(project_root.glob("plan-*.html"))
hotel_files = list(project_root.glob("*hotel*.html"))

print("\n1. HTML FILES COUNT:")
print(f"Root directory: {len(html_files)}")
print(f"Blog directory: {len(blog_files)}")
print(f"Programmatic pages: {len(programmatic_files)}")
print(f"Plan files: {len(plan_files)}")
print(f"Hotel files: {len(hotel_files)}")
print(f"Total HTML files: {len(html_files) + len(blog_files) + len(programmatic_files) + len(plan_files)}")

# 2. Key files verification
print("\n2. KEY FILES VERIFICATION:")
key_files = ["index.html", "planes.html", "blog.html", "sitemap.xml", "robots.txt", "llms.txt"]
for filename in key_files:
    exists = (project_root / filename).exists()
    status = "OK" if exists else "MISSING"
    print(f"{filename}: {status}")

# 3. Sitemap verification
print("\n3. SITEMAP VERIFICATION:")
sitemap = project_root / "sitemap.xml"
if sitemap.exists():
    with open(sitemap, 'r', encoding='utf-8') as f:
        content = f.read()
    url_count = content.count("<url>")
    has_anchor = "#hoteles" in content
    has_index_anchor = "index.html#" in content
    has_blog = "blog.html" in content
    blog_urls = content.count("blog/")
    programmatic_urls = content.count("programmatic-pages/")
    
    print(f"Total URLs in sitemap: {url_count}")
    print(f"Has anchor (#hoteles): {has_anchor}")
    print(f"Has index.html# anchor: {has_index_anchor}")
    print(f"Has blog.html: {has_blog}")
    print(f"Blog URLs: {blog_urls}")
    print(f"Programmatic URLs: {programmatic_urls}")

# 4. Robots.txt verification
print("\n4. ROBOTS.TXT VERIFICATION:")
robots = project_root / "robots.txt"
if robots.exists():
    with open(robots, 'r', encoding='utf-8') as f:
        content = f.read()
    has_crawl_delay = "Crawl-delay" in content
    has_sitemap = "Sitemap:" in content
    allows_blog = "Allow: /blog/" in content
    allows_programmatic = "Allow: /programmatic-pages/" in content
    
    print(f"Has crawl-delay: {has_crawl_delay}")
    print(f"Has sitemap reference: {has_sitemap}")
    print(f"Allows /blog/: {allows_blog}")
    print(f"Allows /programmatic-pages/: {allows_programmatic}")

# 5. Plan names verification
print("\n5. PLAN NAMES VERIFICATION:")
planes_data = project_root / "assets" / "js" / "planes-data.js"
if planes_data.exists():
    with open(planes_data, 'r', encoding='utf-8') as f:
        content = f.read()
    
    old_names = ["Plan 1:", "Plan 2:", "Plan 3:", "Plan 4:", "Plan 5:", "Plan 6:"]
    new_names = ["Escapada Cafetera", "Aventura Natural", "Experiencia Completa", "Relax y Aventura", "Experiencia Premium", "Experiencia Definitiva"]
    
    old_found = any(name in content for name in old_names)
    new_found = any(name in content for name in new_names)
    
    print(f"Old names (Plan 1:, etc.) found: {old_found}")
    print(f"New names (Escapada Cafetera, etc.) found: {new_found}")

# 6. Schema verification in plan files
print("\n6. SCHEMA VERIFICATION IN PLAN FILES:")
for plan_file in plan_files:
    with open(plan_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    has_schema = "@type" in content
    has_organization = "TravelAgency" in content
    has_product = "Product" in content or "TouristTrip" in content
    
    print(f"{plan_file.name}: Schema={has_schema}, Org={has_organization}, Product={has_product}")

print("\n" + "=" * 70)
print("VERIFICATION COMPLETED")