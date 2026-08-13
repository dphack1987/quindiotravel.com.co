/* ==========================================================================
   QUINDÍO TRAVEL - LÓGICA DEL COTIZADOR DINÁMICO MEJORADO
   ========================================================================== */

const DESTINOS_PRECIOS = {
  'valle-cocora': 85000,
  'salento': 45000,
  'filandia': 40000,
  'panaca': 65000,
  'recuca': 55000,
  'termales': 75000,
  'mariposario': 35000,
  'cafe-tour': 50000
};

function runWhenReady(callback) {
    if (document.readyState === 'complete' || document.readyState === 'interactive') {
        callback();
    } else {
        document.addEventListener('DOMContentLoaded', callback, { once: true });
    }
}

window.QUINDIO_TRAVEL_DATA_LOADED = fetch('docs/data/tarifas.json')
    .then(response => response.json())
    .then(data => {
        window.QUINDIO_TRAVEL_DATA = data;
        runWhenReady(actualizarUI); // Ejecutar cálculo inicial después de que DOM y datos estén listos
        return data;
    })
    .catch(error => {
        console.error('Error al cargar tarifas:', error);
        runWhenReady(actualizarUI);
        return null;
    });

function obtenerPrecioOficial(planKey, categoria) {
  if (!window.QUINDIO_TRAVEL_DATA || !window.QUINDIO_TRAVEL_DATA.tarifasOficiales) {
    return null;
  }
  if (!planKey || !categoria) return null;
  const planData = window.QUINDIO_TRAVEL_DATA.tarifasOficiales[planKey];
  return planData ? planData[categoria] || null : null;
}

window.obtenerPrecioOficial = obtenerPrecioOficial;

function calcularCotizacion(plan, categoria, paxCount, destinosSeleccionados, ocupacion = 'individual', incluirTransporte = false) {
  if (!window.QUINDIO_TRAVEL_DATA || !window.QUINDIO_TRAVEL_DATA.tarifasOficiales) {
    return { error: "La base de datos de tarifas no está cargada." };
  }

  const data = window.QUINDIO_TRAVEL_DATA.tarifasOficiales;
  
  if (!data[plan]) {
    return { error: "Datos no encontrados para el plan seleccionado." };
  }

  let precioPorPersona;
  
  // Si se incluye transporte y no es individual, usar precios con transporte
  if (incluirTransporte && ocupacion !== 'individual' && data[plan].precios_con_transporte) {
    const preciosTransporte = data[plan].precios_con_transporte[categoria];
    if (preciosTransporte && preciosTransporte[ocupacion]) {
      precioPorPersona = preciosTransporte[ocupacion];
    } else {
      // Fallback a precio sin transporte si no hay precio con transporte disponible
      precioPorPersona = data[plan][categoria];
    }
  } else {
    // Usar precio sin transporte
    precioPorPersona = data[plan][categoria];
  }

  if (!precioPorPersona) {
    return { error: "No hay tarifa disponible para esta combinación." };
  }

  const totalPlan = precioPorPersona * paxCount;
  
  // Los destinos adicionales ahora son solo para selección visual, no afectan el precio
  let totalDestinos = 0;
  let destinosCount = 0;
  
  if (destinosSeleccionados && destinosSeleccionados.length > 0) {
    destinosCount = destinosSeleccionados.length;
    // Ya no se calculan precios de destinos adicionales
  }

  const total = totalPlan + totalDestinos;

  return {
    precioPorPersona: precioPorPersona,
    totalPlan: total,
    moneda: "COP",
    formateadoPersona: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(precioPorPersona),
    formateadoTotal: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(total),
    destinosExtra: destinosCount,
    ocupacion: ocupacion,
    incluyeTransporte: incluirTransporte
  };
}

