/* ==========================================================================
   QUINDÍO TRAVEL - LÓGICA DEL COTIZADOR DINÁMICO MEJORADO
   ========================================================================== */

// Cargar tarifas desde docs/data/tarifas.json
fetch('docs/data/tarifas.json')
    .then(response => response.json())
    .then(data => {
        window.QUINDIO_TRAVEL_DATA = data;
        actualizarUI(); // Ejecutar cálculo inicial después de cargar datos
    })
    .catch(error => {
        console.error('Error al cargar tarifas:', error);
        // Usar datos fallback que están en planes.html si falla la carga
        actualizarUI();
    });

function calcularCotizacion(temporada, transporte, hotelId, paxCount, destinosSeleccionados) {
  if (typeof QUINDIO_TRAVEL_DATA === 'undefined') {
    return { error: "La base de datos de tarifas no está cargada." };
  }

  const data = QUINDIO_TRAVEL_DATA.tarifasPlan4D3N;
  
  // Usar solo sin_transporte para cotizaciones básicas
  const transportType = "sin_transporte";
  
  if (!data[transportType] || !data[transportType][hotelId]) {
    return { error: "Datos no encontrados para la combinación seleccionada." };
  }

  const keyPax = "pax" + paxCount;
  const precioPorPersona = data[transportType][hotelId][keyPax];

  if (!precioPorPersona) {
    return { error: "No hay tarifa disponible para este número de pasajeros (tarifa pendiente de definir)." };
  }

  let total = precioPorPersona * paxCount;
  
  // Ajustar por destinos adicionales seleccionados
  if (destinosSeleccionados && destinosSeleccionados.length > 0) {
    const precioPorDestino = 85000; // Precio adicional por destino
    const totalDestinos = precioPorDestino * destinosSeleccionados.length * paxCount;
    total += totalDestinos;
  }

  return {
    precioPorPersona: precioPorPersona,
    totalPlan: total,
    moneda: "COP",
    formateadoPersona: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(precioPorPersona),
    formateadoTotal: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(total),
    destinosExtra: destinosSeleccionados ? destinosSeleccionados.length : 0
  };
}

// Actualizar la interfaz si los elementos existen en el DOM
function actualizarUI() {
  const selectCategoria = document.getElementById('select-categoria');
  const selectPax = document.getElementById('select-pax');
  const selectDestinos = document.getElementById('select-destinos');

  const displayPersona = document.getElementById('precio-persona');
  const displayTotal = document.getElementById('precio-total');
  const displayDestinos = document.getElementById('destinos-extra');

  if (!selectCategoria || !selectPax) return;

  // Obtener destinos seleccionados si el elemento existe
  let destinosSeleccionados = [];
  if (selectDestinos) {
    for (let i = 0; i < selectDestinos.options.length; i++) {
      if (selectDestinos.options[i].selected) {
        destinosSeleccionados.push(selectDestinos.options[i].value);
      }
    }
  }

  const res = calcularCotizacion(
    'sin_transporte',
    'sin_transporte',
    selectCategoria.value,
    parseInt(selectPax.value),
    destinosSeleccionados
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
}

document.addEventListener('DOMContentLoaded', () => {
  const inputs = ['select-categoria', 'select-pax', 'select-destinos'];
  inputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', actualizarUI);
  });
  // No ejecutar actualizarUI() inmediatamente, esperar a que carguen los datos del JSON
});

console.log("Módulo de Cotizaciones Quindío Travel mejorado cargado y listo para interactuar.");
