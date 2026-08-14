// Base de datos oficial de 6 planes turísticos - Quindío Travel (RNT 18152)
const planesData = [
  {
    id: "plan-1",
    slug: "plan-vive-eje-cafetero-tematico",
    titulo: "Escapada Cafetera de Fin de Semana",
    duracion: "2d",
    noches: 1,
    dias: 2,
    categoria: "Escapada",
    badge: "Escapada Rápida",
    detalleUrl: "plan-1.html",
    descripcion: "2 días / 1 noche de alojamiento en finca hotel, desayuno y cena incluidos, Pasaporte Múltiple al Parque del Café y Pasaporte Terra a PANACA. Transporte desde el aeropuerto o terminal terrestre en Armenia. Ideal para fin de semana corto.",
    resumenPrograma: [
      "Día 1: Llegada a Armenia, check-in, tarde en PANACA",
      "Día 2: Parque del Café completo con pasaporte múltiple, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA"],
    alojamientosAsociados: ["hotel-campestre-la-tata", "de-la-vega-hotel-campestre", "finca-hotel-dorada"],
    precioSinTransporte: 425000,
    precioConTransporte: 796000,
    preciosOcupacion: {
      doble: 796000,
      triple: 668000,
      cuadruple: 602000
    },
    preciosNinos: {
      ninos_2_10: 596000
    }
  },
  {
    id: "plan-2",
    slug: "plan-naturaleza-y-diversion-cafetera",
    titulo: "Aventura Natural en el Eje Cafetero",
    duracion: "3d",
    noches: 2,
    dias: 3,
    categoria: "Económico",
    badge: "Más Popular",
    detalleUrl: "plan-2.html",
    descripcion: "3 días / 2 noches de alojamiento en finca hotel tradicional, desayunos y cenas incluidos, acceso a PANACA con Pasaporte Terra y Parque del Café con Pasaporte Múltiple. Transporte desde el aeropuerto o terminal terrestre en Armenia.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, tarde en finca hotel",
      "Día 2: PANACA con Pasaporte Terra completo",
      "Día 3: Parque del Café con Pasaporte Múltiple, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Pueblo Tapao"],
    alojamientosAsociados: ["cabanas-la-esmeralda", "hotel-campestre-la-tata"],
    precioSinTransporte: 562000,
    precioConTransporte: 935000,
    preciosOcupacion: {
      doble: 935000,
      triple: 805000,
      cuadruple: 735000
    },
    preciosNinos: {
      ninos_2_10: 729000
    }
  },
  {
    id: "plan-3",
    slug: "plan-experiencia-completa-eje",
    titulo: "Experiencia Completa del Eje Cafetero",
    duracion: "4d",
    noches: 3,
    dias: 4,
    categoria: "Estándar",
    badge: "Experiencia Completa",
    detalleUrl: "plan-3.html",
    descripcion: "4 días / 3 noches de alojamiento, desayunos y cenas incluidos, Valle de Cocora, Salento, Filandia, PANACA y Parque del Café. Transporte desde el aeropuerto o terminal terrestre en Armenia. El programa favorito para conocer lo esencial del Quindío.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, tarde en finca hotel",
      "Día 2: Valle de Cocora, Salento y Filandia",
      "Día 3: PANACA con Pasaporte Terra",
      "Día 4: Parque del Café con Pasaporte Múltiple, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Salento", "Valle de Cocora", "Filandia", "RECUCA"],
    alojamientosAsociados: ["finca-hotel-los-girasoles", "cabanas-la-esmeralda", "finca-hotel-dorada"],
    precioSinTransporte: 777000,
    precioConTransporte: 1385000,
    preciosOcupacion: {
      doble: 1385000,
      triple: 1170000,
      cuadruple: 1050000
    },
    preciosNinos: {
      ninos_2_10: 1038000
    }
  },
  {
    id: "plan-4",
    slug: "plan-aventura-y-relax-termal",
    titulo: "Relax y Aventura en Termales del Eje",
    duracion: "4d",
    noches: 3,
    dias: 4,
    categoria: "Estándar Plus",
    badge: "Termales Incluidos",
    detalleUrl: "plan-4.html",
    descripcion: "4 días / 3 noches de alojamiento, desayunos y cenas incluidos, Balneario Santa Rosa de Cabal, Parque del Café y PANACA. Transporte desde el aeropuerto o terminal terrestre en Armenia. Ideal para familias y parejas.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, tarde en finca hotel",
      "Día 2: Balneario Santa Rosa de Cabal completo",
      "Día 3: Parque del Café con Pasaporte Múltiple",
      "Día 4: PANACA con Pasaporte Terra, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Termales Santa Rosa"],
    alojamientosAsociados: ["finca-hotel-los-girasoles", "hotel-campestre-cafe-cafe"],
    precioSinTransporte: 798000,
    precioConTransporte: 1495000,
    preciosOcupacion: {
      doble: 1495000,
      triple: 1250000,
      cuadruple: 1125000
    },
    preciosNinos: {
      ninos_2_10: 1110000
    }
  },
  {
    id: "plan-5",
    slug: "plan-tradicion-y-raices-arrieria",
    titulo: "Experiencia Premium del Eje Cafetero",
    duracion: "4d",
    noches: 3,
    dias: 4,
    categoria: "Cultural",
    badge: "Vivencial Cultural",
    detalleUrl: "plan-5.html",
    descripcion: "4 días / 3 noches de alojamiento, desayunos y cenas incluidos, Parque Los Arrieros, PANACA y Parque del Café. Transporte desde el aeropuerto o terminal terrestre en Armenia.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, tarde en finca hotel",
      "Día 2: Parque Los Arrieros",
      "Día 3: PANACA con Pasaporte Terra",
      "Día 4: Parque del Café con Pasaporte Múltiple, regreso"
    ],
    atractivosIncluidos: ["Parque Los Arrieros", "PANACA", "Parque del Café"],
    alojamientosAsociados: ["cabanas-la-esmeralda", "finca-hotel-los-girasoles"],
    precioSinTransporte: 788000,
    precioConTransporte: 1297000,
    preciosOcupacion: {
      doble: 1297000,
      triple: 1120000,
      cuadruple: 1020000
    },
    preciosIntermedio: {
      doble: 1360000,
      triple: 1170000,
      cuadruple: 1060000
    },
    preciosNinos: {
      ninos_2_10: 998000
    }
  },
  {
    id: "plan-6",
    slug: "plan-gran-quindio-integral",
    titulo: "La Experiencia Definitiva del Eje Cafetero",
    duracion: "5d",
    noches: 4,
    dias: 5,
    categoria: "Premium",
    badge: "Todo Incluido VIP",
    detalleUrl: "plan-6.html",
    descripcion: "La experiencia definitiva de 5 días y 4 noches. PANACA, Balneario Santa Rosa de Cabal, Parque del Café y RECUCA. Transporte desde el aeropuerto o terminal terrestre en Armenia.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, tarde en finca hotel",
      "Día 2: PANACA con Pasaporte Terra",
      "Día 3: Balneario Santa Rosa de Cabal completo",
      "Día 4: Parque del Café con Pasaporte Múltiple",
      "Día 5: RECUCA, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Termales Santa Rosa", "RECUCA"],
    alojamientosAsociados: ["hotel-campestre-cafe-cafe", "hotel-campestre-las-camelias", "finca-hotel-los-girasoles"],
    precioSinTransporte: 1008000,
    precioConTransporte: 1800000,
    preciosOcupacion: {
      doble: 1800000,
      triple: 1520000,
      cuadruple: 1380000
    },
    preciosIntermedio: {
      doble: 1880000,
      triple: 1580000,
      cuadruple: 1430000
    },
    preciosNinos: {
      ninos_2_10: 1360000
    }
  }
];

