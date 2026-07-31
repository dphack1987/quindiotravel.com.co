/**
 * Quindío Travel Sitemap Generator
 * Generación de sitemaps segmentados para indexación masiva
 * Compatible con Google Search Console y SEO técnico avanzado
 */

const fs = require('fs');
const path = require('path');

class SitemapGenerator {
  constructor() {
    this.baseUrl = 'https://quindiotravel.com.co';
    this.sitemapsDir = path.join(__dirname, '../sitemaps');
    this.sitemapIndex = [];
    this.masterData = this.loadMasterData();
  }

  loadMasterData() {
    try {
      const dataPath = path.join(__dirname, 'pseo-master-data.json');
      const rawData = fs.readFileSync(dataPath, 'utf8');
      return JSON.parse(rawData);
    } catch (error) {
      console.log('No se encontró master data, usando estructura por defecto');
      return {
        municipios: [],
        tiposViaje: [],
        amenidades: [],
        alojamientos: [],
        atractivos: [],
        combinacionesGeneradas: []
      };
    }
  }

  ensureSitemapsDirectory() {
    if (!fs.existsSync(this.sitemapsDir)) {
      fs.mkdirSync(this.sitemapsDir, { recursive: true });
    }
  }

  generateSitemapEntry(url, lastModified = null, changeFreq = 'weekly', priority = 0.7) {
    const lastMod = lastModified || new Date().toISOString().split('T')[0];
    
    return `    <url>
        <loc>${url}</loc>
        <lastmod>${lastMod}</lastmod>
        <changefreq>${changeFreq}</changefreq>
        <priority>${priority}</priority>
    </url>`;
  }

  generateMainSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9
        http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
    <url>
        <loc>${this.baseUrl}/</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/index.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/planes.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/blog-mejor-epoca-eje-cafetero.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/salento.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/filandia.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/valle-de-cocora.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>${this.baseUrl}/parque-del-cafe.html</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>`;

    // Agregar planes individuales
    for (let i = 1; i <= 6; i++) {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/plan-${i}.html`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.8
      );
    }

    // Agregar páginas de alojamientos principales
    const mainAlojamientos = [
      'cabanas-la-esmeralda',
      'hotel-campestre-los-girasoles',
      'hotel-campestre-cafe-cafe',
      'hotel-campestre-la-tata',
      'hotel-campestre-las-camelias',
      'hotel-de-la-vega',
      'finca-hotel-la-dorada'
    ];

    mainAlojamientos.forEach(alojamiento => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/${alojamiento}.html`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.7
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateMunicipiosSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    this.masterData.municipios.forEach(municipio => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/${municipio.slug}`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.8
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateAlojamientosSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    this.masterData.alojamientos.forEach(alojamiento => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/alojamiento/${alojamiento.slug}`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.7
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateAtractivosSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    this.masterData.atractivos.forEach(atractivo => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/atractivo/${atractivo.slug}`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.7
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateTiposViajeSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    this.masterData.tiposViaje.forEach(tipo => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/viajes/${tipo.slug}`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.6
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateAmenidadesSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    this.masterData.amenidades.forEach(amenidad => {
      sitemap += this.generateSitemapEntry(
        `${this.baseUrl}/alojamiento/${amenidad.slug}`,
        new Date().toISOString().split('T')[0],
        'weekly',
        0.5
      );
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateCombinacionesSitemap() {
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">`;

    // Generar sitemap para combinaciones pSEO masivas
    // Limitar a 50,000 URLs por sitemap (límite de Google)
    let counter = 0;
    const maxUrls = 50000;

    this.masterData.combinacionesGeneradas.forEach(combinacion => {
      if (counter < maxUrls) {
        sitemap += this.generateSitemapEntry(
          `${this.baseUrl}/${combinacion.slug}.html`,
          new Date().toISOString().split('T')[0],
          'weekly',
          0.6
        );
        counter++;
      }
    });

    sitemap += `
</urlset>`;

    return sitemap;
  }

  generateSitemapIndex() {
    let index = `<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <sitemap>
        <loc>${this.baseUrl}/sitemap-main.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>
    <sitemap>
        <loc>${this.baseUrl}/sitemap-municipios.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>
    <sitemap>
        <loc>${this.baseUrl}/sitemap-alojamientos.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>
    <sitemap>
        <loc>${this.baseUrl}/sitemap-atractivos.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>
    <sitemap>
        <loc>${this.baseUrl}/sitemap-tipos-viaje.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>
    <sitemap>
        <loc>${this.baseUrl}/sitemap-amenidades.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>`;

    // Agregar sitemap de combinaciones si hay combinaciones generadas
    if (this.masterData.combinacionesGeneradas.length > 0) {
      index += `
    <sitemap>
        <loc>${this.baseUrl}/sitemap-combinaciones.xml</loc>
        <lastmod>${new Date().toISOString().split('T')[0]}</lastmod>
    </sitemap>`;
    }

    index += `
</sitemapindex>`;

    return index;
  }

  generateRobotsTxt() {
    let robots = `# Quindío Travel Robots.txt
# Optimizado para SEO técnico y crawlers

User-agent: *
Allow: /

# Sitemaps
Sitemap: ${this.baseUrl}/sitemap.xml
Sitemap: ${this.baseUrl}/sitemap-main.xml
Sitemap: ${this.baseUrl}/sitemap-municipios.xml
Sitemap: ${this.baseUrl}/sitemap-alojamientos.xml
Sitemap: ${this.baseUrl}/sitemap-atractivos.xml
Sitemap: ${this.baseUrl}/sitemap-tipos-viaje.xml
Sitemap: ${this.baseUrl}/sitemap-amenidades.xml`;

    if (this.masterData.combinacionesGeneradas.length > 0) {
      robots += `
Sitemap: ${this.baseUrl}/sitemap-combinaciones.xml`;
    }

    robots += `

# Disallow directories específicos
Disallow: /admin/
Disallow: /private/
Disallow: /temp/
Disallow: /generated-pages/
Disallow: /pseo-engine/
Disallow: /node_modules/
Disallow: /.git/

# Crawl-delay para no sobrecargar el servidor
Crawl-delay: 1

# Optimización para Googlebot
User-agent: Googlebot
Allow: /

# Optimización para Bingbot
User-agent: Bingbot
Allow: /

# Optimización para crawlers de imágenes
User-agent: Googlebot-Image
Allow: /assets/images/

User-agent: Bingbot-Image
Allow: /assets/images/`;

    return robots;
  }

  generateCanonicalUrls() {
    const canonicalData = {
      baseUrl: this.baseUrl,
      canonicalUrls: {}
    };

    // Generar URLs canónicas para páginas principales
    canonicalData.canonicalUrls.main = {
      home: `${this.baseUrl}/`,
      planes: `${this.baseUrl}/planes.html`,
      blog: `${this.baseUrl}/blog-mejor-epoca-eje-cafetero.html`
    };

    // Generar URLs canónicas para municipios
    canonicalData.canonicalUrls.municipios = {};
    this.masterData.municipios.forEach(municipio => {
      canonicalData.canonicalUrls.municipios[municipio.id] = `${this.baseUrl}/${municipio.slug}`;
    });

    // Generar URLs canónicas para alojamientos
    canonicalData.canonicalUrls.alojamientos = {};
    this.masterData.alojamientos.forEach(alojamiento => {
      canonicalData.canonicalUrls.alojamientos[alojamiento.id] = `${this.baseUrl}/alojamiento/${alojamiento.slug}`;
    });

    // Generar URLs canónicas para atractivos
    canonicalData.canonicalUrls.atractivos = {};
    this.masterData.atractivos.forEach(atractivo => {
      canonicalData.canonicalUrls.atractivos[atractivo.id] = `${this.baseUrl}/atractivo/${atractivo.slug}`;
    });

    return canonicalData;
  }

  saveSitemaps() {
    this.ensureSitemapsDirectory();

    // Guardar sitemap principal
    const mainSitemap = this.generateMainSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-main.xml'), mainSitemap, 'utf8');

    // Guardar sitemap de municipios
    const municipiosSitemap = this.generateMunicipiosSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-municipios.xml'), municipiosSitemap, 'utf8');

    // Guardar sitemap de alojamientos
    const alojamientosSitemap = this.generateAlojamientosSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-alojamientos.xml'), alojamientosSitemap, 'utf8');

    // Guardar sitemap de atractivos
    const atractivosSitemap = this.generateAtractivosSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-atractivos.xml'), atractivosSitemap, 'utf8');

    // Guardar sitemap de tipos de viaje
    const tiposViajeSitemap = this.generateTiposViajeSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-tipos-viaje.xml'), tiposViajeSitemap, 'utf8');

    // Guardar sitemap de amenidades
    const amenidadesSitemap = this.generateAmenidadesSitemap();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-amenidades.xml'), amenidadesSitemap, 'utf8');

    // Guardar sitemap de combinaciones si existen
    if (this.masterData.combinacionesGeneradas.length > 0) {
      const combinacionesSitemap = this.generateCombinacionesSitemap();
      fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap-combinaciones.xml'), combinacionesSitemap, 'utf8');
    }

    // Guardar sitemap index
    const sitemapIndex = this.generateSitemapIndex();
    fs.writeFileSync(path.join(this.sitemapsDir, 'sitemap.xml'), sitemapIndex, 'utf8');

    // Guardar robots.txt
    const robotsTxt = this.generateRobotsTxt();
    fs.writeFileSync(path.join(__dirname, '../robots.txt'), robotsTxt, 'utf8');

    // Guardar datos de URLs canónicas
    const canonicalUrls = this.generateCanonicalUrls();
    fs.writeFileSync(path.join(this.sitemapsDir, 'canonical-urls.json'), JSON.stringify(canonicalUrls, null, 2), 'utf8');

    console.log('✅ Sitemaps generados exitosamente');
    console.log('📁 Directorio de sitemaps:', this.sitemapsDir);
    console.log('📄 Sitemaps creados:');
    console.log('   - sitemap.xml (index)');
    console.log('   - sitemap-main.xml');
    console.log('   - sitemap-municipios.xml');
    console.log('   - sitemap-alojamientos.xml');
    console.log('   - sitemap-atractivos.xml');
    console.log('   - sitemap-tipos-viaje.xml');
    console.log('   - sitemap-amenidades.xml');
    
    if (this.masterData.combinacionesGeneradas.length > 0) {
      console.log('   - sitemap-combinaciones.xml');
    }
    
    console.log('   - robots.txt (actualizado)');
    console.log('   - canonical-urls.json');
  }

  run() {
    console.log('🚀 Iniciando generación de sitemaps...');
    this.saveSitemaps();
    console.log('✅ Generación de sitemaps completada');
  }
}

// Ejecutar si se llama directamente
if (require.main === module) {
  const generator = new SitemapGenerator();
  generator.run();
}

module.exports = SitemapGenerator;