from pathlib import Path

def add_perfect_don_chucho_button():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar el chatbot actual con un botón de Don Chucho perfecto
    don_chucho_button = '''
    <!-- Don Chucho Perfect Button -->
    <div class="don-chucho-perfect-button">
        <a href="#" data-wa-message="Hola Don Chucho, necesito asesoría sobre planes de viaje al Eje Cafetero" target="_blank" rel="noopener" class="don-chucho-link">
            <img src="assets/images/don-chucho-avatar.png" alt="Don Chucho - Guía Local" class="don-chucho-avatar-perfect">
            <span class="don-chucho-tooltip">Hola, soy Don Chucho</span>
        </a>
    </div>
'''
    
    # Eliminar el chatbot actual
    chatbot_pattern = r'<!-- Chatbot Flotante -->.*?</div>\s*</div>'
    import re
    content = re.sub(chatbot_pattern, don_chucho_button, content, flags=re.DOTALL)
    
    # Añadir CSS para el botón perfecto
    don_chucho_css = '''
    
    /* Don Chucho Perfect Button */
    .don-chucho-perfect-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        z-index: 999;
    }
    
    .don-chucho-link {
        display: block;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #8B4513, #D2691E);
        box-shadow: 0 4px 15px rgba(139, 69, 19, 0.3);
        transition: all 0.3s ease;
        position: relative;
        overflow: visible;
    }
    
    .don-chucho-link:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(139, 69, 19, 0.4);
    }
    
    .don-chucho-avatar-perfect {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid rgba(255,255,255,0.3);
        display: block;
    }
    
    .don-chucho-tooltip {
        position: absolute;
        right: 70px;
        top: 50%;
        transform: translateY(-50%);
        background: linear-gradient(135deg, #8B4513, #D2691E);
        color: white;
        padding: 8px 15px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        white-space: nowrap;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        box-shadow: 0 2px 10px rgba(0,0,0,0.2);
    }
    
    .don-chucho-link:hover .don-chucho-tooltip {
        opacity: 1;
        visibility: visible;
    }
    
    @media (max-width: 768px) {
        .don-chucho-perfect-button {
            bottom: 15px;
            right: 15px;
        }
        
        .don-chucho-link {
            width: 50px;
            height: 50px;
        }
        
        .don-chucho-avatar-perfect {
            width: 50px;
            height: 50px;
        }
        
        .don-chucho-tooltip {
            right: 60px;
            font-size: 0.75rem;
            padding: 6px 12px;
        }
    }
'''
    
    # Buscar </style> para añadir CSS
    style_end = '</style>'
    if style_end in content:
        content = content.replace(style_end, don_chucho_css + '\n' + style_end)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Botón perfecto de Don Chucho añadido")

if __name__ == "__main__":
    add_perfect_don_chucho_button()