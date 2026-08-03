/**
 * Quindío Travel pSEO Engine
 * Generador automático de páginas de aterrizaje para Programmatic SEO
 * Genera combinaciones de municipios, tipos de viaje y amenidades
 */

const fs = require('fs');
const path = require('path');

class PSEOGenerator {
  constructor() {
    this.masterData = this.loadMasterData();
    this.generatedPages = [];
    this.combinaciones = [];
  }

  loadMasterData() {
    const dataPath = path.join(__dirname, 'pseo-master-data.json');
    const rawData = fs.readFileSync(dataPath, 'utf8');
    return JSON.parse(rawData);
  }

  generateAllCombinations() {
    const { municipios, tiposViaje, amenidades, alojamientos, atractivos } = this.masterData;
    
    // Generar combinaciones de municipio + tipo de viaje
    municipios.forEach(municipio => {
      tiposViaje.forEach(tipo => {
        this.combinaciones.push({
          tipo: 'municipio-tipo',
          municipio: municipio,
          tipoViaje: tipo,
          slug: `${municipio.slug}/${tipo.slug}`,
          title: `${tipo.nombre} en ${municipio.nombre} - Quindío Travel`,
          description: `Descubre los mejores ${tipo.nombre.toLowerCase()} en ${municipio.nombre}, Quindío. Planes turísticos completos con alojamiento, transporte y guías certificados. RNT 18152.`,
          keywords: [...municipio.keywords, ...tipo.keywords, `${tipo.nombre.toLowerCase()} ${municipio.nombre.toLowerCase()}`]
        });
      });
    });

    // Generar combinaciones de municipio + amenidad
    municipios.forEach(municipio => {
      amenidades.forEach(amenidad => {
        this.combinaciones.push({
          tipo: 'municipio-amenidad',
          municipio: municipio,
          amenidad: amenidad,
          slug: `${municipio.slug}/alojamiento-${amenidad.slug}`,
          title: `Alojamiento ${amenidad.nombre} en ${municipio.nombre} - Quindío Travel`,
          description: `Encuentra alojamientos ${amenidad.nombre.toLowerCase()} en ${municipio.nombre}, Quindío. Las mejores fincas y hoteles con ${amenidad.nombre.toLowerCase()}. Reserva ahora con RNT 18152.`,
          keywords: [...municipio.keywords, ...amenidad.keywords, `alojamiento ${amenidad.nombre.toLowerCase()} ${municipio.nombre.toLowerCase()}`]
        });
      });
    });

    // Generar combinaciones de tipo de viaje + amenidad
    tiposViaje.forEach(tipo => {
      amenidades.forEach(amenidad => {
        this.combinaciones.push({
          tipo: 'tipo-amenidad',
          tipoViaje: tipo,
          amenidad: amenidad,
          slug: `viajes/${tipo.slug}/${amenidad.slug}`,
          title: `${tipo.nombre} ${amenidad.nombre} - Quindío Travel`,
          description: `Planifica ${tipo.nombre.toLowerCase()} con ${amenidad.nombre.toLowerCase()} en el Eje Cafetero. Los mejores alojamientos y experiencias. RNT 18152.`,
          keywords: [...tipo.keywords, ...amenidad.keywords, `${tipo.nombre.toLowerCase()} ${amenidad.nombre.toLowerCase()}`]
        });
      });
    });

    // Generar combinaciones tríadas (municipio + tipo + amenidad) - Alta conversión
    municipios.forEach(municipio => {
      tiposViaje.forEach(tipo => {
        amenidades.forEach(amenidad => {
          this.combinaciones.push({
            tipo: 'triple-combination',
            municipio: municipio,
            tipoViaje: tipo,
            amenidad: amenidad,
            slug: `${municipio.slug}/${tipo.slug}/${amenidad.slug}`,
            title: `${tipo.nombre} ${amenidad.nombre} en ${municipio.nombre} - Quindío Travel`,
            description: `Experiencias de ${tipo.nombre.toLowerCase()} con ${amenidad.nombre.toLowerCase()} en ${municipio.nombre}, Quindío. Planes completos con alojamiento y transporte. RNT 18152.`,
            keywords: [
              ...municipio.keywords, 
              ...tipo.keywords, 
              ...amenidad.keywords,
              `${tipo.nombre.toLowerCase()} ${amenidad.nombre.toLowerCase()} ${municipio.nombre.toLowerCase()}`,
              `${amenidad.nombre.toLowerCase()} ${municipio.nombre.toLowerCase()} ${tipo.nombre.toLowerCase()}`
            ]
          });
        });
      });
    });

    // Generar páginas individuales para alojamientos
    alojamientos.forEach(alojamiento => {
      const municipio = municipios.find(m => m.id === alojamiento.municipio);
      this.combinaciones.push({
        tipo: 'alojamiento',
        alojamiento: alojamiento,
        municipio: municipio,
        slug: `alojamiento/${alojamiento.slug}`,
        title: `${alojamiento.nombre} - ${municipio ? municipio.nombre : 'Quindío'} - Quindío Travel`,
        description: `Reserva ${alojamiento.nombre} en ${municipio ? municipio.nombre : 'Quindío'}. ${alojamiento.descripcion}. Precios desde $${alojamiento.precioDesde.toLocaleString()}. RNT 18152.`,
        keywords: [
          alojamiento.nombre.toLowerCase(),
          alojamiento.tipo.toLowerCase(),
          ...(municipio ? municipio.keywords : []),
          ...alojamiento.amenidades.map(a => a.toLowerCase())
        ]
      });
    });

    // Generar páginas individuales para atractivos
    atractivos.forEach(atractivo => {
      const municipio = municipios.find(m => m.id === atractivo.municipio);
      this.combinaciones.push({
        tipo: 'atractivo',
        atractivo: atractivo,
        municipio: municipio,
        slug: `atractivo/${atractivo.slug}`,
        title: `${atractivo.nombre} - ${municipio ? municipio.nombre : 'Quindío'} - Quindío Travel`,
        description: `Visita ${atractivo.nombre} en ${municipio ? municipio.nombre : 'Quindío'}. ${atractivo.descripcion}. Planes completos con transporte y guía. RNT 18152.`,
        keywords: [
          atractivo.nombre.toLowerCase(),
          atractivo.tipo.toLowerCase(),
          ...(municipio ? municipio.keywords : []),
          ...atractivo.keywords
        ]
      });
    });

    console.log(`Generadas ${this.combinaciones.length} combinaciones de páginas pSEO`);
    return this.combinaciones;
  }

