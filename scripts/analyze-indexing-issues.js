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
console.log(`🔍 Análisis Profundo de Indexación Google Search Console`);
console.log(`📄 Total archivos HTML: ${htmlFiles.length}`);

// Categorías de problemas que causan "Discovered - currently not indexed"
const discoveredNotIndexed = {
  veryNewPages: [],
  lowAuthority: [],
  duplicateContent: [],
  orphanPages: [],
  technicalProblems: []
};

// Categorías de problemas que causan "Crawled - currently not indexed"
const crawledNotIndexed = {
  noIndexTags: [],
  lowQuality: [],
  serverErrors: [],
  blockedResources: []
};

htmlFiles.forEach(filePath => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const relativePath = path.relative(rootDir, filePath);
    const fileName = path.basename(filePath);
    
    // Análisis para "Discovered - currently not indexed"
    
    // Páginas muy nuevas (sin suficiente autoridad)
    const contentLength = content.length;
    if (contentLength < 3000 && fileName !== '404.html' && fileName !== '500.html' && fileName !== 'yandex_05c13632a16e2bef.html') {
      if (discoveredNotIndexed.veryNewPages) {
        discoveredNotIndexed.veryNewPages.push({
          file: relativePath,
          length: contentLength,
          reason: 'Contenido insuficiente para indexación rápida'
        });
      }
    }
    
    // Posible contenido duplicado (títulos genéricos)
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    if (titleMatch) {
      const title = titleMatch[1].toLowerCase();
      if (title.includes('planes') || title.includes('viajes') || title.includes('turismo')) {
        if (title.length < 30) {
          if (discoveredNotIndexed.duplicateContent) {
            discoveredNotIndexed.duplicateContent.push({
              file: relativePath,
              title: titleMatch[1],
              reason: 'Título potencialmente duplicado o genérico'
            });
          }
        }
      }
    }
    
    // Páginas huérfanas (sin enlaces internos)
    const hasInternalLinks = /href="[^"]*\.html"/g.test(content);
    if (!hasInternalLinks && fileName !== 'index.html') {
      if (discoveredNotIndexed.orphanPages) {
        discoveredNotIndexed.orphanPages.push({
          file: relativePath,
          reason: 'Posible página huérfana sin enlaces internos'
        });
      }
    }
    
    // Análisis para "Crawled - currently not indexed"
    
    // Meta tags noindex
    const hasNoIndex = /<meta name="robots".*noindex/i.test(content);
    if (hasNoIndex) {
      if (crawledNotIndexed.noIndexTags) {
        crawledNotIndexed.noIndexTags.push({
          file: relativePath,
          reason: 'Meta tag noindex presente'
        });
      }
    }
    
    // Calidad baja (sin H1, sin contenido estructurado)
    const hasH1 = /<h1/i.test(content);
    const hasStructuredContent = /<(section|article|main)/i.test(content);
    
    if (!hasH1 || !hasStructuredContent) {
      if (crawledNotIndexed.lowQuality) {
        crawledNotIndexed.lowQuality.push({
          file: relativePath,
          missingH1: !hasH1,
          missingStructuredContent: !hasStructuredContent,
          reason: 'Estructura de contenido deficiente'
        });
      }
    }
    
    // Problemas técnicos (recursos bloqueados, errores)
    const hasBrokenLinks = /href=["'](#["'])|href=["'](\s*)["']/g.test(content);
    if (hasBrokenLinks) {
      if (crawledNotIndexed.technicalProblems) {
        crawledNotIndexed.technicalProblems.push({
          file: relativePath,
          reason: 'Posibles enlaces rotos o vacíos'
        });
      }
    }
    
  } catch (error) {
    console.log(`⚠️  Error analizando ${filePath}: ${error.message}`);
  }
});

console.log('\n📋 PÁGINAS "DISCOVERED - CURRENTLY NOT INDEXED" (70 estimadas):');
console.log(`\n📝 Contenido Insuficiente: ${discoveredNotIndexed.veryNewPages.length}`);
if (discoveredNotIndexed.veryNewPages.length > 0 && discoveredNotIndexed.veryNewPages.length <= 15) {
  discoveredNotIndexed.veryNewPages.forEach(item => {
    console.log(`   - ${item.file} (${item.length} chars): ${item.reason}`);
  });
}

