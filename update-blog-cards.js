const fs = require('fs');

const content = fs.readFileSync('index.html', 'utf8');

const oldBlogGrid = `<div class="blog-grid">
                <article class="blog-card">
                    <div class="blog-img" style="background-image: url('assets/images/hero/valle-del-cocora-placeholder.svg');"></div>
                    <div class="blog-body">
                        <p class="blog-date"><i class="far fa-calendar"></i> Marzo 2026 · <i class="fas fa-bookmark"></i> Guías</p>
                        <h3>Los mejores hoteles del Quindío: guía completa 2026</h3>
                        <p class="blog-excerpt">Fincas hotel, cabañas y alojamientos VIP en Salento, Filandia y Armenia. Comparativa de precios, servicios y categorías...</p>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-img" style="background: linear-gradient(135deg, var(--verde-cafe), var(--marron-madera));"></div>
                    <div class="blog-body">
                        <p class="blog-date"><i class="far fa-calendar"></i> Febrero 2026 · <i class="fas fa-bookmark"></i> Destinos</p>
                        <h3>Qué hacer en Salento: 5 lugares imperdibles</h3>
                        <p class="blog-excerpt">Descubre los mejores lugares para visitar en Salento: miradores, cafeterías, arquitectura tradicional y experiencias auténticas...</p>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-img" style="background: linear-gradient(135deg, var(--marron-madera), var(--verde-claro));"></div>
                    <div class="blog-body">
                        <p class="blog-date"><i class="far fa-calendar"></i> Diciembre 2025 · <i class="fas fa-bookmark"></i> Familiares</p>
                        <h3>Qué hacer con niños en el Eje Cafetero: planes familiares 2026</h3>
                        <p class="blog-excerpt">PANACA, Parque del Café, fincas hotel con zonas infantiles, actividades seguras y consejos para viajar con niños pequeños...</p>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-img" style="background: linear-gradient(135deg, var(--verde-cafe), var(--gris-claro));"></div>
                    <div class="blog-body">
                        <p class="blog-date"><i class="far fa-calendar"></i> Noviembre 2025 · <i class="fas fa-bookmark"></i> Transporte</p>
                        <h3>Cómo llegar al Quindío: guía de transporte desde Bogotá, Medellín y Cali</h3>
                        <p class="blog-excerpt">Avianca, buses, rutas terrestres, transporte desde el aeropuerto El Edén y terminal de transportes de Armenia...</p>
                    </div>
                </article>
                <article class="blog-card">
                    <div class="blog-img" style="background: linear-gradient(135deg, var(--verde-claro), var(--amarillo-suave));"></div>
                    <div class="blog-body">
                        <p class="blog-date"><i class="far fa-calendar"></i> Octubre 2025 · <i class="fas fa-bookmark"></i> Clima</p>
                        <h3>Clima del Quindío: qué esperar y mejores épocas para visitar</h3>
                        <p class="blog-excerpt">Temperatura ideal, temporadas secas y lluviosas, qué ropa empacar y cuándo disfrutar de mejor clima en cada mes del año...</p>
                    </div>
                </article>
            </div>`;

const newBlogGrid = `<div class="blog-grid">
                <a href="blog/hoteles-economicos-salento-familias-2026.html" class="blog-card-link">
                    <article class="blog-card">
                        <div class="blog-img" style="background-image: url('assets/images/paisajes/valle-cocoro-hero-banner.jpg');"></div>
                        <div class="blog-body">
                            <p class="blog-date"><i class="far fa-calendar"></i> Marzo 2026 · <i class="fas fa-bookmark"></i> Guías</p>
                            <h3>Los mejores hoteles del Quindío: guía completa 2026</h3>
                            <p class="blog-excerpt">Fincas hotel, cabañas y alojamientos VIP en Salento, Filandia y Armenia. Comparativa de precios, servicios y categorías...</p>
                        </div>
                    </article>
                </a>
                <a href="blog/guia-compras-salento-2026.html" class="blog-card-link">
                    <article class="blog-card">
                        <div class="blog-img" style="background-image: url('assets/images/paisajes/salento-town.jpg');"></div>
                        <div class="blog-body">
                            <p class="blog-date"><i class="far fa-calendar"></i> Febrero 2026 · <i class="fas fa-bookmark"></i> Destinos</p>
                            <h3>Qué hacer en Salento: 5 lugares imperdibles</h3>
                            <p class="blog-excerpt">Descubre los mejores lugares para visitar en Salento: miradores, cafeterías, arquitectura tradicional y experiencias auténticas...</p>
                        </div>
                    </article>
                </a>
                <a href="blog/turismo-familiar-ninos-2026.html" class="blog-card-link">
                    <article class="blog-card">
                        <div class="blog-img" style="background-image: url('assets/images/destinos/logo_panaca.png');"></div>
                        <div class="blog-body">
                            <p class="blog-date"><i class="far fa-calendar"></i> Diciembre 2025 · <i class="fas fa-bookmark"></i> Familiares</p>
                            <h3>Qué hacer con niños en el Eje Cafetero: planes familiares 2026</h3>
                            <p class="blog-excerpt">PANACA, Parque del Café, fincas hotel con zonas infantiles, actividades seguras y consejos para viajar con niños pequeños...</p>
                        </div>
                    </article>
                </a>
                <a href="blog/guia-transporte-eje-cafetero-bogota-2026.html" class="blog-card-link">
                    <article class="blog-card">
                        <div class="blog-img" style="background-image: url('assets/images/paisajes/eje-cafetero-sunset-hills.jpg');"></div>
                        <div class="blog-body">
                            <p class="blog-date"><i class="far fa-calendar"></i> Noviembre 2025 · <i class="fas fa-bookmark"></i> Transporte</p>
                            <h3>Cómo llegar al Quindío: guía de transporte desde Bogotá, Medellín y Cali</h3>
                            <p class="blog-excerpt">Avianca, buses, rutas terrestres, transporte desde el aeropuerto El Edén y terminal de transportes de Armenia...</p>
                        </div>
                    </article>
                </a>
                <a href="blog/mejor-epoca-visitar-quindio-2026.html" class="blog-card-link">
                    <article class="blog-card">
                        <div class="blog-img" style="background-image: url('assets/images/paisajes/coffee-plantation-green.jpg');"></div>
                        <div class="blog-body">
                            <p class="blog-date"><i class="far fa-calendar"></i> Octubre 2025 · <i class="fas fa-bookmark"></i> Clima</p>
                            <h3>Clima del Quindío: qué esperar y mejores épocas para visitar</h3>
                            <p class="blog-excerpt">Temperatura ideal, temporadas secas y lluviosas, qué ropa empacar y cuándo disfrutar de mejor clima en cada mes del año...</p>
                        </div>
                    </article>
                </a>
            </div>`;

const newContent = content.replace(oldBlogGrid, newBlogGrid);
fs.writeFileSync('index.html', newContent);

console.log('Blog cards updated successfully');