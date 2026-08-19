#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re

ROOT_PATH = r'c:\Users\user\Documents\www.quindiotravel.com'

def fix_urgency_banner():
    """Arreglar el banner de urgencia para que no se corte visualmente"""
    
    index_path = Path(ROOT_PATH) / 'index.html'
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("\n" + "="*80)
    print("🔧 ARREGLANDO BANNER DE URGENCIA")
    print("="*80)
    
    # Buscar el banner actual
    old_banner_pattern = r'<div class="urgency-banner"[^>]*style="[^"]*">'
    
    # Nuevo banner mejorado
    new_banner = '<div class="urgency-banner" id="urgency-banner" style="background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; padding: 16px 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 50px; position: relative; z-index: 999; display: flex; align-items: center; justify-content: center; min-height: 70px; flex-wrap: wrap;">'
    
    # Reemplazar
    if 'urgency-banner' in content:
        # Encontrar la línea exacta
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'class="urgency-banner"' in line and 'style=' in line:
                # Arreglar esta línea
                lines[i] = '    <div class="urgency-banner" id="urgency-banner" style="background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; padding: 16px 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); margin-top: 50px; position: relative; z-index: 999; display: flex; align-items: center; justify-content: center; min-height: 70px;">'
                
                # Arreglar la línea del inner
                if i+1 < len(lines) and 'urgency-banner-inner' in lines[i+1]:
                    lines[i+1] = '        <div class="urgency-banner-inner" style="display: flex; align-items: center; justify-content: center; gap: 15px; flex-wrap: wrap; width: 100%; max-width: 1200px; margin: 0 auto; padding: 0 10px;">'
                
                print("✅ Banner mejorado con:")
                print("   - Padding aumentado: 12px → 16px")
                print("   - Altura mínima: 70px")
                print("   - Flexbox mejorado")
                print("   - Contenedor inner con max-width y padding")
                
                content = '\n'.join(lines)
                break
    
    # Añadir CSS responsivo al <style> existente
    # Buscar el cierre de </style>
    style_pattern = r'(}\s*</style>)'
    
    responsive_css = '''
    /* Responsive Urgency Banner */
    @media (max-width: 768px) {
        .urgency-banner {
            padding: 12px 15px !important;
            min-height: 90px !important;
            margin-top: 60px !important;
        }
        .urgency-banner-inner {
            gap: 8px !important;
        }
        .urgency-banner-message {
            flex-basis: 100% !important;
            order: 1;
        }
        .urgency-banner-timer {
            flex-basis: 100% !important;
            order: 2;
            width: 100%;
            justify-content: center !important;
        }
        .urgency-banner-cta {
            flex-basis: 100% !important;
            order: 3;
            width: 100%;
            max-width: 280px !important;
        }
    }
    
    @media (max-width: 480px) {
        .urgency-banner {
            padding: 12px 12px !important;
            min-height: 100px !important;
        }
        .urgency-banner-message span {
            font-size: 0.85rem !important;
        }
        .urgency-banner-timer {
            background: rgba(255,255,255,0.15) !important;
            padding: 4px 8px !important;
        }
        .urgency-banner-timer span:nth-child(2) {
            font-size: 0.95rem !important;
        }
        .urgency-banner-cta {
            font-size: 0.8rem !important;
            padding: 6px 16px !important;
        }
    }
}'''
    
    # Reemplazar el cierre de style
    if re.search(style_pattern, content):
        content = re.sub(style_pattern, responsive_css, content)
        print("✅ CSS responsivo agregado para dispositivos móviles")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n✅ Banner arreglado exitosamente")
    print("="*80)

if __name__ == '__main__':
    fix_urgency_banner()
