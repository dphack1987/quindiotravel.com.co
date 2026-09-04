import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const rootDir = path.join(__dirname, '..');

// Obtener todos los archivos HTML existentes
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
console.log(`📊 Análisis de páginas para Google Search Console`);
console.log(`📄 Total archivos HTML: ${htmlFiles.length}`);

// Análisis de problemas comunes que causan no-indexación
const analysis = {
  lowQualityContent: [],
  duplicateContent: [],
  missingMetaTags: [],
  thinContent: [],
  technicalIssues: []
};

htmlFiles.forEach(filePath => {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const relativePath = path.relative(rootDir, filePath);
    const fileName = path.basename(filePath);
    
    // Verificar longitud del contenido
    const contentLength = content.length;
    if (contentLength < 2000) {
      analysis.thinContent.push({
        file: relativePath,
        length: contentLength,
        issue: 'Contenido muy corto (< 2000 caracteres)'
      });
    }
    
    // Verificar meta tags esenciales
    const hasTitle = /<title>.*<\/title>/i.test(content);
    const hasDescription = /<meta name="description"/i.test(content);
    const hasH1 = /<h1/i.test(content);
    
    if (!hasTitle || !hasDescription || !hasH1) {
      analysis.missingMetaTags.push({
        file: relativePath,
        missing: {
          title: !hasTitle,
          description: !hasDescription,
          h1: !hasH1
        }
      });
    }
    
    // Verificar contenido duplicado potencial (títulos muy similares)
    const titleMatch = content.match(/<title>(.*?)<\/title>/i);
    if (titleMatch) {
      const title = titleMatch[1].toLowerCase();
      if (title.includes('placeholder') || title.includes('template') || title.length < 20) {
        analysis.lowQualityContent.push({
          file: relativePath,
          title: titleMatch[1],
          issue: 'Título de baja calidad'
        });
      }
    }
    
    // Verificar errores técnicos comunes
    const hasNoIndex = /<meta name="robots".*noindex/i.test(content);
    const hasCanonical = /<link rel="canonical"/i.test(content);
    
    if (hasNoIndex) {
      analysis.technicalIssues.push({
        file: relativePath,
        issue: 'Meta tag noindex presente'
      });
    }
    
    if (!hasCanonical && fileName !== '404.html' && fileName !== '500.html') {
      analysis.technicalIssues.push({
        file: relativePath,
        issue: 'Falta canonical tag'
      });
    }
    
  } catch (error) {
    console.log(`⚠️  Error analizando ${filePath}: ${error.message}`);
  }
});

console.log('\n📋 RESULTADOS DEL ANÁLISIS:');
console.log(`\n📝 Contenido Corto (< 2000 caracteres): ${analysis.thinContent.length}`);
if (analysis.thinContent.length > 0 && analysis.thinContent.length <= 10) {
  analysis.thinContent.forEach(item => {
    console.log(`   - ${item.file} (${item.length} chars)`);
  });
}

console.log(`\n🏷️  Faltan Meta Tags Esenciales: ${analysis.missingMetaTags.length}`);
if (analysis.missingMetaTags.length > 0 && analysis.missingMetaTags.length <= 10) {
  analysis.missingMetaTags.forEach(item => {
    console.log(`   - ${item.file}: ${JSON.stringify(item.missing)}`);
  });
}

console.log(`\n⚠️  Contenido de Baja Calidad: ${analysis.lowQualityContent.length}`);
if (analysis.lowQualityContent.length > 0 && analysis.lowQualityContent.length <= 10) {
  analysis.lowQualityContent.forEach(item => {
    console.log(`   - ${item.file}: "${item.title}"`);
  });
}

console.log(`\n🔧 Issues Técnicos: ${analysis.technicalIssues.length}`);
if (analysis.technicalIssues.length > 0 && analysis.technicalIssues.length <= 10) {
  analysis.technicalIssues.forEach(item => {
    console.log(`   - ${item.file}: ${item.issue}`);
  });
}

// Recomendaciones
console.log('\n💡 RECOMENDACIONES PARA MEJORAR INDEXACIÓN:');
console.log('1. Agregar contenido único y valioso a páginas con contenido corto');
console.log('2. Asegurar que todas las páginas tengan title, description y h1');
console.log('3. Agregar canonical tags a todas las páginas importantes');
console.log('4. Revisar páginas con meta noindex');
console.log('5. Crear contenido específico para cada destino/servicio');

const totalIssues = analysis.thinContent.length + analysis.missingMetaTags.length + 
                     analysis.lowQualityContent.length + analysis.technicalIssues.length;
console.log(`\n📊 Total de Issues Detectados: ${totalIssues}`);