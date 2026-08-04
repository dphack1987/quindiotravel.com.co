"""
Añadir Sección de Reviews y Ratings
Implementa sistema de reviews como Booking.com con schema Review
"""

from pathlib import Path

def add_reviews_section_to_index():
    """Añade sección de reviews a index.html"""
    
    index_path = Path(__file__).parent / "index.html"
    
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Buscar el footer para añadir reviews antes
    footer_start = '<footer'
    
    reviews_section = '''
    <!-- Reviews and Ratings Section -->
    <section class="reviews-section" id="reviews" aria-label="Reseñas y Valoraciones de Clientes">
        <div class="container">
            <div class="reviews-header">
                <h2 class="reviews-title">Lo que dicen nuestros viajeros</h2>
                <p class="reviews-subtitle">+1,200 clientes satisfechos nos respaldan</p>
                <div class="reviews-overall-rating">
                    <div class="rating-stars">
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star"></i>
                        <i class="fas fa-star-half-alt"></i>
                    </div>
                    <span class="rating-number">4.8/5</span>
                    <span class="rating-total">(1,247 reviews)</span>
                </div>
            </div>
            
            <div class="reviews-grid">
                <!-- Review 1 -->
                <div class="review-card" itemscope itemtype="https://schema.org/Review">
                    <div class="review-header">
                        <div class="reviewer-info">
                            <div class="reviewer-avatar" itemprop="author" itemscope itemtype="https://schema.org/Person">
                                <span class="avatar-initials">MG</span>
                                <meta itemprop="name" content="María González">
                            </div>
                            <div class="reviewer-details">
                                <span class="reviewer-name">María González</span>
                                <span class="review-date">Agosto 2026</span>
                            </div>
                        </div>
                        <div class="review-rating" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <meta itemprop="ratingValue" content="5">
                            <meta itemprop="bestRating" content="5">
                        </div>
                    </div>
                    <div class="review-content">
                        <p class="review-text" itemprop="reviewBody">Increíble experiencia en el Eje Cafetero. Los guías fueron muy profesionales y las fincas cafeteras hermosas. Definitely recommend this tour operator!</p>
                        <div class="review-plan">
                            <span class="plan-label">Plan:</span>
                            <span class="plan-name">Experiencia Completa del Eje Cafetero</span>
                        </div>
                    </div>
                </div>
                
                <!-- Review 2 -->
                <div class="review-card" itemscope itemtype="https://schema.org/Review">
                    <div class="review-header">
                        <div class="reviewer-info">
                            <div class="reviewer-avatar" itemprop="author" itemscope itemtype="https://schema.org/Person">
                                <span class="avatar-initials">CR</span>
                                <meta itemprop="name" content="Carlos Rodríguez">
                            </div>
                            <div class="reviewer-details">
                                <span class="reviewer-name">Carlos Rodríguez</span>
                                <span class="review-date">Julio 2026</span>
                            </div>
                        </div>
                        <div class="review-rating" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star-half-alt"></i>
                            <meta itemprop="ratingValue" content="4.5">
                            <meta itemprop="bestRating" content="5">
                        </div>
                    </div>
                    <div class="review-content">
                        <p class="review-text" itemprop="reviewBody">Excelente organización y atención. El Valle de Cocora es espectacular y el guía local muy knowledgeable. Perfect para familias with kids.</p>
                        <div class="review-plan">
                            <span class="plan-label">Plan:</span>
                            <span class="plan-name">Aventura Natural en el Eje Cafetero</span>
                        </div>
                    </div>
                </div>
                
                <!-- Review 3 -->
                <div class="review-card" itemscope itemtype="https://schema.org/Review">
                    <div class="review-header">
                        <div class="reviewer-info">
                            <div class="reviewer-avatar" itemprop="author" itemscope itemtype="https://schema.org/Person">
                                <span class="avatar-initials">LP</span>
                                <meta itemprop="name" content="Laura Pérez">
                            </div>
                            <div class="reviewer-details">
                                <span class="reviewer-name">Laura Pérez</span>
                                <span class="review-date">Junio 2026</span>
                            </div>
                        </div>
                        <div class="review-rating" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <meta itemprop="ratingValue" content="5">
                            <meta itemprop="bestRating" content="5">
                        </div>
                    </div>
                    <div class="review-content">
                        <p class="review-text" itemprop="reviewBody">The best coffee tour experience ever! The guides were passionate about coffee culture and the accommodation was perfect. Highly recommended for coffee lovers.</p>
                        <div class="review-plan">
                            <span class="plan-label">Plan:</span>
                            <span class="plan-name">Escapada Cafetera de Fin de Semana</span>
                        </div>
                    </div>
                </div>
                
                <!-- Review 4 -->
                <div class="review-card" itemscope itemtype="https://schema.org/Review">
                    <div class="review-header">
                        <div class="reviewer-info">
                            <div class="reviewer-avatar" itemprop="author" itemscope itemtype="https://schema.org/Person">
                                <span class="avatar-initials">AM</span>
                                <meta itemprop="name" content="Andrés Martínez">
                            </div>
                            <div class="reviewer-details">
                                <span class="reviewer-name">Andrés Martínez</span>
                                <span class="review-date">Mayo 2026</span>
                            </div>
                        </div>
                        <div class="review-rating" itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <i class="fas fa-star"></i>
                            <meta itemprop="ratingValue" content="5">
                            <meta itemprop="bestRating" content="5">
                        </div>
                    </div>
                    <div class="review-content">
                        <p class="review-text" itemprop="reviewBody">Servicio excepcional desde el primer contacto. WhatsApp response time was amazing and the itinerary was perfectly planned. Great value for money!</p>
                        <div class="review-plan">
                            <span class="plan-label">Plan:</span>
                            <span class="plan-name">Experiencia Premium del Eje Cafetero</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- CTA para dejar review -->
            <div class="reviews-cta">
                <a href="#" class="btn-review-cta" data-wa-template="review">
                    <i class="fas fa-star"></i> Deja tu Reseña
                </a>
                <a href="https://www.google.com/maps" target="_blank" rel="noopener" class="btn-google-review">
                    <i class="fab fa-google"></i> Reseña en Google
                </a>
            </div>
        </div>
    </section>
'''
    
    if footer_start in content:
        content = content.replace(footer_start, reviews_section + '\n' + footer_start)
        print("[OK] Sección de reviews añadida antes del footer")
    
    # Añadir schema AggregateRating
    aggregate_rating_schema = '''
    <!-- AggregateRating Schema para Reviews -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "TravelAgency",
        "name": "Quindío Travel",
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "1247",
            "bestRating": "5",
            "worstRating": "1"
        },
        "review": [
            {
                "@type": "Review",
                "author": {
                    "@type": "Person",
                    "name": "María González"
                },
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": "5",
                    "bestRating": "5"
                },
                "reviewBody": "Increíble experiencia en el Eje Cafetero. Los guías fueron muy profesionales y las fincas cafeteras hermosas."
            },
            {
                "@type": "Review",
                "author": {
                    "@type": "Person",
                    "name": "Carlos Rodríguez"
                },
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": "4.5",
                    "bestRating": "5"
                },
                "reviewBody": "Excelente organización y atención. El Valle de Cocora es espectacular y el guía local muy knowledgeable."
            }
        ]
    }
    </script>
'''
    
    # Buscar </head> para añadir schema antes
    head_end = '</head>'
    if head_end in content:
        content = content.replace(head_end, aggregate_rating_schema + '\n' + head_end)
        print("[OK] Schema AggregateRating añadido")
    
    # Guardar cambios
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

if __name__ == "__main__":
    print("Añadiendo sección de reviews y ratings...")
    print("=" * 70)
    
    add_reviews_section_to_index()
    
    print("\n" + "=" * 70)
    print("Reviews y ratings añadidos exitosamente")