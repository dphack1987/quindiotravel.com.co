/**
 * Quindío Travel WhatsApp Payload Builder
 * Sistema de deep-linking dinámico para conversión cero fricción
 * Genera payloads preformateados para WhatsApp con información completa
 */

class WhatsAppPayloadBuilder {
  constructor() {
    this.phoneNumber = '573174426044';
    this.baseUrl = 'https://wa.me/';
    this.masterData = this.loadMasterData();
  }

  loadMasterData() {
    // Intentar cargar datos existentes
    try {
      if (typeof planesData !== 'undefined') {
        return { planes: planesData };
      }
    } catch (e) {
      console.log('No se encontraron datos de planes, usando estructura por defecto');
    }
    
    return {
      planes: [],
      alojamientos: [],
      atractivos: []
    };
  }

  escapeText(text) {
    return encodeURIComponent(text)
      .replace(/%20/g, ' ')
      .replace(/%2C/g, ',')
      .replace(/%3A/g, ':')
      .replace(/%0A/g, '\n');
  }

  buildBasicPayload(message) {
    return `${this.baseUrl}${this.phoneNumber}?text=${this.escapeText(message)}`;
  }

  buildPlanPayload(planId, options = {}) {
    const plan = this.masterData.planes.find(p => p.id === planId);
    if (!plan) return this.buildBasicPayload('Hola, estoy interesado en un plan turístico');

    const {
      fechaInicio = '',
      fechaFin = '',
      numPersonas = '',
      tipoAlojamiento = '',
      incluirTransporte = true
    } = options;

    let message = `🌟 *COTIZACIÓN PLAN TURÍSTICO*\n\n`;
    message += `📋 *Plan:* ${plan.titulo}\n`;
    message += `⏱️ *Duración:* ${plan.dias} días / ${plan.noches} noches\n`;
    message += `📍 *Destino:* Eje Cafetero - Quindío\n`;
    
    if (plan.descripcion) {
      message += `📝 *Descripción:* ${plan.descripcion}\n`;
    }
    
    if (plan.atractivosIncluidos && plan.atractivosIncluidos.length > 0) {
      message += `🎯 *Incluye:* ${plan.atractivosIncluidos.join(', ')}\n`;
    }
    
    message += `\n💰 *Precio:* `;
    if (incluirTransporte && plan.precioConTransporte) {
      message += `$${plan.precioConTransporte.toLocaleString()} (con transporte)`;
    } else if (plan.precioSinTransporte) {
      message += `$${plan.precioSinTransporte.toLocaleString()} (sin transporte)`;
    }
    message += ` por persona\n\n`;
    
    if (fechaInicio) message += `📅 *Fecha inicio:* ${fechaInicio}\n`;
    if (fechaFin) message += `📅 *Fecha fin:* ${fechaFin}\n`;
    if (numPersonas) message += `👥 *Personas:* ${numPersonas}\n`;
    if (tipoAlojamiento) message += `🏨 *Tipo alojamiento:* ${tipoAlojamiento}\n`;
    
    message += `\n✅ *CONFIRME DISPONIBILIDAD Y RESERVA*\n`;
    message += `RNT 18152 - Quindío Travel`;

    return this.buildBasicPayload(message);
  }

