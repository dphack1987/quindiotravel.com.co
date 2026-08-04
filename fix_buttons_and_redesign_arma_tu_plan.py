from pathlib import Path

def fix_buttons_and_redesign():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Mover Don Chucho a la izquierda (bottom-left)
    don_chucho_fixed = '''
    <!-- Don Chucho Avatar - Bottom Left -->
    <div class="don-chucho-bottom-left">
        <a href="#" data-wa-message="Hola Don Chucho, necesito asesoría sobre planes de viaje al Eje Cafetero" target="_blank" rel="noopener" class="don-chucho-link-left">
            <img src="assets/images/don-chucho-avatar.png" alt="Don Chucho - Guía Local" class="don-chucho-avatar-left">
            <span class="don-chucho-tooltip-left">🤠 Hola, soy Don Chucho</span>
        </a>
    </div>
'''
    
    # Eliminar el botón actual de Don Chucho
    don_chucho_pattern = r'<!-- Don Chucho Perfect Button -->.*?</div>'
    import re
    content = re.sub(don_chucho_pattern, don_chucho_fixed, content, flags=re.DOTALL)
    
    # Rediseñar "Arma tu Propio Plan" con mejor diseño
    arma_tu_plan_new = '''
    <!-- Planes Flexibles Section -->
    <section class="flexible-plans-section" id="planes-flexibles" aria-label="Arma tu propio plan">
        <div class="container">
            <div class="flexible-plans-header">
                <h2 class="section-title">🔧 Personaliza tu Experiencia</h2>
                <p class="section-subtitle">Crea tu plan ideal según tus preferencias</p>
            </div>
            
            <div class="flexible-plans-grid">
                <div class="flexible-step-card">
                    <div class="step-icon">🎯</div>
                    <h3 class="step-title">Selecciona Atractivos</h3>
                    <div class="attractions-grid-clean">
                        <label class="attraction-item"><input type="checkbox" value="parque-cafe" data-name="Parque del Café">🎢 Parque del Café</label>
                        <label class="attraction-item"><input type="checkbox" value="panaca" data-name="PANACA">🐄 PANACA</label>
                        <label class="attraction-item"><input type="checkbox" value="valle-cocora" data-name="Valle de Cocora">🌴 Valle de Cocora</label>
                        <label class="attraction-item"><input type="checkbox" value="salento" data-name="Salento">🏘 Salento</label>
                        <label class="attraction-item"><input type="checkbox" value="filandia" data-name="Filandia">🏛 Filandia</label>
                        <label class="attraction-item"><input type="checkbox" value="termales" data-name="Termales">♨ Termales</label>
                    </div>
                </div>
                
                <div class="flexible-step-card">
                    <div class="step-icon">📅</div>
                    <h3 class="step-title">Duración</h3>
                    <div class="duration-options-clean">
                        <label class="duration-item"><input type="radio" name="duration" value="2d1n">2 Días / 1 Noche</label>
                        <label class="duration-item"><input type="radio" name="duration" value="3d2n">3 Días / 2 Noches</label>
                        <label class="duration-item"><input type="radio" name="duration" value="4d3n">4 Días / 3 Noches</label>
                    </div>
                </div>
                
                <div class="flexible-step-card">
                    <div class="step-icon">🏨</div>
                    <h3 class="step-title">Alojamiento</h3>
                    <div class="accommodation-options-clean">
                        <label class="accommodation-item"><input type="radio" name="accommodation" value="economico">💰 Económico</label>
                        <label class="accommodation-item"><input type="radio" name="accommodation" value="intermedio">⭐⭐⭐ Intermedio</label>
                        <label class="accommodation-item"><input type="radio" name="accommodation" value="vip">⭐⭐⭐⭐⭐ VIP</label>
                    </div>
                </div>
            </div>
            
            <div class="flexible-cta">
                <button class="btn-generate-plan" onclick="generateCustomPlan()">
                    <i class="fas fa-magic"></i> Generar mi Plan Personalizado
                </button>
            </div>
        </div>
    </section>
'''
    
    # Reemplazar la sección actual de "Arma tu Propio Plan"
    old_arma_tu_plan = r'<!-- Plans Flexibles Section -->.*?</section>'
    content = re.sub(old_arma_tu_plan, arma_tu_plan_new, content, flags=re.DOTALL)
    
    # Añadir CSS mejorado
    improved_css = '''
    
    /* Don Chucho Bottom Left Button */
    .don-chucho-bottom-left {
        position: fixed;
        bottom: 20px;
        left: 20px;
        z-index: 998;
    }
    
    .don-chucho-link-left {
        display: block;
        width: 65px;
        height: 65px;
        border-radius: 50%;
        background: linear-gradient(135deg, #8B4513, #D2691E);
        box-shadow: 0 4px 15px rgba(139, 69, 19, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: visible;
    }
    
    .don-chucho-link-left:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4);
    }
    
    .don-chucho-avatar-left {
        width: 65px;
        height: 65px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid rgba(255,255,255,0.3);
        display: block;
    }
    
    .don-chucho-tooltip-left {
        position: absolute;
        left: 75px;
        top: 50%;
        transform: translateY(-50%);
        background: linear-gradient(135deg, #8B4513, #D2691E);
        color: white;
        padding: 10px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        font-weight: 600;
        white-space: nowrap;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .don-chucho-link-left:hover .don-chucho-tooltip-left {
        opacity: 1;
        visibility: visible;
    }
    
    /* Improved Flexible Plans Section */
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
    
    .flexible-plans-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .flexible-step-card {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        transition: all 0.3s ease;
    }
    
    .flexible-step-card:hover {
        transform: translateY(-5px);
        background: rgba(255,255,255,0.15);
    }
    
    .step-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .step-title {
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
    }
    
    .attractions-grid-clean,
    .duration-options-clean,
    .accommodation-options-clean {
        display: flex;
        flex-direction: column;
        gap: 0.75rem;
        text-align: left;
    }
    
    .attraction-item,
    .duration-item,
    .accommodation-item {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem;
        background: rgba(255,255,255,0.1);
        border-radius: 10px;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .attraction-item:hover,
    .duration-item:hover,
    .accommodation-item:hover {
        background: rgba(255,255,255,0.2);
    }
    
    .flexible-cta {
        text-align: center;
    }
    
    .btn-generate-plan {
        background: white;
        color: #667eea;
        border: none;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .btn-generate-plan:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    @media (max-width: 768px) {
        .don-chucho-bottom-left {
            bottom: 15px;
            left: 15px;
        }
        
        .don-chucho-link-left {
            width: 55px;
            height: 55px;
        }
        
        .don-chucho-avatar-left {
            width: 55px;
            height: 55px;
        }
        
        .don-chucho-tooltip-left {
            left: 65px;
            font-size: 0.8rem;
            padding: 8px 12px;
        }
        
        .flexible-plans-grid {
            grid-template-columns: 1fr;
        }
    }
'''
    
    # Buscar y eliminar el CSS anterior de Don Chucho
    old_don_chucho_css = r'/\* Don Chucho Perfect Button \*/.*?@media \(max-width: 768px\) \{.*?\}'
    content = re.sub(old_don_chucho_css, '', content, flags=re.DOTALL)
    
    # Buscar y eliminar el CSS anterior de flexible plans
    old_flexible_css = r'/\* Flexible Plans Section \*/.*?@media \(max-width: 768px\) \{.*?\}'
    content = re.sub(old_flexible_css, '', content, flags=re.DOTALL)
    
    # Buscar </style> para añadir el nuevo CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, improved_css + '\n' + style_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Botones reubicados y 'Arma tu plan' rediseñado")

if __name__ == "__main__":
    fix_buttons_and_redesign()