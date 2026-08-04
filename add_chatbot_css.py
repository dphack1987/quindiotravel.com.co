"""
Añadir CSS para Chatbot
Estilos modernos para el asistente virtual
"""

from pathlib import Path

def add_chatbot_css():
    """Añade CSS para el chatbot"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar </style> para añadir CSS antes
    style_end = '</style>'
    
    chatbot_css = '''
    
    /* Chatbot Styles */
    .chatbot-container {
        position: fixed;
        bottom: 30px;
        right: 30px;
        z-index: 1000;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .chatbot-toggle {
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 28px;
        cursor: pointer;
        box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
        transition: all 0.3s ease;
    }
    
    .chatbot-toggle:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 20px rgba(37, 211, 102, 0.6);
    }
    
    .chatbot-header {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white;
        padding: 15px;
        border-radius: 15px 15px 0 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;
    }
    
    .chatbot-header-content {
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .chatbot-header i {
        font-size: 20px;
    }
    
    .chatbot-close {
        background: none;
        border: none;
        color: white;
        font-size: 18px;
        cursor: pointer;
        opacity: 0.8;
        transition: opacity 0.3s ease;
    }
    
    .chatbot-close:hover {
        opacity: 1;
    }
    
    .chatbot-body {
        display: none;
        background: white;
        border-radius: 0 0 15px 15px;
        box-shadow: 0 5px 25px rgba(0,0,0,0.15);
        overflow: hidden;
        max-width: 350px;
        max-height: 450px;
    }
    
    .chatbot-open .chatbot-body {
        display: block;
    }
    
    .chatbot-messages {
        height: 350px;
        overflow-y: auto;
        padding: 15px;
        background: #f8f9fa;
    }
    
    .message {
        margin-bottom: 15px;
        animation: fadeIn 0.3s ease;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .message-content {
        padding: 12px 15px;
        border-radius: 15px;
        max-width: 85%;
        line-height: 1.4;
    }
    
    .bot-message .message-content {
        background: white;
        border-bottom-left-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    
    .user-message .message-content {
        background: linear-gradient(135deg, #25D366 0%, #128C7E 100%);
        color: white;
        border-bottom-right-radius: 5px;
        margin-left: auto;
    }
    
    .quick-replies {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 10px;
    }
    
    .quick-reply {
        background: white;
        border: 1px solid #25D366;
        color: #25D366;
        padding: 8px 12px;
        border-radius: 20px;
        cursor: pointer;
        font-size: 12px;
        transition: all 0.3s ease;
    }
    
    .quick-reply:hover {
        background: #25D366;
        color: white;
    }
    
    .chatbot-input {
        display: flex;
        padding: 15px;
        background: white;
        border-top: 1px solid #e9ecef;
    }
    
    .chatbot-input input {
        flex: 1;
        padding: 10px 15px;
        border: 1px solid #e9ecef;
        border-radius: 20px;
        outline: none;
        font-size: 14px;
    }
    
    .chatbot-input input:focus {
        border-color: #25D366;
    }
    
    .chatbot-input button {
        background: #25D366;
        color: white;
        border: none;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        margin-left: 10px;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    
    .chatbot-input button:hover {
        background: #128C7E;
    }
    
    @media (max-width: 768px) {
        .chatbot-container {
            bottom: 20px;
            right: 20px;
        }
        
        .chatbot-body {
            max-width: 300px;
            max-height: 400px;
        }
        
        .chatbot-messages {
            height: 300px;
        }
    }
'''
    
    if style_end in content:
        content = content.replace(style_end, chatbot_css + '\n' + style_end)
        print("[OK] CSS para chatbot añadido")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Añadiendo CSS para chatbot...")
    print("=" * 70)
    
    add_chatbot_css()
    
    print("\n" + "=" * 70)
    print("CSS para chatbot añadido exitosamente")