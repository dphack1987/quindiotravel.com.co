from pathlib import Path

def add_multi_origin_transport():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir sección de transporte multi-origen
    transport_section = '''
    <!-- Transporte Multi-origen Section -->
    <section class="multi-origin-transport-section" id="transporte-multi-origen" aria-label="Transporte desde múltiples ciudades">
        <div class="container">
            <div class="transport-header">
                <h2 class="section-title">🚐 Transporte desde Tu Ciudad</h2>
                <p class="section-subtitle">Viaja cómodamente desde Bogotá, Medellín o Cali hacia el Eje Cafetero</p>
            </div>
            
            <div class="transport-origins">
                <div class="origin-card bogota">
                    <div class="origin-icon">🏛️</div>
                    <h3 class="origin-title">Desde Bogotá</h3>
                    <p class="origin-description">Transporte terrestre cómodo y seguro</p>
                    <ul class="origin-details">
                        <li>📍 Salida: Terminal de Transporte Bogotá</li>
                        <li>⏰ Duración: 6-7 horas</li>
                        <li>💰 Tarifa: +$80.000 COP por persona</li>
                        <li>🚌 Vehículo: Buseta o Microbús</li>
                    </ul>
                    <button class="btn-origin-select" onclick="selectOrigin('bogota')">Seleccionar Bogotá</button>
                </div>
                
                <div class="origin-card medellin">
                    <div class="origin-icon">🌸</div>
                    <h3 class="origin-title">Desde Medellín</h3>
                    <p class="origin-description">Ruta escénica por el eje cafetero</p>
                    <ul class="origin-details">
                        <li>📍 Salida: Terminal del Sur Medellín</li>
                        <li>⏰ Duración: 3-4 horas</li>
                        <li>💰 Tarifa: +$50.000 COP por persona</li>
                        <li>🚌 Vehículo: Buseta o Microbús</li>
                    </ul>
                    <button class="btn-origin-select" onclick="selectOrigin('medellin')">Seleccionar Medellín</button>
                </div>
                
                <div class="origin-card cali">
                    <div class="origin-icon">🌴</div>
                    <h3 class="origin-title">Desde Cali</h3>
                    <p class="origin-description">Viaje rápido y confortable</p>
                    <ul class="origin-details">
                        <li>📍 Salida: Terminal de Transporte Cali</li>
                        <li>⏰ Duración: 4-5 horas</li>
                        <li>💰 Tarifa: +$60.000 COP por persona</li>
                        <li>🚌 Vehículo: Buseta o Microbús</li>
                    </ul>
                    <button class="btn-origin-select" onclick="selectOrigin('cali')">Seleccionar Cali</button>
                </div>
            </div>
            
            <div class="transport-info">
                <p class="transport-note">💡 <strong>Nota:</strong> El transporte desde otras ciudades está disponible para grupos de 4+ personas. Para grupos menores, consulte tarifas especiales.</p>
            </div>
        </div>
    </section>
'''
    
    # Buscar la sección de cotizador para añadir antes
    cotizador_section = '<section class="cotizador-section"'
    if cotizador_section in content:
        content = content.replace(cotizador_section, transport_section + '\n' + cotizador_section)
    
    # Añadir CSS para transporte multi-origen
    transport_css = '''
    
    /* Multi-Origin Transport Section */
    .multi-origin-transport-section {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        padding: 4rem 0;
        margin: 3rem 0;
        color: white;
    }
    
    .transport-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .transport-header h2 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .transport-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .transport-origins {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .origin-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .origin-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.15);
    }
    
    .origin-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .origin-title {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    .origin-description {
        opacity: 0.9;
        margin-bottom: 1rem;
    }
    
    .origin-details {
        list-style: none;
        padding: 0;
        text-align: left;
        margin-bottom: 1.5rem;
    }
    
    .origin-details li {
        padding: 0.5rem 0;
        opacity: 0.9;
    }
    
    .btn-origin-select {
        background: white;
        color: #3498db;
        border: none;
        padding: 0.75rem 1.5rem;
        border-radius: 25px;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-origin-select:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    .transport-info {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
    }
    
    .transport-note {
        font-size: 1rem;
        opacity: 0.9;
    }
    
    @media (max-width: 768px) {
        .transport-origins {
            grid-template-columns: 1fr;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, transport_css + '\n' + style_end)
    
    # Añadir JavaScript para selección de origen
    transport_js = '''
    <script>
    function selectOrigin(origin) {
        const message = `Hola Quindío Travel, deseo cotizar un plan con transporte desde ${origin.charAt(0).toUpperCase() + origin.slice(1)}. ¿Podrían enviarme las tarifas y disponibilidad?`;
        const whatsappUrl = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;
        window.open(whatsappUrl, '_blank');
    }
    </script>
'''
    
    # Buscar </body> para añadir script
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, transport_js + '\n' + body_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Transporte multi-origen añadido")

if __name__ == "__main__":
    add_multi_origin_transport()