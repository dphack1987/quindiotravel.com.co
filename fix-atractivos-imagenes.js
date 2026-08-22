const fs = require('fs');

// Mapeo de imágenes faltantes a imágenes existentes como fallback
const imageMapping = {
    'assets/images/destinos/logo_valle_cocora.webp': 'assets/images/paisajes/valle-cocoro-hero-banner.webp',
    'assets/images/destinos/logo_salento.webp': 'assets/images/paisajes/salento-colorful-houses.jfif',
    'assets/images/destinos/logo_filandia.webp': 'assets/images/paisajes/filandia-colonial-architecture.jfif',
    'assets/images/destinos/logo_termales.webp': 'assets/images/paisajes/coffee-plantation-green.webp',
    'assets/images/destinos/logo_mariposario.webp': 'assets/images/paisajes/armenia-city-view.jfif',
    'assets/images/destinos/logo_cabalgatas.webp': 'assets/images/paisajes/quindio-traditional-town.jfif',
    'assets/images/destinos/logo_balsaje.webp': 'assets/images/paisajes/natural-landscapes-colombia.avif'
};

const filesToUpdate = ['index.html'];

filesToUpdate.forEach(file => {
    try {
        const content = fs.readFileSync(file, 'utf8');
        let newContent = content;
        
        // Reemplazar imágenes faltantes con fallbacks
        Object.entries(imageMapping).forEach(([missing, fallback]) => {
            newContent = newContent.replace(new RegExp(missing.replace(/\./g, '\\.'), 'g'), fallback);
        });
        
        if (content !== newContent) {
            fs.writeFileSync(file, newContent);
            console.log(`Fixed images in: ${file}`);
        } else {
            console.log(`No image changes needed in: ${file}`);
        }
    } catch (error) {
        console.error(`Error processing ${file}:`, error);
    }
});

console.log('Image fallback fix complete');