"""
Añadir CSS Moderno a la Promoción del Mes
Implementa diseño moderno con gradientes, glassmorphism y animaciones
"""

from pathlib import Path

def add_modern_promo_css():
    """Añade CSS moderno para la sección de promoción"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el </style> del critical CSS para añadir CSS adicional
    critical_css_end = '</style>'
    
    # CSS moderno para promoción
    modern_promo_css = '''
    
    /* Modern Promotion Section Styles */
    .promo-badge {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        background: linear-gradient(135deg, #FF6B6B 0%, #FFD93D 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 50px;
        font-weight: 700;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.3);
        animation: pulse 2s infinite;
    }
    
    .badge-icon {
        font-size: 1.2rem;
        animation: shake 0.5s infinite;
    }
    
    .badge-urgent {
        background: rgba(255, 255, 255, 0.3);
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }
    
    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-10deg); }
        75% { transform: rotate(10deg); }
    }
    
    .promo-month {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        position: relative;
        overflow: hidden;
    }
    
    .promo-month::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: float 6s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(180deg); }
    }
    
    .promo-content {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 3rem;
        align-items: center;
        position: relative;
        z-index: 1;
    }
    
    @media (max-width: 768px) {
        .promo-content {
            grid-template-columns: 1fr;
        }
    }
    
    .promo-img-wrapper {
        background-size: cover;
        background-position: center;
        border-radius: 20px;
        height: 400px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
        transition: transform 0.3s ease;
    }
    
    .promo-img-wrapper:hover {
        transform: scale(1.05);
    }
    
    .promo-overlay {
        background: linear-gradient(to top, rgba(0,0,0,0.7), transparent);
        position: absolute;
        inset: 0;
    }
    
    .promo-discount {
        position: absolute;
        top: 20px;
        right: 20px;
        background: rgba(255,255,255,0.2);
        backdrop-filter: blur(10px);
        padding: 1rem 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.3);
        text-align: center;
    }
    
    .discount-text {
        font-size: 2rem;
        font-weight: 800;
        color: #FFD93D;
        display: block;
    }
    
    .discount-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: white;
    }
    
    .promo-details {
        color: white;
    }
    
    .promo-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 1rem;
        line-height: 1.2;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .promo-subtitle {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    .promo-destinations {
        font-size: 1rem;
        font-weight: 500;
        margin-bottom: 1.5rem;
        opacity: 0.8;
    }
    
    .promo-description {
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    .promo-price {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
        display: inline-block;
    }
    
    .price-main {
        font-size: 2.5rem;
        font-weight: 800;
        color: #FFD93D;
    }
    
    .price-label {
        font-size: 0.875rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.8;
    }
    
    .promo-cta {
        background: linear-gradient(135deg, #FF6B6B 0%, #FFD93D 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 700;
        text-decoration: none;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(255, 107, 107, 0.4);
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
    }
    
    .promo-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 107, 107, 0.6);
    }
    
    .countdown-timer {
        background: rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        padding: 1rem 1.5rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.2);
        display: flex;
        gap: 1rem;
        align-items: center;
    }
    
    .time-block {
        text-align: center;
    }
    
    .time-value {
        font-size: 2rem;
        font-weight: 800;
        color: #FFD93D;
        display: block;
    }
    
    .time-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        opacity: 0.8;
    }
'''
    
    # Buscar </style> del critical CSS para insertar antes
    if critical_css_end in content:
        content = content.replace(critical_css_end, modern_promo_css + '\n' + critical_css_end)
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("[OK] CSS moderno añadido para promoción del mes")
        return True
    else:
        print("[ERROR] No se encontró </style> en critical CSS")
        return False

if __name__ == "__main__":
    print("Añadiendo CSS moderno para promoción del mes...")
    print("=" * 70)
    
    add_modern_promo_css()
    
    print("\n" + "=" * 70)
    print("CSS moderno añadido exitosamente")