// Actualizar la interfaz si los elementos existen en el DOM
function actualizarUI() {
  const selectPlan = document.getElementById('select-plan');
  const selectCategoria = document.getElementById('select-categoria');
  const selectPax = document.getElementById('select-pax');
  const selectDestinos = document.getElementById('select-destinos');
  const selectOcupacion = document.getElementById('select-ocupacion');
  const checkTransporte = document.getElementById('check-transporte');

  const displayPersona = document.getElementById('precio-persona');
  const displayTotal = document.getElementById('precio-total');
  const displayDestinos = document.getElementById('destinos-extra');
  const whatsappBtn = document.getElementById('cotizador-whatsapp-btn');

  if (!selectPlan || !selectCategoria || !selectPax) return;

  // Obtener ocupación (por defecto individual)
  const ocupacion = selectOcupacion ? selectOcupacion.value : 'individual';
  
  // Obtener si incluye transporte (por defecto false)
  const incluirTransporte = checkTransporte ? checkTransporte.checked : false;

  // Obtener destinos seleccionados si el elemento existe
  let destinosSeleccionados = [];
  let destinosNombres = [];
  if (selectDestinos) {
    if (selectDestinos.tagName === 'SELECT') {
      for (let i = 0; i < selectDestinos.options.length; i++) {
        if (selectDestinos.options[i].selected) {
          destinosSeleccionados.push(selectDestinos.options[i].value);
          destinosNombres.push(selectDestinos.options[i].text);
        }
      }
    } else {
      const checks = selectDestinos.querySelectorAll('input[type="checkbox"]:checked');
      checks.forEach(check => {
        destinosSeleccionados.push(check.value);
        destinosNombres.push(check.nextElementSibling.textContent);
      });
    }
  }

  const res = calcularCotizacion(
    selectPlan.value,
    selectCategoria.value,
    parseInt(selectPax.value),
    destinosSeleccionados,
    ocupacion,
    incluirTransporte
  );

  if (res.error) {
    if (displayPersona) displayPersona.innerText = "N/A";
    if (displayTotal) displayTotal.innerText = "Consulte con un asesor";
    if (displayDestinos) displayDestinos.innerText = "";
  } else {
    if (displayPersona) displayPersona.innerText = res.formateadoPersona;
    if (displayTotal) displayTotal.innerText = res.formateadoTotal;
    if (displayDestinos && res.destinosExtra > 0) {
      displayDestinos.innerText = `+ ${res.destinosExtra} destinos adicionales`;
    } else if (displayDestinos) {
      displayDestinos.innerText = "";
    }
  }

  // Actualizar mensaje de WhatsApp con destinos seleccionados
  if (whatsappBtn) {
    const planNombre = selectPlan.options[selectPlan.selectedIndex].text;
    const categoriaNombre = selectCategoria.options[selectCategoria.selectedIndex].text;
    const paxCount = selectPax.value;
    const ocupacionNombre = selectOcupacion ? selectOcupacion.options[selectOcupacion.selectedIndex].text : 'Individual';
    
    let mensaje = `Hola Quindío Travel 🌿, deseo cotizar el ${planNombre} para ${paxCount} personas.\n`;
    mensaje += `Categoría de alojamiento: ${categoriaNombre}\n`;
    mensaje += `Ocupación: ${ocupacionNombre}\n`;
    
    if (incluirTransporte) {
      mensaje += `✅ Incluye transporte completo\n`;
    }
    
    if (destinosNombres.length > 0) {
      mensaje += `Destinos adicionales seleccionados: ${destinosNombres.join(', ')}\n`;
    }
    
    mensaje += `Precio estimado: ${res.formateadoTotal}\n`;
    mensaje += `¿Podrían ayudarme con la disponibilidad y confirmación?`;
    
    whatsappBtn.href = `https://wa.me/573174426044?text=${encodeURIComponent(mensaje)}`;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const inputs = ['select-plan', 'select-categoria', 'select-pax', 'select-destinos', 'select-ocupacion', 'check-transporte'];
  inputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', actualizarUI);
  });
  // No ejecutar actualizarUI() inmediatamente, esperar a que carguen los datos del JSON
});

console.log("Módulo de Cotizaciones Quindío Travel mejorado cargado y listo para interactuar.");
