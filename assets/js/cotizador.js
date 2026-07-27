/* ==========================================================================
   QUINDÍO TRAVEL - LÓGICA DEL COTIZADOR DINÁMICO
   ========================================================================== */

// Cargar tarifas desde docs/data/tarifas.json
fetch('/docs/data/tarifas.json')
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

function calcularCotizacion(temporada, transporte, hotelId, paxCount) {
  if (typeof QUINDIO_TRAVEL_DATA === 'undefined') {
    return { error: "La base de datos de tarifas no está cargada." };
  }

  const data = QUINDIO_TRAVEL_DATA.tarifasPlan4D3N;
  
  if (!data[temporada] || !data[temporada][transporte] || !data[temporada][transporte][hotelId]) {
    return { error: "Datos no encontrados para la combinación seleccionada." };
  }

  const keyPax = "pax" + paxCount;
  const precioPorPersona = data[temporada][transporte][hotelId][keyPax];

  if (!precioPorPersona) {
    return { error: "No hay tarifa disponible para este número de pasajeros (tarifa pendiente de definir)." };
  }

  const total = precioPorPersona * paxCount;

  return {
    precioPorPersona: precioPorPersona,
    totalPlan: total,
    moneda: "COP",
    formateadoPersona: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(precioPorPersona),
    formateadoTotal: new Intl.NumberFormat('es-CO', { style: 'currency', currency: 'COP', maximumFractionDigits: 0 }).format(total)
  };
}

// Actualizar la interfaz si los elementos existen en el DOM
function actualizarUI() {
  const selectTemporada = document.getElementById('select-temporada');
  const selectTransporte = document.getElementById('select-transporte');
  const selectHotel = document.getElementById('select-hotel');
  const selectPax = document.getElementById('select-pax');

  const displayPersona = document.getElementById('precio-persona');
  const displayTotal = document.getElementById('precio-total');

  if (!selectTemporada || !selectTransporte || !selectHotel || !selectPax) return;

  const res = calcularCotizacion(
    selectTemporada.value,
    selectTransporte.value,
    selectHotel.value,
    parseInt(selectPax.value)
  );

  if (res.error) {
    if (displayPersona) displayPersona.innerText = "N/A";
    if (displayTotal) displayTotal.innerText = "Consulte con un asesor";
  } else {
    if (displayPersona) displayPersona.innerText = res.formateadoPersona;
    if (displayTotal) displayTotal.innerText = res.formateadoTotal;
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const inputs = ['select-temporada', 'select-transporte', 'select-hotel', 'select-pax'];
  inputs.forEach(id => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('change', actualizarUI);
  });
  // No ejecutar actualizarUI() inmediatamente, esperar a que carguen los datos del JSON
});

console.log("Módulo de Cotizaciones Quindío Travel cargado y listo para interactuar.");
