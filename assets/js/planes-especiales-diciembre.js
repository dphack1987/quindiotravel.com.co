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
      "3 noches de alojamiento",
      "3 desayunos",
      "3 cenas",
      "Pasaporte al Parque del Café",
      "Visita a Valle de Cocora",
      "Visita a Salento y Filandia",
      "Mirador de Filandia",
      "Museo del Canasto",
      "Calle del Tiempo Detenida",
      "Parque PANACA",
      "Parque RECUCA",
      "Asistencia médica",
      "Transporte desde terminal hasta alojamiento",
      "Transporte a los atractivos propuestos"
    ]
  },
  tarifas: {
    radio_taxi: [
      {
        hotel: "Cabañas La Esmeralda",
        categoria: "Intermedia",
        pax_2: 1290000,
        pax_3: 1200000,
        pax_4: 1160000
      },
      {
        hotel: "Finca Hotel Los Girasoles",
        categoria: "Intermedia VIP",
        pax_2: 1850000,
        pax_3: 1650000,
        pax_4: 1530000
      },
      {
        hotel: "Hotel Campestre Café Café",
        categoria: "Intermedia VIP",
        pax_2: 1990000,
        pax_3: 1730000,
        pax_4: 1590000
      }
    ],
    placa_blanca: [
      {
        hotel: "Cabañas La Esmeralda",
        categoria: "Intermedia",
        pax_2: 1550000,
        pax_3: 1295000,
        pax_4: 1160000
      },
      {
        hotel: "Finca Hotel Los Girasoles",
        categoria: "Intermedia VIP",
        pax_2: 2060000,
        pax_3: 1850000,
        pax_4: 1690000
      },
      {
        hotel: "Hotel Campestre Café Café",
        categoria: "Intermedia VIP",
        pax_2: 2160000,
        pax_3: 1920000,
        pax_4: 1750000
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
 * Generar tabla HTML con tarifas
 */
function generarTablaTarifas(tipoTransporte = 'radio_taxi') {
  const tarifas = planesEspeciales.tarifas[tipoTransporte];
  let html = `
    <div class="tarifas-section-diciembre">
      <h3>${tipoTransporte === 'radio_taxi' ? 'TEMPORADA ALTA - RADIO TAXI DEL QUINDÍO' : 'TEMPORADA ALTA - TRANSPORTE TURÍSTICO PLACA BLANCA'}</h3>
      <table class="tarifas-table-diciembre">
        <thead>
          <tr>
            <th>Hotel</th>
            <th>Categoría</th>
            <th>2 Pax</th>
            <th>3 Pax</th>
            <th>4 Pax</th>
          </tr>
        </thead>
        <tbody>
  `;
  
  tarifas.forEach(plan => {
    html += `
      <tr>
        <td>${plan.hotel}</td>
        <td>${plan.categoria}</td>
        <td>$${plan.pax_2.toLocaleString('es-CO')}</td>
        <td>$${plan.pax_3.toLocaleString('es-CO')}</td>
        <td>$${plan.pax_4.toLocaleString('es-CO')}</td>
      </tr>
    `;
  });
  
  html += `
        </tbody>
      </table>
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
          ${generarTablaTarifas('radio_taxi')}
          ${generarTablaTarifas('placa_blanca')}
          
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
