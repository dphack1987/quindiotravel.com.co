"""
Análisis honesto de capacidad para liderazgo #1 en buscadores
"""

import re
from pathlib import Path
from collections import defaultdict

def analyze_content_depth(file_path):
    """Analiza profundidad de contenido"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer texto visible (eliminar scripts, styles, etc.)
    visible_text = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
    visible_text = re.sub(r'<style[^>]*>.*?</style>', '', visible_text, flags=re.DOTALL)
    visible_text = re.sub(r'<[^>]+>', '', visible_text)
    
    word_count = len(visible_text.split())
    char_count = len(visible_text)
    
    # Detectar diferentes tipos de contenido
    has_itinerary = 'itinerario' in visible_text.lower() or 'día' in visible_text.lower()
    has_pricing = 'precio' in visible_text.lower() or 'cop' in visible_text.lower()
    has_contact = 'whatsapp' in visible_text.lower() or 'teléfono' in visible_text.lower()
    has_images = '<img' in content
    
    return {
        'word_count': word_count,
        'char_count': char_count,
        'has_itinerary': has_itinerary,
        'has_pricing': has_pricing,
        'has_contact': has_contact,
        'has_images': has_images
    }

def analyze_trust_signals(file_path):
    """Analiza señales de confianza"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    trust_signals = {
        'has_rnt': 'RNT' in content or '18152' in content,
        'has_phone': '+57' in content or '317' in content,
        'has_email': '@' in content,
        'has_address': 'Cra' in content or 'calle' in content.lower(),
        'has_social_proof': 'review' in content.lower() or 'rating' in content.lower(),
        'has_testimonials': 'testimonio' in content.lower() or 'opinión' in content.lower(),
        'has_ssl_indicators': 'https' in content
    }
    
    return trust_signals

def analyze_local_signals(file_path):
    """Analiza señales locales"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    local_signals = {
        'has_local_schema': 'LocalBusiness' in content,
        'has_geo_coordinates': 'latitude' in content and 'longitude' in content,
        'has_opening_hours': 'openingHours' in content,
        'has_price_range': 'priceRange' in content,
        'has_payment_methods': 'paymentMethod' in content,
        'has_area_served': 'areaServed' in content
    }
    
    return local_signals

def analyze_content_quality(file_path):
    """Analiza calidad de contenido"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    quality_indicators = {
        'has_headings': '<h1>' in content or '<h2>' in content,
        'has_structured_content': '<h2>' in content and '<h3>' in content,
        'has_bullet_points': '<ul>' in content or '<ol>' in content,
        'has_bold_keywords': '<strong>' in content or '<b>' in content,
        'has_internal_links': 'href="' in content and '.html' in content,
        'has_external_authority': 'wikipedia' in content.lower() or 'gov' in content.lower()
    }
    
    return quality_indicators

def main():
    """Análisis completo de capacidad de liderazgo"""
    base_dir = Path(__file__).parent
    
    print("ANALISIS HONESTO: CAPACIDAD PARA LIDERAZGO #1")
    print("=" * 70)
    
    # Analizar página principal
    print("\n1. ANALISIS DE CONTENIDO - index.html")
    content_analysis = analyze_content_depth(base_dir / "index.html")
    print(f"   Palabras: {content_analysis['word_count']}")
    print(f"   Caracteres: {content_analysis['char_count']}")
    print(f"   Tiene itinerario: {content_analysis['has_itinerary']}")
    print(f"   Tiene precios: {content_analysis['has_pricing']}")
    print(f"   Tiene contacto: {content_analysis['has_contact']}")
    print(f"   Tiene imágenes: {content_analysis['has_images']}")
    
    print("\n2. ANALISIS DE SEÑALES DE CONFIANZA")
    trust_analysis = analyze_trust_signals(base_dir / "index.html")
    print(f"   Tiene RNT: {trust_analysis['has_rnt']}")
    print(f"   Tiene teléfono: {trust_analysis['has_phone']}")
    print(f"   Tiene email: {trust_analysis['has_email']}")
    print(f"   Tiene dirección: {trust_analysis['has_address']}")
    print(f"   Tiene social proof: {trust_analysis['has_social_proof']}")
    print(f"   Tiene testimonios: {trust_analysis['has_testimonials']}")
    
    print("\n3. ANALISIS DE SEÑALES LOCALES")
    local_analysis = analyze_local_signals(base_dir / "index.html")
    print(f"   Tiene LocalBusiness schema: {local_analysis['has_local_schema']}")
    print(f"   Tiene coordenadas geo: {local_analysis['has_geo_coordinates']}")
    print(f"   Tiene horarios: {local_analysis['has_opening_hours']}")
    print(f"   Tiene rango de precios: {local_analysis['has_price_range']}")
    print(f"   Tiene métodos de pago: {local_analysis['has_payment_methods']}")
    print(f"   Tiene área servida: {local_analysis['has_area_served']}")
    
    print("\n4. ANALISIS DE CALIDAD DE CONTENIDO")
    quality_analysis = analyze_content_quality(base_dir / "index.html")
    print(f"   Tiene encabezados: {quality_analysis['has_headings']}")
    print(f"   Tiene contenido estructurado: {quality_analysis['has_structured_content']}")
    print(f"   Tiene listas: {quality_analysis['has_bullet_points']}")
    print(f"   Tiene keywords en negrita: {quality_analysis['has_bold_keywords']}")
    print(f"   Tiene enlaces internos: {quality_analysis['has_internal_links']}")
    print(f"   Tiene autoridad externa: {quality_analysis['has_external_authority']}")
    
    # Analizar planes
    print("\n5. ANALISIS DE PAGINAS DE PLANES")
    plan_files = ["plan-1.html", "plan-2.html", "plan-3.html", "plan-4.html", "plan-5.html", "plan-6.html"]
    
    total_words = 0
    plans_with_faq = 0
    
    for plan_file in plan_files:
        file_path = base_dir / plan_file
        if file_path.exists():
            plan_content = analyze_content_depth(file_path)
            total_words += plan_content['word_count']
            
            # Verificar FAQ schema
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'FAQPage' in content:
                plans_with_faq += 1
    
    print(f"   Total palabras en planes: {total_words}")
    print(f"   Promedio palabras por plan: {total_words // 6}")
    print(f"   Planes con FAQ Schema: {plans_with_faq}/6")
    
    # Análisis de factores externos
    print("\n6. ANALISIS DE FACTORES EXTERNOS (QUE NO PODEMOS CONTROLAR)")
    external_factors = {
        "Backlinks": "NO ANALIZADO - Requiere herramientas externas",
        "Edad del dominio": "NO ANALIZADO - Requiere whois lookup",
        "Autoridad de dominio": "NO ANALIZADO - Requiere Moz/Ahrefs",
        "Velocidad del servidor": "NO ANALIZADO - Requiere PageSpeed Insights",
        "Métricas de usuario": "NO ANALIZADO - Requiere Analytics",
        "Presencia social": "NO ANALIZADO - Requiere investigación manual",
        "Reseñas reales": "NO ANALIZADO - Requiere Google Maps/Trustpilot"
    }
    
    for factor, status in external_factors.items():
        print(f"   {factor}: {status}")
    
    print("\n" + "=" * 70)
    print("RESUMEN DE CAPACIDAD PARA LIDERAZGO #1")
    print("=" * 70)

if __name__ == "__main__":
    main()