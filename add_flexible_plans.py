from pathlib import Path

def add_flexible_plans():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir sección de planes flexibles
    flexible_plans_section = '''
    <!-- Plans Flexibles Section -->
    <section class="flexible-plans-section" id="planes-flexibles" aria-label="Arma tu propio plan">
        <div class="container">
            <div class="flexible-plans-header">
                <h2 class="section-title">🔧 Arma tu Propio Plan</h2>
                <p class="section-subtitle">Personaliza tu experiencia seleccionando atractivos, duración y alojamiento</p>
            </div>
            
            <div class="flexible-plans-container">
                <!-- Paso 1: Atractivos -->
                <div class="flexible-step">
                    <div class="step-number">1</div>
                    <h3 class="step-title">Selecciona Atractivos</h3>
                    <div class="attractions-grid">
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="parque-cafe" data-name="Parque del Café">
                            <span>🎢 Parque del Café</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="panaca" data-name="PANACA">
                            <span>🐄 PANACA</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="valle-cocora" data-name="Valle de Cocora">
                            <span>🌴 Valle de Cocora</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="salento" data-name="Salento">
                            <span>🏘 Salento</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="filandia" data-name="Filandia">
                            <span>🏛 Filandia</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="termales" data-name="Termales Santa Rosa">
                            <span>♨ Termales</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="recuca" data-name="RECUCA">
                            <span>☕ RECUCA</span>
                        </label>
                        <label class="attraction-checkbox">
                            <input type="checkbox" value="parque-arrieros" data-name="Parque Los Arrieros">
                            <span>🎭 Parque Los Arrieros</span>
                        </label>
                    </div>
                </div>
                
                <!-- Paso 2: Duración -->
                <div class="flexible-step">
                    <div class="step-number">2</div>
                    <h3 class="step-title">Duración</h3>
                    <div class="duration-options">
                        <label class="duration-radio">
                            <input type="radio" name="duration" value="2d1n">
                            <span>2 Días / 1 Noche</span>
                        </label>
                        <label class="duration-radio">
                            <input type="radio" name="duration" value="3d2n">
                            <span>3 Días / 2 Noches</span>
                        </label>
                        <label class="duration-radio">
                            <input type="radio" name="duration" value="4d3n">
                            <span>4 Días / 3 Noches</span>
                        </label>
                        <label class="duration-radio">
                            <input type="radio" name="duration" value="5d4n">
                            <span>5 Días / 4 Noches</span>
                        </label>
                    </div>
                </div>
                
                <!-- Paso 3: Alojamiento -->
                <div class="flexible-step">
                    <div class="step-number">3</div>
                    <h3 class="step-title">Categoría de Alojamiento</h3>
                    <div class="accommodation-options">
                        <label class="accommodation-radio">
                            <input type="radio" name="accommodation" value="economico">
                            <span>💰 Económico</span>
                        </label>
                        <label class="accommodation-radio">
                            <input type="radio" name="accommodation" value="intermedio">
                            <span>⭐⭐⭐ Intermedio</span>
                        </label>
                        <label class="accommodation-radio">
                            <input type="radio" name="accommodation" value="vip">
                            <span>⭐⭐⭐⭐⭐ VIP</span>
                        </label>
                    </div>
                </div>
                
                <!-- CTA -->
                <div class="flexible-cta">
                    <button class="btn-custom-plan" onclick="generateCustomPlan()">
                        <i class="fas fa-magic"></i> Generar mi Plan Personalizado
                    </button>
                </div>
            </div>
        </div>
    </section>
'''
    
    # Buscar la sección de planes para añadir antes
    plans_section = '<section class="plans-section container" id="planes">'
    if plans_section in content:
        content = content.replace(plans_section, flexible_plans_section + '\n' + plans_section)
    
    # Añadir CSS para planes flexibles
    flexible_css = '''
    
    /* Flexible Plans Section */
    .flexible-plans-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 4rem 0;
        margin: 3rem 0;
        color: white;
    }
    
    .flexible-plans-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .flexible-plans-header h2 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .flexible-plans-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .flexible-plans-container {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
    }
    
    .flexible-step {
        margin-bottom: 2rem;
        padding: 1.5rem;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
    }
    
    .step-number {
        width: 40px;
        height: 40px;
        background: #fff;
        color: #667eea;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1.2rem;
        margin-bottom: 1rem;
    }
    
    .step-title {
        font-size: 1.3rem;
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .attractions-grid,
    .duration-options,
    .accommodation-options {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 1rem;
    }
    
    .attraction-checkbox,
    .duration-radio,
    .accommodation-radio {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.75rem;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .attraction-checkbox:hover,
    .duration-radio:hover,
    .accommodation-radio:hover {
        background: rgba(255,255,255,0.2);
    }
    
    .attraction-checkbox input,
    .duration-radio input,
    .accommodation-radio input {
        accent-color: #fff;
    }
    
    .flexible-cta {
        text-align: center;
        margin-top: 2rem;
    }
    
    .btn-custom-plan {
        background: white;
        color: #667eea;
        border: none;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-custom-plan:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    @media (max-width: 768px) {
        .attractions-grid,
        .duration-options,
        .accommodation-options {
            grid-template-columns: 1fr;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, flexible_css + '\n' + style_end)
    
    # Añadir JavaScript para planes flexibles
    flexible_js = '''
    <script>
    function generateCustomPlan() {
        const selectedAttractions = [];
        document.querySelectorAll('.attraction-checkbox input:checked').forEach(checkbox => {
            selectedAttractions.push(checkbox.dataset.name);
        });
        
        const duration = document.querySelector('input[name="duration"]:checked')?.value;
        const accommodation = document.querySelector('input[name="accommodation"]:checked')?.value;
        
        if (selectedAttractions.length === 0 || !duration || !accommodation) {
            alert('Por favor selecciona al menos un atractivo, duración y categoría de alojamiento');
            return;
        }
        
        const message = `Hola Quindío Travel, quiero armar mi propio plan personalizado:\\n\\n` +
            `🎯 Atractivos: ${selectedAttractions.join(', ')}\\n` +
            `📅 Duración: ${duration}\\n` +
            `🏨 Alojamiento: ${accommodation}\\n\\n` +
            `¿Podrían cotizarme este plan personalizado?`;
        
        const whatsappUrl = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;
        window.open(whatsappUrl, '_blank');
    }
    </script>
'''
    
    # Buscar </body> para añadir script
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, flexible_js + '\n' + body_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Planes flexibles añadidos")

if __name__ == "__main__":
    add_flexible_plans()