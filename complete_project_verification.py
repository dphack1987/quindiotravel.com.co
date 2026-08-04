"""
Verificación Completa del Proyecto Quindío Travel
Cuenta y verifica todas las páginas del proyecto
"""

from pathlib import Path
import os
import sys

# Configurar encoding para Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

def count_html_files():
    """Cuenta todos los archivos HTML del proyecto"""
    
    project_root = Path(__file__).parent
    
    # Contar archivos HTML en diferentes directorios
    html_files = {
        "raiz": list(project_root.glob("*.html")),
        "blog": list(project_root.glob("blog/*.html")),
        "programmatic_pages": list(project_root.glob("programmatic-pages/*.html")),
        "planes": list(project_root.glob("plan-*.html")),
        "alojamientos": list(project_root.glob("*hotel*.html")),
        "generated_pages": list(project_root.glob("generated-pages/**/*.html")),
        "generated_alojamiento": list(project_root.glob("generated-pages/alojamiento/*.html")),
        "generated_armenia": list(project_root.glob("generated-pages/armenia/**/*.html"))
    }
    
    total_count = 0
    report = {}
    
    for category, files in html_files.items():
        count = len(files)
        total_count += count
        report[category] = count
        print(f"{category}: {count} HTML files")
    
    print(f"\nTotal HTML files: {total_count}")
    return report, total_count

def verify_key_files():
    """Verifica archivos clave del proyecto"""
    
    project_root = Path(__file__).parent
    
    key_files = {
        "index.html": project_root / "index.html",
        "planes.html": project_root / "planes.html",
        "blog.html": project_root / "blog.html",
        "sitemap.xml": project_root / "sitemap.xml",
        "robots.txt": project_root / "robots.txt",
        "llms.txt": project_root / "llms.txt",
        "assets/js/planes-data.js": project_root / "assets" / "js" / "planes-data.js"
    }
    
    print("\nVerificación de archivos clave:")
    print("=" * 70)
    
    status = {}
    for filename, filepath in key_files.items():
        exists = filepath.exists()
        status[filename] = exists
        symbol = "[OK]" if exists else "[ERROR]"
        print(f"{symbol} {filename}: {'EXISTS' if exists else 'MISSING'}")
    
    return status

def verify_plan_names():
    """Verifica nombres de planes en archivos clave"""
    
    project_root = Path(__file__).parent
    
    # Verificar planes-data.js
    planes_data = project_root / "assets" / "js" / "planes-data.js"
    
    if planes_data.exists():
        with open(planes_data, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar nombres viejos no existan
        old_names = ["Plan 1:", "Plan 2:", "Plan 3:", "Plan 4:", "Plan 5:", "Plan 6:"]
        new_names = ["Escapada Cafetera", "Aventura Natural", "Experiencia Completa", "Relax y Aventura", "Experiencia Premium", "Experiencia Definitiva"]
        
        old_found = any(name in content for name in old_names)
        new_found = any(name in content for name in new_names)
        
        print("\nVerificación de nombres de planes:")
        print("=" * 70)
        print(f"[INFO] Nombres viejos (Plan 1:, etc.): {'ENCONTRADOS' if old_found else 'NO ENCONTRADOS'}")
        print(f"[OK] Nombres nuevos (Escapada Cafetera, etc.): {'ENCONTRADOS' if new_found else 'NO ENCONTRADOS'}")
        
        return {"old_names_found": old_found, "new_names_found": new_found}
    else:
        print("[ERROR] planes-data.js no encontrado")
        return {"old_names_found": None, "new_names_found": None}

def verify_sitemap():
    """Verifica sitemap.xml"""
    
    sitemap_path = Path(__file__).parent / "sitemap.xml"
    
    if sitemap_path.exists():
        with open(sitemap_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar problemas conocidos
        has_anchor = "#hoteles" in content
        has_crawl_delay = "Crawl-delay" in content
        
        # Contar URLs
        url_count = content.count("<url>")
        
        print("\nVerificación de sitemap.xml:")
        print("=" * 70)
        print(f"[OK] Total URLs: {url_count}")
        print(f"[INFO] Tiene anchor (#hoteles): {'SI' if has_anchor else 'NO'}")
        print(f"[INFO] Tiene crawl-delay: {'SI' if has_crawl_delay else 'NO'}")
        
        return {"url_count": url_count, "has_anchor": has_anchor, "has_crawl_delay": has_crawl_delay}
    else:
        print("[ERROR] sitemap.xml no encontrado")
        return None

def verify_robots_txt():
    """Verifica robots.txt"""
    
    robots_path = Path(__file__).parent / "robots.txt"
    
    if robots_path.exists():
        with open(robots_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_crawl_delay = "Crawl-delay" in content
        has_sitemap = "Sitemap:" in content
        
        print("\nVerificación de robots.txt:")
        print("=" * 70)
        print(f"[INFO] Tiene crawl-delay: {'SI' if has_crawl_delay else 'NO'}")
        print(f"[OK] Tiene sitemap referenciado: {'SI' if has_sitemap else 'NO'}")
        
        return {"has_crawl_delay": has_crawl_delay, "has_sitemap": has_sitemap}
    else:
        print("[ERROR] robots.txt no encontrado")
        return None

if __name__ == "__main__":
    print("VERIFICACIÓN COMPLETA DEL PROYECTO QUINDÍO TRAVEL")
    print("=" * 70)
    
    # Contar archivos HTML
    html_report, total_html = count_html_files()
    
    # Verificar archivos clave
    key_files_status = verify_key_files()
    
    # Verificar nombres de planes
    plan_names_status = verify_plan_names()
    
    # Verificar sitemap
    sitemap_status = verify_sitemap()
    
    # Verificar robots.txt
    robots_status = verify_robots_txt()
    
    print("\n" + "=" * 70)
    print("VERIFICACIÓN COMPLETADA")
    print(f"Total archivos HTML: {total_html}")
    print(f"Archivos clave: {sum(key_files_status.values())}/{len(key_files_status)} existentes")