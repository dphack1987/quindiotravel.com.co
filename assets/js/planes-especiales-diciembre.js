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
      imagen: "assets/images/alojamientos/finca-hotel-la-esmeralda/finca-hotel-cabanas-la.webp",
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
      imagen: "assets/images/alojamientos/finca-hotel-los-girasoles/Finca-los-Girasoles-7.webp",
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
      imagen: "assets/images/alojamientos/hotel-campestre-cafe-cafe/406282624.webp",
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
      imagen: "assets/images/alojamientos/hotel-campestre-la-tata/finca-hotel-la-tata.webp",
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
      imagen: "assets/images/alojamientos/hotel-de-la-vega/hotel-campestre-de-la-vega-3.webp",
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
      imagen: "assets/images/alojamientos/finca-hotel-la-dorada/1414317914.webp",
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
      imagen: "assets/images/alojamientos/hotel-campestre-las-camelias/las-camelias-hotel-campestre.jpg",
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
 * Tarjeta de hotel compacta para el teaser (sin lista interminable de servicios)
 */
function generarTarjetaHotel(hotelKey) {
  const hotel = planesEspeciales.hoteles[hotelKey];
  if (!hotel) return '';

  const serviciosTop = hotel.servicios.slice(0, 4);

  return `
    <div class="hotel-card-diciembre">
      <div class="hotel-card-media">
        <img src="${hotel.imagen}" alt="${hotel.nombre} en el Quindío" loading="lazy" width="800" height="450">
      </div>
      <h4>${hotel.nombre}</h4>
      <p class="categoria-badge">${hotel.categoria}</p>
      ${hotel.ubicacion ? `<p class="ubicacion"><i class="fas fa-map-marker-alt"></i> ${hotel.ubicacion}</p>` : ''}
      <ul class="servicios-list servicios-list-compact">
        ${serviciosTop.map(s => `<li><i class="fas fa-check-circle"></i> ${s}</li>`).join('')}
      </ul>
    </div>`;
}

/**
 * Teaser compacto de temporada alta (15 dic – 20 ene).
 * Solo tarifas Radio Taxi autorizadas; Placa Blanca solo por cotización.
 * Sin CTA propio (la página usa un único CTA WhatsApp).
 */
function initPlanesEspeciales() {
  const container = document.getElementById('planes-especiales-container');
  if (!container) return;

  const tarifas = planesEspeciales.tarifas.radio_taxi;
  const incluyeTop = planesEspeciales.plan.incluye.slice(0, 6);
  const hotelesClave = ['cabanas_la_esmeralda', 'finca_hotel_los_girasoles', 'hotel_campestre_cafe_cafe'];

  const tarifasHtml = tarifas.map(plan => `
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
      </div>`).join('');

  const hotelesHtml = hotelesClave.map(key => generarTarjetaHotel(key)).join('');

  container.innerHTML = `
    <section class="planes-especiales-diciembre planes-especiales-compact">
      <div class="container">
        <div class="planes-header">
          <h2>🎄 Planes Especiales Temporada Alta</h2>
          <p>${planesEspeciales.plan.temporada} · 4 Días / 3 Noches · Tarifa por persona</p>
          <span class="badge-cupos">Consulta disponibilidad para tu fecha</span>
        </div>

        <div class="plan-details plan-details-compact">
          <h3>Incluye</h3>
          <ul class="incluye-list incluye-list-compact">
            ${incluyeTop.map(item => `<li><i class="fas fa-check"></i> ${item}</li>`).join('')}
          </ul>
          <p class="incluye-mas">+ Salento, Filandia, PANACA, RECUCA y asistencia médica 24/7</p>
        </div>

        <div class="tarifas-container">
          <div class="tarifas-section-diciembre">
            <h3>Temporada Alta — Radio Taxi del Quindío</h3>
            <div class="tarifas-cards-grid">
              ${tarifasHtml}
            </div>
          </div>
          <div class="nota-transporte">
            <p><strong>📝 Nota:</strong> Precios con Radio Taxi (conductores capacitados en turismo). Transporte Placa Blanca solo por cotización especial.</p>
          </div>
        </div>

        <div class="hoteles-incluidos">
          <h3>🏨 Alojamiento disponible</h3>
          <div class="hoteles-grid hoteles-grid-compact">
            ${hotelesHtml}
          </div>
        </div>
      </div>
    </section>
  `;
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
