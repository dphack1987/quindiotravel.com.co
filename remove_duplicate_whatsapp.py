from pathlib import Path

def remove_duplicate_whatsapp():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eliminar el botón flotante de WhatsApp duplicado que choca con el chatbot
    start_marker = '<!-- Botón flotante de WhatsApp para contacto inmediato -->'
    end_marker = '</style>'
    
    if start_marker in content:
        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker, start_idx) + len(end_marker)
        
        if start_idx != -1 and end_idx != -1:
            content = content[:start_idx] + content[end_idx:]
            print("Botón flotante WhatsApp duplicado eliminado")
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    remove_duplicate_whatsapp()