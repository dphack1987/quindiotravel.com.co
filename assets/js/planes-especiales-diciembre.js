/**
 * Módulo de Planes Especiales para Diciembre
 * Carga y gestiona la información de planes especiales de temporada alta
 * 
 * Uso: Incluir este script en planes.html y llamar a initPlanesEspeciales()
 */

const planesEspeciales = {
  plan: {
    nombre: "Planes Especiales Temporada Alta - Diciembre a Enero",
    temporada: "15 DICIEMBRE AL 20 ENERO",
    duracion: {
      dias: 4,
      noches: 3
    },
    tarifa_por_persona: true,
    max_cupos: 30,
    incluye: [
      "Alojamiento 3 noches con desayuno y cena",
      "Transporte interno",
      "Entradas a Parque del Café",
      "Entradas a PANACA",
      "Entradas a RECUCA",
      "Valle de Cocora a las 10:30",
      "Traslado a Salento (no incluye almuerzo)",
      "12:30 m. traslado a Filandia",
      "Conocer mirador de Filandia",
      "Museo del canasto",
      "Calle del tiempo",
      "Asistencia médica 24/7"
    ],
    itinerario: {
      dia1: "9:00 a.m. - Llegada al terminal o aeropuerto de Armenia, registro en alojamiento y traslado al Parque del Café con pasaporte múltiple. No incluye almuerzo. 5:00 p.m. - Regreso al alojamiento elegido y cena.",
      dia2: "8:00 a.m. - Desayuno. 10:30 a.m. - Traslado a Valle de Cocora. Traslado a Salento (no incluye almuerzo). 12:30 p.m. - Traslado a Filandia para conocer el mirador de Filandia, museo del canasto y la calle del tiempo detenida. 5:00 p.m. - Regreso al alojamiento.",
      dia3: "9:00 a.m. - Desayuno. Traslado al Parque PANACA con pasaporte TERRA. No incluye almuerzo. 5:00 p.m. - Regreso al alojamiento elegido y cena.",
      dia4: "8:00 a.m. - Desayuno. Traslado al Parque RECUCA con experiencia Bogadera. A medio día traslado al alojamiento y traslado al aeropuerto o terminal de Armenia."
    }
  },
  tarifas: {
    radio_taxi: [
      {
        hotel: "Cabañas La Esmeralda",
        categoria: "Intermedia",
        pax_2: 1840000,
        pax_3: 1589000,
        pax_4: 1464000
      },
      {
        hotel: "Finca Hotel Los Girasoles",
        categoria: "Intermedia VIP",
        pax_2: 2828000,
        pax_3: 2577000,
        pax_4: 2452000
      },
      {
        hotel: "Hotel Campestre Café Café",
        categoria: "Intermedia VIP",
        pax_2: 4034000,
        pax_3: 3784000,
        pax_4: 3658000
      }
    ],
    placa_blanca: [
      {
        hotel: "Cabañas La Esmeralda",
        categoria: "Intermedia",
        pax_2: 2574000,
        pax_3: 2080000,
        pax_4: 1833000
      },
      {
        hotel: "Finca Hotel Los Girasoles",
        categoria: "Intermedia VIP",
        pax_2: 3562000,
        pax_3: 3068000,
        pax_4: 2821000
      },
      {
        hotel: "Hotel Campestre Café Café",
        categoria: "Intermedia VIP",
        pax_2: 4768000,
        pax_3: 4275000,
        pax_4: 4027000
      }
    ]
  },
  hoteles: {
    "cabanas_la_esmeralda": {
      nombre: "CABAÑAS LA ESMERALDA",
      categoria: "Intermedia",
      servicios: [
        "Habitaciones y Cabañas con baño privado y T.V",
        "Piscina Adultos - Niños",
        "Jacuzzi",
        "Cancha de Microfútbol",
        "Cancha de Volley Playa",
        "Juegos Infantiles",
        "Restaurante",
        "Zona de Asados",
        "Juegos de Mesa",
        "Ping Pong - Sapo",
        "Hamacas",
        "Asador",
        "Kiosco",
        "Horno de Barro, Estufa a Gas",
        "Bar",
        "Amplias Zonas Verdes"
      ]
    },
    "finca_hotel_los_girasoles": {
      nombre: "FINCA HOTEL LOS GIRASOLES",
      categoria: "Intermedia VIP",
      servicios: [
        "Recepción y lobby",
        "Zona de juegos ping pong",
        "Juegos de mesa",
        "Piscina",
        "Jacuzzi",
        "Cancha de micro fútbol en césped",
        "Voleibol grama",
        "Parque infantil",
        "Salón de lectura",
        "Salón comedor con capacidad para 100 personas",
        "Oratorio",
        "Amplios jardines y zonas verde",
        "Zona WiFi en recepción",
        "DIRECTV en salón de juegos"
      ]
    },
    "hotel_campestre_cafe_cafe": {
      nombre: "HOTEL CAMPESTRE CAFÉ CAFÉ",
      categoria: "Intermedia VIP",
      descripcion: "Un lugar mágico donde se mezcla el colorido y el aroma de nuestros cafetales, las costumbres de la cultura Quindiana, la arquitectura colonial y la calidez de nuestra gente.",
      servicios: [
        "WiFi",
        "Televisión satelital",
        "Baño privado",
        "Mini bar",
        "Agua caliente",
        "Amplio parqueadero",
        "Juegos de mesa",
        "Billar",
        "Cancha de voleibol",
        "Ping pong",
        "Sapo y más"
      ]
    },
    "hotel_campestre_la_tata": {
      nombre: "HOTEL CAMPESTRE LA TATA",
      categoria: "Intermedia",
      ubicacion: "A 100 mts de Parque del Café",
      servicios: [
        "Piscina niños y adultos",
        "Jacuzzi",
        "Juegos infantiles",
        "Parqueadero",
        "Restaurante",
        "Lavandería",
        "Juegos de mesa"
      ]
    },
    "de_la_vega_hotel_campestre": {
      nombre: "DE LA VEGA HOTEL CAMPESTRE",
      categoria: "Intermedia",
      ubicacion: "A 200 mts del Parque el Café en Montenegro, Quindío",
      servicios: [
        "Zonas húmedas (Piscina, 3 jacuzzi)",
        "Zona de juegos (billar pool, rana, pin pon, entre otros)",
        "Parque infantil",
        "Parqueadero"
      ]
    },
    "finca_hotel_dorada": {
      nombre: "FINCA HOTEL DORADA",
      categoria: "Económica",
      ubicacion: "Km. 5 Pueblo Tapao, Vía a la Tebadia",
      servicios: [
        "Piscina niños y adultos",
        "Juegos infantiles",
        "Parqueadero",
        "Restaurante",
        "Lavandería",
        "Hamacas",
        "Juegos de mesa"
      ]
    },
    "hotel_campestre_las_camelias": {
      nombre: "HOTEL CAMPESTRE LAS CAMELIAS",
      categoria: "VIP",
      servicios: [
        "Capilla",
        "Tienda de regalos",
        "Sauna",
        "Turco",
        "5 piscinas",
        "Parque acualandia",
        "Canchas de fútbol",
        "Voleibol",
        "Baloncesto",
        "Tenis",
        "Recreativa",
        "Pista de karts",
        "Billar",
        "Billar pool",
        "Golfito",
        "Sendero ecológico",
        "Parque infantil"
      ]
    }
  }
};

