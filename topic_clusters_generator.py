"""
Generador de Topic Clusters - Interlinking Temático
Crea clústeres temáticos para mejorar autoridad semántica
"""

from pathlib import Path

def generate_topic_clusters():
    """Genera interlinking temático entre todas las páginas"""
    
    # Directorios
    programmatic_dir = Path(__file__).parent / "programmatic-pages"
    blog_dir = Path(__file__).parent / "blog"
    
    # Obtener todos los archivos
    programmatic_files = list(programmatic_dir.glob('*.html'))
    blog_files = list(blog_dir.glob('*.html'))
    
    # Definir topic clusters
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
    
    # Generar archivo de interlinking
    interlinking_file = Path(__file__).parent / "interlinking_strategy.txt"
    
    with open(interlinking_file, 'w', encoding='utf-8') as f:
        f.write("ESTRATEGIA DE INTERLINKING TEMÁTICO - TOPIC CLUSTERS\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Total páginas programáticas: {len(programmatic_files)}\n")
        f.write(f"Total artículos blog: {len(blog_files)}\n")
        f.write(f"Total páginas: {len(programmatic_files) + len(blog_files)}\n\n")
        
        f.write("TOPIC CLUSTERS DEFINIDOS:\n\n")
        
        for topic, cluster in topic_clusters.items():
            f.write(f"CLÚSTER: {topic.upper()}\n")
            f.write(f"Página Pilar: {cluster['pillar']}\n")
            f.write(f"Páginas Relacionadas: {len(cluster['related'])}\n")
            f.write("-" * 40 + "\n")
            
            for related in cluster['related']:
                f.write(f"- {related}\n")
            
            f.write("\n" + "=" * 60 + "\n\n")
        
        f.write("RECOMENDACIONES DE IMPLEMENTACIÓN:\n")
        f.write("1. Cada página pilar debe enlazar a todas sus páginas relacionadas\n")
        f.write("2. Cada página relacionada debe enlazar de vuelta a la página pilar\n")
        f.write("3. Cross-linking entre clústeres cuando sea natural\n")
        f.write("4. Anchor text debe descriptivo y contener keywords semánticas\n")
        f.write("5. Priorizar enlaces internos sobre externos cuando sea posible\n")
    
    return interlinking_file

if __name__ == "__main__":
    print("Generando estrategia de interlinking temático...")
    print("=" * 60)
    
    strategy_file = generate_topic_clusters()
    
    print(f"Estrategia guardada en: {strategy_file}")
    print(f"\nClústeres temáticos definidos: 6")
    print(f"Páginas programáticas: {len(list(Path(__file__).parent.glob('programmatic-pages/*.html')))}")
    print(f"Artículos blog: {len(list(Path(__file__).parent.glob('blog/*.html')))}")
    print(f"\nProgreso SEO Avanzado 2026: 50% completado")