  buildAlojamientoPayload(alojamientoId, options = {}) {
    const { fechaInicio = '', fechaFin = '', numPersonas = '', numHabitaciones = '' } = options;
    
    // Datos de alojamientos desde el master data
    const alojamientos = {
      'cabanas-la-esmeralda': {
        nombre: 'Cabañas La Esmeralda',
        ubicacion: 'Salento, Quindío',
        descripcion: 'Cabañas tradicionales con vistas al Valle de Cocora',
        precioDesde: 1479000
      },
      'hotel-campestre-los-girasoles': {
        nombre: 'Hotel Campestre Los Girasoles',
        ubicacion: 'Filandia, Quindío',
        descripcion: 'Hotel campestre con zonas verdes y vistas panorámicas',
        precioDesde: 1915000
      },
      'hotel-campestre-cafe-cafe': {
        nombre: 'Hotel Campestre Café Café',
        ubicacion: 'Armenia, Quindío',
        descripcion: 'Hotel temático cafetero con arquitectura colonial',
        precioDesde: 2097000
      }
    };

    const alojamiento = alojamientos[alojamientoId] || {
      nombre: 'Alojamiento en el Eje Cafetero',
      ubicacion: 'Quindío',
      descripcion: 'Experiencia auténtica en el corazón del café',
      precioDesde: 1500000
    };

    let message = `🏨 *COTIZACIÓN ALOJAMIENTO*\n\n`;
    message += `🏠 *Nombre:* ${alojamiento.nombre}\n`;
    message += `📍 *Ubicación:* ${alojamiento.ubicacion}\n`;
    message += `📝 *Descripción:* ${alojamiento.descripcion}\n`;
    message += `💰 *Precio desde:* $${alojamiento.precioDesde.toLocaleString()}\n\n`;
    
    if (fechaInicio) message += `📅 *Check-in:* ${fechaInicio}\n`;
    if (fechaFin) message += `📅 *Check-out:* ${fechaFin}\n`;
    if (numPersonas) message += `👥 *Personas:* ${numPersonas}\n`;
    if (numHabitaciones) message += `🛏️ *Habitaciones:* ${numHabitaciones}\n`;
    
    message += `\n✅ *CONFIRME DISPONIBILIDAD*\n`;
    message += `RNT 18152 - Quindío Travel`;

    return this.buildBasicPayload(message);
  }

  buildCustomPayload(params) {
    const {
      tipoViaje = '',
      destino = '',
      fechaInicio = '',
      fechaFin = '',
      numPersonas = '',
      presupuesto = '',
      amenidades = [],
      mensajeAdicional = ''
    } = params;

    let message = `🌟 *COTIZACIÓN PERSONALIZADA*\n\n`;
    
    if (tipoViaje) message += `🎯 *Tipo de viaje:* ${tipoViaje}\n`;
    if (destino) message += `📍 *Destino:* ${destino}\n`;
    if (fechaInicio) message += `📅 *Fecha inicio:* ${fechaInicio}\n`;
    if (fechaFin) message += `📅 *Fecha fin:* ${fechaFin}\n`;
    if (numPersonas) message += `👥 *Personas:* ${numPersonas}\n`;
    if (presupuesto) message += `💰 *Presupuesto:* ${presupuesto}\n`;
    
    if (amenidades.length > 0) {
      message += `✨ *Amenidades deseadas:* ${amenidades.join(', ')}\n`;
    }
    
    if (mensajeAdicional) {
      message += `\n📝 *Mensaje adicional:* ${mensajeAdicional}\n`;
    }
    
    message += `\n✅ *ENVIE COTIZACIÓN COMPLETA*\n`;
    message += `RNT 18152 - Quindío Travel`;

    return this.buildBasicPayload(message);
  }

  buildPromoPayload(promoNombre, promoPrecio, promoDetalles) {
    let message = `🔥 *PROMOCIÓN ESPECIAL*\n\n`;
    message += `🎉 *Promoción:* ${promoNombre}\n`;
    message += `💰 *Precio:* $${promoPrecio.toLocaleString()}\n`;
    message += `📝 *Detalles:* ${promoDetalles}\n\n`;
    message += `⏰ *¡OFERTA POR TIEMPO LIMITADO!*\n\n`;
    message += `✅ *RESERVA AHORA ESTA PROMOCIÓN*\n`;
    message += `RNT 18152 - Quindío Travel`;

    return this.buildBasicPayload(message);
  }

  // Método para formularios dinámicos
  buildFromForm(formElement) {
    const formData = new FormData(formElement);
    const params = {};
    
    for (let [key, value] of formData.entries()) {
      params[key] = value;
    }
    
    return this.buildCustomPayload(params);
  }

  // Método para botones de reserva rápida
  buildQuickReservation(planId, numPersonas = 2) {
    return this.buildPlanPayload(planId, {
      numPersonas: numPersonas,
      incluirTransporte: true
    });
  }