/**
 * Obtener tarifa para un hotel específico según tipo de transporte y número de pax
 */
function obtenerTarifa(nombreHotel, tipoTransporte, numPax) {
  const tarifas = planesEspeciales.tarifas[tipoTransporte];
  const plan = tarifas.find(p => p.hotel === nombreHotel);
  
  if (!plan) return null;
  
  const paxKey = `pax_${numPax}`;
  return plan[paxKey] || null;
}

/**
 * Generar cards HTML con tarifas (sustituye tablas)
 */
function generarTarifasCards(tipoTransporte = 'radio_taxi') {
  const tarifas = planesEspeciales.tarifas[tipoTransporte];
  let html = `
    <div class="tarifas-section-diciembre">
      <h3>${tipoTransporte === 'radio_taxi' ? 'TEMPORADA ALTA - RADIO TAXI DEL QUINDÍO' : 'TEMPORADA ALTA - TRANSPORTE TURÍSTICO PLACA BLANCA'}</h3>
      <div class="tarifas-cards-grid">
  `;
  
  tarifas.forEach(plan => {
    html += `
      <div class="tarifa-card">
        <div class="tarifa-card-header">
          <h4>${plan.hotel}</h4>
          <span class="tarifa-categoria">${plan.categoria}</span>
        </div>
        <div class="tarifa-prices">
          <div class="price-item">
            <span class="price-label">2 Pax</span>
            <span class="price-value">$${plan.pax_2.toLocaleString('es-CO')}</span>
          </div>
          <div class="price-item">
            <span class="price-label">3 Pax</span>
            <span class="price-value">$${plan.pax_3.toLocaleString('es-CO')}</span>
          </div>
          <div class="price-item">
            <span class="price-label">4 Pax</span>
            <span class="price-value">$${plan.pax_4.toLocaleString('es-CO')}</span>
          </div>
        </div>
      </div>
    `;
  });
  
  html += `
      </div>
    </div>
  `;
  
  return html;
}

