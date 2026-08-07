const fs = require('fs');

const rootFiles = [
    'index.html',
    'planes.html',
    'blog.html',
    'blog-mejor-epoca-eje-cafetero.html',
    'promo-agosto-2026.html',
    'cabalgatas-quindio.html',
    'coffee-tour-armenia.html',
    'filandia.html',
    'balsaje-rio-la-vieja.html',
    'cabanas-la-esmeralda.html',
    'finca-hotel-la-dorada.html',
    'finca-hotel-los-girasoles.html',
    'mariposario-quindio.html',
    'authority_content.html',
    'generate-qr-online.html'
];

rootFiles.forEach(file => {
    try {
        const content = fs.readFileSync(file, 'utf8');
        
        // Fix logo paths for root level files
        let newContent = content
            .replace(/src="logo_quindio_travel\.png"/g, 'src="assets/images/logo_quindio_travel.png"')
            .replace(/src="\/logo_quindio_travel\.png"/g, 'src="assets/images/logo_quindio_travel.png"')
            .replace(/"logo": "https:\/\/quindiotravel\.com\.co\/logo\.png"/g, '"logo": "https://quindiotravel.com.co/assets/images/logo_quindio_travel.png"');
        
        if (content !== newContent) {
            fs.writeFileSync(file, newContent);
            console.log(`Fixed logo in: ${file}`);
        } else {
            console.log(`No logo changes needed in: ${file}`);
        }
    } catch (error) {
        console.error(`Error processing ${file}:`, error);
    }
});

console.log('Root files logo fix complete');