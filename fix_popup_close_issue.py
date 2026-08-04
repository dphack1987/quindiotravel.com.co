from pathlib import Path

def fix_popup_close_issue():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar que los event listeners del popup estén configurados correctamente
    popup_js_fix = '''
    <script>
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
    </script>
'''
    
    # Buscar </body> para añadir el script de corrección
    body_end = '</body>'
    if body_end in content:
        content = content.replace(body_end, popup_js_fix + '\n' + body_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Corrección de cierre de popup añadida")

if __name__ == "__main__":
    fix_popup_close_issue()