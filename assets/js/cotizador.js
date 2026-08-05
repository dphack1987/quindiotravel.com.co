/* ==========================================================================
   QUINDÍO TRAVEL - LÓGICA DEL COTIZADOR DINÁMICO MEJORADO
   ========================================================================== */

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

function calcularCotizacion(plan, categoria, paxCount, destinosSeleccionados) {
  if (!window.QUINDIO_TRAVEL_DATA || !window.QUINDIO_TRAVEL_DATA.tarifasOficiales) {
    return { error: "La base de datos de tarifas no está cargada." };
  }

  const data = window.QUINDIO_TRAVEL_DATA.tarifasOficiales;
  
  if (!data[plan] || !data[plan][categoria]) {
    return { error: "Datos no encontrados para la combinación seleccionada." };
  }

  const precioPorPersona = data[plan][categoria];

  if (!precioPorPersona) {
    return { error: "No hay tarifa disponible para esta combinación." };
  }

  const totalPlan = precioPorPersona * paxCount;
  const total = totalPlan;

  return {
    precioPorPersona: precioPorPersona,
    totalPlan: total,
    moneda: "COP",
    formateadoPersona: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(precioPorPersona),
    formateadoTotal: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(total),
    destinosExtra: 0
  };
}

// Actualizar la interfaz si los elementos existen en el DOM
function actualizarUI() {
  const selectPlan = document.getElementById('select-plan');
  const selectCategoria = document.getElementById('select-categoria');
  const selectPax = document.getElementById('select-pax');
  const selectDestinos = document.getElementById('select-destinos');

  const displayPersona = document.getElementById('precio-persona');
  const displayTotal = document.getElementById('precio-total');
  const displayDestinos = document.getElementById('destinos-extra');

  if (!selectPlan || !selectCategoria || !selectPax) return;

  // Obtener destinos seleccionados si el elemento existe
  const res = calcularCotizacion(
    selectPlan.value,
    selectCategoria.value,
    parseInt(selectPax.value),
    []
  );

  if (res.error) {
    if (displayPersona) displayPersona.innerText = "N/A";
    if (displayTotal) displayTotal.innerText = "Consulte con un asesor";
    if (displayDestinos) displayDestinos.innerText = "";
  } else {
    if (displayPersona) displayPersona.innerText = res.formateadoPersona;
    if (displayTotal) displayTotal.innerText = res.formateadoTotal;
    if (displayDestinos) displayDestinos.innerText = "";
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const inputs = ['select-plan', 'select-categoria', 'select-pax', 'select-destinos'];
  inputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', actualizarUI);
  });
  // No ejecutar actualizarUI() inmediatamente, esperar a que carguen los datos del JSON
});

console.log("Módulo de Cotizaciones Quindío Travel mejorado cargado y listo para interactuar.");
