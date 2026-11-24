/**
 * Quindío Travel — Scroll Reveal
 * Observa tarjetas y bloques de contenido y los revela al entrar en viewport.
 * Se auto-etiqueta: no requiere cambios en el HTML.
 * Respeta prefers-reduced-motion y no toca elementos visibles al cargar.
 */
(function () {
    'use strict';

    var SELECTORS = [
        '.experiencia-card',
        '.hotel-card',
        '.municipio-card',
        '.blog-card',
        '.review-card',
        '.stat-card',
        '.plan-card',
        '.plan-card-enhanced',
        '.flexible-step-card',
        '.home-season-promo__content > *',
        '.home-season-promo__visual',
        '.why-us > *',
        '.trust-signals > *',
        '.sustainability-section > *',
        '.loyalty-program-section > *',
        '.followup-section > *',
        '.map-section > *'
    ];

    function init() {
        if (!('IntersectionObserver' in window)) return;
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

        var viewportH = window.innerHeight || document.documentElement.clientHeight;
        var targets = [];

        SELECTORS.forEach(function (sel) {
            try {
                document.querySelectorAll(sel).forEach(function (el) {
                    if (el.dataset.revealTagged) return;
                    el.dataset.revealTagged = '1';
                    // No animar lo que ya es visible al cargar (evita flash)
                    var rect = el.getBoundingClientRect();
                    if (rect.top < viewportH * 0.95 && rect.bottom > 0) return;
                    el.classList.add('reveal-on-scroll');
                    targets.push(el);
                });
            } catch (e) { /* selector inválido: ignorar */ }
        });

        if (!targets.length) return;

        var observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (entry.isIntersecting) {
                    entry.target.classList.add('revealed');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

        targets.forEach(function (el) { observer.observe(el); });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