/**
 * Generar lista de servicios incluidos
 */
function generarListaIncluye() {
  let html = '<div class="incluye-section-diciembre"><h3>✅ Incluye:</h3><ul class="incluye-list">';
  
  planesEspeciales.plan.incluye.forEach(item => {
    html += `<li><i class="fas fa-check"></i> ${item}</li>`;
  });
  
  html += '</ul></div>';
  
  return html;
}

/**
 * Generar tarjeta de hotel
 */
function generarTarjetaHotel(hotelKey) {
  const hotel = planesEspeciales.hoteles[hotelKey];
  
  if (!hotel) return '';
  
  let html = `
    <div class="hotel-card-diciembre">
      <h4>${hotel.nombre}</h4>
      <p class="categoria-badge">${hotel.categoria}</p>
  `;
  
  if (hotel.ubicacion) {
    html += `<p class="ubicacion"><i class="fas fa-map-marker-alt"></i> ${hotel.ubicacion}</p>`;
  }
  
  if (hotel.descripcion) {
    html += `<p class="descripcion">${hotel.descripcion}</p>`;
  }
  
  html += '<ul class="servicios-list">';
  hotel.servicios.forEach(servicio => {
    html += `<li><i class="fas fa-check-circle"></i> ${servicio}</li>`;
  });
  html += '</ul></div>';
  
  return html;
}

/**
 * Inicializar sección de planes especiales
 */
function initPlanesEspeciales() {
  const container = document.getElementById('planes-especiales-container');
  
  if (!container) return;
  
  let html = `
    <section class="planes-especiales-diciembre">
      <div class="container">
        <div class="planes-header">
          <h2>🎄 Planes Especiales Temporada Alta</h2>
          <p>${planesEspeciales.plan.temporada}</p>
          <span class="badge-cupos">Máximo ${planesEspeciales.plan.max_cupos} cupos</span>
        </div>
        
        <div class="plan-details">
          <h3>Duración: ${planesEspeciales.plan.duracion.dias} Días / ${planesEspeciales.plan.duracion.noches} Noches</h3>
          ${generarListaIncluye()}
        </div>
        
        <div class="tarifas-container">
          ${generarTarifasCards('radio_taxi')}
          ${generarTarifasCards('placa_blanca')}
          
          <div class="nota-transporte">
            <p><strong>📝 Nota:</strong> ${planesEspeciales.plan.incluye[planesEspeciales.plan.incluye.length - 1]}</p>
          </div>
        </div>
        
        <div class="hoteles-incluidos">
          <h3>🏨 Hoteles Incluidos en el Plan</h3>
          <div class="hoteles-grid">
            ${Object.keys(planesEspeciales.hoteles).map(key => generarTarjetaHotel(key)).join('')}
          </div>
        </div>
        
        <div class="contacto-cta">
          <h3>¿Listo para tu aventura en diciembre?</h3>
          <a href="https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20me%20interesa%20un%20plan%20especial%20para%20diciembre" target="_blank" class="btn btn-whatsapp-grande">
            <i class="fab fa-whatsapp"></i> Cotizar Plan de Diciembre
          </a>
        </div>
      </div>
    </section>
  `;
  
  container.innerHTML = html;
}

// Ejecutar cuando el DOM esté listo
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initPlanesEspeciales);
} else {
  initPlanesEspeciales();
}

// Exportar para uso en otros scripts
if (typeof module !== 'undefined' && module.exports) {
  module.exports = planesEspeciales;
}
