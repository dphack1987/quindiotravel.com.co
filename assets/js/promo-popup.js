(function () {
    'use strict';

    var DISMISS_KEY = 'qt_promo_dic2026_closed';
    var DISMISS_HOURS = 24;
    var SHOW_DELAY_MS = 15000;

    function inPromoWindow() {
        var d = new Date();
        var m = d.getMonth() + 1;
        var y = d.getFullYear();
        return ((y === 2026 && (m === 11 || m === 12)) || (y === 2027 && m === 1));
    }

    function recentlyDismissed() {
        try {
            var ts = parseInt(localStorage.getItem(DISMISS_KEY) || '0', 10);
            return ts && (Date.now() - ts) < DISMISS_HOURS * 3600 * 1000;
        } catch (e) {
            return false;
        }
    }

    function buildMarkup() {
        return '' +
            '<div id="promo-popup-dynamic" class="lead-capture-popup" data-popup-type="promo" style="display: none;">' +
            '  <div class="popup-overlay" data-popup-close></div>' +
            '  <div class="popup-content">' +
            '    <button class="popup-close" data-popup-close aria-label="Cerrar popup">&times;</button>' +
            '    <div class="popup-header">' +
            '      <h3>&#127876; PLANES ESPECIALES DICIEMBRE 2026!</h3>' +
            '      <p>Temporada alta 15 dic – 20 ene · M&aacute;x. 30 cupos</p>' +
            '    </div>' +
            '    <div class="promo-popup-content">' +
            '      <div style="text-align: center; margin-bottom: 20px;">' +
            '        <img src="assets/images/promocion-mes/promo-hero.png" alt="Planes Especiales Diciembre 2026 - Quind&iacute;o Travel" style="width: 100%; max-height: 200px; object-fit: cover; object-position: center top; border-radius: 10px; margin-bottom: 15px;" loading="lazy">' +
            '        <div style="background: #E63946; color: white; padding: 8px 16px; border-radius: 20px; display: inline-block; font-weight: 800; font-size: 0.9rem; margin-bottom: 15px;">&#127876; TEMPORADA NAVIDE&Ntilde;A</div>' +
            '      </div>' +
            '      <div style="margin-bottom: 20px;">' +
            '        <h4 style="color: #1b4332; margin-bottom: 10px;">4 D&iacute;as / 3 Noches (15 dic – 20 ene)</h4>' +
            '        <ul style="list-style: none; padding: 0; margin: 0;">' +
            '          <li style="padding: 8px 0; border-bottom: 1px solid #eee;">&#127976; Alojamiento + desayuno y cena</li>' +
            '          <li style="padding: 8px 0; border-bottom: 1px solid #eee;">&#127796; Cocora, Salento, Filandia y miradores</li>' +
            '          <li style="padding: 8px 0; border-bottom: 1px solid #eee;">&#9749; Parque del Caf&eacute;, PANACA y RECUCA</li>' +
            '          <li style="padding: 8px 0;">&#128666; Transporte interno y asistencia m&eacute;dica 24/7</li>' +
            '        </ul>' +
            '      </div>' +
            '      <div style="background: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 20px; text-align: center;">' +
            '        <div style="color: #1b4332; font-size: 1.5rem; font-weight: 800;">$1.464.000 <span style="font-size: 0.75rem; color: #666;">/ persona (4 pax, radio taxi)</span></div>' +
            '        <div style="color: #666; font-size: 0.8rem; margin-top: 6px;">Los Girasoles desde $2.452.000 &middot; Caf&eacute; Caf&eacute; desde $3.658.000</div>' +
            '      </div>' +
            '      <div style="display: flex; gap: 10px; flex-wrap: wrap;">' +
            '        <a href="https://wa.me/573174426044?text=Hola,%20quiero%20aprovechar%20los%20planes%20de%20diciembre%202026" target="_blank" rel="noopener" style="flex: 1; background: #25D366; color: white; padding: 12px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; text-align: center; display: inline-flex; align-items: center; justify-content: center; gap: 8px;">&#128172; Reservar Ahora</a>' +
            '        <a href="planes-especiales-diciembre-2026.html" style="flex: 1; background: transparent; border: 2px solid #1b4332; color: #1b4332; padding: 10px 20px; border-radius: 8px; text-decoration: none; font-weight: 700; text-align: center;">Ver Detalles</a>' +
            '      </div>' +
            '    </div>' +
            '  </div>' +
            '</div>';
    }

    function init() {
        if (!inPromoWindow()) return;
        if (document.getElementById('promo-popup')) return;
        if (document.getElementById('promo-popup-dynamic')) return;
        if (recentlyDismissed()) return;

        var path = window.location.pathname;
        if (path.indexOf('planes-especiales-diciembre-2026.html') !== -1 || path.indexOf('promo-noviembre-2026.html') !== -1) return;
        if (path.indexOf('promo-octubre-2026.html') !== -1) return;

        document.body.insertAdjacentHTML('beforeend', buildMarkup());

        var popup = document.getElementById('promo-popup-dynamic');

        function close() {
            popup.style.display = 'none';
            document.body.style.overflow = '';
            try { localStorage.setItem(DISMISS_KEY, String(Date.now())); } catch (e) {}
            if (Array.isArray(window.dataLayer)) {
                window.dataLayer.push({
                    event: 'promo_popup_closed',
                    page_path: window.location.pathname
                });
            }
        }

        popup.addEventListener('click', function (e) {
            if (e.target.closest && e.target.closest('[data-popup-close]')) {
                e.preventDefault();
                close();
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && popup.style.display === 'block') close();
        });

        setTimeout(function () {
            if (recentlyDismissed()) return;
            popup.style.display = 'block';
            if (Array.isArray(window.dataLayer)) {
                window.dataLayer.push({
                    event: 'promo_popup_shown',
                    page_path: window.location.pathname
                });
            }
        }, SHOW_DELAY_MS);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
