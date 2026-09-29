import https from 'https';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const sitemapUrl = 'https://quindiotravel.com.co/sitemap.xml';

console.log('📡 Notificando a motores de búsqueda sobre sitemap actualizado...\n');

// Google (Ping deprecated, se necesita GSC manual)
console.log('🔍 Google Search Console:');
console.log('❌ El ping automático está deprecated');
console.log('✅ Acción requerida: Ir a Google Search Console > Sitemaps y verificar que esté actualizado');
console.log('📍 URL: https://search.google.com/search-console/sitemaps?resource_id=sc-domain:quindiotravel.com.co\n');

// Bing (Ping puede no funcionar correctamente)
console.log('🔍 Bing Webmaster Tools:');
console.log('⚠️  El ping automático puede no funcionar');
console.log('✅ Acción recomendada: Ir a Bing Webmaster Tools > Sitemaps y reenviar sitemap');
console.log('📍 URL: https://www.bing.com/webmasters/about\n');

// Yandex (Ping funciona)
console.log('🔍 Yandex Webmaster:');
const yandexUrl = `https://webmaster.yandex.com/ping?sitemap=${sitemapUrl}`;
https.get(yandexUrl, (res) => {
    console.log(`✅ Ping enviado a Yandex: ${res.statusCode}`);
    console.log(`📍 URL: ${yandexUrl}\n`);
}).on('error', (err) => {
    console.log(`❌ Error al hacer ping a Yandex: ${err.message}\n`);
});

// General information
console.log('📋 Información del Sitemap:');
console.log(`📍 URL: ${sitemapUrl}`);
console.log(`📅 Fecha actualización: 2026-09-29`);
console.log(`📊 Total URLs: 94\n`);

console.log('💡 Recomendaciones adicionales:');
console.log('1. Google Search Console: Solicitar reindexación de páginas principales');
console.log('2. Bing Webmaster Tools: Agregar sitemap manualmente si no está registrado');
console.log('3. Monitorear indexación en los próximos días');
console.log('4. Verificar que las redirecciones 404 funcionen correctamente');