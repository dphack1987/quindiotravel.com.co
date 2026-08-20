import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

console.log('🚀 Iniciando optimización de assets...\n');

// Minificar CSS
const cssFiles = [
  'styles.css',
  'assets/css/critical.css',
  'assets/css/planes-especiales-diciembre.css'
];

console.log('📦 Minificando archivos CSS...');
cssFiles.forEach(file => {
  const filePath = path.join(rootDir, file);
  if (fs.existsSync(filePath)) {
    const minPath = filePath.replace('.css', '.min.css');
    try {
      execSync(`npx cssnano ${filePath} ${minPath}`, { stdio: 'inherit' });
      console.log(`✅ ${file} → ${path.basename(minPath)}`);
    } catch (error) {
      console.log(`⚠️  Error minificando ${file}:`, error.message);
    }
  }
});

// Minificar JS principales
const jsFiles = [
  'assets/js/main.js',
  'assets/js/cotizador.js',
  'assets/js/don-chucho-chat.js',
  'assets/js/language-detector.js',
  'assets/js/performance-optimizer.js',
  'assets/js/whatsapp-payload-builder.js',
  'assets/js/whatsapp-template-handler.js'
];

console.log('\n📦 Minificando archivos JS...');
jsFiles.forEach(file => {
  const filePath = path.join(rootDir, file);
  if (fs.existsSync(filePath)) {
    const minPath = filePath.replace('.js', '.min.js');
    try {
      execSync(`npx terser ${filePath} -o ${minPath} -c -m`, { stdio: 'inherit' });
      console.log(`✅ ${file} → ${path.basename(minPath)}`);
    } catch (error) {
      console.log(`⚠️  Error minificando ${file}:`, error.message);
    }
  }
});

console.log('\n✨ Optimización de assets completada.');