  generateHTMLPage(combinacion) {
    const { masterData } = this;
    const urlTemplates = masterData.urlTemplates;
    
    // Crear estructura básica de la página
    let html = `<!DOCTYPE html>
<html lang="es" itemscope itemtype="https://schema.org/TravelAgency">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${combinacion.title}</title>
    <meta name="description" content="${combinacion.description}">
    <meta name="keywords" content="${combinacion.keywords.join(', ')}">
    <link rel="canonical" href="${urlTemplates.base}/${combinacion.slug}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="${combinacion.title}">
    <meta property="og:description" content="${combinacion.description}">
    <meta property="og:url" content="${urlTemplates.base}/${combinacion.slug}">
    <meta property="og:type" content="website">
    
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": "Quindío Travel",
        "description": "${combinacion.description}",
        "url": "${urlTemplates.base}/${combinacion.slug}",
        "keywords": "${combinacion.keywords.join(', ')}"
    }
    </script>
    
    <!-- CSS -->
    <link rel="stylesheet" href="/styles.css">
</head>
<body>
    <header class="main-header">
        <div class="container nav-container">
            <div class="logo">
                <a href="/" aria-label="Inicio Quindío Travel">
                    <span style="color: var(--verde-cafe); font-weight: 800; font-size: 1.8rem;">QUINDÍO</span>
                    <span style="color: var(--marron-madera); font-weight: 700; font-size: 1.2rem;">TRAVEL</span>
                </a>
            </div>
            <nav class="nav-menu" id="nav-menu" aria-label="Menú principal">
                <ul>
                    <li><a href="/">Inicio</a></li>
                    <li><a href="/planes.html">Planes</a></li>
                    <li><a href="/alojamientos">Alojamientos</a></li>
                    <li><a href="/atractivos">Atractivos</a></li>
                </ul>
            </nav>
            <div class="header-actions">
                <button class="hamburger-btn" id="hamburger-btn" aria-label="Abrir menú de navegación" aria-expanded="false" aria-controls="nav-menu">
                    <i class="fas fa-bars"></i>
                </button>
                <a href="https://wa.me/573174426044" target="_blank" rel="noopener" class="btn btn-whatsapp">
                    <i class="fab fa-whatsapp"></i> WhatsApp
                </a>
            </div>
        </div>
    </header>
    
    <main>
        <section class="hero">
            <h1>${combinacion.title}</h1>
            <p>${combinacion.description}</p>
        </section>
        
        <section class="content">
            ${this.generateContentSection(combinacion)}
        </section>
        
        <section class="cta">
            <a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20${encodeURIComponent(combinacion.title)}" 
               class="btn-whatsapp">
                Cotizar Plan Ahora
            </a>
        </section>
    </main>
    
    <footer>
        <p>Quindío Travel - RNT 18152 - Operador Turístico Certificado</p>
    </footer>
    
    <script src="/assets/js/whatsapp-payload.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function () {
            const hambBtn = document.getElementById('hamburger-btn');
            const navMenu = document.getElementById('nav-menu');
            if (!hambBtn || !navMenu) return;

            hambBtn.addEventListener('click', function () {
                const abierto = navMenu.classList.toggle('nav-menu-open');
                hambBtn.setAttribute('aria-expanded', abierto ? 'true' : 'false');
                hambBtn.innerHTML = abierto ? '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
            });

            navMenu.querySelectorAll('a').forEach(function (link) {
                link.addEventListener('click', function () {
                    if (navMenu.classList.contains('nav-menu-open')) {
                        navMenu.classList.remove('nav-menu-open');
                        hambBtn.setAttribute('aria-expanded', 'false');
                        hambBtn.innerHTML = '<i class="fas fa-bars"></i>';
                    }
                });
            });
        });
    </script>
</body>
</html>`;

    return html;
  }