console.log(`\n🔄 Posible Contenido Duplicado: ${discoveredNotIndexed.duplicateContent.length}`);
if (discoveredNotIndexed.duplicateContent.length > 0 && discoveredNotIndexed.duplicateContent.length <= 10) {
  discoveredNotIndexed.duplicateContent.forEach(item => {
    console.log(`   - ${item.file}: "${item.title}" - ${item.reason}`);
  });
}

console.log(`\n🔗 Páginas Huérfanas: ${discoveredNotIndexed.orphanPages.length}`);
if (discoveredNotIndexed.orphanPages.length > 0 && discoveredNotIndexed.orphanPages.length <= 10) {
  discoveredNotIndexed.orphanPages.forEach(item => {
    console.log(`   - ${item.file}: ${item.reason}`);
  });
}

console.log('\n📋 PÁGINAS "CRAWLED - CURRENTLY NOT INDEXED" (18 estimadas):');
console.log(`\n🚫 Meta Tags NoIndex: ${crawledNotIndexed.noIndexTags.length}`);
if (crawledNotIndexed.noIndexTags.length > 0 && crawledNotIndexed.noIndexTags.length <= 10) {
  crawledNotIndexed.noIndexTags.forEach(item => {
    console.log(`   - ${item.file}: ${item.reason}`);
  });
}

console.log(`\n⬇️  Calidad Baja: ${crawledNotIndexed.lowQuality.length}`);
if (crawledNotIndexed.lowQuality.length > 0 && crawledNotIndexed.lowQuality.length <= 10) {
  crawledNotIndexed.lowQuality.forEach(item => {
    console.log(`   - ${item.file}: H1=${!item.missingH1}, Estructura=${!item.missingStructuredContent} - ${item.reason}`);
  });
}

console.log(`\n🔧 Problemas Técnicos: ${crawledNotIndexed.technicalProblems ? crawledNotIndexed.technicalProblems.length : 0}`);
if (crawledNotIndexed.technicalProblems && crawledNotIndexed.technicalProblems.length > 0 && crawledNotIndexed.technicalProblems.length <= 10) {
  crawledNotIndexed.technicalProblems.forEach(item => {
    console.log(`   - ${item.file}: ${item.reason}`);
  });
}

// Recomendaciones específicas
console.log('\n💡 RECOMENDACIONES ESPECÍFICAS:');
console.log('\nPara "Discovered - currently not indexed":');
console.log('1. Agregar más contenido único a páginas cortas');
console.log('2. Crear títulos más específicos y descriptivos');
console.log('3. Agregar enlaces internos desde páginas principales');
console.log('4. Mejorar la estructura con headings apropiados');

console.log('\nPara "Crawled - currently not indexed":');
console.log('1. Revisar meta tags noindex (eliminar si no son necesarios)');
console.log('2. Agregar H1 y estructura semántica (section, article)');
console.log('3. Corregir enlaces rotos o vacíos');
console.log('4. Aumentar la profundidad del contenido');

const totalDiscovered = (discoveredNotIndexed.veryNewPages ? discoveredNotIndexed.veryNewPages.length : 0) + 
                       (discoveredNotIndexed.duplicateContent ? discoveredNotIndexed.duplicateContent.length : 0) + 
                       (discoveredNotIndexed.orphanPages ? discoveredNotIndexed.orphanPages.length : 0);
const totalCrawled = (crawledNotIndexed.noIndexTags ? crawledNotIndexed.noIndexTags.length : 0) + 
                     (crawledNotIndexed.lowQuality ? crawledNotIndexed.lowQuality.length : 0) + 
                     (crawledNotIndexed.technicalProblems ? crawledNotIndexed.technicalProblems.length : 0);

console.log(`\n📊 TOTAL PÁGINAS CON ISSUES: ${totalDiscovered + totalCrawled}`);
console.log(`   - Discovered not indexed: ${totalDiscovered}`);
console.log(`   - Crawled not indexed: ${totalCrawled}`);