"""
Implementar Filtros Avanzados como los Gigantes de Reservas
Añade filtros por tipo, duración, precio, capacidad, transporte
"""

from pathlib import Path

def add_advanced_filters_to_planes():
    """Añade filtros avanzados a planes.html"""
    
    planes_path = Path(__file__).parent / "planes.html"
    
    with open(planes_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar la sección de planes para añadir filtros antes
    plans_section_start = '<section class="plans-section"'
    
    if plans_section_start in content:
        # Insertar filtros avanzados antes de la sección de planes
        advanced_filters = '''
    <!-- Advanced Filters Section -->
    <section class="filters-section" id="filtros" aria-label="Filtros Avanzados de Planes">
        <div class="container">
            <div class="filters-header">
                <h2 class="filters-title">Encuentra tu Plan Perfecto</h2>
                <p class="filters-subtitle">Filtra por tipo, duración, precio y capacidad</p>
            </div>
            
            <div class="filters-container">
                <!-- Filter by Type -->
                <div class="filter-group">
                    <label class="filter-label">Tipo de Experiencia</label>
                    <select class="filter-select" id="filter-type" onchange="filterPlans()">
                        <option value="all">Todos los tipos</option>
                        <option value="cultural">Turismo Cultural</option>
                        <option value="aventura">Turismo de Aventura</option>
                        <option value="relax">Turismo de Relaj</option>
                        <option value="gastronomico">Turismo Gastronómico</option>
                        <option value="naturaleza">Turismo de Naturaleza</option>
                    </select>
                </div>
                
                <!-- Filter by Duration -->
                <div class="filter-group">
                    <label class="filter-label">Duración</label>
                    <select class="filter-select" id="filter-duration" onchange="filterPlans()">
                        <option value="all">Todas las duraciones</option>
                        <option value="2d1n">2 Días / 1 Noche</option>
                        <option value="3d2n">3 Días / 2 Noches</option>
                        <option value="4d3n">4 Días / 3 Noches</option>
                        <option value="5d4n">5 Días / 4 Noches</option>
                        <option value="6d5n">6 Días / 5 Noches</option>
                    </select>
                </div>
                
                <!-- Filter by Price -->
                <div class="filter-group">
                    <label class="filter-label">Rango de Precio</label>
                    <select class="filter-select" id="filter-price" onchange="filterPlans()">
                        <option value="all">Todos los precios</option>
                        <option value="economico">Económico ($500k - $1M)</option>
                        <option value="intermedio">Intermedio ($1M - $1.5M)</option>
                        <option value="premium">Premium ($1.5M+)</option>
                    </select>
                </div>
                
                <!-- Filter by Capacity -->
                <div class="filter-group">
                    <label class="filter-label">Capacidad</label>
                    <select class="filter-select" id="filter-capacity" onchange="filterPlans()">
                        <option value="all">Todas las capacidades</option>
                        <option value="individual">Individual</option>
                        <option value="pareja">Pareja</option>
                        <option value="familia">Familia (3-6)</option>
                        <option value="grupo">Grupo (7+)</option>
                    </select>
                </div>
                
                <!-- Filter by Transport -->
                <div class="filter-group">
                    <label class="filter-label">Transporte</label>
                    <select class="filter-select" id="filter-transport" onchange="filterPlans()">
                        <option value="all">Todos</option>
                        <option value="con-transporte">Con Transporte</option>
                        <option value="sin-transporte">Sin Transporte</option>
                    </select>
                </div>
                
                <!-- Filter by Attractions -->
                <div class="filter-group">
                    <label class="filter-label">Atractivos</label>
                    <select class="filter-select" id="filter-attraction" onchange="filterPlans()">
                        <option value="all">Todos los atractivos</option>
                        <option value="parque-cafe">Parque del Café</option>
                        <option value="panaca">PANACA</option>
                        <option value="valle-cocora">Valle de Cocora</option>
                        <option value="termales">Termales</option>
                        <option value="salento">Salento</option>
                        <option value="filandia">Filandia</option>
                    </select>
                </div>
                
                <!-- Reset Filters -->
                <div class="filter-group">
                    <button class="filter-reset" onclick="resetFilters()">
                        <i class="fas fa-undo"></i> Limpiar Filtros
                    </button>
                </div>
            </div>
            
            <!-- Results Count -->
            <div class="filters-results">
                <span id="results-count">Mostrando 6 planes</span>
                <span class="results-label">de 6 disponibles</span>
            </div>
        </div>
    </section>
'''
        
        content = content.replace(plans_section_start, advanced_filters + '\n' + plans_section_start)
        print("[OK] Filtros avanzados añadidos a planes.html")
    
    # Añadir JavaScript para filtrado
    js_script = '''
    <script>
    function filterPlans() {
        const typeFilter = document.getElementById('filter-type').value;
        const durationFilter = document.getElementById('filter-duration').value;
        const priceFilter = document.getElementById('filter-price').value;
        const capacityFilter = document.getElementById('filter-capacity').value;
        const transportFilter = document.getElementById('filter-transport').value;
        const attractionFilter = document.getElementById('filter-attraction').value;
        
        // Get all plan cards
        const planCards = document.querySelectorAll('.plan-card');
        let visibleCount = 0;
        
        planCards.forEach(card => {
            let isVisible = true;
            
            // Apply filters (simplified logic - should be enhanced with actual data attributes)
            if (typeFilter !== 'all' && !card.dataset.type?.includes(typeFilter)) {
                isVisible = false;
            }
            
            if (durationFilter !== 'all' && !card.dataset.duration?.includes(durationFilter)) {
                isVisible = false;
            }
            
            if (priceFilter !== 'all' && !card.dataset.price?.includes(priceFilter)) {
                isVisible = false;
            }
            
            if (capacityFilter !== 'all' && !card.dataset.capacity?.includes(capacityFilter)) {
                isVisible = false;
            }
            
            if (transportFilter !== 'all' && !card.dataset.transport?.includes(transportFilter)) {
                isVisible = false;
            }
            
            if (attractionFilter !== 'all' && !card.dataset.attraction?.includes(attractionFilter)) {
                isVisible = false;
            }
            
            card.style.display = isVisible ? 'block' : 'none';
            if (isVisible) visibleCount++;
        });
        
        // Update results count
        document.getElementById('results-count').textContent = `Mostrando ${visibleCount} planes`;
    }
    
    function resetFilters() {
        document.getElementById('filter-type').value = 'all';
        document.getElementById('filter-duration').value = 'all';
        document.getElementById('filter-price').value = 'all';
        document.getElementById('filter-capacity').value = 'all';
        document.getElementById('filter-transport').value = 'all';
        document.getElementById('filter-attraction').value = 'all';
        filterPlans();
    }
    </script>
'''
    
    # Buscar </body> para añadir script antes
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, js_script + '\n' + body_end)
        print("[OK] JavaScript de filtrado añadido")
    
    # Guardar cambios
    with open(planes_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Implementando filtros avanzados como los gigantes de reservas...")
    print("=" * 70)
    
    add_advanced_filters_to_planes()
    
    print("\n" + "=" * 70)
    print("Filtros avanzados implementados exitosamente")