// Script para optimizar atributos alt de imágenes
document.addEventListener('DOMContentLoaded', function() {
    // Lista de imágenes principales que necesitan optimización
    const imageOptimizations = {
        'assets/images/paisajes/eje-cafetero-aerial-view.webp': 'Vista panorámica del Eje Cafetero con pueblos tradicionales, cafetales verdes y montañas neblinosas del Quindío',
        'assets/images/paisajes/valle-cocora-hero-banner.webp': 'Valle de Cocora con palmas de cera gigantes al atardecer, montañas neblinosas del Eje Cafetero',
        'assets/images/paisajes/palma-cera-sunlight.webp': 'Palmas de cera gigantes iluminadas por el sol en el Valle de Cocora, paisaje icónico del Quindío',
        'assets/images/atractivos/parque-del-cafe/parque-cafe-3.jpg': 'Parque del Café en el Eje Cafetero colombiano con montañas rusas y cafetales',
        'assets/images/atractivos/valle-cocora/valle-cocora.jpg': 'Valle de Cocora con sendero de palmas de cera, destino natural del Quindío',
        'assets/images/atractivos/salento/salento-pueblo.jpg': 'Pueblo de Salento con arquitectura tradicional colorida, balcones y vistas al Eje Cafetero',
        'assets/images/alojamientos/finca-hotel-los-girasoles.jpg': 'Finca Hotel Los Girasoles con piscina y paisajes cafeteros en Quindío',
        'assets/images/alojamientos/cabanas-la-esmeralda.jpg': 'Cabañas La Esmeralda con vistas panorámicas al paisaje cafetero'
    };

    // Aplicar optimizaciones a las imágenes
    document.querySelectorAll('img').forEach(img => {
        const src = img.getAttribute('src');
        if (src && imageOptimizations[src]) {
            img.setAttribute('alt', imageOptimizations[src]);
        }
    });

    // Agregar atributos de lazy loading y dimensiones a imágenes que no los tienen
    document.querySelectorAll('img').forEach(img => {
        if (!img.hasAttribute('loading')) {
            img.setAttribute('loading', 'lazy');
        }
        
        // Agregar dimensiones si no están presentes
        if (!img.hasAttribute('width') || !img.hasAttribute('height')) {
            const width = img.naturalWidth || 1200;
            const height = img.naturalHeight || 630;
            img.setAttribute('width', width);
            img.setAttribute('height', height);
        }
    });

    console.log('✅ Optimización de imágenes completada');
});