// Base de datos de alojamientos aliados importados desde docs/data/alojamientos
const alojamientosData = [
  {
    id: "cabanas-la-esmeralda",
    nombre: "Cabañas La Esmeralda",
    categoria: "Intermedia",
    ubicacion: "Quindío, Colombia",
    servicios: ["Piscina Adultos y Niños", "Jacuzzy", "Cancha de Microfútbol", "Cancha de Volley Playa", "Restaurante", "Bar", "Zona de Asados", "Amplias Zonas Verdes", "Kiosco", "Juegos de Mesa"]
  },
  {
    id: "de-la-vega-hotel-campestre",
    nombre: "De La Vega Hotel Campestre",
    categoria: "Estándar",
    ubicacion: "A 200 mts del Parque del Café, Montenegro, Quindío",
    servicios: ["Zonas húmedas (Piscina, 3 jacuzzi)", "Zona de juegos (billar pool, rana, pin pon)", "Parque infantil", "Parqueadero"]
  },
  {
    id: "finca-hotel-dorada",
    nombre: "Finca Hotel Dorada",
    categoria: "Estándar",
    ubicacion: "Km. 5 Pueblo Tapao Vía a La Tebaida, Quindío",
    servicios: ["Piscina niños y adultos", "Juegos infantiles", "Parqueadero", "Restaurante", "Lavandería", "Hamacas", "Juegos de mesa"]
  },
  {
    id: "finca-hotel-los-girasoles",
    nombre: "Finca Hotel Los Girasoles",
    categoria: "Intermedia VIP",
    ubicacion: "Quindío, Colombia",
    servicios: ["Recepción 24h", "Zona de juegos ping pong, juegos de mesa", "Piscina", "Jacuzzi", "Cancha de micro fútbol en césped", "Voleibol grama", "Parque infantil", "WiFi en recepción", "DIRECTV salón", "Oratorio", "Amplios jardines"]
  },
  {
    id: "hotel-campestre-cafe-cafe",
    nombre: "Hotel Campestre Café Café",
    categoria: "Intermedia VIP",
    ubicacion: "Quindío, Colombia",
    servicios: ["Wifi", "Televisión satelital", "Baño privado", "Mini bar", "Agua caliente", "Amplio parqueadero", "Juegos de mesa, billar", "Cancha de voleibol", "Ping pong, sapo"]
  },
  {
    id: "hotel-campestre-la-tata",
    nombre: "Hotel Campestre La Tata",
    categoria: "Estándar",
    ubicacion: "A 100 mts de Parque del Café, Quindío",
    servicios: ["Piscina niños y adultos", "Jacuzzi", "Juegos infantiles", "Parqueadero", "Restaurante", "Lavandería", "Juegos de mesa"]
  },
  {
    id: "hotel-campestre-las-camelias",
    nombre: "Hotel Campestre Las Camelias",
    categoria: "VIP",
    ubicacion: "Quindío, Colombia",
    servicios: ["Capilla", "Tienda de regalos", "Sauna", "Turco", "5 piscinas", "Parque Acualandia", "Canchas de fútbol, voleibol, baloncesto", "Tenis recreativa", "Pista de karts", "Billar, billar pool", "Golfito", "Sendero ecológico", "Parque infantil"]
  }
];

