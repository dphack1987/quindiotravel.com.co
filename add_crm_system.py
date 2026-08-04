from pathlib import Path

def add_crm_system():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Añadir formulario de captura de leads CRM
    crm_section = '''
    <!-- CRM Lead Capture Section -->
    <section class="crm-lead-section" id="crm-leads" aria-label="Captura de Leads CRM">
        <div class="container">
            <div class="crm-header">
                <h2 class="section-title">📊 Sistema de Gestión de Viajeros</h2>
                <p class="section-subtitle">Regístrate para recibir ofertas personalizadas y seguimiento exclusivo</p>
            </div>
            
            <div class="crm-container">
                <div class="crm-form-wrapper">
                    <form class="crm-lead-form" id="crmLeadForm">
                        <div class="form-group">
                            <label for="crm-name">Nombre Completo *</label>
                            <input type="text" id="crm-name" name="name" required placeholder="Tu nombre completo">
                        </div>
                        
                        <div class="form-group">
                            <label for="crm-email">Correo Electrónico *</label>
                            <input type="email" id="crm-email" name="email" required placeholder="tu@email.com">
                        </div>
                        
                        <div class="form-group">
                            <label for="crm-phone">WhatsApp *</label>
                            <input type="tel" id="crm-phone" name="phone" required placeholder="+57 3XX XXX XXXX">
                        </div>
                        
                        <div class="form-group">
                            <label for="crm-city">Ciudad de Origen</label>
                            <select id="crm-city" name="city">
                                <option value="">Selecciona tu ciudad</option>
                                <option value="bogota">Bogotá</option>
                                <option value="medellin">Medellín</option>
                                <option value="cali">Cali</option>
                                <option value="barranquilla">Barranquilla</option>
                                <option value="armenia">Armenia</option>
                                <option value="otra">Otra ciudad</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="crm-interest">Intereses de Viaje</label>
                            <div class="interests-checkboxes">
                                <label><input type="checkbox" name="interests" value="naturaleza"> Naturaleza</label>
                                <label><input type="checkbox" name="interests" value="cultura"> Cultura Cafetera</label>
                                <label><input type="checkbox" name="interests" value="aventura"> Aventura</label>
                                <label><input type="checkbox" name="interests" value="familia"> Familiar</label>
                                <label><input type="checkbox" name="interests" value="romantico"> Romántico</label>
                                <label><input type="checkbox" name="interests" value="empresarial"> Empresarial</label>
                            </div>
                        </div>
                        
                        <div class="form-group">
                            <label for="crm-budget">Presupuesto Aproximado</label>
                            <select id="crm-budget" name="budget">
                                <option value="">Selecciona tu presupuesto</option>
                                <option value="bajo">Menos de $500.000 COP</option>
                                <option value="medio">$500.000 - $1.000.000 COP</option>
                                <option value="alto">$1.000.000 - $2.000.000 COP</option>
                                <option value="premium">Más de $2.000.000 COP</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label class="privacy-agreement">
                                <input type="checkbox" name="privacy" required>
                                <span>Acepto la política de privacidad y tratamiento de datos personales</span>
                            </label>
                        </div>
                        
                        <button type="submit" class="btn-crm-submit">
                            <i class="fas fa-user-plus"></i> Registrarme en el Sistema
                        </button>
                    </form>
                </div>
                
                <div class="crm-benefits">
                    <h3>🎁 Beneficios de Registrarte</h3>
                    <ul class="benefits-list">
                        <li>✅ <strong>Ofertas Exclusivas:</strong> Recibe promociones antes que nadie</li>
                        <li>✅ <strong>Seguimiento Personalizado:</strong> Asesoría según tus intereses</li>
                        <li>✅ <strong>Descuentos Progresivos:</strong> Acumula beneficios con cada viaje</li>
                        <li>✅ <strong>Recordatorios:</strong> Te avisamos de cupos limitados</li>
                        <li>✅ <strong>Contenido Personalizado:</strong> Recomendaciones a tu medida</li>
                    </ul>
                </div>
            </div>
        </div>
    </section>
'''
    
    # Buscar la sección de contacto para añadir antes
    contact_section = '<footer class="main-footer-section" id="contacto">'
    if contact_section in content:
        content = content.replace(contact_section, crm_section + '\n' + contact_section)
    
    # Añadir CSS para CRM
    crm_css = '''
    
    /* CRM Lead Capture Section */
    .crm-lead-section {
        background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
        padding: 4rem 0;
        margin: 3rem 0;
        color: white;
    }
    
    .crm-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .crm-header h2 {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .crm-header p {
        font-size: 1.2rem;
        opacity: 0.9;
    }
    
    .crm-container {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: start;
    }
    
    .crm-form-wrapper {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
    }
    
    .crm-lead-form .form-group {
        margin-bottom: 1.5rem;
    }
    
    .crm-lead-form label {
        display: block;
        margin-bottom: 0.5rem;
        font-weight: 600;
    }
    
    .crm-lead-form input[type="text"],
    .crm-lead-form input[type="email"],
    .crm-lead-form input[type="tel"],
    .crm-lead-form select {
        width: 100%;
        padding: 0.75rem;
        border: 1px solid rgba(255,255,255,0.3);
        border-radius: 10px;
        background: rgba(255,255,255,0.1);
        color: white;
        font-size: 1rem;
    }
    
    .crm-lead-form input:focus,
    .crm-lead-form select:focus {
        outline: none;
        border-color: #3498db;
    }
    
    .interests-checkboxes {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.5rem;
    }
    
    .interests-checkboxes label {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-weight: normal;
    }
    
    .privacy-agreement {
        display: flex;
        align-items: flex-start;
        gap: 0.5rem;
        font-size: 0.9rem;
    }
    
    .privacy-agreement input {
        margin-top: 0.2rem;
    }
    
    .btn-crm-submit {
        background: #3498db;
        color: white;
        border: none;
        padding: 1rem 2rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 700;
        cursor: pointer;
        width: 100%;
        transition: all 0.3s ease;
    }
    
    .btn-crm-submit:hover {
        background: #2980b9;
        transform: translateY(-2px);
    }
    
    .crm-benefits {
        background: rgba(255,255,255,0.05);
        border-radius: 20px;
        padding: 2rem;
    }
    
    .crm-benefits h3 {
        font-size: 1.5rem;
        margin-bottom: 1.5rem;
    }
    
    .benefits-list {
        list-style: none;
        padding: 0;
    }
    
    .benefits-list li {
        padding: 1rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }
    
    .benefits-list li:last-child {
        border-bottom: none;
    }
    
    @media (max-width: 768px) {
        .crm-container {
            grid-template-columns: 1fr;
        }
        
        .interests-checkboxes {
            grid-template-columns: 1fr;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, crm_css + '\n' + style_end)
    
    # Añadir JavaScript para CRM
    crm_js = '''
    <script>
    document.getElementById('crmLeadForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        const name = formData.get('name');
        const email = formData.get('email');
        const phone = formData.get('phone');
        const city = formData.get('city');
        const interests = Array.from(document.querySelectorAll('input[name="interests"]:checked')).map(cb => cb.value);
        const budget = formData.get('budget');
        
        const message = `Hola Quindío Travel, deseo registrarme en su sistema de gestión de viajeros:\\n\\n` +
            `👤 Nombre: ${name}\\n` +
            `📧 Email: ${email}\\n` +
            `📱 WhatsApp: ${phone}\\n` +
            `🏙 Ciudad: ${city}\\n` +
            `🎯 Intereses: ${interests.join(', ') || 'No especificados'}\\n` +
            `💰 Presupuesto: ${budget}\\n\\n` +
            `Quiero recibir ofertas personalizadas y seguimiento exclusivo.`;
        
        const whatsappUrl = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;
        window.open(whatsappUrl, '_blank');
        
        alert('¡Gracias por registrarte! Pronto recibirás asesoría personalizada.');
        this.reset();
    });
    </script>
'''
    
    # Buscar </body> para añadir script
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, crm_js + '\n' + body_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Sistema CRM añadido")

if __name__ == "__main__":
    add_crm_system()