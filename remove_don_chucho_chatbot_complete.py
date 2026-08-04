from pathlib import Path

def remove_don_chucho_chatbot_complete():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eliminar todo el chatbot Don Chucho completo
    don_chucho_pattern = r'<!-- Chatbot Don Chucho - Arriero Guía Turístico -->.*?</div>\s*</div>\s*</div>\s*</script>\s*<style>.*?</style>\s*</script>'
    import re
    content = re.sub(don_chucho_pattern, '', content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Chatbot Don Chucho completo eliminado")

if __name__ == "__main__":
    remove_don_chucho_chatbot_complete()