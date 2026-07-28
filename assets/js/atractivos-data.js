// Base de datos de atractivos turísticos - Quindío Travel (RNT 18152)
const atractivosData = [
  {
    id: "parque-del-cafe",
    nombre: "Parque del Café",
    nombreCorto: "Parque del Café",
    categoria: "Parque Temático",
    ubicacion: "Montenegro, Quindío",
    descripcion: "Parque temático dedicado a la cultura cafetera colombiana. Cuenta con atracciones mecánicas, shows culturales, museo del café, sendero cafetero y espectáculos temáticos. Es uno de los parques más importantes de Colombia.",
    descripcionDetallada: "El Parque del Café es una experiencia inmersiva en la cultura cafetera colombiana. Los visitantes pueden disfrutar de más de 30 atracciones mecánicas, shows en vivo que narran la historia del café, un museo interactivo sobre el proceso de producción cafetera, y recorridos por plantaciones de café. El parque ofrece diferentes pasaportes según las preferencias de los visitantes.",
    caracteristicas: [
      "Más de 30 atracciones mecánicas",
      "Shows culturales y temáticos",
      "Museo del café interactivo",
      "Sendero cafetero guiado",
      "Mecanizado de café tradicional",
      "Zonas infantiles y familiares",
      "Restaurantes temáticos",
      "Tienda de café especializado"
    ],
    actividades: [
      "Montañas rusas y atracciones extremas",
      "Show del café - Narración histórica",
      "Recorrido por plantaciones de café",
      "Mecanizado de café tradicional",
      "Degustación de café especializado",
      "Show de mariposas tropicales",
      "Espectáculo de aves rapaces"
    ],
    horario: "Todos los días 9:00 AM - 6:00 PM",
    duracionRecomendada: "1 día completo",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Totalmente accesible",
    imagenes: [
      "assets/images/atractivos/parque-del-cafe.jpg",
      "parque-del-cafe/PDC_ParqueDelCafe_001.jpg",
      "parque-del-cafe/parque-del-cafe-20-870x555.jpg",
      "parque-del-cafe/caption.jpg"
    ],
    precioEntrada: "Desde $75,000 COP",
    planesAsociados: ["plan-1", "plan-2", "plan-3", "plan-4", "plan-6"],
    keywords: ["parque temático", "café", "montenegro", "atracciones mecánicas", "shows culturales"]
  },
  {
    id: "panaca",
    nombre: "PANACA",
    nombreCorto: "PANACA",
    categoria: "Parque Agropecuario",
    ubicacion: "Quimbaya, Quindío",
    descripcion: "Parque de la naturaleza y la cultura agropecuaria. Cuenta con más de 300 especies animales, zonas interactivas con animales domésticos, shows educativos y recorridos temáticos.",
    descripcionDetallada: "PANACA (Parque Nacional de la Cultura Agropecuaria) es un espacio educativo y recreativo donde los visitantes pueden interactuar con más de 300 especies animales. El parque ofrece experiencias vivenciales como ordeñar vacas, montar caballos, alimentar animales y participar en shows educativos sobre la importancia de la agricultura y ganadería en Colombia.",
    caracteristicas: [
      "Más de 300 especies animales",
      "Zonas interactivas con animales",
      "Shows educativos temáticos",
      "Recorridos guiados agropecuarios",
      "Zonas de alimentación directa",
      "Actividades familiares",
      "Museo de herramientas agrícolas",
      "Senderos ecológicos"
    ],
    actividades: [
      "Interacción con animales domésticos",
      "Ordeñado de vacas",
      "Montar caballos",
      "Alimentar animales en libertad",
      "Show de perros pastores",
      "Recorrido por granjas tradicionales",
      "Demostración de herramientas agrícolas"
    ],
    horario: "Todos los días 9:00 AM - 5:00 PM",
    duracionRecomendada: "1 día completo",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Totalmente accesible",
    imagenes: [
      "assets/images/atractivos/panaca.jpg",
      "panaca/panaca-imagen.jpg",
      "panaca/ZIP-LINE.webp"
    ],
    precioEntrada: "Desde $45,000 COP",
    planesAsociados: ["plan-1", "plan-2"],
    keywords: ["parque agropecuario", "animales", "quimbaya", "educación", "familia"]
  },
  {
    id: "valle-de-cocora",
    nombre: "Valle de Cocora",
    nombreCorto: "Valle de Cocora",
    categoria: "Destino Natural",
    ubicacion: "Salento, Quindío",
    descripcion: "Valle sagrado con las palmas de cera más altas del mundo. Patrimonio natural de Colombia, ideal para senderismo, fotografía y conexión con la naturaleza.",
    descripcionDetallada: "El Valle de Cocora es un destino natural sagrado que alberga la palma de cera (Ceroxylon quindiuense), el árbol nacional de Colombia y una de las palmas más altas del mundo, que puede alcanzar hasta 60 metros de altura. Los visitantes pueden realizar senderismo por el valle, observar colibríes, admirar el paisaje dramático y conectar con la naturaleza en su estado más puro.",
    caracteristicas: [
      "Palmas de cera más altas del mundo",
      "Senderos ecológicos señalizados",
      "Observación de colibríes",
      "Paisajes dramáticos",
      "Patrimonio natural de Colombia",
      "Zonas de picnic",
      "Miradores panorámicos",
      "Flora y fauna autóctona"
    ],
    actividades: [
      "Senderismo por el valle principal",
      "Caminata hasta la nube",
      "Observación de colibríes",
      "Fotografía de paisajes",
      "Cabalgata por el valle",
      "Picnic en zonas naturales",
      "Visita a viveros de palmas"
    ],
    horario: "Todos los días 6:00 AM - 6:00 PM",
    duracionRecomendada: "4-6 horas",
    temporadaRecomendada: "Todo el año (mejor en seco)",
    nivelDificultad: "Moderado",
    accesibilidad: "Parcialmente accesible",
    imagenes: [
      "assets/images/paisajes/foto_hero1.jpg",
      "assets/images/planes/plan-3.jpg"
    ],
    precioEntrada: "Entrada gratuita",
    planesAsociados: ["plan-3", "plan-4", "plan-6"],
    keywords: ["palma de cera", "senderismo", "salento", "naturaleza", "patrimonio"]
  },
  {
    id: "salento",
    nombre: "Salento",
    nombreCorto: "Salento",
    categoria: "Pueblo Patrimonio",
    ubicacion: "Salento, Quindío",
    descripcion: "Pueblo patrimonio con arquitectura tradicional, balcones coloridos, artesanías en guadua y gastronomía típica. Punto de acceso al Valle de Cocora.",
    descripcionDetallada: "Salento es uno de los pueblos más hermosos del Eje Cafetero, declarado patrimonio histórico y cultural de Colombia. Su arquitectura tradicional con balcones coloridos, calles empedradas y artesanías en guadua lo convierten en un destino imperdible. Es el punto de acceso principal al Valle de Cocora y ofrece una experiencia auténtica de la cultura paisa.",
    caracteristicas: [
      "Arquitectura tradicional paisa",
      "Balcones coloridos típicos",
      "Artesanías en guadua",
      "Gastronomía típica",
      "Mirador cóndor",
      "Calle real empedrada",
      "Plaza principal histórica",
      "Iglesia colonial"
    ],
    actividades: [
      "Recorrido por el pueblo histórico",
      "Visita al mirador cóndor",
      "Compra de artesanías en guadua",
      "Degustación de gastronomía típica",
      "Fotografía de arquitectura tradicional",
      "Visita a cafeterías tradicionales",
      "Paseo en Willys jeep"
    ],
    horario: "Todos los días 8:00 AM - 8:00 PM",
    duracionRecomendada: "Medio día",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Parcialmente accesible",
    imagenes: [
      "assets/images/paisajes/foto_hero1.jpg"
    ],
    precioEntrada: "Acceso gratuito",
    planesAsociados: ["plan-2", "plan-3", "plan-6"],
    keywords: ["pueblo patrimonio", "arquitectura", "artesanías", "balcones", "cultura"]
  },
  {
    id: "filandia",
    nombre: "Filandia",
    nombreCorto: "Filandia",
    categoria: "Pueblo Patrimonio",
    ubicacion: "Filandia, Quindío",
    descripcion: "Pueblo conocido por su mirador cóndor, artesanías en guadua de alta calidad, arquitectura colonial y vistas panorámicas del valle.",
    descripcionDetallada: "Filandia es un pueblo encantador conocido por sus artesanías en guadua de alta calidad y su mirador cóndor que ofrece vistas panorámicas espectaculares del valle. Su arquitectura colonial bien conservada, plazas tranquilas y ambiente relajado lo hacen ideal para una experiencia cultural auténtica del Eje Cafetero.",
    caracteristicas: [
      "Mirador cóndor con vistas panorámicas",
      "Artesanías en guadua premium",
      "Arquitectura colonial bien conservada",
      "Plazas tranquilas",
      "Vistas espectaculares del valle",
      "Gastronomía local",
      "Ambiente relajado",
      "Cultura cafetera auténtica"
    ],
    actividades: [
      "Visita al mirador cóndor",
      "Compra de artesanías en guadua",
      "Recorrido por el pueblo colonial",
      "Degustación de gastronomía local",
      "Fotografía de vistas panorámicas",
      "Visita a talleres artesanales",
      "Experiencia cultural cafetera"
    ],
    horario: "Todos los días 8:00 AM - 7:00 PM",
    duracionRecomendada: "Medio día",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Parcialmente accesible",
    imagenes: [
      "assets/images/paisajes/foto_hero1.jpg"
    ],
    precioEntrada: "Acceso gratuito",
    planesAsociados: ["plan-3", "plan-6"],
    keywords: ["mirador cóndor", "artesanías", "guadua", "pueblo colonial", "vistas"]
  },
  {
    id: "termales-santa-rosa",
    nombre: "Termales Santa Rosa",
    nombreCorto: "Termales Santa Rosa",
    categoria: "Wellness",
    ubicacion: "Santa Rosa de Cabal, Risaralda",
    descripcion: "Complejo termal con aguas minerales naturales, piscinas termales, tratamientos de wellness y conexión con la naturaleza.",
    descripcionDetallada: "Los Termales Santa Rosa son un complejo wellness de alta categoría con aguas minerales naturales con propiedades terapéuticas. El complejo ofrece múltiples piscinas termales a diferentes temperaturas, tratamientos de wellness, masajes, y una experiencia de relax en medio de la naturaleza. Es ideal para desestresarse y revitalizarse.",
    caracteristicas: [
      "Aguas minerales naturales",
      "Múltiples piscinas termales",
      "Tratamientos de wellness",
      "Masajes terapéuticos",
      "Entorno natural",
      "Restaurantes saludables",
      "Zonas de relax",
      "Acceso hotel incluido"
    ],
    actividades: [
      "Baños en piscinas termales",
      "Tratamientos de wellness",
      "Masajes terapéuticos",
      "Caminatas por senderos naturales",
      "Degustación de comida saludable",
      "Relax en zonas tranquilas",
      "Yoga al aire libre"
    ],
    horario: "Todos los días 8:00 AM - 9:00 PM",
    duracionRecomendada: "Medio día",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Totalmente accesible",
    imagenes: [
      "assets/images/atractivos/termales-santa-rosa.jpg",
      "termales-de-santa-rosa/termales-santa-rosa-cabal-hotel-2k1-scaled.jpg",
      "termales-de-santa-rosa/termales-santa-rosa-03.jpg"
    ],
    precioEntrada: "Desde $120,000 COP",
    planesAsociados: ["plan-4", "plan-6"],
    keywords: ["termales", "wellness", "aguas minerales", "masajes", "relax"]
  },
  {
    id: "recuca",
    nombre: "RECUCA",
    nombreCorto: "RECUCA",
    categoria: "Experiencia Cultural",
    ubicacion: "Pereira, Risaralda",
    descripcion: "Parque temático de la cultura cafetera con experiencias vivenciales, recorrido por senderos cafeteros y muestra tradicional del proceso del café.",
    descripcionDetallada: "RECUCA (Reserva Natural Cafetera) es una experiencia cultural vivencial donde los visitantes pueden participar activamente en el proceso tradicional del café. El recorrido incluye senderos cafeteros, muestra de recolección de café, beneficio tradicional, tostado y cata de café. Es una experiencia auténtica que conecta al visitante con la historia y tradición cafetera.",
    caracteristicas: [
      "Experiencia cultural vivencial",
      "Senderos cafeteros educativos",
      "Proceso tradicional del café",
      "Recolección de café",
      "Beneficio tradicional",
      "Tostado y cata de café",
      "Cultura cafetera auténtica",
      "Experiencia multisensorial"
    ],
    actividades: [
      "Recolección de café en plantaciones",
      "Beneficio tradicional del café",
      "Tostado artesanal de café",
      "Cata de cafés especiales",
      "Recorrido por senderos cafeteros",
      "Interacción con caficultores",
      "Degustación de productos locales"
    ],
    horario: "Todos los días 8:00 AM - 5:00 PM",
    duracionRecomendada: "4 horas",
    temporadaRecomendada: "Todo el año (mejor en cosecha)",
    nivelDificultad: "Moderado",
    accesibilidad: "Parcialmente accesible",
    imagenes: [
      "assets/images/atractivos/recuca.jpg",
      "recuca/recuca-sendero-cafetero.jpg",
      "recuca/recuca7.jpg"
    ],
    precioEntrada: "Desde $60,000 COP",
    planesAsociados: ["plan-2", "plan-3", "plan-5"],
    keywords: ["café", "cultura", "sendero", "cata", "tradición"]
  },
  {
    id: "quinti-patas-arriba",
    nombre: "Quinti Patas Arriba",
    nombreCorto: "Quinti Patas Arriba",
    categoria: "Experiencia Cultural",
    ubicacion: "Pereira, Risaralda",
    descripcion: "Parque temático de la cultura arriería y ganadera con shows tradicionales, paseo en mulas y experiencias vivenciales de la tradición.",
    descripcionDetallada: "Quinti Patas Arriba es un parque temático dedicado a la cultura arriería y ganadera del Eje Cafetero. Los visitantes pueden experimentar la tradición de los arrieros a través de shows tradicionales, paseo en mulas, demostraciones de técnicas ganaderas y experiencias vivenciales que reviven la historia de los arrieros que conectaban las regiones.",
    caracteristicas: [
      "Cultura arriería tradicional",
      "Shows tradicionales de arrieros",
      "Paseo en mulas",
      "Experiencias vivenciales",
      "Historia de los arrieros",
      "Cultura ganadera",
      "Demostraciones tradicionales",
      "Ambiente histórico"
    ],
    actividades: [
      "Paseo en mulas por senderos",
      "Shows tradicionales de arrieros",
      "Demostraciones de técnicas ganaderas",
      "Experiencia vivencial arriería",
      "Fotografía con arrieros tradicionales",
      "Recorridos históricos",
      "Interacción con animales"
    ],
    horario: "Todos los días 9:00 AM - 5:00 PM",
    duracionRecomendada: "4 horas",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Parcialmente accesible",
    imagenes: [
      "assets/images/atractivos/quinti-patas-arriba.jpg",
      "quinti-patas-arriba/qintiparque.jpg"
    ],
    precioEntrada: "Desde $55,000 COP",
    planesAsociados: ["plan-5"],
    keywords: ["arrieros", "mulas", "cultura", "tradición", "ganadería"]
  },
  {
    id: "mariposario",
    nombre: "Mariposario",
    nombreCorto: "Mariposario",
    categoria: "Destino Natural",
    ubicacion: "Armenia, Quindío",
    descripcion: "Mariposario con más de 50 especies de mariposas tropicales, jardines botánicos y experiencias educativas sobre polinización y conservación.",
    descripcionDetallada: "El Mariposario es un destino natural educativo que alberga más de 50 especies de mariposas tropicales en un ambiente de jardines botánicos. Los visitantes pueden aprender sobre el ciclo de vida de las mariposas, su importancia en la polinización, y esfuerzos de conservación. Es una experiencia mágica para todas las edades.",
    caracteristicas: [
      "Más de 50 especies de mariposas",
      "Jardines botánicos",
      "Experiencias educativas",
      "Ciclo de vida de mariposas",
      "Conservación ambiental",
      "Experiencia multisensorial",
      "Ambiente natural",
      "Actividades familiares"
    ],
    actividades: [
      "Observación de mariposas en libertad",
      "Aprendizaje sobre ciclo de vida",
      "Fotografía de mariposas",
      "Recorrido por jardines botánicos",
      "Experiencias educativas",
      "Interacción con la naturaleza",
      "Actividades de conservación"
    ],
    horario: "Todos los días 9:00 AM - 5:00 PM",
    duracionRecomendada: "2-3 horas",
    temporadaRecomendada: "Todo el año",
    nivelDificultad: "Fácil",
    accesibilidad: "Totalmente accesible",
    imagenes: [
      "assets/images/atractivos/mariposario.jpg",
      "mariposario/contamos-con-el-mariposario.jpg"
    ],
    precioEntrada: "Desde $25,000 COP",
    planesAsociados: [],
    keywords: ["mariposas", "naturaleza", "educación", "jardines", "conservación"]
  }
];

// Función para obtener atractivo por nombre
function getAtractivoPorNombre(nombre) {
  return atractivosData.find(atractivo => 
    atractivo.nombreCorto.toLowerCase() === nombre.toLowerCase() ||
    atractivo.nombre.toLowerCase() === nombre.toLowerCase() ||
    atractivo.id === nombre.toLowerCase()
  );
}

// Función para obtener atractivos por plan
function getAtractivosPorPlan(planId) {
  return atractivosData.filter(atractivo => 
    atractivo.planesAsociados.includes(planId)
  );
}

// Función para obtener atractivos por categoría
function getAtractivosPorCategoria(categoria) {
  return atractivosData.filter(atractivo => 
    atractivo.categoria.toLowerCase() === categoria.toLowerCase()
  );
}

// Función para buscar atractivos por keywords
function buscarAtractivosPorKeywords(termino) {
  const terminoLower = termino.toLowerCase();
  return atractivosData.filter(atractivo => 
    atractivo.keywords.some(keyword => 
      keyword.toLowerCase().includes(terminoLower)
    ) ||
    atractivo.nombre.toLowerCase().includes(terminoLower) ||
    atractivo.descripcion.toLowerCase().includes(terminoLower)
  );
}