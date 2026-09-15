/**
 * Quindío Travel Schema.org Generator v2
 * Tipos correctos: TravelAgency, TouristTrip, LodgingBusiness, TouristAttraction
 * Sin ratings fabricados — AggregateRating solo con datos reales verificables
 */

class SchemaGenerator {
  constructor() {
    this.baseUrl = 'https://quindiotravel.com.co';
  }

  // ── Organization / LocalBusiness ──────────────────────────────
  // Se usa en TODAS las páginas como schema base
  generateOrganizationSchema() {
    return {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "@id": `${this.baseUrl}/#organization`,
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
        "@type": "State",
        "name": "Quindío, Colombia"
      },
      "founder": {
        "@type": "Person",
        "name": "Álvaro Alzate Ortiz",
        "jobTitle": "Gerente General"
      },
      "foundingDate": "2010",
      "priceRange": "$$",
      "currenciesAccepted": "COP",
      "paymentAccepted": ["Cash", "Credit Card", "Bank Transfer"],
      "openingHoursSpecification": {
        "@type": "OpeningHoursSpecification",
        "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "opens": "08:00",
        "closes": "20:00"
      },
      "sameAs": [
        "https://www.facebook.com/quindiotravel",
        "https://www.instagram.com/quindiotravel",
        "https://www.tiktok.com/@quindiotravel"
      ],
      "logo": `${this.baseUrl}/logo_quindio_travel.png`,
      "image": `${this.baseUrl}/assets/images/paisajes/eje-cafetero-aerial-view.webp`
    };
  }

  // ── WebSite + SearchAction (Sitelinks Searchbox) ──────────────
  generateWebSiteSchema() {
    return {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Quindío Travel",
      "url": this.baseUrl,
      "potentialAction": {
        "@type": "SearchAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": `${this.baseUrl}/index.html?q={search_term_string}`
        },
        "query-input": "required name=search_term_string"
      }
    };
  }

  // ── TouristTrip (para paquetes turísticos) ────────────────────
  generateTouristTripSchema(plan) {
    const offers = [];
    if (plan.precioSinTransporte) {
      offers.push({
        "@type": "Offer",
        "name": "Sin Transporte",
        "price": plan.precioSinTransporte,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock"
      });
    }
    if (plan.precioConTransporte) {
      offers.push({
        "@type": "Offer",
        "name": "Con Transporte",
        "price": plan.precioConTransporte,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock"
      });
    }

    const schema = {
      "@context": "https://schema.org",
      "@type": "TouristTrip",
      "name": plan.titulo,
      "description": plan.descripcion,
      "url": `${this.baseUrl}/${plan.detalleUrl}`,
      "touristType": plan.categoria || "Turista",
      "offers": offers.length > 0 ? offers : undefined,
      "itinerary": {
        "@type": "ItemList",
        "name": "Itinerario",
        "itemListElement": (plan.resumenPrograma || []).map((actividad, index) => ({
          "@type": "ListItem",
          "position": index + 1,
          "name": actividad
        }))
      },
      "potentialAction": {
        "@type": "ReserveAction",
        "target": {
          "@type": "EntryPoint",
          "urlTemplate": `https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20estoy%20interesado%20en%20${encodeURIComponent(plan.titulo)}`,
          "actionPlatform": "http://schema.org/MobileWebPlatform"
        }
      }
    };

    return schema;
  }

  // ── LodgingBusiness / VacationRental (para alojamientos) ──────
  generateLodgingSchema(alojamiento) {
    const municipio = this.getMunicipio(alojamiento.municipio);

    return {
      "@context": "https://schema.org",
      "@type": alojamiento.tipo === "Finca Hotel" ? "VacationRental" : "LodgingBusiness",
      "name": alojamiento.nombre,
      "description": alojamiento.descripcion,
      "url": `${this.baseUrl}/generated-pages/alojamiento/${alojamiento.slug}.html`,
      "telephone": "+573174426044",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": municipio ? municipio.nombre : "Quindío",
        "addressRegion": "Quindío",
        "addressCountry": "CO"
      },
      "geo": municipio ? {
        "@type": "GeoCoordinates",
        "latitude": municipio.geo.lat,
        "longitude": municipio.geo.lng
      } : undefined,
      "starRating": alojamiento.rating ? {
        "@type": "Rating",
        "ratingValue": alojamiento.rating,
        "bestRating": "5"
      } : undefined,
      "priceRange": alojamiento.precioDesde ? `$${alojamiento.precioDesde.toLocaleString()} COP` : undefined,
      "amenityFeature": (alojamiento.amenidades || []).map(a => ({
        "@type": "LocationFeatureSpecification",
        "name": a,
        "value": true
      })),
      "makesOffer": alojamiento.precioDesde ? {
        "@type": "Offer",
        "price": alojamiento.precioDesde,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock"
      } : undefined
    };
  }

  // ── TouristAttraction (para atractivos turísticos) ────────────
  generateAttractionSchema(atractivo) {
    const municipio = this.getMunicipio(atractivo.municipio);

    const schema = {
      "@context": "https://schema.org",
      "@type": "TouristAttraction",
      "name": atractivo.nombre,
      "description": atractivo.descripcion,
      "url": `${this.baseUrl}/generated-pages/atractivo/${atractivo.slug}.html`,
      "touristType": (atractivo.idealPara || []).join(', '),
      "isAccessibleForFree": !atractivo.precio || atractivo.precio === 0,
      "address": {
        "@type": "PostalAddress",
        "addressLocality": municipio ? municipio.nombre : "Quindío",
        "addressRegion": "Quindío",
        "addressCountry": "CO"
      },
      "geo": municipio ? {
        "@type": "GeoCoordinates",
        "latitude": municipio.geo.lat,
        "longitude": municipio.geo.lng
      } : undefined
    };

    if (atractivo.precio > 0) {
      schema.offers = {
        "@type": "Offer",
        "price": atractivo.precio,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock"
      };
    }

    return schema;
  }

  // ── City (para páginas de municipios) ─────────────────────────
  generateCitySchema(municipio) {
    return {
      "@context": "https://schema.org",
      "@type": "City",
      "name": municipio.nombre,
      "description": municipio.descripcion,
      "url": `${this.baseUrl}/${municipio.slug}.html`,
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
        "@type": "State",
        "name": "Quindío",
        "containedInPlace": {
          "@type": "Country",
          "name": "Colombia"
        }
      }
    };
  }

  // ── FAQPage (únicos por página — NUNCA genéricos) ─────────────
  generateFAQSchema(faqs) {
    if (!faqs || faqs.length === 0) return null;

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

  // ── BreadcrumbList (para navegación) ──────────────────────────
  generateBreadcrumbSchema(items) {
    if (!items || items.length === 0) return null;

    return {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": items.map((item, index) => ({
        "@type": "ListItem",
        "position": index + 1,
        "name": item.name,
        "item": item.url ? `${this.baseUrl}${item.url}` : undefined
      }))
    };
  }

  // ── AggregateRating (solo si hay datos reales) ────────────────
  // NO fabricar ratings — esto viola las políticas de Google
  generateAggregateRatingSchema(ratingValue, reviewCount, bestRating = 5) {
    if (!ratingValue || !reviewCount || reviewCount < 1) return null;

    return {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "@id": `${this.baseUrl}/#organization`,
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": ratingValue,
        "reviewCount": reviewCount,
        "bestRating": bestRating,
        "worstRating": 1
      }
    };
  }

  // ── HowTo (para guías de viaje) ──────────────────────────────
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
        "text": step.descripcion
      }))
    };
  }

  // ── Event (para eventos especiales) ──────────────────────────
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
        "price": evento.precio || 0,
        "priceCurrency": "COP",
        "availability": "https://schema.org/InStock"
      },
      "organizer": {
        "@type": "LocalBusiness",
        "name": "Quindío Travel",
        "url": this.baseUrl
      }
    };
  }

  // ── Helpers ──────────────────────────────────────────────────

  getMunicipio(municipioId) {
    const municipios = {
      'armenia': { nombre: 'Armenia', geo: { lat: 4.5338, lng: -75.6811 } },
      'salento': { nombre: 'Salento', geo: { lat: 4.6374, lng: -75.5719 } },
      'filandia': { nombre: 'Filandia', geo: { lat: 4.6719, lng: -75.6611 } },
      'montenegro': { nombre: 'Montenegro', geo: { lat: 4.5578, lng: -75.7567 } },
      'calarca': { nombre: 'Calarcá', geo: { lat: 4.5167, lng: -75.6333 } },
      'buenavista': { nombre: 'Buenavista', geo: { lat: 4.5564, lng: -75.7392 } },
      'cordoba': { nombre: 'Córdoba', geo: { lat: 4.3925, lng: -75.6869 } },
      'pijao': { nombre: 'Pijao', geo: { lat: 4.3372, lng: -75.7000 } },
      'genova': { nombre: 'Génova', geo: { lat: 4.3167, lng: -75.7833 } },
      'la-tebaida': { nombre: 'La Tebaida', geo: { lat: 4.4531, lng: -75.7833 } }
    };
    return municipios[municipioId] || null;
  }

  // ── Inyección en DOM ─────────────────────────────────────────

  injectSchema(schemaObject) {
    if (!schemaObject) return;
    const script = document.createElement('script');
    script.type = 'application/ld+json';
    script.text = JSON.stringify(schemaObject, null, 2);
    document.head.appendChild(script);
  }

  // Inyectar schema base (Organization + WebSite) en todas las páginas
  injectBaseSchemas() {
    this.injectSchema(this.generateOrganizationSchema());
    this.injectSchema(this.generateWebSiteSchema());
  }
}

// Instancia global
const schemaGenerator = new SchemaGenerator();

function injectSchema(schemaObject) {
  schemaGenerator.injectSchema(schemaObject);
}
