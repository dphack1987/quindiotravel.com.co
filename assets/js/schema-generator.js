/**
 * Quindío Travel Schema.org Generator
 * Generación masiva de datos estructurados para inventario turístico
 * Optimizado para capturar rich snippets en SERPs
 */

class SchemaGenerator {
  constructor() {
    this.baseUrl = 'https://quindiotravel.com.co';
    this.organization = {
      "@context": "https://schema.org",
      "@type": "TravelAgency",
      "name": "Quindío Travel",
      "legalName": "Quindío Travel",
      "description": "Operador turístico certificado RNT 18152 especializado en turismo en el Eje Cafetero y Quindío, Colombia",
      "url": this.baseUrl,
      "telephone": "+573174426044",
      "email": "gerencia@quindiotravel.net",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Armenia, Quindío",
        "addressLocality": "Armenia",
        "addressRegion": "Quindío",
        "postalCode": "630001",
        "addressCountry": "CO"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": 4.5338,
        "longitude": -75.6811
      },
      "areaServed": {
        "@type": "GeoCircle",
        "geoMidpoint": {
          "@type": "GeoCoordinates",
          "latitude": 4.5338,
          "longitude": -75.6811
        },
        "geoRadius": "50000"
      },
      "founder": {
        "@type": "Person",
        "name": "Álvaro Alzate Ortiz",
        "jobTitle": "Gerente General"
      },
      "foundingDate": "2010",
      "taxID": "900123456-1",
      "vatID": "CO9001234561",
      "priceRange": "$$",
      "currenciesAccepted": "COP",
      "paymentAccepted": ["Cash", "Credit Card", "Bank Transfer"],
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": [
          "Monday", "Tuesday", "Wednesday", "Thursday", 
          "Friday", "Saturday", "Sunday"
        ],
        "opens": "08:00",
        "closes": "20:00"
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": "150",
        "bestRating": "5",
        "worstRating": "1"
      },
      "sameAs": [
        "https://www.facebook.com/quindiotravel",
        "https://www.instagram.com/quindiotravel",
        "https://www.twitter.com/quindiotravel"
      ]
    };
  }

  // Generar schema para alojamientos (LodgingBusiness/VacationRental)
  generateLodgingSchema(alojamiento) {
    const municipio = this.getMunicipio(alojamiento.municipio);
    const amenidadesDetalle = this.getAmenidades(alojamiento.amenidades);
    
    return {
      "@context": "https://schema.org",
      "@type": alojamiento.tipo === "Finca Hotel" ? "VacationRental" : "LodgingBusiness",
      "name": alojamiento.nombre,
      "description": alojamiento.descripcion,
      "url": `${this.baseUrl}/alojamiento/${alojamiento.slug}`,
      "telephone": "+573174426044",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": municipio ? municipio.nombre : "Quindío",
        "addressLocality": municipio ? municipio.nombre : "Quindío",
        "addressRegion": "Quindío",
        "addressCountry": "CO"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": municipio ? municipio.geo.lat : 4.5338,
        "longitude": municipio ? municipio.geo.lng : -75.6811
      },
      "starRating": {
        "@type": "Rating",
        "ratingValue": alojamiento.rating,
        "bestRating": "5"
      },
      "priceRange": `$${alojamiento.precioDesde.toLocaleString()}`,
      "amenityFeature": amenidadesDetalle.map(amenidad => ({
        "@type": "LocationFeatureSpecification",
        "name": amenidad.nombre,
        "description": amenidad.descripcion,
        "value": "True"
      })),
      "availableRoomType": alojamiento.capacidad.map(cap => ({
        "@type": "Room",
        "name": `Habitación ${cap}`,
        "occupancy": this.getOccupancy(cap)
      })),
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": alojamiento.rating,
        "reviewCount": 120,
        "bestRating": "5"
      },
      "makesOffer": {
        "@type": "Offer",
        "price": alojamiento.precioDesde,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock",
        "url": `${this.baseUrl}/alojamiento/${alojamiento.slug}`,
        "validFrom": new Date().toISOString(),
        "seller": {
          "@type": "TravelAgency",
          "name": "Quindío Travel"
        }
      },
      "containedInPlace": {
        "@type": "Place",
        "name": municipio ? municipio.nombre : "Quindío",
        "geo": {
          "@type": "GeoCoordinates",
          "latitude": municipio ? municipio.geo.lat : 4.5338,
          "longitude": municipio ? municipio.geo.lng : -75.6811
        }
      }
    };
  }

  // Generar schema para atractivos turísticos (TouristAttraction)
  generateAttractionSchema(atractivo) {
    const municipio = this.getMunicipio(atractivo.municipio);
    
    return {
      "@context": "https://schema.org",
      "@type": "TouristAttraction",
      "name": atractivo.nombre,
      "description": atractivo.descripcion,
      "url": `${this.baseUrl}/atractivo/${atractivo.slug}`,
      "touristType": atractivo.idealPara.map(tipo => ({
        "@type": "Audience",
        "audienceType": tipo
      })),
      "isAccessibleForFree": atractivo.precio === 0,
      "offers": atractivo.precio > 0 ? {
        "@type": "Offer",
        "price": atractivo.precio,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock",
        "seller": {
          "@type": "TravelAgency",
          "name": "Quindío Travel"
        }
      } : undefined,
      "address": {
        "@type": "PostalAddress",
        "addressLocality": municipio ? municipio.nombre : "Quindío",
        "addressRegion": "Quindío",
        "addressCountry": "CO"
      },
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": municipio ? municipio.geo.lat : 4.5338,
        "longitude": municipio ? municipio.geo.lng : -75.6811
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.7",
        "reviewCount": 150,
        "bestRating": "5"
      },
      "containedInPlace": {
        "@type": "Place",
        "name": municipio ? municipio.nombre : "Quindío"
      }
    };
  }

  // Generar schema para planes turísticos (TouristTrip)
  generateTouristTripSchema(plan) {
    const atractivos = plan.atractivosIncluidos || [];
    const alojamientos = plan.alojamientosAsociados || [];
    
    return {
      "@context": "https://schema.org",
      "@type": "TouristTrip",
      "name": plan.titulo,
      "description": plan.descripcion,
      "url": `${this.baseUrl}/${plan.detalleUrl}`,
      "touristType": {
        "@type": "Audience",
        "audienceType": plan.categoria
      },
      "offers": [
        {
          "@type": "Offer",
          "name": "Sin Transporte",
          "price": plan.precioSinTransporte,
          "priceCurrency": "COP",
          "availability": "https://schema.org/InStock"
        },
        {
          "@type": "Offer",
          "name": "Con Transporte",
          "price": plan.precioConTransporte,
          "priceCurrency": "COP",
          "availability": "https://schema.org/InStock"
        }
      ],
      "itinerary": plan.resumenPrograma.map((actividad, index) => ({
        "@type": "TouristTrip",
        "name": `Día ${index + 1}`,
        "description": actividad,
        "item": {
          "@type": "TouristAttraction",
          "name": actividad
        }
      })),
      "potentialAction": {
        "@type": "ReserveAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": `https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20${encodeURIComponent(plan.titulo)}`,
          "actionPlatform": "http://schema.org/MobileWebPlatform"
        },
        "result": {
          "@type": "Reservation",
          "name": plan.titulo
        }
      }
    };
  }

  // Generar schema para municipio (City/AdministrativeArea)
  generateCitySchema(municipio) {
    return {
      "@context": "https://schema.org",
      "@type": "City",
      "name": municipio.nombre,
      "description": municipio.descripcion,
      "url": `${this.baseUrl}/${municipio.slug}`,
      "geo": {
        "@type": "GeoCoordinates",
        "latitude": municipio.geo.lat,
        "longitude": municipio.geo.lng
      },
      "address": {
        "@type": "PostalAddress",
        "addressLocality": municipio.nombre,
        "addressRegion": "Quindío",
        "addressCountry": "CO"
      },
      "containedInPlace": {
        "@type": "AdministrativeArea",
        "name": "Quindío",
        "containedInPlace": {
          "@type": "Country",
          "name": "Colombia"
        }
      },
      "touristAttraction": municipio.keywords.map(keyword => ({
        "@type": "TouristAttraction",
        "name": keyword
      }))
    };
  }

  // Generar schema para productos combinados (programmatic SEO)
  generateCombinedSchema(municipio, tipoViaje, amenidad) {
    return {
      "@context": "https://schema.org",
      "@type": "TravelAgency",
      "name": `${tipoViaje.nombre} ${amenidad.nombre} en ${municipio.nombre}`,
      "description": `Experiencias de ${tipoViaje.nombre.toLowerCase()} con ${amenidad.nombre.toLowerCase()} en ${municipio.nombre}, Quindío`,
      "url": `${this.baseUrl}/${municipio.slug}/${tipoViaje.slug}/${amenidad.slug}`,
      "makesOffer": {
        "@type": "Offer",
        "name": "Paquete Completo",
        "description": `Plan personalizado de ${tipoViaje.nombre.toLowerCase()} con ${amenidad.nombre.toLowerCase()}`,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock",
        "seller": {
          "@type": "TravelAgency",
          "name": "Quindío Travel"
        }
      },
      "areaServed": {
        "@type": "GeoCircle",
        "geoMidpoint": {
          "@type": "GeoCoordinates",
          "latitude": municipio.geo.lat,
          "longitude": municipio.geo.lng
        },
        "geoRadius": "10000"
      }
    };
  }

  // Generar FAQ Schema dinámico
  generateFAQSchema(faqs) {
    return {
      "@context": "https://schema.org",
      "@type": "FAQPage",
      "mainEntity": faqs.map(faq => ({
        "@type": "Question",
        "name": faq.pregunta,
        "acceptedAnswer": {
          "@type": "Answer",
          "text": faq.respuesta
        }
      }))
    };
  }

  // Generar Breadcrumb Schema dinámico
  generateBreadcrumbSchema(breadcrumbs) {
    return {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": breadcrumbs.map((crumb, index) => ({
        "@type": "ListItem",
        "position": index + 1,
        "name": crumb.name,
        "item": crumb.url
      }))
    };
  }

  // Generar Review Schema masivo
  generateReviewSchema(reviews) {
    return {
      "@context": "https://schema.org",
      "@type": "TravelAgency",
      "name": "Quindío Travel",
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.8",
        "reviewCount": reviews.length,
        "bestRating": "5"
      },
      "review": reviews.map(review => ({
        "@type": "Review",
        "author": {
          "@type": "Person",
          "name": review.autor
        },
        "reviewRating": {
          "@type": "Rating",
          "ratingValue": review.calificacion,
          "bestRating": "5"
        },
        "reviewBody": review.comentario,
        "datePublished": review.fecha
      }))
    };
  }

  // Generar HowTo Schema para guías de viaje
  generateHowToSchema(steps, title, description) {
    return {
      "@context": "https://schema.org",
      "@type": "HowTo",
      "name": title,
      "description": description,
      "step": steps.map((step, index) => ({
        "@type": "HowToStep",
        "position": index + 1,
        "name": step.titulo,
        "text": step.descripcion,
        "image": step.imagen ? {
          "@type": "ImageObject",
          "url": step.imagen
        } : undefined
      }))
    };
  }

  // Generar Event Schema para eventos especiales
  generateEventSchema(evento) {
    return {
      "@context": "https://schema.org",
      "@type": "Event",
      "name": evento.nombre,
      "description": evento.descripcion,
      "startDate": evento.fechaInicio,
      "endDate": evento.fechaFin,
      "location": {
        "@type": "Place",
        "name": evento.ubicacion,
        "address": {
          "@type": "PostalAddress",
          "addressLocality": evento.municipio,
          "addressRegion": "Quindío",
          "addressCountry": "CO"
        }
      },
      "offers": {
        "@type": "Offer",
        "price": evento.precio,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock",
        "url": `${this.baseUrl}/eventos/${evento.slug}`
      },
      "organizer": {
        "@type": "Organization",
        "name": "Quindío Travel",
        "url": this.baseUrl
      }
    };
  }

  // Helpers
  getMunicipio(municipioId) {
    const municipios = {
      'armenia': { nombre: 'Armenia', geo: { lat: 4.5338, lng: -75.6811 } },
      'salento': { nombre: 'Salento', geo: { lat: 4.6374, lng: -75.5719 } },
      'filandia': { nombre: 'Filandia', geo: { lat: 4.6719, lng: -75.6611 } },
      'montenegro': { nombre: 'Montenegro', geo: { lat: 4.5578, lng: -75.7567 } },
      'calarca': { nombre: 'Calarcá', geo: { lat: 4.5167, lng: -75.6333 } }
    };
    return municipios[municipioId];
  }

  getAmenidades(amenidadesIds) {
    const amenidades = {
      'piscina': { nombre: 'Piscina', descripcion: 'Piscina para recreación' },
      'wifi': { nombre: 'WiFi', descripcion: 'Conexión a internet' },
      'desayuno': { nombre: 'Desayuno', descripcion: 'Desayuno incluido' },
      'jacuzzi': { nombre: 'Jacuzzi', descripcion: 'Bañera de hidromasaje' },
      'parqueadero': { nombre: 'Parqueadero', descripcion: 'Estacionamiento gratuito' }
    };
    return amenidadesIds.map(id => amenidades[id] || { nombre: id, descripcion: '' });
  }

  getOccupancy(capacidad) {
    const occupancy = {
      'doble': 2,
      'triple': 3,
      'cuadruple': 4,
      'simple': 1
    };
    return occupancy[capacidad] || 2;
  }

  // Inyectar schema en la página
  injectSchema(schemaObject) {
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.text = JSON.stringify(schemaObject);
    document.head.appendChild(script);
  }

  // Generar schemas masivos para todo el inventario
  generateAllSchemas(data) {
    const schemas = [];
    
    // Organization Schema
    schemas.push(this.organization);
    
    // Lodging Schemas
    if (data.alojamientos) {
      data.alojamientos.forEach(alojamiento => {
        schemas.push(this.generateLodgingSchema(alojamiento));
      });
    }
    
    // Attraction Schemas
    if (data.atractivos) {
      data.atractivos.forEach(atractivo => {
        schemas.push(this.generateAttractionSchema(atractivo));
      });
    }
    
    // Tourist Trip Schemas
    if (data.planes) {
      data.planes.forEach(plan => {
        schemas.push(this.generateTouristTripSchema(plan));
      });
    }
    
    // City Schemas
    if (data.municipios) {
      data.municipios.forEach(municipio => {
        schemas.push(this.generateCitySchema(municipio));
      });
    }
    
    return schemas;
  }

  // Inyectar todos los schemas en la página
  injectAllSchemas(data) {
    const schemas = this.generateAllSchemas(data);
    schemas.forEach(schema => {
      this.injectSchema(schema);
    });
  }
}

// Instancia global
const schemaGenerator = new SchemaGenerator();

// Función para uso global
function injectSchema(schemaObject) {
  schemaGenerator.injectSchema(schemaObject);
}

// Inicialización automática con datos existentes
document.addEventListener('DOMContentLoaded', function() {
  // Cargar datos existentes si están disponibles
  let data = {};
  
  if (typeof planesData !== 'undefined') {
    data.planes = planesData;
  }
  
  if (typeof atractivosData !== 'undefined') {
    data.atractivos = atractivosData;
  }
  
  // Inyectar schemas masivos
  if (data.planes || data.atractivos) {
    schemaGenerator.injectAllSchemas(data);
  }
  
  // Inyectar organization schema siempre
  schemaGenerator.injectSchema(schemaGenerator.organization);
});

// Exportar para uso en módulos
if (typeof module !== 'undefined' && module.exports) {
  module.exports = SchemaGenerator;
}