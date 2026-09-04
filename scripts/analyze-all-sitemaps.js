import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const rootDir = path.join(__dirname, '..');

// Sitemaps mencionados en robots.txt
const sitemapFiles = [
  'sitemap.xml',
  'sitemap-main.xml', 
  'sitemap-content.xml',
  'sitemap-alojamientos.xml',
  'sitemap-atractivos.xml',
  'sitemap-municipios.xml',
  'sitemap-tipos-viaje.xml',
  'sitemap-amenidades.xml'
];

// Obtener todos los archivos HTML existentes
function getAllHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  
  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isDirectory()) {
      // Ignorar directorios bloqueados
      if (!['node_modules', '.git', 'docs', 'competitive-engine', 'don-chucho-backend', 
            'generated-pages', 'outreach_data', 'pseo-engine', 'programmatic-pages', 
            'scripts', 'sitemaps', 'promocion-del-mes'].includes(file)) {
        getAllHtmlFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  
  return fileList;
}

const htmlFiles = getAllHtmlFiles(rootDir);
console.log(`📄 Total archivos HTML existentes: ${htmlFiles.length}`);

// Directorios bloqueados por robots.txt
const blockedDirs = ['/programmatic-pages/', '/generated-pages/', '/docs/', '/competitive-engine/', 
                     '/don-chucho-backend/', '/outreach_data/', '/pseo-engine/', '/scripts/', 
                     '/sitemaps/', '/promocion-del-mes/'];

let totalUrls = 0;
let totalMissingFiles = 0;
let totalBlockedUrls = 0;
let allMissingFiles = [];
let allBlockedUrls = [];

sitemapFiles.forEach(sitemapFile => {
  const sitemapPath = path.join(rootDir, sitemapFile);
  
  if (!fs.existsSync(sitemapPath)) {
    console.log(`⚠️  Sitemap no encontrado: ${sitemapFile}`);
    return;
  }
  
  console.log(`\n📊 Analizando ${sitemapFile}:`);
  
  const sitemapContent = fs.readFileSync(sitemapPath, 'utf-8');
  
  // Extraer URLs del sitemap
  const urlRegex = /<loc>(https:\/\/[^<]+)<\/loc>/g;
  const urls = [];
  let match;
  while ((match = urlRegex.exec(sitemapContent)) !== null) {
    urls.push(match[1]);
  }
  
  console.log(`   URLs totales: ${urls.length}`);
  totalUrls += urls.length;
  
  // Convertir URLs a rutas de archivo locales
  const sitemapPaths = urls.map(url => {
    const relativePath = url.replace('https://quindiotravel.com.co/', '').replace(/^\//, '');
    return path.join(rootDir, relativePath);
  });
  
  // Identificar URLs que no corresponden a archivos existentes
  const missingFiles = [];
  const existingFiles = [];
  
  sitemapPaths.forEach(sitemapPath => {
    if (fs.existsSync(sitemapPath)) {
      existingFiles.push(sitemapPath);
    } else {
      missingFiles.push(sitemapPath);
    }
  });
  
  console.log(`   ✅ Archivos existentes: ${existingFiles.length}`);
  console.log(`   ❌ Archivos faltantes (404): ${missingFiles.length}`);
  
  if (missingFiles.length > 0) {
    missingFiles.forEach(file => {
      const relativePath = path.relative(rootDir, file);
      const originalUrl = urls[sitemapPaths.indexOf(file)];
      allMissingFiles.push({ file: relativePath, url: originalUrl, sitemap: sitemapFile });
    });
  }
  
  totalMissingFiles += missingFiles.length;
  
  // Verificar URLs en directorios bloqueados
  const blockedUrls = urls.filter(url => 
    blockedDirs.some(dir => url.includes(dir))
  );
  
  console.log(`   🚫 URLs en directorios bloqueados: ${blockedUrls.length}`);
  
  if (blockedUrls.length > 0) {
    blockedUrls.forEach(url => {
      allBlockedUrls.push({ url: url, sitemap: sitemapFile });
    });
  }
  
  totalBlockedUrls += blockedUrls.length;
});

// Resumen total
console.log('\n' + '='.repeat(60));
console.log('📋 RESUMEN TOTAL DE TODOS LOS SITEMAPS');
console.log('='.repeat(60));
console.log(`📊 Total URLs en todos los sitemaps: ${totalUrls}`);
console.log(`❌ Total archivos faltantes (404): ${totalMissingFiles}`);
console.log(`🚫 Total URLs en directorios bloqueados: ${totalBlockedUrls}`);

if (allMissingFiles.length > 0) {
  console.log('\n📋 TODOS LOS ARCHIVOS FALTANTES (CAUSAN ERROR 404):');
  allMissingFiles.forEach((item, index) => {
    console.log(`${index + 1}. ${item.file}`);
    console.log(`   URL: ${item.url}`);
    console.log(`   Sitemap: ${item.sitemap}`);
  });
}

if (allBlockedUrls.length > 0) {
  console.log('\n📋 TODAS LAS URLs BLOQUEADAS POR ROBOTS.TXT:');
  allBlockedUrls.forEach((item, index) => {
    console.log(`${index + 1}. ${item.url}`);
    console.log(`   Sitemap: ${item.sitemap}`);
  });
}