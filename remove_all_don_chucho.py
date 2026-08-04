from pathlib import Path

def remove_all_don_chucho():
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Eliminar todas las referencias a don-chucho-avatar.png
    content = content.replace('<img src="assets/images/don-chucho-avatar.png"', '<i class="fab fa-whatsapp"></i>')
    
    # Eliminar el chatbot Don Chucho completo si existe
    import re
    don_chucho_complete = r'<!-- Chatbot Don Chucho - Arriero Guía Turístico -->.*?</div>\s*</div>\s*</div>\s*<script>.*?</script>\s*<style>.*?</style>'
    content = re.sub(don_chucho_complete, '', content, flags=re.DOTALL)
    
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Todas las referencias de Don Chucho eliminadas")

if __name__ == "__main__":
    remove_all_don_chucho()