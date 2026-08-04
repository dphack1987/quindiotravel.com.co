from pathlib import Path

def add_missing_html_sections():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar la sección de planes para añadir las nuevas secciones antes
    plans_section = '<section class="plans-section container" id="planes">'
    
    if plans_section in content:
        # Añadir las tres secciones antes de planes
        flexible_html = '''    <!-- Plans Flexibles Section -->
    <section class="flexible-plans-section" id="planes-flexibles" aria-label="Arma tu propio plan">
        <div class="container">
            <div class="flexible-plans-header">
                <h2 class="section-title">🔧 Arma tu Propio Plan</h2>
                <p class="section-subtitle">Personaliza tu experiencia seleccionando atractivos, duración y alojamiento</p>
            </div>
            
            <div class="flexible-plans-container">
                <div class="flexible-step">
                    <div class="step-number">1</div>
                    <h3 class="step-title">Selecciona Atractivos</h3>
                    <div class="attractions-grid">
                        <label class="attraction-checkbox"><input type="checkbox" value="parque-cafe" data-name="Parque del Café"><span>🎢 Parque del Café</span></label>
                        <label class="attraction-checkbox"><input type="checkbox" value="panaca" data-name="PANACA"><span>🐄 PANACA</span></label>
                        <label class="attraction-checkbox"><input type="checkbox" value="valle-cocora" data-name="Valle de Cocora"><span>🌴 Valle de Cocora</span></label>
                        <label class="attraction-checkbox"><input type="checkbox" value="salento" data-name="Salento"><span>🏘 Salento</span></label>
                        <label class="attraction-checkbox"><input type="checkbox" value="filandia" data-name="Filandia"><span>🏛 Filandia</span></label>
                        <label class="attraction-checkbox"><input type="checkbox" value="termales" data-name="Termales Santa Rosa"><span>♨ Termales</span></label>
                    </div>
                </div>
                
                <div class="flexible-step">
                    <div class="step-number">2</div>
                    <h3 class="step-title">Duración</h3>
                    <div class="duration-options">
                        <label class="duration-radio"><input type="radio" name="duration" value="2d1n"><span>2 Días / 1 Noche</span></label>
                        <label class="duration-radio"><input type="radio" name="duration" value="3d2n"><span>3 Días / 2 Noches</span></label>
                        <label class="duration-radio"><input type="radio" name="duration" value="4d3n"><span>4 Días / 3 Noches</span></label>
                    </div>
                </div>
                
                <div class="flexible-step">
                    <div class="step-number">3</div>
                    <h3 class="step-title">Categoría de Alojamiento</h3>
                    <div class="accommodation-options">
                        <label class="accommodation-radio"><input type="radio" name="accommodation" value="economico"><span>💰 Económico</span></label>
                        <label class="accommodation-radio"><input type="radio" name="accommodation" value="intermedio"><span>⭐⭐⭐ Intermedio</span></label>
                        <label class="accommodation-radio"><input type="radio" name="accommodation" value="vip"><span>⭐⭐⭐⭐⭐ VIP</span></label>
                    </div>
                </div>
                
                <div class="flexible-cta">
                    <button class="btn-custom-plan" onclick="generateCustomPlan()"><i class="fas fa-magic"></i> Generar mi Plan Personalizado</button>
                </div>
            </div>
        </div>
    </section>
'''
        
        loyalty_html = '''    <!-- Programa de Lealtad Section -->
    <section class="loyalty-program-section" id="programa-lealtad" aria-label="Programa de Lealtad">
        <div class="container">
            <div class="loyalty-header">
                <h2 class="section-title">⭐ Programa de Lealtad Quindío Travel</h2>
                <p class="section-subtitle">Viaja más, ahorra más. Beneficios exclusivos para nuestros viajeros recurrentes</p>
            </div>
            
            <div class="loyalty-tiers">
                <div class="loyalty-tier bronze">
                    <div class="tier-icon">🥉</div>
                    <h3 class="tier-title">Bronce</h3>
                    <p class="tier-description">Primer viaje</p>
                    <ul class="tier-benefits">
                        <li>✅ 5% de descuento en segundo viaje</li>
                        <li>✅ Acceso prioritario a promociones</li>
                    </ul>
                </div>
                
                <div class="loyalty-tier silver">
                    <div class="tier-icon">🥈</div>
                    <h3 class="tier-title">Plata</h3>
                    <p class="tier-description">2-3 viajes</p>
                    <ul class="tier-benefits">
                        <li>✅ 10% de descuento en todos los viajes</li>
                        <li>✅ Upgrade gratuito de categoría</li>
                        <li>✅ Soporte prioritario WhatsApp</li>
                    </ul>
                </div>
                
                <div class="loyalty-tier gold">
                    <div class="tier-icon">🥇</div>
                    <h3 class="tier-title">Oro</h3>
                    <p class="tier-description">4+ viajes</p>
                    <ul class="tier-benefits">
                        <li>✅ 15% de descuento en todos los viajes</li>
                        <li>✅ Alojamiento VIP gratuito en viajes especiales</li>
                        <li>✅ Gerente personal dedicado</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
'''
        
        transport_html = '''    <!-- Transporte Multi-origen Section -->
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
                    </ul>
                    <button class="btn-origin-select" onclick="selectOrigin('cali')">Seleccionar Cali</button>
                </div>
            </div>
        </div>
    </section>
'''
        
        content = content.replace(plans_section, flexible_html + '\n' + loyalty_html + '\n' + transport_html + '\n' + plans_section)
        print("Secciones HTML añadidas")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    add_missing_html_sections()