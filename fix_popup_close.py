from pathlib import Path

def fix_popup_close():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el script de cierre del popup y reemplazarlo con una versión mejorada
    old_popup_script = '''    <script>
    // Asegurar que el popup se pueda cerrar correctamente
    document.addEventListener('DOMContentLoaded', function() {
        const popup = document.getElementById('lead-capture-popup');
        const closeButtons = document.querySelectorAll('[data-popup-close]');
        
        // Función para cerrar popup
        function closePopup() {
            if (popup) {
                popup.style.display = 'none';
                document.body.style.overflow = ''; // Restaurar scroll
            }
        }
        
        // Añadir event listeners a todos los botones de cierre
        closeButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                closePopup();
            });
        });
        
        // También cerrar al hacer click en el overlay
        const overlay = document.querySelector('.popup-overlay');
        if (overlay) {
            overlay.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                closePopup();
            });
        }
        
        // Permitir cerrar con tecla ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && popup.style.display === 'block') {
                closePopup();
            }
        });
        
        // Sobrescribir la función closePopup existente
        window.closePopup = closePopup;
    });
    </script>'''
    
    new_popup_script = '''    <script>
    // Script CORREGIDO para asegurar que el popup se pueda cerrar correctamente
    document.addEventListener('DOMContentLoaded', function() {
        const popup = document.getElementById('lead-capture-popup');
        
        // Función robusta para cerrar popup
        function closePopup() {
            if (popup) {
                popup.style.display = 'none';
                document.body.style.overflow = ''; // Restaurar scroll del body
                console.log('Popup cerrado correctamente');
            }
        }
        
        // Hacer la función global para que pueda ser llamada desde otros scripts
        window.closePopup = closePopup;
        
        // Añadir event listeners a todos los botones de cierre usando múltiples métodos
        const closeButtons = document.querySelectorAll('[data-popup-close], .popup-close');
        
        closeButtons.forEach(button => {
            // Usar addEventListener con captura para asegurar que se ejecute
            button.addEventListener('click', function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('Botón de cierre clickeado');
                closePopup();
            }, true); // true = capture phase
            
            // También añadir onclick directo como respaldo
            button.onclick = function(e) {
                e.preventDefault();
                e.stopPropagation();
                console.log('Botón de cierre clickeado (onclick)');
                closePopup();
            };
        });
        
        // Cerrar al hacer click en el overlay (fuera del contenido)
        const overlay = document.querySelector('.popup-overlay');
        if (overlay) {
            overlay.addEventListener('click', function(e) {
                // Solo cerrar si el clic es directamente en el overlay, no en elementos hijos
                if (e.target === overlay) {
                    e.preventDefault();
                    e.stopPropagation();
                    console.log('Overlay clickeado');
                    closePopup();
                }
            }, true);
        }
        
        // Permitir cerrar con tecla ESC
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && popup && popup.style.display === 'block') {
                e.preventDefault();
                console.log('Tecla ESC presionada');
                closePopup();
            }
        });
        
        // Asegurar que el popup tenga z-index suficiente
        if (popup) {
            popup.style.zIndex = '9999';
        }
        
        console.log('Script de cierre de popup inicializado correctamente');
    });
    </script>'''
    
    if old_popup_script in content:
        content = content.replace(old_popup_script, new_popup_script)
        print("Script de cierre del popup actualizado con correcciones")
    else:
        print("No se encontró el script original, intentando inserción manual")
        # Buscar el final del body para insertar allí
        body_end = content.find('</body>')
        if body_end > 0:
            content = content[:body_end] + new_popup_script + '\n' + content[body_end:]
            print("Script de cierre del popup insertado manualmente")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_popup_close()