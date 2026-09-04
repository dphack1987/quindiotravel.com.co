import sharp from 'sharp';
import fs from 'fs';
import path from 'path';

const sourceLogo = 'assets/images/logo_quindio_travel.png';
const outputDir = '';

const sizes = [
  { name: 'favicon-16x16.png', size: 16 },
  { name: 'favicon-32x32.png', size: 32 },
  { name: 'apple-touch-icon.png', size: 180 }
];

async function generateFavicons() {
  try {
    console.log('🎨 Generando archivos de favicon...');
    
    // Verificar que el archivo source existe
    if (!fs.existsSync(sourceLogo)) {
      throw new Error(`Archivo fuente no encontrado: ${sourceLogo}`);
    }

    // Generar PNGs de diferentes tamaños
    for (const { name, size } of sizes) {
      const outputPath = path.join(outputDir, name);
      await sharp(sourceLogo)
        .resize(size, size, { fit: 'cover', background: { r: 0, g: 0, b: 0, alpha: 0 } })
        .png()
        .toFile(outputPath);
      console.log(`✅ Generado: ${name} (${size}x${size})`);
    }

    // Generar favicon.ico como PNG (compatibilidad)
    const icoPath = path.join(outputDir, 'favicon.ico');
    await sharp(sourceLogo)
      .resize(48, 48, { fit: 'cover' })
      .png()
      .toFile(icoPath);
    console.log(`✅ Generado: favicon.ico (48x48)`);

    console.log('🎉 ¡Favicons generados exitosamente!');
  } catch (error) {
    console.error('❌ Error generando favicons:', error.message);
    process.exit(1);
  }
}

generateFavicons();