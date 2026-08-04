from pathlib import Path

def fix_don_chucho_usage():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remover avatar de botones de WhatsApp (usar icono FontAwesome en su lugar)
    avatar_pattern = '<img src="assets/images/don-chucho-avatar.png" alt="Don Chucho" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;">'
    whatsapp_icon = '<i class="fab fa-whatsapp"></i>'
    
    # Reemplazar avatar con icono de WhatsApp en botones (excepto chatbot)
    import re
    
    # Encontrar todas las instancias del avatar en botones wa-cta-link
    wa_buttons = re.findall(r'<a[^>]*class="[^"]*wa-cta-link[^"]*"[^>]*>' + re.escape(avatar_pattern) + r'[^<]*</a>', content)
    
    for button in wa_buttons:
        new_button = button.replace(avatar_pattern, whatsapp_icon)
        content = content.replace(button, new_button)
    
    # Mantener solo en el chatbot
    content = content.replace(
        '<div class="chatbot-toggle" onclick="toggleChatbot()"><i class="fab fa-whatsapp"></i></div>',
        '<div class="chatbot-toggle" onclick="toggleChatbot()"><img src="assets/images/don-chucho-avatar.png" alt="Don Chucho" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;"></div>'
    )
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Avatar Don Chucho limitado al chatbot solamente")

if __name__ == "__main__":
    fix_don_chucho_usage()