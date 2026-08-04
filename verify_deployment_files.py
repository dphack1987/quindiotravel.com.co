"""
Verificación de archivos para despliegue
Confirma que todos los archivos críticos existen y están listos para subir
"""

from pathlib import Path
import os

def verify_deployment_files():
    """Verifica que todos los archivos críticos existan"""
    
    root_dir = Path(__file__).parent
    
    # Archivos críticos para subir
    critical_files = [
        "sitemap.xml",
        "llms.txt", 
        "robots.txt",
        "index.html",
        ".well-known/ai-metadata.json"
    ]
    
    print("Verificando archivos críticos para despliegue...")
    print("=" * 60)
    
    all_exist = True
    file_sizes = {}
    
    for file_path in critical_files:
        full_path = root_dir / file_path
        
        if full_path.exists():
            size = os.path.getsize(full_path)
            file_sizes[file_path] = size
            print(f"[OK] {file_path} ({size} bytes)")
        else:
            print(f"[X] {file_path} (NO EXISTE)")
            all_exist = False
    
    print("\n" + "=" * 60)
    
    if all_exist:
        print("[OK] Todos los archivos críticos existen")
        print(f"Total tamaño: {sum(file_sizes.values())} bytes")
        print("\nArchivos listos para subir al servidor")
        
        # Verificar directorios
        programmatic_dir = root_dir / "programmatic-pages"
        blog_dir = root_dir / "blog"
        
        programmatic_count = len(list(programmatic_dir.glob('*.html')))
        blog_count = len(list(blog_dir.glob('*.html')))
        
        print(f"\nDirectorios:")
        print(f"- programmatic-pages: {programmatic_count} archivos HTML")
        print(f"- blog: {blog_count} archivos HTML")
        
        return True
    else:
        print("[X] Algunos archivos críticos faltan")
        print("Por favor generar los archivos faltantes antes del despliegue")
        return False

if __name__ == "__main__":
    success = verify_deployment_files()
    
    if success:
        print("\n" + "=" * 60)
        print("PROXIMO PASO:")
        print("1. Elegir metodo de subida (FTP, SSH, Panel de Control)")
        print("2. Subir archivos segun guia deployment_guide.md")
        print("3. Verificar accesibilidad de archivos en servidor")
        print("4. Someter sitemap a Google Search Console")
    else:
        print("\nPor favor generar archivos faltantes primero")