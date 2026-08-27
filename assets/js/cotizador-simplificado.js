// Cotizador Simplificado - JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Datos de planes por duración
    const planesPorDuracion = {
        '2d1n': [
            {
                nombre: 'Plan Vive El Eje Cafetero Temático',
                precio: '$425.000',
                incluye: 'Parque del Café, Salento, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20Vive%20El%20Eje%20Cafetero%20Temático'
            }
        ],
        '3d2n': [
            {
                nombre: 'Plan Naturaleza y Diversión Cafetera',
                precio: '$562.000',
                incluye: 'Parque del Café, PANACA, Salento, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20Naturaleza%20y%20Diversión%20Cafetera'
            }
        ],
        '4d3n': [
            {
                nombre: 'Plan La Experiencia Completa del Eje',
                precio: '$777.000',
                incluye: 'Valle de Cocora, Salento, Filandia, parques, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20La%20Experiencia%20Completa%20del%20Eje'
            },
            {
                nombre: 'Plan Aventura y Relax Termal',
                precio: '$798.000',
                incluye: 'Valle de Cocora, Termales Santa Rosa, pueblos, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20Aventura%20y%20Relax%20Termal'
            },
            {
                nombre: 'Plan Tradición y Raíces de la Arriería',
                precio: '$788.000',
                incluye: 'Cultura cafetera, Salento, Filandia, Parque Los Arrieros, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20Tradición%20y%20Raíces%20de%20la%20Arriería'
            }
        ],
        '5d4n': [
            {
                nombre: 'Plan Gran Quindío Integral',
                precio: '$1.008.000',
                incluye: 'Experiencia completa Eje Cafetero, todos los destinos, alojamiento, desayuno y cena',
                link: 'https://wa.me/573174426044?text=Hola%20Quindío%20Travel,%20quiero%20el%20Plan%20Gran%20Quindío%20Integral'
            }
        ]
    };

    // Función para mostrar planes según duración seleccionada
    function mostrarPlanes(duracion) {
        // Remover clase active de todas las tarjetas de duración
        document.querySelectorAll('.duracion-card').forEach(card => {
            card.classList.remove('active');
        });

        // Agregar clase active a la tarjeta seleccionada
        const tarjetaSeleccionada = document.querySelector(`[data-duracion="${duracion}"]`);
        if (tarjetaSeleccionada) {
            tarjetaSeleccionada.classList.add('active');
        }

        // Ocultar todos los contenedores de planes
        document.querySelectorAll('.planes-container').forEach(container => {
            container.classList.remove('active');
        });

        // Mostrar contenedor de planes correspondiente
        const containerPlanes = document.getElementById(`planes-${duracion}`);
        if (containerPlanes) {
            containerPlanes.classList.add('active');
        }
    }

    // Agregar event listeners a las tarjetas de duración
    document.querySelectorAll('.duracion-card').forEach(card => {
        card.addEventListener('click', function() {
            const duracion = this.getAttribute('data-duracion');
            mostrarPlanes(duracion);
        });
    });

    // Renderizar planes dinámicamente
    function renderizarPlanes() {
        Object.keys(planesPorDuracion).forEach(duracion => {
            const container = document.getElementById(`planes-${duracion}`);
            if (container) {
                const planes = planesPorDuracion[duracion];
                container.innerHTML = `
                    <div class="plans-simplificados">
                        ${planes.map(plan => `
                            <div class="plan-simplificado">
                                <h4>${plan.nombre}</h4>
                                <div class="plan-price">${plan.precio} COP</div>
                                <div class="plan-includes">${plan.incluye}</div>
                                <a href="${plan.link}" target="_blank" class="btn-cotizar">
                                    <i class="fab fa-whatsapp"></i> ¡Cotizar Ahora!
                                </a>
                            </div>
                        `).join('')}
                    </div>
                `;
            }
        });
    }

    // Inicializar
    renderizarPlanes();
    
    // Seleccionar 3D/2N por defecto (recomendado)
    mostrarPlanes('3d2n');
});