// Helper: parseo de query params para filtros
function obtenerParametroURL(nombre) {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get(nombre);
}

// Función para renderizar los planes dinámicamente en el DOM
function renderizarPlanes(filtroDuracion = "all", filtroAtractivo = "all", contenedorId = "catalogo-planes") {
  const contenedor = document.getElementById(contenedorId);
  if (!contenedor) return;

  contenedor.innerHTML = "";

  let planesFiltrados = planesData;

  if (filtroDuracion !== "all") {
    planesFiltrados = planesFiltrados.filter(plan => plan.duracion === filtroDuracion);
  }

  if (filtroAtractivo !== "all") {
    planesFiltrados = planesFiltrados.filter(plan =>
      plan.atractivosIncluidos.some(a =>
        a.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").includes(
          filtroAtractivo.toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "")
        )
      )
    );
  }

  if (planesFiltrados.length === 0) {
    contenedor.innerHTML = `
      <div class="no-results-enhanced">
        <div class="no-results-icon">
          <i class="fas fa-search"></i>
        </div>
        <h3>No hay planes para este filtro</h3>
        <p>Prueba combinando otra duración u otro destino turístico.</p>
        <button onclick="renderizarPlanes('all', 'all')" class="btn-reset-enhanced-inline">
          <i class="fas fa-redo"></i> Ver todos los planes
        </button>
      </div>
    `;
    return;
  }

  planesFiltrados.forEach(plan => {
    // Obtener foto del primer alojamiento asociado
    const primerAlojamiento = plan.alojamientosAsociados[0];
    const fotosAlojamiento = {
      "hotel-campestre-la-tata": "assets/images/alojamientos/hotel-campestre-la-tata/finca-hotel-la-tata.jpg",
      "de-la-vega-hotel-campestre": "assets/images/alojamientos/hotel-de-la-vega/hotel-campestre-de-la-vega-3.webp",
      "finca-hotel-dorada": "assets/images/alojamientos/finca-hotel-la-dorada/1414317914.webp",
      "cabanas-la-esmeralda": "assets/images/alojamientos/finca-hotel-la-esmeralda/finca-hotel-cabanas-la.jpg",
      "finca-hotel-los-girasoles": "assets/images/alojamientos/finca-hotel-los-girasoles/Finca-los-Girasoles-7.jpg",
      "hotel-campestre-cafe-cafe": "assets/images/alojamientos/hotel-campestre-cafe-cafe/406282624.jpg",
      "hotel-campestre-las-camelias": "assets/images/alojamientos/hotel-las-camelias.jpg"
    };
    
    const fotoAlojamiento = fotosAlojamiento[primerAlojamiento] || "assets/images/alojamientos/cafetal.jpg";
    
    const card = document.createElement("div");
    card.className = "plan-card-enhanced";
    card.innerHTML = `
      <div class="plan-card-image-enhanced">
        <img src="${fotoAlojamiento}" alt="${plan.titulo}">
        <div class="plan-badge-overlay">
          <div class="plan-badge-enhanced">${plan.badge}</div>
        </div>
      </div>
      
      <div class="plan-card-header-enhanced">
        <div class="plan-duration-enhanced">
          <i class="fas fa-clock"></i>
          <span>${plan.dias}D/${plan.noches}N</span>
        </div>
      </div>
      
      <div class="plan-card-body-enhanced">
        <h3 class="plan-title-enhanced">${plan.titulo}</h3>
        <p class="plan-description-enhanced">${plan.descripcion}</p>
        
        <div class="plan-features-enhanced">
          <div class="feature-item-enhanced">
            <i class="fas fa-map-marker-alt"></i>
            <span>${plan.atractivosIncluidos.length} destinos</span>
          </div>
          <div class="feature-item-enhanced">
            <i class="fas fa-utensils"></i>
            <span>Alimentación incluida</span>
          </div>
          <div class="feature-item-enhanced">
            <i class="fas fa-shield-alt"></i>
            <span>Asistencia médica</span>
          </div>
        </div>
        
        <div class="plan-destinations-enhanced">
          ${plan.atractivosIncluidos.map(a => `<span class="destination-tag-enhanced">${a}</span>`).join("")}
        </div>
        
        <div class="plan-programa-enhanced">
          <h4><i class="fas fa-list-ol"></i> Itinerario</h4>
          <ul>
            ${plan.resumenPrograma.map(dia => `<li>${dia}</li>`).join("")}
          </ul>
        </div>
        
        <div class="plan-pricing-enhanced">
          <div class="price-item-enhanced">
            <span class="price-label-enhanced">Sin transporte</span>
            <span class="price-value-enhanced">$${plan.precioSinTransporte.toLocaleString('es-CO')}</span>
          </div>
          <div class="price-item-enhanced featured">
            <span class="price-label-enhanced">Con transporte</span>
            <span class="price-value-enhanced">$${plan.precioConTransporte.toLocaleString('es-CO')}</span>
          </div>
        </div>
      </div>
      
      <div class="plan-card-footer-enhanced">
        <a href="${plan.detalleUrl}" class="btn-plan-enhanced btn-outline-plan">
          <i class="fas fa-file-alt"></i>
          <span>Ver detalles</span>
        </a>
        <a href="https://wa.me/573174426044?text=${encodeURIComponent('Hola Quindío Travel 🌿, deseo cotizar el ' + plan.titulo + ' para ' + (obtenerParametroURL('personas') || 2) + ' personas. Fecha aproximada: ' + (obtenerParametroURL('fecha') || 'Por confirmar') + '. ¿Podrían ayudarme con la disponibilidad?')}" class="btn-plan-enhanced btn-whatsapp-plan" target="_blank" rel="noopener">
          <i class="fab fa-whatsapp"></i>
          <span>Cotizar ahora</span>
        </a>
      </div>
    `;
    contenedor.appendChild(card);
  });
}

