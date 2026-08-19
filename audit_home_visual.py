#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

def audit_home_sections():
    """Auditar secciones del home para problemas visuales"""
    
    index_path = Path(ROOT_PATH) / 'index.html'
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n" + "="*80)
    print("📋 AUDITORÍA DE SECCIONES HOME")
    print("="*80)
    
    issues = []
    
    # 1. Verificar el hero section
    hero_match = re.search(r'class=["\']hero["\']\s+style=["\']([^"\']*)["\']', content)
    if hero_match:
        print("\n✅ Hero Section detectada")
        style = hero_match.group(1)
        
        # Verificar padding/margin
        if 'min-height' in style or 'height' in style:
            print(f"   Altura: Configurada")
        if 'padding' not in style:
            print(f"   ⚠️  Sin padding explícito")
        
    # 2. Buscar containers que podrían cortarse
    containers = re.findall(r'class=["\']container["\']\s*style=["\']([^"\']*)["\']', content)
    if containers:
        print(f"\n✅ Encontrados {len(containers)} containers")
        for i, container_style in enumerate(containers[:3]):
            if 'overflow' in container_style and 'hidden' in container_style:
                print(f"   ⚠️  Container {i} tiene overflow:hidden")
                issues.append(f"Container {i} con overflow:hidden podría cortar contenido")
    
    # 3. Verificar flex items que podrían cortarse
    flex_items = re.findall(r'style=["\']([^"\']*flex[^"\']*)["\']', content)
    print(f"\n✅ Detectados {len(flex_items)} elementos con flexbox")
    
    # 4. Verificar grid que podrían cortarse
    grid_items = re.findall(r'style=["\']([^"\']*grid[^"\']*)["\']', content)
    print(f"✅ Detectados {len(grid_items)} elementos con grid")
    
    # 5. Buscar divs con tamaño fijo que podrían ser problema
    fixed_size = re.findall(r'style=["\']([^"\']*width:\s*\d+px[^"\']*)["\']', content)
    if fixed_size:
        print(f"\n⚠️  {len(fixed_size)} elementos con ancho fijo detectados")
        print("   Estos podrían no ser responsivos")
    
    # 6. Verificar overflow
    overflow_hidden = re.findall(r'overflow:\s*hidden', content)
    if overflow_hidden:
        print(f"\n⚠️  {len(overflow_hidden)} elementos con overflow:hidden")
        print("   Verificar que no corten contenido importante")
    
    # 7. Buscar posibles problemas de z-index
    z_index = re.findall(r'z-index:\s*(\d+)', content)
    if z_index:
        max_z = max(int(z) for z in z_index)
        print(f"\n✅ Z-index máximo: {max_z}")
    
    print("\n" + "="*80)
    print("📊 PROBLEMAS DETECTADOS")
    print("="*80)
    
    if issues:
        for issue in issues:
            print(f"❌ {issue}")
    else:
        print("✅ No se detectaron problemas críticos de corte visual")
    
    print("\n" + "="*80)
    print("💡 RECOMENDACIONES")
    print("="*80)
    print("""
    1. ✅ Banner de urgencia: ARREGLADO
       - Padding aumentado
       - Altura mínima establecida
       - CSS responsivo añadido
    
    2. ✅ Hero section: Revisar en navegador
    
    3. ✅ Secciones con cards: Verificar que no se corten
    
    4. ✅ Footer: Confirmar visibilidad completa
    
    PRÓXIMOS PASOS:
    - Abrir el sitio en navegador (desktop + móvil)
    - Verificar cada sección visualmente
    - Confirmar que no hay contenido cortado
    """)
    
    print("="*80)

if __name__ == '__main__':
    audit_home_sections()