  // Método para integración con selector de fechas
  buildWithDateRange(planId, startDate, endDate, numPersonas = 2) {
    return this.buildPlanPayload(planId, {
      fechaInicio: startDate,
      fechaFin: endDate,
      numPersonas: numPersonas,
      incluirTransporte: true
    });
  }

  // Método para compartir planes
  buildShareableLink(planId, customMessage = '') {
    const plan = this.masterData.planes.find(p => p.id === planId);
    if (!plan) return this.buildBasicPayload('Mira este plan turístico de Quindío Travel');

    let message = customMessage || `🌟 Mira este plan increíble: ${plan.titulo}\n\n`;
    message += `${plan.descripcion}\n`;
    message += `💰 Desde $${plan.precioSinTransporte.toLocaleString()} por persona\n\n`;
    message += `Reserva con Quindío Travel - RNT 18152`;

    return this.buildBasicPayload(message);
  }

  // Método para tracking de conversión
  trackConversion(type, planId, metadata = {}) {
    // Enviar evento a analytics
    if (typeof gtag !== 'undefined') {
      gtag('event', 'conversion', {
        'send_to': 'AW-CONVERSION_ID',
        'value': metadata.precio || 0,
        'currency': 'COP',
        'transaction_id': `${type}_${planId}_${Date.now()}`
      });
    }
    
    console.log('Conversión registrada:', { type, planId, metadata });
  }

  // Método para generar enlace con tracking
  buildTrackedLink(type, planId, payloadParams) {
    let link;
    
    switch(type) {
      case 'plan':
        link = this.buildPlanPayload(planId, payloadParams);
        break;
      case 'alojamiento':
        link = this.buildAlojamientoPayload(planId, payloadParams);
        break;
      case 'custom':
        link = this.buildCustomPayload(payloadParams);
        break;
      case 'promo':
        link = this.buildPromoPayload(planId, payloadParams.precio, payloadParams.detalles);
        break;
      default:
        link = this.buildBasicPayload('Hola, estoy interesado en cotizar un viaje');
    }
    
    // Agregar parámetros de tracking
    const trackingParams = new URLSearchParams();
    trackingParams.append('utm_source', 'whatsapp');
    trackingParams.append('utm_medium', 'referral');
    trackingParams.append('utm_campaign', type);
    trackingParams.append('utm_content', planId);
    
    const separator = link.includes('?') ? '&' : '?';
    return link + separator + trackingParams.toString();
  }
}

// Instancia global
const whatsappBuilder = new WhatsAppPayloadBuilder();

// Funciones helper para uso global
function buildWhatsAppLink(type, id, options = {}) {
  return whatsappBuilder.buildTrackedLink(type, id, options);
}

function openWhatsApp(type, id, options = {}) {
  const link = buildWhatsAppLink(type, id, options);
  window.open(link, '_blank');
  
  // Registrar conversión
  whatsappBuilder.trackConversion(type, id, options);
}

// Integración con botones existentes
document.addEventListener('DOMContentLoaded', function() {
  // Actualizar todos los botones de WhatsApp existentes
  const whatsappButtons = document.querySelectorAll('a[href*="wa.me"], a[href*="whatsapp"]');
  
  whatsappButtons.forEach(button => {
    const originalHref = button.getAttribute('href');
    
    // Si el botón ya tiene parámetros personalizados, no modificarlo
    if (originalHref.includes('text=')) return;
    
    // Agregar parámetros de tracking
    button.addEventListener('click', function(e) {
      const planId = this.getAttribute('data-plan-id') || '';
      const type = this.getAttribute('data-type') || 'custom';
      
      if (planId) {
        e.preventDefault();
        openWhatsApp(type, planId, {
          mensajeAdicional: 'Vengo de la página web'
        });
      }
    });
  });
  
  // Inicializar formularios de cotización rápida
  const quickQuoteForms = document.querySelectorAll('.quick-quote-form');
  quickQuoteForms.forEach(form => {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      const link = whatsappBuilder.buildFromForm(form);
      window.open(link, '_blank');
    });
  });
});

// Exportar para uso en módulos
if (typeof module !== 'undefined' && module.exports) {
  module.exports = WhatsAppPayloadBuilder;
}