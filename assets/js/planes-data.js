// Base de datos de planes turísticos oficiales - Quindío Travel (RNT 18152)
const planesData = [
  {
    id: "plan-1",
    titulo: "Plan Económico 3 Días / 2 Noches",
    duracion: "3d",
    noches: 2,
    dias: 3,
    descripcion: "Incluye alojamiento campestre, desayunos y cenas, pasaporte al Parque del Café y Panaca, tarjeta de asistencia médica y guía local.",
    precioSinTransporte: 580000,
    precioConTransporte: 790000,
    badge: "Más Popular"
  },
  {
    id: "plan-2",
    titulo: "Plan Super Económico 4 Días / 3 Noches",
    duracion: "4d",
    noches: 3,
    dias: 4,
    descripcion: "Alojamiento en finca hotel tradicional, desayunos y cenas, Parque del Café, Panaca, Salento y Valle de Cocora, asistencia médica.",
    precioSinTransporte: 750000,
    precioConTransporte: 980000,
    badge: "Económico"
  },
  {
    id: "plan-3",
    titulo: "Plan Flex 2 Días / 1 Noche",
    duracion: "2d",
    noches: 1,
    dias: 2,
    descripcion: "Escapada rápida de fin de semana. Incluye 1 noche en finca hotel, desayuno, pasaporte a 1 parque principal a elección (Parque del Café o Panaca) y asistencia médica.",
    precioSinTransporte: 320000,
    precioConTransporte: 450000,
    badge: "Escapada"
  },
  {
    id: "plan-4",
    titulo: "Plan Quindío 5 Días / 4 Noches",
    duracion: "5d",
    noches: 4,
    dias: 5,
    descripcion: "Experiencia completa: Alojamiento campestre, alimentación completa (desayunos y cenas), Parque del Café, Panaca, Termales, Salento, Valle de Cocora y Recuca.",
    precioSinTransporte: 990000,
    precioConTransporte: 1250000,
    badge: "Todo Incluido"
  }
];

// Función para renderizar los planes dinámicamente en el DOM
function renderizarPlanes(filtro = "all") {
  const contenedor = document.getElementById("catalogo-planes");
  if (!contenedor) return;

  contenedor.innerHTML = "";

  const planesFiltrados = filtro === "all" 
    ? planesData 
    : planesData.filter(plan => plan.duracion === filtro);

  if (planesFiltrados.length === 0) {
    contenedor.innerHTML = `<p class="no-results">No hay planes disponibles para este filtro en este momento.</p>`;
    return;
  }

  planesFiltrados.forEach(plan => {
    const card = document.createElement("div");
    card.className = "plan-card";
    card.innerHTML = `
      <div class="plan-header">
        <span class="badge-plan">${plan.badge}</span>
        <h3>${plan.titulo}</h3>
      </div>
      <div class="plan-body">
        <p>${plan.descripcion}</p>
        <div class="plan-prices">
          <div class="price-row">
            <span>Sin Transporte:</span>
            <strong>$ ${plan.precioSinTransporte.toLocaleString('es-CO')} COP</strong>
          </div>
          <div class="price-row">
            <span>Con Transporte:</span>
            <strong>$ ${plan.precioConTransporte.toLocaleString('es-CO')} COP</strong>
          </div>
        </div>
      </div>
      <div class="plan-footer">
        <a href="https://wa.me/573174426044?text=Hola%20Quind&iacute;o%20Travel,%20deseo%20cotizar%20el%20${encodeURIComponent(plan.titulo)}" class="btn btn-primary" target="_blank" rel="noopener">
          Cotizar Plan
        </a>
      </div>
    `;
    contenedor.appendChild(card);
  });
}

// Inicializar renderizado al cargar la página
document.addEventListener("DOMContentLoaded", () => {
  renderizarPlanes("all");

  // Conectar con los botones de filtro
  const pills = document.querySelectorAll(".filter-pills .pill");
  pills.forEach(pill => {
    pill.addEventListener("click", () => {
      pills.forEach(p => p.classList.remove("active"));
      pill.classList.add("active");
      const filtro = pill.getAttribute("data-filter");
      renderizarPlanes(filtro);
    });
  });
});