  generateContentSection(combinacion) {
    let content = '';
    
    switch(combinacion.tipo) {
      case 'triple-combination':
        content = this.generateTripleCombinationContent(combinacion);
        break;
      case 'alojamiento':
        content = this.generateAlojamientoContent(combinacion);
        break;
      case 'atractivo':
        content = this.generateAtractivoContent(combinacion);
        break;
      default:
        content = this.generateGenericContent(combinacion);
    }
    
    return content;
  }

  generateTripleCombinationContent(combinacion) {
    const { municipio, tipoViaje, amenidad } = combinacion;
    const alojamientosFiltrados = this.masterData.alojamientos.filter(a => 
      a.municipio === municipio.id && a.amenidades.includes(amenidad.id)
    );
    
    return `
        <h2>${tipoViaje.nombre} ${amenidad.nombre} en ${municipio.nombre}</h2>
        <p>Descubre las mejores opciones para ${tipoViaje.nombre.toLowerCase()} con ${amenidad.nombre.toLowerCase()} en ${municipio.nombre}.</p>
        
        <h3>Alojamientos Disponibles</h3>
        <div class="alojamientos-grid">
            ${alojamientosFiltrados.map(a => `
                <div class="alojamiento-card">
                    <h4>${a.nombre}</h4>
                    <p>${a.descripcion}</p>
                    <p><strong>Precio desde:</strong> $${a.precioDesde.toLocaleString()}</p>
                    <p><strong>Capacidad:</strong> ${a.capacidad.join(', ')}</p>
                    <a href="/alojamiento/${a.slug}" class="btn-ver-mas">Ver Detalles</a>
                </div>
            `).join('')}
        </div>
        
        <h3>¿Por qué elegir ${municipio.nombre} para ${tipoViaje.nombre.toLowerCase()}?</h3>
        <p>${municipio.descripcion}. Ubicación privilegiada en el corazón del Eje Cafetero.</p>
    `;
  }

  generateAlojamientoContent(combinacion) {
    const { alojamiento, municipio } = combinacion;
    const amenidadesDetalle = alojamiento.amenidades.map(a => {
      const amenidadInfo = this.masterData.amenidades.find(am => am.id === a);
      return amenidadInfo ? amenidadInfo.nombre : a;
    });
    
    return `
        <h2>${alojamiento.nombre}</h2>
        <p><strong>Tipo:</strong> ${alojamiento.tipo}</p>
        <p><strong>Ubicación:</strong> ${municipio ? municipio.nombre : 'Quindío'}</p>
        <p><strong>Descripción:</strong> ${alojamiento.descripcion}</p>
        
        <h3>Amenidades</h3>
        <ul>
            ${amenidadesDetalle.map(a => `<li>${a}</li>`).join('')}
        </ul>
        
        <h3>Capacidad</h3>
        <p>Habitaciones: ${alojamiento.capacidad.join(', ')}</p>
        
        <h3>Precios</h3>
        <p>Desde: $${alojamiento.precioDesde.toLocaleString()} por persona</p>
        
        <h3>Calificación</h3>
        <p>⭐ ${alojamiento.rating}/5.0</p>
    `;
  }

