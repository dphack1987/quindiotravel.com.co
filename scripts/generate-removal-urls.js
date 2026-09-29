import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.join(__dirname, '..');

// URLs que necesitan ser removidas de Google (404s históricos)
const urlsToRemove = [
    // Programmatic pages excluidas del deploy
    '/programmatic-pages/alojamiento-economico-salento-2026.html',
    '/programmatic-pages/alojamiento-lujo-quindio-2026.html',
    '/programmatic-pages/hoteles-economicos-salento-2026.html',
    '/programmatic-pages/valle-cocora-caminata-2026.html',
    '/programmatic-pages/tour-salento-desde-bogota-2026.html',
    '/programmatic-pages/mejor-epoca-visitar-filandia-2026.html',
    '/programmatic-pages/hoteles-familiares-salento-2026.html',
    '/programmatic-pages/termales-santa-rosa-plan-2026.html',
    '/programmatic-pages/parque-cafe-entradas-2026.html',
    '/programmatic-pages/finca-cafe-salento-2026.html',
    '/programmatic-pages/planes-grupos-4-personas-quindio-2026.html',
    '/programmatic-pages/tour-eje-cafetero-sin-transporte-2026.html',
    '/programmatic-pages/hoteles-cerca-parque-cafe-2026.html',
    // Generated pages excluidas del deploy
    '/generated-pages/alojamiento/cabanas-la-esmeralda.html',
    '/generated-pages/alojamiento/finca-hotel-la-dorada.html',
    '/generated-pages/alojamiento/hotel-campestre-cafe-cafe.html',
    '/generated-pages/alojamiento/hotel-campestre-la-tata.html',
    '/generated-pages/alojamiento/hotel-campestre-las-camelias.html',
    '/generated-pages/alojamiento/hotel-campestre-los-girasoles.html',
    '/generated-pages/alojamiento/hotel-de-la-vega.html',
    '/generated-pages/atractivo/mariposario.html',
    '/generated-pages/atractivo/panaca.html',
    '/generated-pages/atractivo/parque-del-cafe.html',
    '/generated-pages/atractivo/recuca.html',
    '/generated-pages/atractivo/termales-santa-rosa.html',
    '/generated-pages/atractivo/valle-de-cocora.html',
    // Páginas duplicadas eliminadas
    '/blog-mejor-epoca-eje-cafetero.html',
    '/mejor-epoca-para-visitar-quindio.html',
    '/quindio-viajes-planes-turisticos.html',
    '/viajes-economicos-quindio.html',
    '/turismo-familiar-eje-cafetero.html',
    '/blog/mejor-epoca-para-visitar-quindio-en-2026-guia-completa.html'
];

// Generar URLs completas
const fullUrls = urlsToRemove.map(url => `https://quindiotravel.com.co${url}`);

// Crear archivo para Google Search Console Removal Tool
const removalFile = path.join(rootDir, 'google-removal-urls.txt');
const removalContent = fullUrls.join('\n');

fs.writeFileSync(removalFile, removalContent);
console.log(`✅ Archivo de remoción generado: ${removalFile}`);
console.log(`📊 Total URLs para remover: ${fullUrls.length}`);

// Crear archivo para análisis
const analysisFile = path.join(rootDir, 'removal-analysis.json');
const analysisData = {
    totalUrls: fullUrls.length,
    urlsByCategory: {
        programmaticPages: urlsToRemove.filter(url => url.includes('programmatic-pages')).length,
        generatedPages: urlsToRemove.filter(url => url.includes('generated-pages')).length,
        duplicatePages: urlsToRemove.filter(url => !url.includes('programmatic-pages') && !url.includes('generated-pages')).length
    },
    urls: fullUrls,
    generatedAt: new Date().toISOString(),
    recommendations: [
        '1. Subir este archivo a Google Search Console Removal Tool',
        '2. Monitorear impacto en indexación durante 2 semanas',
        '3. Solicitar reindexación de páginas principales después de limpieza',
        '4. Verificar que redirecciones en 404.html funcionan correctamente'
    ]
};

fs.writeFileSync(analysisFile, JSON.stringify(analysisData, null, 2));
console.log(`📋 Análisis generado: ${analysisFile}`);
console.log('\n📊 Distribución de URLs:');
console.log(`   - Programmatic pages: ${analysisData.urlsByCategory.programmaticPages}`);
console.log(`   - Generated pages: ${analysisData.urlsByCategory.generatedPages}`);
console.log(`   - Duplicate pages: ${analysisData.urlsByCategory.duplicatePages}`);