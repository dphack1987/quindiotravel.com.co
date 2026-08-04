"""
Integrar Avatar Don Chucho en el Chatbot
Personalizar el asistente virtual con imagen de Don Chucho
"""

from pathlib import Path
import shutil

def integrate_don_chucho_avatar():
    """Integra el avatar de Don Chucho en el chatbot"""
    
    avatar_source = Path(__file__).parent / "avatar_chucho" / "Don Chucho.png"
    avatar_destination = Path(__file__).parent / "assets" / "images" / "don-chucho-avatar.png"
    
    # Copiar avatar a assets/images
    if avatar_source.exists():
        shutil.copy(avatar_source, avatar_destination)
        print(f"[OK] Avatar Don Chucho copiado a: {avatar_destination}")
    else:
        print(f"[ERROR] Avatar no encontrado: {avatar_source}")
        return False
    
    # Actualizar index.html para usar el avatar
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Reemplazar el icono del chatbot con el avatar de Don Chucho
    old_chatbot_icon = '<i class="fab fa-whatsapp"></i>'
    new_chatbot_icon = '<img src="assets/images/don-chucho-avatar.png" alt="Don Chucho" style="width: 40px; height: 40px; border-radius: 50%; object-fit: cover;">'
    
    content = content.replace(old_chatbot_icon, new_chatbot_icon)
    
    # Actualizar el header del chatbot para incluir avatar
    old_header_content = '''<div class="chatbot-header-content">
                <i class="fas fa-robot"></i>
                <span>Asistente Quindío Travel</span>
            </div>'''
    
    new_header_content = '''<div class="chatbot-header-content">
                <img src="assets/images/don-chucho-avatar.png" alt="Don Chucho" style="width: 35px; height: 35px; border-radius: 50%; object-fit: cover; margin-right: 10px;">
                <span>Don Chucho - Asistente Quindío Travel</span>
            </div>'''
    
    content = content.replace(old_header_content, new_header_content)
    
    # Actualizar nombre del bot en mensajes
    content = content.replace('¡Hola! 👋 Soy el asistente virtual de Quindío Travel', '¡Hola! 👋 Soy Don Chucho, tu asistente experto en el Eje Cafetero')
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("[OK] Avatar Don Chucho integrado en el chatbot")
    return True

if __name__ == "__main__":
    print("Integrando avatar Don Chucho en el chatbot...")
    print("=" * 70)
    
    integrate_don_chucho_avatar()
    
    print("\n" + "=" * 70)
    print("Avatar Don Chucho integrado exitosamente")