  generateAtractivoContent(combinacion) {
    const { atractivo, municipio } = combinacion;
    
    return `
        <h2>${atractivo.nombre}</h2>
        <p><strong>Tipo:</strong> ${atractivo.tipo}</p>
        <p><strong>Ubicación:</strong> ${municipio ? municipio.nombre : 'Quindío'}</p>
        <p><strong>Descripción:</strong> ${atractivo.descripcion}</p>
        
        <h3>Información Práctica</h3>
        <p><strong>Precio:</strong> $${atractivo.precio.toLocaleString()}</p>
        <p><strong>Duración:</strong> ${atractivo.duracion}</p>
        <p><strong>Ideal para:</strong> ${atractivo.idealPara.join(', ')}</p>
        
        <h3>Palabras clave</h3>
        <p>${atractivo.keywords.join(', ')}</p>
    `;
  }

  generateGenericContent(combinacion) {
    return `
        <h2>Experiencias Turísticas en el Eje Cafetero</h2>
        <p>Explora nuestra selección de planes turísticos diseñados para brindarte la mejor experiencia en el Quindío.</p>
        
        <h3>Planes Destacados</h3>
        <div class="planes-grid">
            <div class="plan-card">
                <h4>Plan Vive Eje Cafetero</h4>
                <p>2 días / 1 noche - Parque del Café y PANACA</p>
                <a href="/plan-1.html" class="btn-ver-mas">Ver Plan</a>
            </div>
            <div class="plan-card">
                <h4>Plan Naturaleza y Diversión</h4>
                <p>3 días / 2 noches - Experiencia completa</p>
                <a href="/plan-2.html" class="btn-ver-mas">Ver Plan</a>
            </div>
        </div>
    `;
  }

  generateSitemap() {
    const { urlTemplates } = this.masterData;
    let sitemap = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>${urlTemplates.base}/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>${urlTemplates.base}/planes.html</loc>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>${urlTemplates.base}/index.html</loc>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>`;
    
    this.combinaciones.forEach(combinacion => {
      sitemap += `
    <url>
        <loc>${urlTemplates.base}/${combinacion.slug}.html</loc>
        <changefreq>weekly</changefreq>
        <priority>0.7</priority>
    </url>`;
    });
    
    sitemap += `
</urlset>`;
    
    return sitemap;
  }

  saveGeneratedPages() {
    const outputDir = path.join(__dirname, '../generated-pages');
    
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }
    
    this.combinaciones.forEach(combinacion => {
      const html = this.generateHTMLPage(combinacion);
      const filename = `${combinacion.slug}.html`;
      const filepath = path.join(outputDir, filename);
      
      // Crear subdirectorios según el tipo
      const subdirs = filename.split('/');
      if (subdirs.length > 1) {
        const dirPath = path.join(outputDir, ...subdirs.slice(0, -1));
        if (!fs.existsSync(dirPath)) {
          fs.mkdirSync(dirPath, { recursive: true });
        }
      }
      
      fs.writeFileSync(filepath, html, 'utf8');
      this.generatedPages.push(filepath);
    });
    
    // Guardar sitemap
    const sitemap = this.generateSitemap();
    fs.writeFileSync(path.join(outputDir, 'pseo-sitemap.xml'), sitemap, 'utf8');
    
    console.log(`Páginas generadas: ${this.generatedPages.length}`);
    console.log(`Sitemap generado: pseo-sitemap.xml`);
  }

  updateMasterData() {
    this.masterData.combinacionesGeneradas = this.combinaciones.map(c => ({
      slug: c.slug,
      tipo: c.tipo,
      title: c.title,
      keywords: c.keywords
    }));
    
    fs.writeFileSync(
      path.join(__dirname, 'pseo-master-data.json'),
      JSON.stringify(this.masterData, null, 2),
      'utf8'
    );
    
    console.log('Master data actualizado con combinaciones generadas');
  }

  run() {
    console.log('🚀 Iniciando generación pSEO...');
    this.generateAllCombinations();
    this.saveGeneratedPages();
    this.updateMasterData();
    console.log('✅ Generación pSEO completada');
  }
}

// Ejecutar si se llama directamente
if (require.main === module) {
  const generator = new PSEOGenerator();
  generator.run();
}

module.exports = PSEOGenerator;