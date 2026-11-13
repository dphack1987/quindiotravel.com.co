/* ============================================
   QUINDÍO TRAVEL — Temática Diciembre
   Inyecta pill navideño + nieve ambiental.
   Activo en temporada: noviembre, diciembre y enero.
   ============================================ */
(function () {
    'use strict';

    // Solo en temporada navideña (mes 10 = noviembre, 11 = diciembre, 0 = enero)
    var mes = new Date().getMonth();
    if (mes !== 10 && mes !== 11 && mes !== 0) return;
    if (document.getElementById('qt-diciembre-pill')) return;

    var CTA_URL = '/planes-especiales-diciembre-2026.html';
    var CTA_LABEL = 'Ver Planes 🎄';

    // --- Nieve ambiental ---
    function crearNieve() {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
        var capa = document.createElement('div');
        capa.className = 'qt-nieve';
        capa.setAttribute('aria-hidden', 'true');

        var copos = 26;
        for (var i = 0; i < copos; i++) {
            var flake = document.createElement('span');
            flake.className = 'qt-nieve__flake';
            var tam = 2 + Math.random() * 4; // 2-6px
            var dur = 9 + Math.random() * 14; // 9-23s
            var delay = -Math.random() * 20; // inicio desfasado
            flake.style.left = (Math.random() * 100) + '%';
            flake.style.width = tam + 'px';
            flake.style.height = tam + 'px';
            flake.style.animationDuration = dur + 's';
            flake.style.animationDelay = delay + 's';
            flake.style.setProperty('--flake-opacity', (0.35 + Math.random() * 0.45).toFixed(2));
            flake.style.setProperty('--flake-drift', ((Math.random() * 120) - 60).toFixed(0) + 'px');
            capa.appendChild(flake);
        }
        document.body.appendChild(capa);
    }

    // --- Pill ---
    function crearPill() {
        var pill = document.createElement('div');
        pill.id = 'qt-diciembre-pill';
        pill.className = 'qt-diciembre-pill';
        pill.setAttribute('role', 'complementary');
        pill.setAttribute('aria-label', 'Promoción de diciembre');
        pill.innerHTML =
            '<span class="qt-diciembre-pill__text">🎄 <strong>Diciembre llegó al Quindío</strong> — Planes navideños</span>' +
            '<a class="qt-diciembre-pill__cta" href="' + CTA_URL + '">' + CTA_LABEL + '</a>' +
            '<button type="button" class="qt-diciembre-pill__close" aria-label="Cerrar promoción navideña">✕</button>';

        pill.querySelector('.qt-diciembre-pill__close').addEventListener('click', function () {
            pill.style.display = 'none';
            try { localStorage.setItem('qt-diciembre-pill-dismissed', '1'); } catch (e) {}
        });

        try {
            if (localStorage.getItem('qt-diciembre-pill-dismissed') === '1') return;
        } catch (e) {}

        document.body.appendChild(pill);
    }

    function init() {
        crearNieve();
        crearPill();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
