/* ==========================================================================
   QUINDÍO TRAVEL - DATOS OFICIALES DE PLANES, HOTELES Y TARIFAS (2026)
   ========================================================================== */

const QUINDIO_TRAVEL_DATA = {
  empresa: {
    nombre: "Quindío Travel",
    gerente: "Alvaro Alzate Ortiz",
    telefono: "(317) 4426044",
    email: "gerencia@quindiotravel.net"
  },

  hoteles: [
    {
      id: "esmeralda",
      nombre: "Cabañas La Esmeralda",
      categoria: "Intermedia",
      servicios: ["Habitaciones y cabañas con baño privado y TV", "Piscina adultos y niños", "Jacuzzi", "Cancha microfútbol y volley playa", "Juegos infantiles", "Restaurante y zona de asados", "Kiosco, ping pong, sapo y hamacas", "Bar y amplias zonas verdes"]
    },
    {
      id: "girasoles",
      nombre: "Finca Hotel Los Girasoles",
      categoria: "Intermedia VIP",
      servicios: ["Recepción y lobby", "Piscina y Jacuzzi", "Cancha de microfútbol en césped y voleibol grama", "Parque infantil y salón de lectura", "Comedor para 100 personas", "Oratorio", "Zonas verdes", "WiFi en recepción", "DirecTV en salón de juegos"]
    },
    {
      id: "cafe-cafe",
      nombre: "Hotel Campestre Café Café",
      categoria: "Intermedia VIP",
      servicios: ["Entorno cafetero y arquitectura colonial", "WiFi y TV satelital", "Baño privado y agua caliente", "Mini bar", "Amplio parqueadero", "Billar, ping pong, sapo y cancha de voleibol"]
    },
    {
      id: "la-tata",
      nombre: "Hotel Campestre La Tata",
      categoria: "Intermedia VIP",
      ubicacion: "A 100 mts del Parque del Café",
      servicios: ["Piscina niños y adultos", "Jacuzzi", "Juegos infantiles", "Parqueadero", "Restaurante", "Lavandería", "Juegos de mesa"]
    },
    {
      id: "de-la-vega",
      nombre: "De La Vega Hotel Campestre",
      categoria: "Intermedia VIP",
      ubicacion: "A 200 mts del Parque del Café (Montenegro)",
      servicios: ["Piscina y 3 jacuzzis", "Billar pool, rana, ping pong", "Parque infantil", "Parqueadero"]
    },
    {
      id: "dorada",
      nombre: "Finca Hotel Dorada",
      categoria: "Intermedia",
      ubicacion: "Km. 5 Pueblo Tapao Vía a La Tebaida",
      servicios: ["Piscina niños y adultos", "Juegos infantiles", "Parqueadero", "Restaurante", "Hamacas y juegos de mesa"]
    },
    {
      id: "las-camelias",
      nombre: "Hotel Campestre Las Camelias",
      categoria: "Resort VIP",
      servicios: ["Capilla", "Tienda de regalos", "Sauna y turco", "5 piscinas y Parque Acualandia", "Canchas fútbol, vóley, baloncesto y tenis", "Pista de karts", "Golfito y sendero ecológico"]
    }
  ],

  tarifasPlan4D3N: {
    temporadaBaja: {
      radioTaxi: {
        esmeralda: { pax2: 1479000, pax3: 1261000, pax4: 1152000 },
        girasoles: { pax2: 1915000, pax3: 1697000, pax4: 1588000 },
        cafeCafe:  { pax2: 2097000, pax3: 1879000, pax4: 1770000 }
      },
      placaBlanca: {
        esmeralda: { pax2: 2117000, pax3: 1688000, pax4: 1473000 },
        girasoles: { pax2: 2553000, pax3: 2124000, pax4: 1909000 },
        cafeCafe:  { pax2: 2735000, pax3: 2306000, pax4: 2091000 }
      }
    },
    temporadaMedia: {
      radioTaxi: {
        esmeralda: { pax2: 1600000, pax3: 1382000, pax4: 1273000 },
        girasoles: { pax2: 2459000, pax3: 2241000, pax4: 2132000 },
        cafeCafe:  { pax2: 3508000, pax3: 3290000, pax4: 3181000 }
      },
      placaBlanca: {
        esmeralda: { pax2: 2238000, pax3: 1809000, pax4: 1594000 },
        girasoles: { pax2: 3097000, pax3: 2668000, pax4: 2453000 },
        cafeCafe:  { pax2: 4146000, pax3: 3717000, pax4: 3502000 }
      }
    },
    temporadaAlta: {
      radioTaxi: {
        esmeralda: { pax2: 1840000, pax3: 1589000, pax4: 1464000 },
        girasoles: { pax2: 2828000, pax3: 2577000, pax4: 2452000 },
        cafeCafe:  { pax2: 4034000, pax3: 3784000, pax4: 3658000 }
      },
      placaBlanca: {
        esmeralda: { pax2: 2574000, pax3: 2080000, pax4: 1833000 },
        girasoles: { pax2: 3562000, pax3: 3068000, pax4: 2821000 },
        cafeCafe:  { pax2: 4768000, pax3: 4275000, pax4: 4027000 }
      }
    }
  }
};
