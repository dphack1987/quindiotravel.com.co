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
            'scripts', 'sitemaps', 'promocion-del-mes', 'components', 'blog', 'tests'].includes(file)) {
        getAllHtmlFiles(filePath, fileList);
      }
    } else if (file.endsWith('.html')) {
      fileList.push(filePath);
    }
  });
  
  return fileList;
}

const htmlFiles = getAllHtmlFiles(rootDir);
console.log('🔍 Validación de Enlaces en Archivos HTML');
console.log(`📄 Total archivos HTML: ${htmlFiles.length}`);

const linkIssues = {
  brokenLinks: [],
  emptyLinks: [],
  missingAltText: [],
  externalLinks: []
};

htmlFiles.forEach(filePath => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const relativePath = path.relative(rootDir, filePath);
    
    // Buscar enlaces vacíos
    const emptyLinkRegex = /href=["']\s*["']/g;
    let match;
    while ((match = emptyLinkRegex.exec(content)) !== null) {
      linkIssues.emptyLinks.push({
        file: relativePath,
        issue: 'Enlace vacío encontrado'
      });
    }
    
    // Buscar enlaces a archivos que no existen
    const linkRegex = /href=["']([^"']+\.html?)["']/g;
    while ((match = linkRegex.exec(content)) !== null) {
      const linkPath = match[1];
      // Ignorar enlaces externos y anclas
      if (!linkPath.startsWith('http') && !linkPath.startsWith('#') && !linkPath.startsWith('mailto:') && !linkPath.startsWith('tel:')) {
        const fullPath = path.join(path.dirname(filePath), linkPath);
        if (!fs.existsSync(fullPath)) {
          linkIssues.brokenLinks.push({
            file: relativePath,
            link: linkPath,
            issue: 'Archivo de destino no existe'
          });
        }
      }
    }
    
    // Buscar imágenes sin alt text
    const imgRegex = /<img[^>]*>/g;
    while ((match = imgRegex.exec(content)) !== null) {
      const imgTag = match[0];
      if (!imgTag.includes('alt=') || imgTag.includes('alt=""') || imgTag.includes("alt=''")) {
        linkIssues.missingAltText.push({
          file: relativePath,
          issue: 'Imagen sin atributo alt o vacío'
        });
      }
    }
    
    // Buscar enlaces externos
    const externalLinkRegex = /href=["'](https?:\/\/[^"']+)["']/g;
    while ((match = externalLinkRegex.exec(content)) !== null) {
      const externalUrl = match[1];
      if (!externalUrl.includes('quindiotravel.com.co') && !externalUrl.includes('cdnjs.cloudflare.com') && !externalUrl.includes('font-awesome')) {
        linkIssues.externalLinks.push({
          file: relativePath,
          url: externalUrl,
          issue: 'Enlace externo detectado'
        });
      }
    }
    
  } catch (error) {
    console.log(`⚠️  Error analizando ${filePath}: ${error.message}`);
  }
});

console.log('\n📋 RESULTADOS DE VALIDACIÓN:');
console.log(`\n🔗 Enlaces Rotos: ${linkIssues.brokenLinks.length}`);
if (linkIssues.brokenLinks.length > 0 && linkIssues.brokenLinks.length <= 10) {
  linkIssues.brokenLinks.forEach(item => {
    console.log(`   - ${item.file}: ${item.link} - ${item.issue}`);
  });
}

console.log(`\n⚪ Enlaces Vacíos: ${linkIssues.emptyLinks.length}`);
if (linkIssues.emptyLinks.length > 0 && linkIssues.emptyLinks.length <= 10) {
  linkIssues.emptyLinks.forEach(item => {
    console.log(`   - ${item.file}: ${item.issue}`);
  });
}

console.log(`\n🖼️  Imágenes sin Alt Text: ${linkIssues.missingAltText.length}`);
if (linkIssues.missingAltText.length > 0 && linkIssues.missingAltText.length <= 10) {
  linkIssues.missingAltText.forEach(item => {
    console.log(`   - ${item.file}: ${item.issue}`);
  });
}

console.log(`\n🌐 Enlaces Externos: ${linkIssues.externalLinks.length}`);
if (linkIssues.externalLinks.length > 0 && linkIssues.externalLinks.length <= 10) {
  linkIssues.externalLinks.forEach(item => {
    console.log(`   - ${item.file}: ${item.url}`);
  });
}

const totalIssues = linkIssues.brokenLinks.length + linkIssues.emptyLinks.length + 
                     linkIssues.missingAltText.length + linkIssues.externalLinks.length;

console.log(`\n📊 TOTAL DE ISSUES: ${totalIssues}`);

if (totalIssues === 0) {
  console.log('✅ ¡Todos los enlaces están validados!');
} else {
  console.log('⚠️  Se detectaron issues que requieren atención.');
}