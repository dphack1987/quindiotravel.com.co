import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const sitemapPath = path.join(__dirname, '../sitemap.xml');
const rootDir = path.join(__dirname, '..');

// Leer sitemap.xml
const sitemapContent = fs.readFileSync(sitemapPath, 'utf-8');

// Extraer URLs del sitemap
const urlRegex = /<loc>(https:\/\/[^<]+)<\/loc>/g;
const urls = [];
let match;
while ((match = urlRegex.exec(sitemapContent)) !== null) {
  urls.push(match[1]);
}

console.log(`📊 Total URLs en sitemap.xml: ${urls.length}`);

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

console.log(`\n✅ URLs correspondientes a archivos existentes: ${existingFiles.length}`);
console.log(`❌ URLs sin archivo correspondiente (404): ${missingFiles.length}`);

if (missingFiles.length > 0) {
  console.log('\n📋 Archivos faltantes (causan error 404):');
  missingFiles.forEach((file, index) => {
    const relativePath = path.relative(rootDir, file);
    const originalUrl = urls[sitemapPaths.indexOf(file)];
    console.log(`${index + 1}. ${relativePath}`);
    console.log(`   URL: ${originalUrl}`);
  });
}

// Verificar directorios bloqueados por robots.txt
const blockedDirs = ['/programmatic-pages/', '/generated-pages/', '/docs/', '/competitive-engine/', 
                     '/don-chucho-backend/', '/outreach_data/', '/pseo-engine/', '/scripts/', 
                     '/sitemaps/', '/promocion-del-mes/'];

const blockedUrls = urls.filter(url => 
  blockedDirs.some(dir => url.includes(dir))
);

console.log(`\n🚫 URLs en directorios bloqueados por robots.txt: ${blockedUrls.length}`);
if (blockedUrls.length > 0) {
  console.log('\n📋 URLs bloqueadas por robots.txt:');
  blockedUrls.forEach((url, index) => {
    console.log(`${index + 1}. ${url}`);
  });
}