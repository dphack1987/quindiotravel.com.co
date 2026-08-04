"""
Añadir CSS para Reviews y Ratings
Estilos modernos inspirados en Booking.com
"""

from pathlib import Path

def add_reviews_css():
    """Añade CSS para la sección de reviews"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar </style> para añadir CSS antes
    style_end = '</style>'
    
    reviews_css = '''
    
    /* Reviews and Ratings Section Styles */
    .reviews-section {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 4rem 0;
        margin: 3rem 0;
    }
    
    .reviews-header {
        text-align: center;
        margin-bottom: 3rem;
    }
    
    .reviews-title {
        font-size: 2.5rem;
        font-weight: 800;
        color: var(--texto-oscuro);
        margin-bottom: 0.5rem;
    }
    
    .reviews-subtitle {
        font-size: 1.2rem;
        color: var(--marron-madera);
        margin-bottom: 1.5rem;
    }
    
    .reviews-overall-rating {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 1rem;
        font-size: 1.5rem;
        font-weight: 700;
    }
    
    .rating-stars {
        color: #FFD93D;
        font-size: 1.8rem;
    }
    
    .rating-number {
        color: var(--texto-oscuro);
    }
    
    .rating-total {
        color: var(--marron-madera);
        font-size: 1rem;
        font-weight: 500;
    }
    
    .reviews-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    .review-card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }
    
    .review-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }
    
    .review-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 1rem;
    }
    
    .reviewer-info {
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .reviewer-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 1.2rem;
    }
    
    .reviewer-details {
        display: flex;
        flex-direction: column;
    }
    
    .reviewer-name {
        font-weight: 600;
        color: var(--texto-oscuro);
    }
    
    .review-date {
        font-size: 0.85rem;
        color: var(--marron-madera);
    }
    
    .review-rating {
        color: #FFD93D;
        font-size: 1.2rem;
    }
    
    .review-content {
        margin-bottom: 1rem;
    }
    
    .review-text {
        color: var(--texto-oscuro);
        line-height: 1.6;
        margin-bottom: 0.75rem;
    }
    
    .review-plan {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        font-size: 0.9rem;
    }
    
    .plan-label {
        font-weight: 600;
        color: var(--marron-madera);
    }
    
    .plan-name {
        color: var(--texto-oscuro);
    }
    
    .reviews-cta {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
    }
    
    .btn-review-cta,
    .btn-google-review {
        padding: 1rem 2rem;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .btn-review-cta {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .btn-review-cta:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
    }
    
    .btn-google-review {
        background: white;
        color: var(--texto-oscuro);
        border: 2px solid var(--texto-oscuro);
    }
    
    .btn-google-review:hover {
        background: var(--texto-oscuro);
        color: white;
    }
    
    @media (max-width: 768px) {
        .reviews-title {
            font-size: 2rem;
        }
        
        .reviews-grid {
            grid-template-columns: 1fr;
        }
        
        .reviews-cta {
            flex-direction: column;
        }
    }
'''
    
    if style_end in content:
        content = content.replace(style_end, reviews_css + '\n' + style_end)
        print("[OK] CSS para reviews añadido")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Añadiendo CSS para reviews y ratings...")
    print("=" * 70)
    
    add_reviews_css()
    
    print("\n" + "=" * 70)
    print("CSS para reviews añadido exitosamente")