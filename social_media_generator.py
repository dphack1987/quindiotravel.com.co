"""
Generación de Contenido de Redes Sociales
Posts para Instagram y Facebook para Quindío Travel
"""

from pathlib import Path

def generate_social_media_content():
    """Genera contenido de redes sociales"""
    
    social_dir = Path(__file__).parent / "social_media_content"
    social_dir.mkdir(exist_ok=True)
    
    instagram_posts = [
        {
            "file": "instagram_post_1.txt",
            "caption": """🌿 ¿Sueñas con el Eje Cafetero? 🌿

Valle de Cocora está esperándote con sus palmas de cera gigantes y paisajes de postal. Quindío Travel te lleva a la experiencia más auténtica con guías certificados MINCIT.

✨ Planes desde $425.000 COP por persona
✅ 15+ años de experiencia (RNT 18152)
✅ Transporte, alojamiento y guías incluidos

📍 Salento, Filandia, Valle de Cocora y más

📩 Cotiza gratis: +57-317-4426044
🌐 quindiotravel.com.co

#EjeCafetero #Colombia #TurismoColombia #ValleDeCocora #QuindioTravel #TurismoSostenible #PaisajesColombianos #ViajesColombia"""
        },
        {
            "file": "instagram_post_2.txt",
            "caption": """☕ Cultura Cafetera Auténtica ☕

Conoce el proceso del café desde la recolección hasta la taza en fincas cafeteras tradicionales del Quindío. Experiencias inolvidables con Quindío Travel RNT 18152.

🏆 Operador turístico certificado con 15+ años de experiencia
🏡 Alojamiento en fincas tradicionales
🎓 Guías certificados MINCIT
💰 Planes desde $570.000 COP

📱 WhatsApp: +57-317-4426044
🌐 quindiotravel.com.co

#CafeColombiano #CulturaCafetera #TurismoEjeCafetero #FincasCafeteras #CafeTercia #Quindio #ColombiaReal #ExperienciasAutenticas"""
        },
        {
            "file": "instagram_post_3.txt",
            "caption": """🏛️ Pueblos Bohemios del Quindío 🏛️

Salento y Filandia te esperan con arquitectura colonial, artesanías locales y vistas panorámicas espectaculares. Recorrido guiado con Quindío Travel RNT 18152.

🚍 Calle del Tiempo Detenido
🎨 Artesanías de cuero y café
🌅 Miradores 360 grados
🏠 Hospedaje en casas tradicionales

💰 Planes completos desde $570.000 COP
📅 Disponible todos los días del año

📩 Cotiza tu viaje: +57-317-4426044
🌐 quindiotravel.com.co

#Salento #Filandia #PueblosColombianos #ArquitecturaColonial #PueblosBohemios #Quindio #TurismoColombia #PueblosPueblitos #ColombiaMagica"""
        },
        {
            "file": "instagram_post_4.txt",
            "caption": """🌄 Atardecer en Valle de Cocora 🌄

El momento más mágico del Eje Cafetero: las palmas de cera doradas por el sol atardecer. Experiencia fotográfica inolvidable con Quindío Travel RNT 18152.

📸 Guía fotográfica incluida
🏥 Transporte seguro
🏡 Alojamiento con vista
🌙 Experiencia nocturna opcional

🎟 Plan Vientos de Agosto: Desde $1.152.000 COP
📅 Disponible temporada alta

📩 Reserva tu experiencia: +57-317-4426044
🌐 quindiotravel.com.co

#ValleDeCocora #Atardecer #Fotografia #PaisajesColombianos #PalmasDeCera #EjeCafetero #Colombia #PuestaDeSol #NaturalezaColombia"""
        },
        {
            "file": "instagram_post_5.txt",
            "caption": """🏥 Turismo Seguro en 2026 🏥

Viaja con tranquilidad por el Eje Cafetero con Quindío Travel RNT 18152. 15+ años de experiencia en turismo seguro con guías certificados MINCIT.

✅ Rutas seguras señalizadas
✅ Seguro de viaje incluido
✅ Guías certificados
✅ Hoteles verificados
✅ Transporte seguro

🏆 Operador turístico certificado
📍 Salento, Filandia, Armenia y más

📩 Viaja seguro: +57-317-4426044
🌐 quindiotravel.com.co

#TurismoSeguro #ViajaSeguro #EjeCafetero #Colombia2026 #SeguridadTuristica #QuindioTravel #RNT18152 #GuíasCertificados #TurismoResponsable"""
        }
    ]
    
    facebook_posts = [
        {
            "file": "facebook_post_1.txt",
            "caption": """🌿 ¿Listo para el Eje Cafetero? 🌿

Quindío Travel RNT 18152 te ofrece planes completos al Eje Cafetero con 15+ años de experiencia:

✨ VALLE DE COCORA: Palmas de cera gigantes
✨ SALENTO: Pueblo bohemio colonial
✨ FILANDIA: Vistas panorámicas 360 grados
✨ FINCAS CAFETERAS: Experiencias auténticas

💰 Planes desde $425.000 COP por persona
📅 Disponible todos los días
🚗 Transporte desde Bogotá y Medellín
🏡 Alojamiento en hoteles y fincas
🎓 Guías certificados MINCIT

📍 Salento, Filandia, Armenia, Valle de Cocora
📩 Cotiza gratis: +57-317-4426044
🌐 quindiotravel.com.co

👥 Más de 5,000 viajeros satisfechos desde 2010
🏆 Operador turístico certificado RNT 18152

#EjeCafetero #TurismoColombia #QuindioTravel #ValleDeCocora #Salento #Filandia #TurismoSeguro #ColombiaReal #PaisajesColombianos"""
        },
        {
            "file": "facebook_post_2.txt",
            "caption": """☕ Experiencias Cafeteras Auténticas ☕

Conoce el verdadero proceso del café colombiano con Quindío Travel RNT 18152:

🌱 RECOLECCIÓN: Cosecha tu propio café
🔥 PROCESAMIENTO: Tostado artesanal
☕ DEGUSTACIÓN: Catas profesionales
🏡 ALOJAMIENTO: Fincas tradicionales

🏆 15+ años de experiencia en turismo cafetero
🎓 Guías certificados MINCIT
💰 Planes desde $570.000 COP
📅 Experiencias disponibles todos los días

📍 Finca cafeteras Salento, Filandia, Armenia
📩 Reserva tu experiencia: +57-317-4426044
🌐 quindiotravel.com.co

✨ Más de 5,000 viajeros satisfechos
✨ Operador turístico certificado RNT 18152

#CafeColombiano #CulturaCafetera #FincasCafeteras #TurismoCafetero #Quindio #EjeCafetero #ExperienciasAutenticas #CafeTercia #Colombia"""
        },
        {
            "file": "facebook_post_3.txt",
            "caption": """🎟 PROMOCIÓN AGOSTO 2026: PLAN VIENTOS DE AGOSTO 🎟

¡Viaja más pagando menos! Quindío Travel RNT 18152 te ofrece planes especiales para agosto:

🌅 VALLE DE COCORA: Excursión completa
🏡 HOSPEDAJE: Cabañas y hoteles campestres
🍽️ ALIMENTACIÓN: Comida típica incluida
🎓 GUÍAS: Certificados MINCIT
🚗 TRANSPORTE: Desde Bogotá/Medellín

💰 PROMOCIÓN: Desde $1.152.000 COP por persona
📅 DISPONIBILIDAD: Agosto 2026
👥 GRUPOS: Descuentos especiales 4+ personas

📍 Salento, Filandia, Valle de Cocora
📩 Cotiza tu promoción: +57-317-4426044
🌐 quindiotravel.com.co

✨ 15+ años de experiencia operativa
✨ Más de 5,000 viajeros satisfechos
✨ Operador turístico certificado RNT 18152

#PromocionesAgosto #OfertasTurismo #Descuentos #VientosDeAgosto #EjeCafetero #QuindioTravel #PromocionesColombia #ViajesEconomicos #TurismoAsequible"""
        }
    ]
    
    generated_count = 0
    
    # Generar posts de Instagram
    for post in instagram_posts:
        try:
            filepath = social_dir / post["file"]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(post["caption"])
            
            generated_count += 1
            print(f"Post Instagram generado: {post['file']}")
            
        except Exception as e:
            print(f"Error generando {post['file']}: {e}")
    
    # Generar posts de Facebook
    for post in facebook_posts:
        try:
            filepath = social_dir / post["file"]
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(post["caption"])
            
            generated_count += 1
            print(f"Post Facebook generado: {post['file']}")
            
        except Exception as e:
            print(f"Error generando {post['file']}: {e}")
    
    return generated_count

if __name__ == "__main__":
    print("Generando contenido de redes sociales...")
    print("=" * 60)
    
    count = generate_social_media_content()
    
    print(f"\nTotal posts generados: {count}")
    print(f"Instagram: 5 posts")
    print(f"Facebook: 3 posts")
    print("\nProgreso despliegue contenido adicional: 50% completado")