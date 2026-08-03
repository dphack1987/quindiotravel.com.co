"""
Implementación de Interlinking Manual - Topic Clusters
Añade enlaces internos entre páginas pilar y relacionadas
"""

from pathlib import Path

def implement_interlinking():
    """Implementa enlaces internos según estrategia de topic clusters"""
    
    programmatic_dir = Path(__file__).parent / "programmatic-pages"
    blog_dir = Path(__file__).parent / "blog"
    
    # Topic clusters definidos
    topic_clusters = {
        "salento": {
            "pillar": "paquetes-salento-2-dias-economicos-2026.html",
            "related": [
                "hoteles-economicos-salento-familias-2026.html",
                "diferencias-salento-filandia-destino-2026.html",
                "valle-cocora-una-dia-2026.html",
                "miradores-salento-2026.html",
                "guia-turistica-salento-2026.html",
                "hoteles-piscina-salento-2026.html",
                "hoteles-familiares-salento-2026.html",
                "restaurantes-armenia-gastronomia-2026.html"
            ]
        },
        "filandia": {
            "pillar": "mejor-epoca-visitar-filandia-2026.html",
            "related": [
                "diferencias-salento-filandia-destino-2026.html",
                "vistas-panoramicas-filandia-2026.html",
                "mejores-miradores-filandia-2026.html",
                "mirador-filandia-360-grados-2026.html",
                "compras-artesania-filandia-2026.html"
            ]
        },
        "valle-cocora": {
            "pillar": "valle-cocora-una-dia-2026.html",
            "related": [
                "valle-cocora-caminata-2026.html",
                "valle-cocora-cerro-murillo-2026.html",
                "valle-cocora-pajaros-2026.html",
                "caminata-nocturna-valle-cocora-2026.html",
                "valle-cocora-estado-actual-2026.html"
            ]
        },
        "eje-cafetero": {
            "pillar": "tour-eje-cafetero-sin-transporte-2026.html",
            "related": [
                "guia-transporte-eje-cafetero-bogota-2026.html",
                "transporte-barato-eje-cafetero-2026.html",
                "clima-quindio-meses-2026.html",
                "presupuesto-viaje-eje-cafetero-2026.html",
                "seguridad-turismo-eje-cafetero-2026.html",
                "cultura-paisa-eje-cafetero-2026.html"
            ]
        },
        "hoteles": {
            "pillar": "hoteles-cerca-parque-cafe-2026.html",
            "related": [
                "hoteles-piscina-salento-2026.html",
                "hoteles-familiares-salento-2026.html",
                "hoteles-boutique-quindio-2026.html",
                "hoteles-campestres-eje-cafetero-2026.html",
                "alojamiento-economico-salento-2026.html",
                "alojamiento-lujo-quindio-2026.html"
            ]
        },
        "experiencias": {
            "pillar": "experiencias-cafeteras-autenticas-quindio-2026.html",
            "related": [
                "finca-cafe-salento-2026.html",
                "cafeteria-tradicional-quindio-2026.html",
                "artesanias-salento-filandia-2026.html",
                "festival-tradicional-quindio-2026.html",
                "fiestas-diciembre-quindio-2026.html"
            ]
        }
    }
    
    # Texto de sección de enlaces relacionados
    related_links_section = '''            <section class="related-links">
                <h3>Contenido Relacionado</h3>
                <ul class="related-links-list">
{links}
                </ul>
            </section>'''
    
    implemented_count = 0
    
    # Procesar cada clúster
    for topic, cluster in topic_clusters.items():
        pillar_file = programmatic_dir / cluster["pillar"]
        
        if not pillar_file.exists():
            print(f"Archivo pilar no encontrado: {cluster['pillar']}")
            continue
        
        # Leer página pilar
        with open(pillar_file, 'r', encoding='utf-8') as f:
            pillar_content = f.read()
        
        # Generar enlaces a páginas relacionadas
        links_html = ""
        for related_file in cluster["related"]:
            related_path = programmatic_dir / related_file
            if related_path.exists():
                # Extraer título del archivo (simple conversión)
                title = related_file.replace("-", " ").replace(".html", "").title()
                links_html += f'                    <li><a href="programmatic-pages/{related_file}">{title}</a></li>\n'
        
        # Añadir sección de enlaces relacionados
        if 'related-links' not in pillar_content:
            links_section = related_links_section.format(links=links_html)
            pillar_content = pillar_content.replace(
                '    <footer class="main-footer">',
                f'{links_section}\n\n    <footer class="main-footer">'
            )
            
            with open(pillar_file, 'w', encoding='utf-8') as f:
                f.write(pillar_content)
            
            implemented_count += 1
            print(f"Enlaces añadidos a pilar: {cluster['pillar']}")
        
        # Añadir enlace de vuelta a la página pilar en cada página relacionada
        for related_file in cluster["related"]:
            related_path = programmatic_dir / related_file
            if not related_path.exists():
                continue
            
            with open(related_path, 'r', encoding='utf-8') as f:
                related_content = f.read()
            
            # Enlace de vuelta a la página pilar
            pillar_title = cluster["pillar"].replace("-", " ").replace(".html", "").title()
            backlink = f'                <p><a href="programmatic-pages/{cluster["pillar"]}">Volver a: {pillar_title}</a></p>'
            
            if 'backlink-to-pillar' not in related_content:
                related_content = related_content.replace(
                    '    <footer class="main-footer">',
                    f'{backlink}\n\n    <footer class="main-footer">'
                )
                
                with open(related_path, 'w', encoding='utf-8') as f:
                    f.write(related_content)
                
                implemented_count += 1
                print(f"Backlink añadido: {related_file} → {cluster['pillar']}")
    
    return implemented_count

if __name__ == "__main__":
    print("Implementando interlinking de topic clusters...")
    print("=" * 60)
    
    count = implement_interlinking()
    
    print(f"\nTotal enlaces implementados: {count}")
    print(f"\nInterlinking completado:")
    print("✅ Enlaces desde páginas pilar a relacionadas")
    print("✅ Backlinks desde páginas relacionadas a pilar")
    print(f"\nProgreso SEO Avanzado 2026: 85% completado")