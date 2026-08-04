"""
Verificar Accesibilidad de Sitemap
Comprueba que el sitemap sea accesible y válido
"""

import requests
from pathlib import Path

def verify_sitemap():
    """Verifica accesibilidad del sitemap"""
    
    sitemap_url = "https://quindiotravel.com.co/sitemap.xml"
    
    try:
        response = requests.get(sitemap_url, timeout=10)
        
        print(f"Estado HTTP: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type', 'No especificado')}")
        print(f"Longitud: {len(response.content)} bytes")
        
        if response.status_code == 200:
            print("\n[OK] Sitemap accesible correctamente")
            
            # Verificar contenido XML
            content = response.text
            if '<?xml version="1.0"' in content and '<urlset' in content:
                print("[OK] Formato XML válido")
                
                # Contar URLs
                url_count = content.count('<url>')
                print(f"[OK] Total URLs: {url_count}")
                
                return True
            else:
                print("[ERROR] Formato XML inválido")
                return False
        else:
            print(f"[ERROR] Error HTTP: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"[ERROR] Excepción: {e}")
        return False

if __name__ == "__main__":
    print("Verificando accesibilidad del sitemap...")
    print("=" * 70)
    
    verify_sitemap()
    
    print("\n" + "=" * 70)
    print("Verificación completada")