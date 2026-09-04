import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const rootDir = path.join(__dirname, '..');

// Obtener todos los archivos HTML
function getAllHtmlFiles(dir, fileList = []) {
  const files = fs.readdirSync(dir);
  
  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    
    if (stat.isDirectory()) {
      if (!['node_modules', '.git', 'docs', 'competitive-engine', 'don-chucho-backend', 
            'generated-pages', 'outreach_data', 'pseo-engine', 'programmatic-pages', 
            'scripts', 'sitemaps', 'promocion-del-mes', 'components', 'blog'].includes(file)) {
        getAllHtmlFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  
  return fileList;
}

const htmlFiles = getAllHtmlFiles(rootDir);
console.log(`📄 Analizando ${htmlFiles.length} archivos HTML para canonical tags...`);

const canonicalIssues = [];
const pagesWithCanonical = [];
const pagesWithoutCanonical = [];

htmlFiles.forEach(filePath => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const relativePath = path.relative(rootDir, filePath);
    
    // Buscar canonical tags
    const canonicalRegex = /<link rel="canonical" href="([^"]+)"/i;
    const match = content.match(canonicalRegex);
    
    if (match) {
      const canonicalUrl = match[1];
      pagesWithCanonical.push({ file: relativePath, canonical: canonicalUrl });
      
      // Verificar si el canonical apunta a una URL diferente
      const fileName = path.basename(filePath);
      const expectedCanonical = `https://quindiotravel.com.co/${fileName}`;
      
      if (canonicalUrl !== expectedCanonical && canonicalUrl !== `https://quindiotravel.com.co/`) {
        canonicalIssues.push({
          file: relativePath,
          canonical: canonicalUrl,
          expected: expectedCanonical,
          issue: 'Canonical apunta a URL diferente'
        });
      }
    } else {
      pagesWithoutCanonical.push(relativePath);
    }
  } catch (error) {
    console.log(`⚠️  Error leyendo ${filePath}: ${error.message}`);
  }
});

console.log(`\n✅ Páginas con canonical tag: ${pagesWithCanonical.length}`);
console.log(`❌ Páginas sin canonical tag: ${pagesWithoutCanonical.length}`);
console.log(`⚠️  Páginas con canonical issues: ${canonicalIssues.length}`);

if (canonicalIssues.length > 0) {
  console.log('\n📋 PÁGINAS CON CANONICAL ISSUES:');
  canonicalIssues.forEach((issue, index) => {
    console.log(`${index + 1}. ${issue.file}`);
    console.log(`   Canonical actual: ${issue.canonical}`);
    console.log(`   Canonical esperado: ${issue.expected}`);
    console.log(`   Issue: ${issue.issue}`);
  });
}

if (pagesWithoutCanonical.length > 0 && pagesWithoutCanonical.length < 20) {
  console.log('\n📋 PÁGINAS SIN CANONICAL TAG (primeras 10):');
  pagesWithoutCanonical.slice(0, 10).forEach((file, index) => {
    console.log(`${index + 1}. ${file}`);
  });
}