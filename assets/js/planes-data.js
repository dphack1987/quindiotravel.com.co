// Base de datos oficial de 8 planes turísticos - Quindío Travel (RNT 18152)
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
    descripcion: "2 días / 1 noche de alojamiento en finca hotel, desayuno y cena incluidos, Pasaporte Múltiple al Parque del Café y Pasaporte Terra a PANACA. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia. Ideal para fin de semana corto.",
    resumenPrograma: [
      "Día 1: Llegada a Armenia, check-in, tarde en PANACA",
      "Día 2: Parque del Café completo con pasaporte múltiple, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA"],
    alojamientosAsociados: ["hotel-campestre-la-tata", "de-la-vega-hotel-campestre", "finca-hotel-dorada"],
    precioSinTransporte: 450000,
    precioConTransporte: 580000,
    preciosOcupacion: {
      doble: 520000,
      triple: 480000,
      cuadruple: 450000
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
    descripcion: "3 días / 2 noches de alojamiento en finca hotel tradicional, desayunos y cenas incluidos, acceso a los parques temáticos principales y recorrido por pueblos tradicionales. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, recorrido por Pueblo Tapao o Montenegro",
      "Día 2: Parque del Café día completo + show de café",
      "Día 3: PANACA día completo, regreso en la tarde"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Pueblo Tapao"],
    alojamientosAsociados: ["cabanas-la-esmeralda", "hotel-campestre-la-tata"],
    precioSinTransporte: 680000,
    precioConTransporte: 820000,
    preciosOcupacion: {
      doble: 750000,
      triple: 700000,
      cuadruple: 680000
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
    descripcion: "4 días / 3 noches de alojamiento, desayunos y cenas incluidos, Parques del Café y PANACA, Valle de Cocora, Salento, Filandia y RECUCA. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia. El programa favorito para conocer lo esencial del Quindío.",
    resumenPrograma: [
      "Día 1: Llegada Armenia, check-in, bienvenida",
      "Día 2: Salento, Valle de Cocora con palma de cera, caminata",
      "Día 3: Parque del Café día completo",
      "Día 4: Filandia + RECUCA + PANACA medio día, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Salento", "Valle de Cocora", "Filandia", "RECUCA"],
    alojamientosAsociados: ["finca-hotel-los-girasoles", "cabanas-la-esmeralda", "finca-hotel-dorada"],
    precioSinTransporte: 979000,
    precioConTransporte: 1152000,
    preciosOcupacion: {
      doble: 1150000,
      triple: 1050000,
      cuadruple: 979000
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
    descripcion: "4 días / 3 noches de alojamiento, desayunos y cenas incluidos, parques temáticos combinados con un día completo de relajación en los Termales de Santa Rosa de Cabal. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia. Ideal para familias y parejas.",
    resumenPrograma: [
      "Día 1: Llegada, check-in, bienvenida y descanso",
      "Día 2: Termales de Santa Rosa de Cabal todo el día",
      "Día 3: Parque del Café + Parque Los Arrieros",
      "Día 4: PANACA medio día, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Termales Santa Rosa", "Parque Los Arrieros"],
    alojamientosAsociados: ["finca-hotel-los-girasoles", "hotel-campestre-cafe-cafe"],
    precioSinTransporte: 979000,
    precioConTransporte: 1273000,
    preciosOcupacion: {
      doble: 1270000,
      triple: 1120000,
      cuadruple: 979000
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
    descripcion: "4 días / 3 noches con enfoque cultural vivencial en las raíces de la arriería quindiana, desayunos y cenas incluidos. Incluye experiencias con mulas, Finca tradicional, Recuca y Parque Los Arrieros. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia.",
    resumenPrograma: [
      "Día 1: Llegada y check-in, charla cultura cafetera",
      "Día 2: Parque Los Arrieros + experiencia de arriería con mulas",
      "Día 3: RECUCA + Finca tradicional cafetera con almuerzo típico",
      "Día 4: Salento pueblo + miradores, regreso"
    ],
    atractivosIncluidos: ["RECUCA", "Parque Los Arrieros", "Salento", "Finca Cafetera Tradicional"],
    alojamientosAsociados: ["cabanas-la-esmeralda", "finca-hotel-los-girasoles"],
    precioSinTransporte: 950000,
    precioConTransporte: 1200000,
    preciosOcupacion: {
      doble: 1200000,
      triple: 1080000,
      cuadruple: 950000
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
    descripcion: "La experiencia definitiva de 5 días y 4 noches. Abrarca TODOS los atractivos del Quindío: parques temáticos, termales, RECUCA, pueblos patrimonio, y el Valle de Cocora con caminata guiada. Transporte desde Aeropuerto Edén o Terminal de Transportes de Armenia.",
    resumenPrograma: [
      "Día 1: Llegada Armenia, check-in, noche de bienvenida",
      "Día 2: Parque del Café completo + show nocturno",
      "Día 3: Salento + Valle de Cocora + caminata guiada palma de cera",
      "Día 4: PANACA + RECUCA + Termales Santa Rosa tarde/noche",
      "Día 5: Filandia + Parque Los Arrieros, almuerzo típico y regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "PANACA", "Valle de Cocora", "Salento", "Filandia", "RECUCA", "Termales Santa Rosa", "Parque Los Arrieros"],
    alojamientosAsociados: ["hotel-campestre-cafe-cafe", "hotel-campestre-las-camelias", "finca-hotel-los-girasoles"],
    precioSinTransporte: 1150000,
    precioConTransporte: 1473000,
    preciosOcupacion: {
      doble: 1650000,
      triple: 1550000,
      cuadruple: 1473000
    }
  },
  {
    id: "plan-7",
    slug: "plan-premium-vip",
    titulo: "Plan Premium: Experiencia VIP",
    duracion: "4d",
    noches: 3,
    dias: 4,
    categoria: "Premium",
    badge: "VIP",
    detalleUrl: "planes.html",
    descripcion: "4 días / 3 noches con desayunos y cenas incluidos. Experiencia premium con alojamientos VIP, transporte exclusivo placa blanca desde Aeropuerto Edén o Terminal de Transportes de Armenia, asistencia bilingüe y acceso prioritario a atractivos. Incluye experiencias exclusivas.",
    resumenPrograma: [
      "Día 1: Llegada VIP, check-in en hotel 5 estrellas",
      "Día 2: Parque del Café con acceso prioritario",
      "Día 3: Valle de Cocora con helicóptero (opcional)",
      "Día 4: Termales exclusivos y spa, regreso"
    ],
    atractivosIncluidos: ["Parque del Café", "Valle de Cocora", "Termales Exclusivos"],
    alojamientosAsociados: ["hotel-campestre-las-camelias", "hotel-campestre-cafe-cafe"],
    precioSinTransporte: 1500000,
    precioConTransporte: 1800000
  },
  {
    id: "plan-8",
    slug: "plan-empresarial",
    titulo: "Plan Empresarial: Team Building",
    duracion: "3d",
    noches: 2,
    dias: 3,
    categoria: "Empresarial",
    badge: "Corporativo",
    detalleUrl: "planes.html",
    descripcion: "3 días / 2 noches con desayunos y cenas incluidos. Programa especial para empresas y grupos desde Aeropuerto Edén o Terminal de Transportes de Armenia. Incluye actividades de team building, salas de conferencias, alimentación ejecutiva y transporte corporativo.",
    resumenPrograma: [
      "Día 1: Llegada, check-in corporativo, conferencia inaugural",
      "Día 2: Actividades team building en finca cafetera",
      "Día 3: Recorrido turístico y cierre corporativo, regreso"
    ],
    atractivosIncluidos: ["Team Building", "Conferencias", "Recorrido Turístico"],
    alojamientosAsociados: ["finca-hotel-los-girasoles", "hotel-campestre-cafe-cafe"],
    precioSinTransporte: 1200000,
    precioConTransporte: 1450000
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
      "hotel-campestre-las-camelias": "assets/images/alojamientos/hotel-campestre-las-camelias/las-camelias-hotel-campestre.jpg"
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
