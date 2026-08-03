"""
SemanticAuthorityMatrix - Sistema de autoridad semántica con NetworkX

Este módulo implementa análisis avanzado de autoridad usando teoría de grafos,
PageRank personalizado, análisis de long-tails geolocalizadas y optimización de enlaces internos.
"""

import networkx as nx
from typing import Dict, List, Set, Tuple
import json
from collections import defaultdict
import math
import logging
from pathlib import Path
from datetime import datetime

class SemanticAuthorityMatrix:
    """
    Sistema avanzado de autoridad semántica usando teoría de grafos 
    y análisis de long-tails geolocalizadas con NLP básico.
    """
    
    def __init__(self, domain: str, data_dir: str = "competitive-engine/data"):
        self.domain = domain
        self.graph = nx.DiGraph()
        self.keyword_clusters = defaultdict(list)
        self.authority_scores = {}
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Datos geolocalizados del Quindío
        self.quindio_locations = [
            "Armenia", "Salento", "Filandia", "Circasia", "Calarcá",
            "La Tebaida", "Montenegro", "Quimbaya", "Buenavista", "Cordoba", "Pijao"
        ]
        
        # Intenciones de búsqueda
        self.search_intents = [
            "barato", "económico", "familiar", "lujo", "guía", "tour",
            "paquete", "plan", "hotel", "cabaña", "reserva", "precios"
        ]
        
        # Temas principales del Eje Cafetero
        self.main_themes = [
            "café", "cultura", "naturaleza", "aventura", "gastronomía",
            "paisajes", "tradición", "ecoturismo", "bienestar", "fotografía"
        ]
        
    def add_page(self, url: str, keywords: List[str], content_length: int, title: str = ""):
        """
        Agrega una página al grafo de autoridad con análisis de contenido.
        
        Args:
            url: URL de la página
            keywords: Lista de palabras clave principales
            content_length: Longitud del contenido en caracteres
            title: Título de la página (opcional)
        """
        # Calcular autoridad inicial basada en longitud y calidad
        base_authority = math.log(content_length + 1) * len(keywords)
        
        # Bonus por título descriptivo
        if title and len(title) > 30:
            base_authority *= 1.2
        
        self.graph.add_node(
            url, 
            keywords=keywords, 
            content_length=content_length,
            title=title,
            base_authority=base_authority
        )
        
        self.authority_scores[url] = base_authority
        
        # Agrupar keywords en clusters semánticos
        for keyword in keywords:
            self.keyword_clusters[keyword.lower()].append(url)
        
        self.logger.info(f"✅ Página agregada: {url} ({len(keywords)} keywords, autoridad: {base_authority:.2f})")
    
    def add_internal_link(self, source_url: str, target_url: str, anchor_text: str, weight: float = 1.0):
        """
        Agrega enlace interno con análisis de texto ancla.
        
        Args:
            source_url: URL de origen
            target_url: URL de destino
            anchor_text: Texto del enlace
            weight: Peso del enlace (opcional)
        """
        if source_url in self.graph and target_url in self.graph:
            # Calcular relevancia del anchor text
            calculated_weight = self._calculate_anchor_relevance(anchor_text, target_url)
            final_weight = weight * calculated_weight
            
            self.graph.add_edge(
                source_url, 
                target_url, 
                weight=final_weight, 
                anchor=anchor_text
            )
            
            self.logger.info(
                f"🔗 Enlace agregado: {source_url} → {target_url} "
                f"(anchor: '{anchor_text}', peso: {final_weight:.2f})"
            )
        else:
            self.logger.warning(f"⚠️ No se puede agregar enlace: una de las páginas no existe")
    
    def _calculate_anchor_relevance(self, anchor_text: str, target_url: str) -> float:
        """
        Calcula relevancia del texto ancla usando NLP básico.
        
        Args:
            anchor_text: Texto del enlace
            target_url: URL de destino
            
        Returns:
            Puntuación de relevancia (0.1 - 1.0)
        """
        if target_url not in self.graph:
            return 0.1
            
        target_keywords = self.graph.nodes[target_url].get('keywords', [])
        anchor_words = set(anchor_text.lower().split())
        
        # Intersección de palabras clave
        relevance = len(anchor_words.intersection(set(target_keywords)))
        
        # Normalizar (mínimo 0.1 para evitar división por cero)
        return max(0.1, min(1.0, relevance / len(target_keywords) if target_keywords else 0.1))
    
    def calculate_pagerank(self, damping: float = 0.85, iterations: int = 100) -> Dict[str, float]:
        """
        Calcula PageRank personalizado para autoridad interna.
        
        Args:
            damping: Factor de amortiguación (default: 0.85)
            iterations: Número de iteraciones (default: 100)
            
        Returns:
            Diccionario con scores de PageRank por URL
        """
        if self.graph.number_of_edges() == 0:
            self.logger.warning("⚠️ Grafo sin enlaces, usando autoridad base")
            return self.authority_scores
        
        try:
            pagerank = nx.pagerank(
                self.graph,
                alpha=damping,
                max_iter=iterations,
                weight='weight'
            )
        except Exception as e:
            self.logger.warning(f"⚠️ PageRank default failed: {e}")
            self.logger.info("🔧 Usando fallback de PageRank iterativo en Python")
            pagerank = {node: 1.0 / self.graph.number_of_nodes() for node in self.graph.nodes()}
            for _ in range(iterations):
                new_pagerank = {}
                for node in self.graph.nodes():
                    rank_sum = 0.0
                    for predecessor in self.graph.predecessors(node):
                        edge_weight = self.graph[predecessor][node].get('weight', 1.0)
                        outgoing_weight = sum(
                            self.graph[predecessor][nbr].get('weight', 1.0)
                            for nbr in self.graph.successors(predecessor)
                        )
                        if outgoing_weight > 0:
                            rank_sum += pagerank[predecessor] * edge_weight / outgoing_weight
                    new_pagerank[node] = (1 - damping) / self.graph.number_of_nodes() + damping * rank_sum
                pagerank = new_pagerank
        
        # Combinar con autoridad base
        combined_scores = {}
        for url in pagerank:
            combined_scores[url] = pagerank[url] * (1 + self.authority_scores.get(url, 0) / 100)
        
        self.logger.info(f"✅ PageRank calculado para {len(combined_scores)} páginas")
        
        return combined_scores
    
    def identify_long_tail_opportunities(self, base_keywords: List[str]) -> List[str]:
        """
        Identifica oportunidades de long-tail geolocalizadas usando combinatoria.
        
        Args:
            base_keywords: Lista de keywords base (ej: ['tour', 'viaje', 'plan'])
            
        Returns:
            Lista de long-tails geolocalizadas
        """
        opportunities = []
        
        for keyword in base_keywords:
            for location in self.quindio_locations:
                for intent in self.search_intents:
                    # Combinación keyword + ubicación + intención
                    long_tail = f"{keyword} {location} {intent}"
                    opportunities.append(long_tail)
                
                # Combinación keyword + ubicación
                long_tail_loc = f"{keyword} {location}"
                opportunities.append(long_tail_loc)
                
                # Combinación keyword + intención
                long_tail_intent = f"{keyword} {intent}"
                opportunities.append(long_tail_intent)
        
        # Eliminar duplicados manteniendo orden
        unique_opportunities = list(dict.fromkeys(opportunities))
        
        self.logger.info(f"✅ {len(unique_opportunities)} oportunidades de long-tail identificadas")
        
        return unique_opportunities
    
    def generate_topic_clusters(self) -> Dict[str, List[str]]:
        """
        Genera topic clusters para estructura silo basada en contenido existente.
        
        Returns:
            Diccionario con clusters temáticos
        """
        clusters = defaultdict(list)
        
        for keyword, pages in self.keyword_clusters.items():
            # Clasificar keyword en temas
            keyword_lower = keyword.lower()
            
            # Tema: Destinos
            if any(loc in keyword_lower for loc in self.quindio_locations):
                clusters["destinos"].append(keyword)
            
            # Tema: Servicios
            elif any(act in keyword_lower for act in ["tour", "viaje", "plan", "paquete", "reserva"]):
                clusters["servicios"].append(keyword)
            
            # Tema: Alojamiento
            elif any(aloj in keyword_lower for aloj in ["hotel", "cabaña", "hostal", "finca", "resort"]):
                clusters["alojamiento"].append(keyword)
            
            # Tema: Conversión (precios)
            elif any(bud in keyword_lower for bud in ["precio", "costo", "barato", "económico", "oferta"]):
                clusters["conversión"].append(keyword)
            
            # Tema: Experiencias
            elif any(exp in keyword_lower for exp in self.main_themes):
                clusters["experiencias"].append(keyword)
            
            # Tema: General
            else:
                clusters["general"].append(keyword)
        
        self.logger.info(f"✅ {len(clusters)} topic clusters generados")
        
        return dict(clusters)
    
    def optimize_internal_linking(self, max_links_per_page: int = 5) -> Dict[str, List[Dict]]:
        """
        Genera recomendaciones de enlaces internos optimizados.
        
        Args:
            max_links_per_page: Máximo de enlaces recomendados por página
            
        Returns:
            Diccionario con recomendaciones por página
        """
        recommendations = defaultdict(list)
        pagerank = self.calculate_pagerank()
        
        # Ordenar páginas por autoridad
        sorted_pages = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)
        
        for source_url, _ in sorted_pages:
            if source_url not in self.graph:
                continue
                
            source_keywords = self.graph.nodes[source_url].get('keywords', [])
            recommendations_count = 0
            
            # Encontrar páginas relevantes para enlazar
            for target_url, target_keywords in self.graph.nodes(data='keywords'):
                if source_url != target_url and recommendations_count < max_links_per_page:
                    # Calcular similitud semántica
                    similarity = len(set(source_keywords) & set(target_keywords))
                    
                    if similarity >= 2:  # Umbral de similitud
                        target_pagerank = pagerank.get(target_url, 0)
                        
                        recommendations[source_url].append({
                            'target': target_url,
                            'similarity': similarity,
                            'pagerank': target_pagerank,
                            'suggested_anchor': self._generate_anchor_text(source_keywords, target_keywords),
                            'priority': 'high' if similarity >= 3 else 'medium'
                        })
                        
                        recommendations_count += 1
        
        self.logger.info(f"✅ {len(recommendations)} páginas con recomendaciones de enlaces")
        
        return dict(recommendations)
    
    def _generate_anchor_text(self, source_keywords: List[str], target_keywords: List[str]) -> str:
        """
        Genera texto ancla optimizado basado en keywords comunes.
        
        Args:
            source_keywords: Keywords de página origen
            target_keywords: Keywords de página destino
            
        Returns:
            Texto ancla optimizado
        """
        common = set(source_keywords) & set(target_keywords)
        
        if common:
            # Usar primeras 2 palabras comunes
            anchor = " ".join(list(common)[:2])
            return anchor if len(anchor) <= 50 else "más información"
        
        # Fallback a primera keyword de destino
        return target_keywords[0] if target_keywords else "más información"
    
    def export_structure(self, filename: str = "authority_structure.json") -> Dict:
        """
        Exporta la estructura de autoridad para análisis.
        
        Args:
            filename: Nombre del archivo de salida
            
        Returns:
            Estructura completa de autoridad
        """
        structure = {
            'domain': self.domain,
            'timestamp': datetime.now().isoformat(),
            'pages_count': self.graph.number_of_nodes(),
            'links_count': self.graph.number_of_edges(),
            'pagerank': self.calculate_pagerank(),
            'topic_clusters': self.generate_topic_clusters(),
            'long_tail_opportunities': self.identify_long_tail_opportunities(
                ['tour', 'viaje', 'plan', 'hotel', 'cabaña', 'experiencia']
            ),
            'internal_linking': self.optimize_internal_linking(),
            'keyword_clusters': dict(self.keyword_clusters)
        }
        
        output_path = self.data_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(structure, f, indent=2, ensure_ascii=False)
        
        self.logger.info(f"💾 Estructura de autoridad exportada a {output_path}")
        
        return structure
    
    def generate_silo_structure(self) -> Dict[str, List[str]]:
        """
        Genera estructura silo para organización de contenido.
        
        Returns:
            Diccionario con estructura silo
        """
        topic_clusters = self.generate_topic_clusters()
        
        silo_structure = {}
        
        for topic, keywords in topic_clusters.items():
            silo_pages = []
            
            for keyword in keywords:
                # Encontrar páginas relacionadas con este keyword
                related_pages = self.keyword_clusters.get(keyword.lower(), [])
                silo_pages.extend(related_pages)
            
            # Eliminar duplicados
            silo_structure[topic] = list(dict.fromkeys(silo_pages))
        
        self.logger.info(f"✅ Estructura silo generada para {len(silo_structure)} temas")
        
        return silo_structure
    
    def analyze_content_gaps(self) -> List[str]:
        """
        Identifica gaps de contenido basado en long-tails no cubiertas.
        
        Returns:
            Lista de oportunidades de contenido faltantes
        """
        # Keywords actuales
        current_keywords = set(self.keyword_clusters.keys())
        
        # Generar todas las combinaciones posibles
        all_opportunities = set(self.identify_long_tail_opportunities(
            ['tour', 'viaje', 'plan', 'hotel', 'cabaña', 'experiencia', 'café', 'cultura']
        ))
        
        # Identificar gaps
        content_gaps = list(all_opportunities - current_keywords)
        
        self.logger.info(f"✅ {len(content_gaps)} gaps de contenido identificados")
        
        return content_gaps


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Crear matriz de autoridad
    matrix = SemanticAuthorityMatrix("https://quindiotravel.com.co")
    
    # Agregar páginas con análisis de contenido
    print("🚀 Agregando páginas al grafo de autoridad...")
    matrix.add_page("index.html", 
                   ["tour eje cafetero", "planes quindío", "turismo colombia", "cultura cafetera"], 
                   5000,
                   "Quindío Travel - Turismo Eje Cafetero")
    
    matrix.add_page("valle-de-cocora.html", 
                   ["valle de cocora", "palmas de cera", "salento", "naturaleza", "fotografía"], 
                   3000,
                   "Valle de Cocora - Palmas de Cera")
    
    matrix.add_page("hoteles-salento.html", 
                   ["hoteles salento", "cabañas", "alojamiento", "hospedaje", "finca hotel"], 
                   2500,
                   "Hoteles y Cabañas en Salento")
    
    matrix.add_page("parque-cafe.html", 
                   ["parque del café", "panaca", "turismo familiar", "cultura café", "diversión"], 
                   2000,
                   "Parque del Café y PANACA")
    
    matrix.add_page("filandia.html",
                   ["filandia", "artesanías", "mirador", "pueblo patrimonio", "guadua"],
                   1800,
                   "Filandia - Pueblo Patrimonio")
    
    # Agregar enlaces internos con análisis
    print("\n🚀 Agregando enlaces internos...")
    matrix.add_internal_link("index.html", "valle-de-cocora.html", "descubre el valle de cocora")
    matrix.add_internal_link("valle-de-cocora.html", "hoteles-salento.html", "hoteles en salento")
    matrix.add_internal_link("index.html", "parque-cafe.html", "parque temático café")
    matrix.add_internal_link("index.html", "filandia.html", "visita filandia")
    matrix.add_internal_link("valle-de-cocora.html", "filandia.html", "pueblos cercanos")
    
    # Generar estructura de autoridad
    print("\n🚀 Generando estructura de autoridad...")
    authority_structure = matrix.export_structure()
    
    # Análisis adicional
    print("\n🚀 Análisis de autoridad:")
    print(f"📊 PageRank top 3:")
    pagerank = authority_structure['pagerank']
    for url, score in sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"   {url}: {score:.4f}")
    
    print(f"\n🎯 Topic Clusters:")
    for topic, keywords in authority_structure['topic_clusters'].items():
        print(f"   {topic}: {len(keywords)} keywords")
    
    print(f"\n🔗 Recomendaciones de enlaces:")
    for url, recs in list(authority_structure['internal_linking'].items())[:2]:
        print(f"   {url}: {len(recs)} recomendaciones")
    
    print(f"\n📈 Oportunidades de long-tail: {len(authority_structure['long_tail_opportunities'])}")
    
    # Identificar gaps de contenido
    print("\n🚀 Identificando gaps de contenido...")
    content_gaps = matrix.analyze_content_gaps()
    print(f"📋 Gaps identificados: {len(content_gaps)}")
    
    print(f"\n✅ Sistema SemanticAuthorityMatrix funcionando correctamente")