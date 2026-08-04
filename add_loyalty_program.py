from pathlib import Path

def add_loyalty_program():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir sección de programa de lealtad
    loyalty_section = '''
    <!-- Programa de Lealtad Section -->
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
                        <li>✅ Newsletter exclusiva</li>
                    </ul>
                </div>
                
                <div class="loyalty-tier silver">
                    <div class="tier-icon">🥈</div>
                    <h3 class="tier-title">Plata</h3>
                    <p class="tier-description">2-3 viajes</p>
                    <ul class="tier-benefits">
                        <li>✅ 10% de descuento en todos los viajes</li>
                        <li>✅ Upgrade gratuito de categoría</li>
                        <li>✅ Acceso anticipado a ofertas especiales</li>
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
                        <li>✅ Experiencias exclusivas (privadas)</li>
                        <li>✅ Gerente personal dedicado</li>
                        <li>✅ Cancelación flexible sin costo</li>
                    </ul>
                </div>
            </div>
            
            <div class="loyalty-cta">
                <p class="loyalty-cta-text">¿Ya has viajado con nosotros? <a href="#" data-wa-message="Hola Quindío Travel, ya he viajado con ustedes anteriormente. Me gustaría inscribirme en el programa de lealtad" class="loyalty-link">Inscríbete al programa de lealtad</a></p>
            </div>
        </div>
    </section>
'''
    
    # Buscar la sección de promoción para añadir después
    promo_section = '<section class="promo-section-enhanced"'
    if promo_section in content:
        # Encontrar el cierre de la sección promo
        promo_end = '</section>'
        promo_idx = content.find(promo_section)
        if promo_idx != -1:
            next_section = content.find(promo_end, promo_idx) + len(promo_end)
            content = content[:next_section] + '\n' + loyalty_section + content[next_section:]
    
    # Añadir CSS para programa de lealtad
    loyalty_css = '''
    
    /* Loyalty Program Section */
    .loyalty-program-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 4rem 0;
        margin: 3rem 0;
    }
    
    .loyalty-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .loyalty-header h2 {
        font-size: 2.5rem;
        color: var(--texto-oscuro);
        margin-bottom: 1rem;
    }
    
    .loyalty-header p {
        font-size: 1.2rem;
        color: var(--marron-madera);
    }
    
    .loyalty-tiers {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    
    .loyalty-tier {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .loyalty-tier:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .loyalty-tier.bronze {
        border-top: 4px solid #cd7f32;
    }
    
    .loyalty-tier.silver {
        border-top: 4px solid #c0c0c0;
    }
    
    .loyalty-tier.gold {
        border-top: 4px solid #ffd700;
    }
    
    .tier-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    .tier-title {
        font-size: 1.5rem;
        color: var(--texto-oscuro);
        margin-bottom: 0.5rem;
    }
    
    .tier-description {
        color: var(--marron-madera);
        margin-bottom: 1rem;
    }
    
    .tier-benefits {
        list-style: none;
        padding: 0;
        text-align: left;
    }
    
    .tier-benefits li {
        padding: 0.5rem 0;
        color: var(--texto-oscuro);
    }
    
    .loyalty-cta {
        text-align: center;
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }
    
    .loyalty-cta-text {
        font-size: 1.1rem;
        color: var(--texto-oscuro);
    }
    
    .loyalty-link {
        color: var(--verde-cafe);
        font-weight: 700;
        text-decoration: none;
    }
    
    .loyalty-link:hover {
        text-decoration: underline;
    }
    
    @media (max-width: 768px) {
        .loyalty-tiers {
            grid-template-columns: 1fr;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, loyalty_css + '\n' + style_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Programa de lealtad añadido")

if __name__ == "__main__":
    add_loyalty_program()