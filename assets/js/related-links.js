/* ============================================
   QUINDÍO TRAVEL — Enlaces internos contextuales
   Inyecta "Te puede interesar" según mapa de
   clusters generado por seo-engine/build_link_map.py
   ============================================ */
(function () {
    'use strict';

    var MAP_URL = (function () {
        // Ruta absoluta: el mapa vive en la raíz del sitio
        return '/assets/data/related-links-map.json';
    })();

    function currentKey() {
        var p = decodeURIComponent(window.location.pathname || '');
        p = p.replace(/^\/+/, '');
        if (p === '') return 'index.html';
        if (p.endsWith('/')) return p + 'index.html';
        return p;
    }

    function ensureStyles() {
        if (document.getElementById('qt-related-links-css')) return;
        var s = document.createElement('style');
        s.id = 'qt-related-links-css';
        s.textContent =
            '.qt-related{max-width:1100px;margin:44px auto;padding:0 16px;box-sizing:border-box;}' +
            '.qt-related__box{background:#fff;border:1px solid #e2e8f0;border-radius:16px;box-shadow:0 8px 24px rgba(0,0,0,.06);padding:26px 28px;}' +
            '.qt-related__title{font-family:"Fraunces",Georgia,serif;color:#2E5A36;font-size:1.25rem;margin:0 0 6px;}' +
            '.qt-related__sub{color:#5b6b63;font-size:.9rem;margin:0 0 16px;}' +
            '.qt-related__list{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px;}' +
            '.qt-related__list a{display:flex;align-items:center;gap:10px;padding:12px 14px;border:1px solid #e4ebe6;border-radius:12px;text-decoration:none;color:#2C3E35;font-weight:600;font-size:.92rem;transition:border-color .2s,box-shadow .2s,transform .2s;background:#fbfdfc;}' +
            '.qt-related__list a:hover,.qt-related__list a:focus-visible{border-color:#2E5A36;box-shadow:0 4px 14px rgba(46,90,54,.15);transform:translateY(-1px);color:#2E5A36;outline:none;}' +
            '.qt-related__list a::before{content:"→";color:#E67300;font-weight:800;flex-shrink:0;}' +
            '@media(max-width:600px){.qt-related__box{padding:20px 16px;}.qt-related__list{grid-template-columns:1fr;}}';
        document.head.appendChild(s);
    }

    function fallbackLinks(map, key) {
        // Garantizar mínimo 3 enlaces útiles si el mapa trae pocos
        var seen = {};
        (map[key] || []).forEach(function (l) { seen[l[0]] = true; });
        var extra = ['planes.html', 'cotizador-simplificado.html', 'blog.html'];
        var out = (map[key] || []).slice();
        extra.forEach(function (e) {
            if (out.length < 4 && map[e] && !seen[e]) {
                out.push([e, e === 'planes.html' ? 'Ver todos los planes'
                    : e === 'cotizador-simplificado.html' ? 'Cotizar por WhatsApp'
                    : 'Guías y consejos de viaje']);
            }
        });
        return out.slice(0, 6);
    }

    function inject(links) {
        if (!links.length) return;
        // No duplicar si la plantilla ya trae sección de relacionados
        if (document.querySelector('.qt-related, .related-links, .related-posts, .articulos-relacionados')) return;
        ensureStyles();

        var nav = document.createElement('nav');
        nav.className = 'qt-related';
        nav.setAttribute('aria-label', 'Páginas relacionadas');

        var box = document.createElement('div');
        box.className = 'qt-related__box';
        box.innerHTML =
            '<h2 class="qt-related__title">Te puede interesar</h2>' +
            '<p class="qt-related__sub">Sigue explorando el Eje Cafetero con nuestras guías y planes.</p>';

        var ul = document.createElement('ul');
        ul.className = 'qt-related__list';
        links.forEach(function (l) {
            var li = document.createElement('li');
            var a = document.createElement('a');
            a.href = '/' + l[0];
            a.textContent = l[1] || l[0];
            li.appendChild(a);
            ul.appendChild(li);
        });
        box.appendChild(ul);
        nav.appendChild(box);

        // Insertar antes del footer si existe; si no, antes de </main>; si no, al final
        var footer = document.querySelector('footer, .main-footer-section, #contacto');
        var main = document.querySelector('main, #main-content');
        if (footer && footer.parentNode) {
            footer.parentNode.insertBefore(nav, footer);
        } else if (main && main.parentNode) {
            main.parentNode.insertBefore(nav, main.nextSibling);
        } else {
            document.body.appendChild(nav);
        }
    }

    fetch(MAP_URL)
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (map) {
            if (!map) return;
            var key = currentKey();
            if (!map[key]) return;
            inject(fallbackLinks(map, key));
        })
        .catch(function () { /* sin red / file:// : no hacer nada */ });
})();
