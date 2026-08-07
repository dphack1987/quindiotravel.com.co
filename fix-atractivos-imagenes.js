const fs = require('fs');

// Mapeo de imágenes faltantes a imágenes existentes como fallback
const imageMapping = {
    'assets/images/destinos/logo_valle_cocora.jpg': 'assets/images/paisajes/valle-cocoro-hero-banner.jpg',
    'assets/images/destinos/logo_salento.jpg': 'assets/images/paisajes/salento-colorful-houses.jfif',
    'assets/images/destinos/logo_filandia.jpg': 'assets/images/paisajes/filandia-colonial-architecture.jfif',
    'assets/images/destinos/logo_termales.jpg': 'assets/images/paisajes/coffee-plantation-green.jpg',
    'assets/images/destinos/logo_mariposario.jpg': 'assets/images/paisajes/armenia-city-view.jfif',
    'assets/images/destinos/logo_cabalgatas.jpg': 'assets/images/paisajes/quindio-traditional-town.jfif',
    'assets/images/destinos/logo_balsaje.jpg': 'assets/images/paisajes/natural-landscapes-colombia.avif'
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