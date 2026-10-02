(function () {
    'use strict';

    function ensureDataLayer() {
        if (!Array.isArray(window.dataLayer)) {
            window.dataLayer = [];
        }
        return window.dataLayer;
    }

    function cleanText(el) {
        var text = (el.textContent || '').replace(/\s+/g, ' ').trim();
        return text.slice(0, 80);
    }

    function sectionOf(el) {
        var section = el.closest('section');
        if (section && section.id) return section.id;
        if (section && section.className && typeof section.className === 'string') {
            var cls = section.className.trim().split(/\s+/)[0];
            if (cls) return cls;
        }
        var withId = el.closest('[id]');
        if (withId && withId.id) return withId.id;
        var footer = el.closest('footer, .main-footer, .site-footer');
        if (footer) return 'footer';
        return (el.closest('header, nav') ? 'header_nav' : 'other');
    }

    document.addEventListener('click', function (e) {
        var target = e.target;
        if (!target || typeof target.closest !== 'function') return;
        var link = target.closest('a[href*="wa.me"], a[href*="api.whatsapp.com"]');
        if (!link) return;

        ensureDataLayer().push({
            event: 'click_whatsapp',
            page_path: window.location.pathname,
            page_title: document.title,
            cta_text: cleanText(link),
            cta_section: sectionOf(link),
            wa_number: (link.getAttribute('href').match(/(\d{10,15})/) || [])[1] || ''
        });
    }, true);
})();
