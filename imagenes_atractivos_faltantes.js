const fs = require('fs');
const path = require('path');

// Lista de imágenes de atractivos referenciadas en index.html
const requiredImages = [
    'assets/images/destinos/logo_parque_del_cafe.jpg',
    'assets/images/destinos/logo_panaca.png',
    'assets/images/destinos/logo_valle_cocora.jpg',
    'assets/images/destinos/logo_salento.jpg',
    'assets/images/destinos/logo_filandia.jpg',
    'assets/images/destinos/logo_termales.jpg',
    'assets/images/destinos/logo_recuca.png',
    'assets/images/destinos/logo_mariposario.jpg',
    'assets/images/destinos/logo_cabalgatas.jpg',
    'assets/images/destinos/logo_parque_los_arrieros.png',
    'assets/images/destinos/logo_balsaje.jpg'
];

console.log('Verificando imágenes de atractivos turísticos...\n');

const missingImages = [];
const existingImages = [];
const availableImages = [];

// Verificar directorio destinos
const destinosDir = path.join(__dirname, 'assets/images/destinos');
if (fs.existsSync(destinosDir)) {
    const files = fs.readdirSync(destinosDir);
    files.forEach(file => {
        if (file.match(/\.(jpg|png|jpeg|jfif)$/i)) {
            availableImages.push(`assets/images/destinos/${file}`);
        }
    });
}

console.log(`Imágenes disponibles en destinos/: ${availableImages.length}`);
availableImages.forEach(img => console.log(`  - ${img}`));

requiredImages.forEach(imagePath => {
    const fullPath = path.join(__dirname, imagePath);
    if (fs.existsSync(fullPath)) {
        existingImages.push(imagePath);
        console.log(`✅ EXISTS: ${imagePath}`);
    } else {
        missingImages.push(imagePath);
        console.log(`❌ MISSING: ${imagePath}`);
    }
});

console.log('\n=== RESUMEN ===');
console.log(`Imágenes requeridas: ${requiredImages.length}`);
console.log(`Imágenes existentes: ${existingImages.length}`);
console.log(`Imágenes faltantes: ${missingImages.length}`);
console.log(`Imágenes disponibles: ${availableImages.length}`);

if (missingImages.length > 0) {
    console.log('\n=== IMÁGENES FALTANTES ===');
    missingImages.forEach(img => console.log(`  - ${img}`));
    
    console.log('\n=== SUGERENCIAS DE MAPPING ===');
    console.log('Usar imágenes disponibles como fallback:');
    missingImages.forEach(missing => {
        const imageName = path.basename(missing).replace(/\.(jpg|png)$/, '');
        const available = availableImages.find(img => img.includes(imageName.substring(5)));
        if (available) {
            console.log(`  ${missing} -> ${available}`);
        } else {
            console.log(`  ${missing} -> assets/images/paisajes/salento-colorful-houses.jfif (fallback)`);
        }
    });
}