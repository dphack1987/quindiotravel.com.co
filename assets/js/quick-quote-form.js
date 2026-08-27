/**
 * Formulario de Cotización Rápida
 * Sistema simplificado de contacto para maximizar conversiones
 */

(function() {
    'use strict';

    class QuickQuoteForm {
        constructor() {
            this.form = this.createForm();
            this.init();
        }

        createForm() {
            // Crear formulario flotante
            const formContainer = document.createElement('div');
            formContainer.id = 'quick-quote-form';
            formContainer.style.cssText = `
                position: fixed;
                bottom: 90px;
                right: 20px;
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.15);
                z-index: 9999;
                width: 300px;
                display: none;
                border: 2px solid #2E5A36;
            `;

            formContainer.innerHTML = `
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px;">
                    <h3 style="margin: 0; color: #2E5A36; font-size: 1.1rem;">Cotización Rápida</h3>
                    <button id="close-form" style="background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #666;">&times;</button>
                </div>
                <form id="quote-form">
                    <div style="margin-bottom: 12px;">
                        <label style="display: block; margin-bottom: 5px; font-weight: 600; color: #333; font-size: 0.9rem;">Nombre:</label>
                        <input type="text" id="quote-name" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 0.9rem;" placeholder="Tu nombre">
                    </div>
                    <div style="margin-bottom: 12px;">
                        <label style="display: block; margin-bottom: 5px; font-weight: 600; color: #333; font-size: 0.9rem;">Fecha deseada:</label>
                        <input type="date" id="quote-date" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 0.9rem;">
                    </div>
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; margin-bottom: 5px; font-weight: 600; color: #333; font-size: 0.9rem;">Destino:</label>
                        <select id="quote-destination" required style="width: 100%; padding: 10px; border: 1px solid #ddd; border-radius: 6px; font-size: 0.9rem;">
                            <option value="">Selecciona destino</option>
                            <option value="Valle de Cocora">Valle de Cocora</option>
                            <option value="Parque del Café">Parque del Café</option>
                            <option value="Plan completo Eje Cafetero">Plan completo Eje Cafetero</option>
                            <option value="Termales">Termales</option>
                            <option value="Otro">Otro destino</option>
                        </select>
                    </div>
                    <button type="submit" style="width: 100%; background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color: white; padding: 12px; border: none; border-radius: 8px; font-weight: 700; cursor: pointer; font-size: 0.95rem; transition: all 0.3s ease;">
                        <i class="fab fa-whatsapp"></i> Enviar por WhatsApp
                    </button>
                    <p style="font-size: 0.75rem; color: #666; text-align: center; margin-top: 10px;">Respuesta en 15 minutos</p>
                </form>
            `;

            document.body.appendChild(formContainer);
            return formContainer;
        }

        init() {
            // Botón flotante para abrir formulario
            const floatingButton = document.createElement('button');
            floatingButton.id = 'quote-button';
            floatingButton.innerHTML = '<i class="fas fa-calculator"></i> Cotizar Rápido';
            floatingButton.style.cssText = `
                position: fixed;
                bottom: 90px;
                right: 20px;
                background: linear-gradient(135deg, #2E5A36 0%, #1a3a1f 100%);
                color: white;
                padding: 15px 25px;
                border-radius: 50px;
                border: none;
                cursor: pointer;
                font-weight: 700;
                font-size: 0.95rem;
                box-shadow: 0 4px 15px rgba(46, 90, 54, 0.4);
                z-index: 9998;
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                gap: 8px;
            `;

            floatingButton.onmouseover = function() {
                this.style.transform = 'scale(1.05)';
                this.style.boxShadow = '0 6px 20px rgba(46, 90, 54, 0.6)';
            };

            floatingButton.onmouseout = function() {
                this.style.transform = 'scale(1)';
                this.style.boxShadow = '0 4px 15px rgba(46, 90, 54, 0.4)';
            };

            floatingButton.onclick = () => {
                this.form.style.display = 'block';
                floatingButton.style.display = 'none';
            };

            document.body.appendChild(floatingButton);

            // Evento de cerrar formulario
            document.getElementById('close-form').onclick = () => {
                this.form.style.display = 'none';
                floatingButton.style.display = 'flex';
            };

            // Manejar envío del formulario
            document.getElementById('quote-form').onsubmit = (e) => {
                e.preventDefault();
                this.handleFormSubmit();
            };

            // Establecer fecha mínima (hoy)
            const dateInput = document.getElementById('quote-date');
            const today = new Date().toISOString().split('T')[0];
            dateInput.min = today;
        }

        handleFormSubmit() {
            const name = document.getElementById('quote-name').value;
            const date = document.getElementById('quote-date').value;
            const destination = document.getElementById('quote-destination').value;

            // Crear mensaje de WhatsApp
            const message = `Hola Quindío Travel 🌿, quiero cotizar un plan:\n\n👤 Nombre: ${name}\n📅 Fecha deseada: ${date}\n🎯 Destino: ${destination}\n\n¿Me pueden dar información y precio disponible?`;

            // URL de WhatsApp
            const whatsappUrl = `https://wa.me/573174426044?text=${encodeURIComponent(message)}`;

            // Tracking de conversión
            this.trackConversion('quick_quote_submit');

            // Abrir WhatsApp
            window.open(whatsappUrl, '_blank');

            // Cerrar formulario
            this.form.style.display = 'none';
            document.getElementById('quote-button').style.display = 'flex';

            // Resetear formulario
            document.getElementById('quote-form').reset();
        }

        trackConversion(eventType) {
            if (typeof gtag !== 'undefined') {
                gtag('event', eventType, {
                    'event_category': 'quick_quote',
                    'event_label': 'form_submission'
                });
            }
            
            console.log(`Conversion event tracked: ${eventType}`);
        }
    }

    // Inicializar cuando el DOM esté listo
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            new QuickQuoteForm();
        });
    } else {
        new QuickQuoteForm();
    }

})();