// Inicializar renderizado al cargar la página
document.addEventListener("DOMContentLoaded", () => {
  const filtroInicialDuracion = obtenerParametroURL("duracion") || "all";
  const filtroInicialAtractivo = obtenerParametroURL("destino") || "all";

  renderizarPlanes(filtroInicialDuracion, filtroInicialAtractivo);

  const pillsDuracion = document.querySelectorAll(".filter-pills-enhanced.duracion .pill-enhanced");
  pillsDuracion.forEach(pill => {
    pill.addEventListener("click", () => {
      pillsDuracion.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      const filtro = pill.getAttribute("data-filter");
      const filtroActivoAtractivo = document.querySelector(".filter-pills-enhanced.atractivos .pill-enhanced.active")?.getAttribute("data-filter") || "all";
      renderizarPlanes(filtro, filtroActivoAtractivo);
    });
    if (pill.getAttribute("data-filter") === filtroInicialDuracion) {
      pill.classList.add("active");
    }
  });

  const pillsAtractivos = document.querySelectorAll(".filter-pills-enhanced.atractivos .pill-enhanced");
  pillsAtractivos.forEach(pill => {
    pill.addEventListener("click", () => {
      const estabaActivo = pill.classList.contains("active");
      pillsAtractivos.forEach(p => p.classList.remove("active"));
      if (!estabaActivo) pill.classList.add("active");
      const filtro = estabaActivo ? "all" : pill.getAttribute("data-filter");
      const filtroActivoDuracion = document.querySelector(".filter-pills-enhanced.duracion .pill-enhanced.active")?.getAttribute("data-filter") || "all";
      renderizarPlanes(filtroActivoDuracion, filtro);
    });
    if (pill.getAttribute("data-filter") === filtroInicialAtractivo && filtroInicialAtractivo !== "all") {
      pill.classList.add("active");
    }
  });

  const selectTodos = document.getElementById("select-todos");
  if (selectTodos) {
    selectTodos.addEventListener("click", () => {
      pillsDuracion.forEach(p => p.classList.remove("active"));
      pillsAtractivos.forEach(p => p.classList.remove("active"));
      const pillTodos = document.querySelector('.filter-pills-enhanced.duracion .pill-enhanced[data-filter="all"]');
      if (pillTodos) pillTodos.classList.add("active");
      renderizarPlanes("all", "all");
    });
  }
});
