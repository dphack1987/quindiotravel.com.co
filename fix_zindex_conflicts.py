from pathlib import Path

def fix_zindex_conflicts():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Ajustar z-index para evitar superposiciones
    # Don Chucho Sidebar: z-index 998 (más bajo)
    # Chatbot: z-index 1000 (normal)
    # WhatsApp float: eliminar o mover
    
    # Reemplazar z-index de Don Chucho Sidebar
    content = content.replace(
        '.don-chucho-sidebar {\n        position: fixed;\n        left: 20px;\n        top: 50%;\n        transform: translateY(-50%);\n        z-index: 999;',
        '.don-chucho-sidebar {\n        position: fixed;\n        left: 20px;\n        top: 50%;\n        transform: translateY(-50%);\n        z-index: 998;'
    )
    
    # Eliminar whatsapp-float duplicado que choca con chatbot
    whatsapp_float_pattern = r'<style>\s*\.whatsapp-float \{[^}]*position:\s*fixed;[^}]*bottom:\s*30px;[^}]*right:\s*30px;[^}]*\}[^}*</style>'
    import re
    content = re.sub(whatsapp_float_pattern, '', content)
    
    # Eliminar don-chucho-chat duplicado
    don_chucho_chat_pattern = r'<style>\s*/\*\s*DON CHUCHO CHATBOT STYLES[^}]*\.don-chucho-chat \{[^}]*position:\s*fixed;[^}]*\}[^}*</style>'
    content = re.sub(don_chucho_chat_pattern, '', content)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Conflictos de z-index corregidos")

if __name__ == "__main__":
    fix_zindex_conflicts()