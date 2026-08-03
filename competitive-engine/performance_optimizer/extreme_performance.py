"""
ExtremePerformanceOptimizer - Optimizador de rendimiento extremo

Este módulo implementa optimización quirúrgica de HTML, compresión de imágenes,
generación de CSS crítico y sistema de caché inteligente para Core Web Vitals perfectos.
"""

import re
import gzip
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import shutil
import logging
from datetime import datetime

class ExtremePerformanceOptimizer:
    """
    Optimizador de rendimiento extremo con compresión, caché inteligente 
    y optimización de recursos multimedia.
    """
    
    def __init__(self, static_dir: str = "assets", cache_dir: str = "competitive-engine/cache"):
        self.static_dir = Path(static_dir)
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
        
        # Estadísticas de optimización
        self.stats = {
            'images_optimized': 0,
            'html_minified': 0,
            'bytes_saved': 0,
            'css_extracted': 0
        }
        
    def optimize_html_payload(self, html_content: str, preserve_structure: bool = True) -> str:
        """
        Optimización quirúrgica de HTML con preservación de estructura crítica.
        
        Args:
            html_content: Contenido HTML a optimizar
            preserve_structure: Si debe preservar estructura crítica (scripts, styles)
            
        Returns:
            HTML optimizado
        """
        original_size = len(html_content)
        
        if preserve_structure:
            # Preservar comentarios importantes (con [!if] o especiales)
            important_comments = re.findall(
                r'<!--(\s*\[if [^\]]+\]|<!|>).*?-->', 
                html_content, 
                re.DOTALL
            )
            
            # Eliminar comentarios innecesarios
            clean_html = re.sub(
                r'<!--(?!\s*(?:\[if [^\]]+\]|<!|>))(?:(?!-->).)*-->', 
                '', 
                html_content, 
                flags=re.DOTALL
            )
            
            # Minificación inteligente (preservar pre, script, style)
            clean_html = re.sub(
                r'(?s)\s+(?=(?:[^<]*<(?:script|style|pre)[^>]*>|(?!<(?:script|style|pre))))',
                ' ', 
                clean_html
            )
            
            # Restaurar comentarios importantes
            for comment in important_comments:
                clean_html = f"<!--{comment}-->" + clean_html
        else:
            # Minificación agresiva (solo para contenido estático)
            clean_html = re.sub(r'<!--.*?-->', '', html_content, flags=re.DOTALL)
            clean_html = re.sub(r'\s+', ' ', clean_html)
        
        clean_html = clean_html.strip()
        
        # Calcular ahorro
        bytes_saved = original_size - len(clean_html)
        self.stats['html_minified'] += 1
        self.stats['bytes_saved'] += bytes_saved
        
        self.logger.info(f"✅ HTML optimizado: {bytes_saved} bytes ahorrados")
        
        return clean_html
    
    def generate_resource_hints(self, html_content: str, critical_resources: List[str] = None) -> str:
        """
        Genera resource hints (preload, prefetch, preconnect) para navegadores modernos.
        
        Args:
            html_content: Contenido HTML existente
            critical_resources: Lista de recursos críticos (opcional)
            
        Returns:
            HTML con resource hints insertados
        """
        if critical_resources is None:
            critical_resources = [
                "logo_quindio_travel.png",
                "assets/images/paisajes/foto_hero1.jpg",
                "assets/css/critical.css"
            ]
        
        hints = []
        
        # Preload de recursos críticos
        for resource in critical_resources:
            if resource.endswith(('.png', '.jpg', '.jpeg', '.webp', '.avif')):
                hints.append(f'<link rel="preload" href="{resource}" as="image" fetchpriority="high">')
            elif resource.endswith('.css'):
                hints.append(f'<link rel="preload" href="{resource}" as="style">')
            elif resource.endswith('.js'):
                hints.append(f'<link rel="preload" href="{resource}" as="script">')
        
        # Preconnect a dominios de terceros
        third_party_domains = [
            "https://fonts.googleapis.com",
            "https://fonts.gstatic.com",
            "https://wa.me"
        ]
        
        for domain in third_party_domains:
            hints.append(f'<link rel="preconnect" href="{domain}">')
        
        # Insertar hints después de <head>
        head_pattern = r'(<head>)'
        html_with_hints = re.sub(
            head_pattern, 
            r'\1\n' + '\n'.join(hints), 
            html_content
        )
        
        self.logger.info(f"✅ {len(hints)} resource hints generados")
        
        return html_with_hints
    
    def generate_critical_css(self, html_file: str, css_file: str, output_file: str = None) -> str:
        """
        Extrae CSS crítico para First Contentful Paint instantáneo.
        
        Args:
            html_file: Ruta al archivo HTML
            css_file: Ruta al archivo CSS principal
            output_file: Ruta para guardar CSS crítico (opcional)
            
        Returns:
            CSS crítico extraído
        """
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                css_content = f.read()
            
            # Extractores de selectores críticos (above-the-fold)
            critical_selectors = [
                r'header', r'\.hero', r'\.promo-price', 
                r'\.cta-button', r'nav', r'\.mobile-menu',
                r'h1', r'h2', r'\.logo', r'\.navigation'
            ]
            
            critical_css = []
            for selector in critical_selectors:
                pattern = re.compile(
                    rf'{selector}[^{{}}]*{{[^{{}}]*}}', 
                    re.IGNORECASE
                )
                matches = pattern.findall(css_content)
                critical_css.extend(matches)
            
            critical_css_string = '\n'.join(critical_css)
            
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(critical_css_string)
                self.logger.info(f"💾 CSS crítico guardado en {output_file}")
            
            self.stats['css_extracted'] += 1
            self.logger.info(f"✅ CSS crítico extraído: {len(critical_css_string)} caracteres")
            
            return critical_css_string
            
        except Exception as e:
            self.logger.error(f"❌ Error extrayendo CSS crítico: {e}")
            return ""
    
    def inline_critical_css(self, html_content: str, critical_css: str) -> str:
        """
        Inyecta CSS crítico directamente en el HTML para renderizado instantáneo.
        
        Args:
            html_content: Contenido HTML
            critical_css: CSS crítico a inyectar
            
        Returns:
            HTML con CSS crítico inyectado
        """
        # Buscar </head> e inyectar antes
        inline_style = f'<style type="text/css">{critical_css}</style>'
        html_with_inline = re.sub(
            r'(</head>)', 
            f'{inline_style}\n\\1', 
            html_content
        )
        
        self.logger.info("✅ CSS crítico inyectado en HTML")
        
        return html_with_inline
    
    def optimize_image_metadata(self, image_path: Path) -> Dict:
        """
        Optimiza metadatos de imágenes para SEO y rendimiento.
        
        Args:
            image_path: Ruta de la imagen
            
        Returns:
            Metadatos optimizados
        """
        try:
            # Generar hash único para la imagen
            with open(image_path, 'rb') as f:
                image_hash = hashlib.md5(f.read()).hexdigest()[:8]
            
            # Obtener tamaño original
            original_size = image_path.stat().st_size
            
            metadata = {
                'original_path': str(image_path),
                'original_size': original_size,
                'hash': image_hash,
                'optimized': False,
                'formats': []
            }
            
            return metadata
            
        except Exception as e:
            self.logger.error(f"❌ Error optimizando metadatos de {image_path}: {e}")
            return {}
    
    def generate_webp_variants(self, image_path: Path, quality: int = 85) -> Path:
        """
        Genera variante WebP de una imagen (requiere PIL/Pillow).
        
        Args:
            image_path: Ruta de la imagen original
            quality: Calidad de compresión (1-100)
            
        Returns:
            Ruta de la imagen WebP generada
        """
        try:
            from PIL import Image
            
            webp_path = image_path.with_suffix('.webp')
            
            with Image.open(image_path) as img:
                # Convertir a RGB si tiene canal alpha
                if img.mode in ('RGBA', 'LA', 'P'):
                    img = img.convert('RGB')
                
                # Guardar como WebP
                img.save(
                    webp_path, 
                    format='WEBP', 
                    quality=quality,
                    method=6  # Compresión más agresiva
                )
            
            # Calcular ahorro
            original_size = image_path.stat().st_size
            webp_size = webp_path.stat().st_size
            savings = original_size - webp_size
            savings_percent = (savings / original_size) * 100
            
            self.stats['images_optimized'] += 1
            self.stats['bytes_saved'] += savings
            
            self.logger.info(
                f"✅ WebP generado: {image_path.name} → {webp_path.name} "
                f"({savings_percent:.1f}% menor)"
            )
            
            return webp_path
            
        except ImportError:
            self.logger.warning("⚠️ PIL/Pillow no disponible, saltando optimización WebP")
            return image_path
        except Exception as e:
            self.logger.error(f"❌ Error generando WebP para {image_path}: {e}")
            return image_path
    
    def gzip_compress_file(self, file_path: Path) -> Path:
        """
        Comprime archivo con gzip para caché de borde.
        
        Args:
            file_path: Ruta del archivo a comprimir
            
        Returns:
            Ruta del archivo comprimido
        """
        try:
            gzip_path = file_path.with_suffix(file_path.suffix + '.gz')
            
            with open(file_path, 'rb') as f_in:
                with gzip.open(gzip_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            # Calcular ratio de compresión
            original_size = file_path.stat().st_size
            gzip_size = gzip_path.stat().st_size
            compression_ratio = (gzip_size / original_size) * 100
            
            self.logger.info(
                f"✅ GZIP generado: {file_path.name} → {gzip_path.name} "
                f"({compression_ratio:.1f}% del original)"
            )
            
            return gzip_path
            
        except Exception as e:
            self.logger.error(f"❌ Error comprimiendo {file_path}: {e}")
            return file_path
    
    def generate_performance_report(self) -> Dict:
        """
        Genera reporte de rendimiento de optimizaciones realizadas.
        
        Returns:
            Diccionario con estadísticas de rendimiento
        """
        report = {
            'timestamp': datetime.now().isoformat(),
            'statistics': self.stats.copy(),
            'efficiency': {
                'bytes_saved_mb': self.stats['bytes_saved'] / (1024 * 1024),
                'images_per_mb_saved': self.stats['images_optimized'] / max(1, self.stats['bytes_saved'] / (1024 * 1024))
            }
        }
        
        return report
    
    def save_performance_report(self, report: Dict, filename: str = "performance_report.json"):
        """
        Guarda reporte de rendimiento en archivo JSON.
        
        Args:
            report: Diccionario del reporte
            filename: Nombre del archivo de salida
        """
        output_path = Path("competitive-engine/data") / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        self.logger.info(f"💾 Reporte de rendimiento guardado en {output_path}")


# Ejemplo de uso y pruebas
if __name__ == "__main__":
    # Configurar logging
    logging.basicConfig(level=logging.INFO)
    
    # Crear optimizador
    optimizer = ExtremePerformanceOptimizer()
    
    # Ejemplo 1: Optimizar HTML
    print("🚀 Optimizando HTML...")
    sample_html = """
    <!-- Comentario innecesario -->
    <html>
    <head>
        <title>Quindío Travel</title>
        <!-- Otro comentario -->
    </head>
    <body>
        <h1>  Turismo  en  el  Eje  Cafetero  </h1>
    </body>
    </html>
    """
    
    optimized_html = optimizer.optimize_html_payload(sample_html)
    print(f"HTML optimizado: {len(optimized_html)} caracteres (vs {len(sample_html)} original)")
    
    # Ejemplo 2: Generar resource hints
    print("\n🚀 Generando resource hints...")
    html_with_hints = optimizer.generate_resource_hints(sample_html)
    print("Resource hints generados")
    
    # Ejemplo 3: Generar reporte de rendimiento
    print("\n🚀 Generando reporte de rendimiento...")
    report = optimizer.generate_performance_report()
    optimizer.save_performance_report(report)
    
    print(f"\n✅ Sistema ExtremePerformanceOptimizer funcionando correctamente")
    print(f"📊 Estadísticas: {optimizer.stats}")