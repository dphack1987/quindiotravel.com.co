"""
Mejorar Visualmente la Promoción del Mes
Actualiza la sección de promoción con diseño moderno y mejor SEO
"""

from pathlib import Path

def improve_promo_visual():
    """Mejora visualmente la sección de promoción del mes"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mejorar schema Offer con más detalles
    old_offer_schema = '''            "offers": {
                "@type": "Offer",
                "name": "Plan Vientos de Agosto 2026",
                "price": "1152000",
                "priceCurrency": "COP",
                "availability": "http://schema.org/InStock",
                "validFrom": "2026-08-01"'''
    
    new_offer_schema = '''            "offers": {
                "@type": "Offer",
                "name": "Plan Vientos de Agosto 2026 - Cupos Limitados",
                "description": "Plan exclusivo de temporada alta con solo 15 cupos disponibles",
                "price": "1152000",
                "priceCurrency": "COP",
                "validFrom": "2026-08-01",
                "validUntil": "2026-08-31",
                "availability": "https://schema.org/InStock",
                "inventoryLevel": 15,
                "url": "https://quindiotravel.com.co/#promo-mes",
                "seller": {
                    "@type": "TravelAgency",
                    "name": "Quindío Travel",
                    "telephone": "+57-317-4426044"
                },
                "discount": "20",
                "discountCurrency": "COP"
            }'''
    
    if old_offer_schema in content:
        content = content.replace(old_offer_schema, new_offer_schema)
        print("[OK] Schema Offer mejorado con detalles de cupos y descuento")
    
    # Mejorar badge de promoción
    old_badge = '''<div class="promo-badge">🔥 PROMOCIÓN DEL MES</div>'''
    new_badge = '''<div class="promo-badge">
        <span class="badge-icon">🔥</span>
        <span class="badge-text">PROMOCIÓN DEL MES</span>
        <span class="badge-urgent">SOLO 15 CUPOS</span>
    </div>'''
    
    if old_badge in content:
        content = content.replace(old_badge, new_badge)
        print("[OK] Badge mejorado con urgencia destacada")
    
    # Mejorar título con keywords SEO
    old_title = '''<h2 class="promo-title">Promoción Exclusiva Eje Cafetero: Plan Vientos de Agosto 2026</h2>'''
    new_title = '''<h2 class="promo-title">Promoción Exclusiva Eje Cafetero 2026: Plan Vientos de Agosto - Cupos Limitados</h2>'''
    
    if old_title in content:
        content = content.replace(old_title, new_title)
        print("[OK] Título mejorado con keywords SEO")
    
    # Mejorar subtítulo con keywords long-tail
    old_subtitle = '''<h3 class="promo-subtitle">🌟 Experiencia Completa del Eje Cafetero en Temporada Alta</h3>'''
    new_subtitle = '''<h3 class="promo-subtitle">🌟 Experiencia Completa del Eje Cafetero en Temporada Alta - Tour 4 Días 3 Noches Todo Incluido</h3>'''
    
    if old_subtitle in content:
        content = content.replace(old_subtitle, new_subtitle)
        print("[OK] Subtítulo mejorado con keywords long-tail")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n[OK] Mejoras visuales y SEO aplicadas a la promoción del mes")
    return True

if __name__ == "__main__":
    print("Mejorando visualmente la promoción del mes...")
    print("=" * 70)
    
    improve_promo_visual()
    
    print("\n" + "=" * 70)
    print("Mejoras aplicadas exitosamente")