from pathlib import Path

def verify_mobile_optimization():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Verificar responsive queries en CSS
    responsive_count = content.count('@media (max-width: 768px)')
    print(f"Responsive queries: {responsive_count}")
    
    # Verificar viewport meta tag
    viewport_found = 'viewport' in content
    print(f"Viewport meta tag: {viewport_found}")
    
    # Verificar flexbox y grid layouts
    flexbox_count = content.count('display: flex')
    grid_count = content.count('display: grid')
    print(f"Flexbox layouts: {flexbox_count}")
    print(f"Grid layouts: {grid_count}")
    
    # Verificar secciones nuevas
    flexible_found = 'flexible-plans-section' in content
    loyalty_found = 'loyalty-program-section' in content
    transport_found = 'multi-origin-transport-section' in content
    print(f"Planes flexibles section: {flexible_found}")
    print(f"Programa lealtad section: {loyalty_found}")
    print(f"Transporte multi-origen section: {transport_found}")
    
    # Verificar Don Chucho sidebar
    sidebar_found = 'don-chucho-sidebar' in content
    print(f"Don Chucho sidebar: {sidebar_found}")
    
    # Verificar chatbot
    chatbot_found = 'chatbot-container' in content
    print(f"Chatbot container: {chatbot_found}")
    
    # Verificar multilenguaje
    language_found = 'language-selector' in content
    print(f"Language selector: {language_found}")
    
    print("\n✅ Verificación completada")

if __name__ == "__main__":
    verify_mobile_optimization()