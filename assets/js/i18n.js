(function () {
    'use strict';

    var STORAGE_KEY = 'quindio-language';
    var CALLBACK = 'qtGoogleTranslateInit';
    var CONTAINER_ID = 'qt-translate-container';
    var COMBO_RETRY_MS = 250;
    var COMBO_MAX_TRIES = 60;

    var LANGS = [
        { code: 'es', label: '\u{1F1EA}\u{1F1F8} Espa\u00F1ol', gt: 'es' },
        { code: 'en', label: '\u{1F1FA}\u{1F1F8} English', gt: 'en' },
        { code: 'pt', label: '\u{1F1E7}\u{1F1F7} Portugu\u00EAs', gt: 'pt' },
        { code: 'fr', label: '\u{1F1EB}\u{1F1F7} Fran\u00E7ais', gt: 'fr' },
        { code: 'ru', label: '\u{1F1F7}\u{1F1FA} \u0420\u0443\u0441\u0441\u043A\u0438\u0439', gt: 'ru' },
        { code: 'zh', label: '\u{1F1E8}\u{1F1F3} \u4E2D\u6587', gt: 'zh-CN' }
    ];

    var pendingLang = null;
    var initialized = false;

    function storeGet() {
        try { return localStorage.getItem(STORAGE_KEY); } catch (e) { return null; }
    }

    function storeSet(lang) {
        try { localStorage.setItem(STORAGE_KEY, lang); } catch (e) {}
    }

    function byCode(code) {
        for (var i = 0; i < LANGS.length; i++) {
            if (LANGS[i].code === code) return LANGS[i];
        }
        return null;
    }

    function pageLangGt() {
        var raw = String(document.documentElement.getAttribute('lang') || 'es').toLowerCase();
        if (raw.indexOf('zh') === 0) return 'zh-CN';
        var base = raw.split('-')[0];
        return ['es', 'en', 'pt', 'fr', 'ru'].indexOf(base) !== -1 ? base : 'es';
    }

    function pageLangCode() {
        return pageLangGt() === 'zh-CN' ? 'zh' : pageLangGt();
    }

    function comboTarget(lang) {
        return lang.code === pageLangCode() ? '' : lang.gt;
    }

    function detectLanguage() {
        var stored = byCode(storeGet());
        if (stored) return stored;
        var pageLang = pageLangCode();
        if (pageLang !== 'es') return byCode(pageLang);
        var nav = (navigator.languages && navigator.languages[0]) || navigator.language || 'es';
        var base = String(nav).toLowerCase().split('-')[0];
        var found = byCode(base);
        if (found) return found;
        return byCode('es');
    }

    function injectCss() {
        var css = '' +
            '#' + CONTAINER_ID + ' { position: absolute !important; left: -99999px !important; top: auto !important; }' +
            '.goog-te-banner-frame, .skiptranslate iframe { display: none !important; }' +
            'body { top: 0 !important; }' +
            '#goog-gt-tt, .goog-te-balloon-frame, .goog-text-highlight { display: none !important; box-shadow: none !important; background: none !important; }' +
            '.qt-lang-pill { position: fixed; left: 16px; bottom: 16px; z-index: 6000; }' +
            '.qt-lang-pill select, select#language-selector {' +
            '  padding: 8px 10px; border-radius: 8px; border: 2px solid rgba(46, 90, 54, 0.6);' +
            '  background: #2e5a36; color: #fff; font-size: 14px; font-weight: 600;' +
            '  cursor: pointer; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.25); max-width: 180px;' +
            '  font-family: inherit; appearance: auto;' +
            '}' +
            '.qt-lang-pill select:focus, select#language-selector:focus { outline: 2px solid #74c69d; }';
        var style = document.createElement('style');
        style.textContent = css;
        document.head.appendChild(style);
    }

    function buildOptions(select, lang) {
        select.innerHTML = '';
        for (var i = 0; i < LANGS.length; i++) {
            var opt = document.createElement('option');
            opt.value = LANGS[i].code;
            opt.textContent = LANGS[i].label;
            select.appendChild(opt);
        }
        select.value = lang.code;
        select.setAttribute('aria-label', 'Seleccionar idioma / Select language');
        select.setAttribute('translate', 'no');
    }

    function ensureSelector(lang) {
        var select = document.getElementById('language-selector');

        if (!select) {
            var pill = document.createElement('div');
            pill.className = 'qt-lang-pill skiptranslate';
            pill.setAttribute('translate', 'no');
            select = document.createElement('select');
            select.id = 'language-selector';
            pill.appendChild(select);
            document.body.appendChild(pill);
        }

        buildOptions(select, lang);

        select.addEventListener('change', function () {
            var chosen = byCode(this.value);
            if (!chosen) return;
            storeSet(chosen.code);
            applyLanguage(chosen);
            if (Array.isArray(window.dataLayer)) {
                window.dataLayer.push({ event: 'language_change', language: chosen.code });
            }
        });
    }

    function applyLanguage(lang) {
        pendingLang = lang;
        var combo = document.querySelector('select.goog-te-combo');
        if (combo) {
            combo.value = comboTarget(lang);
            var evt;
            try {
                evt = new Event('change', { bubbles: true });
            } catch (e) {
                evt = document.createEvent('Event');
                evt.initEvent('change', true, true);
            }
            combo.dispatchEvent(evt);
            pendingLang = null;
            return true;
        }
        return false;
    }

    function waitForCombo(tries) {
        if (applyLanguage(pendingLang || detectLanguage())) {
            return;
        }
        if (tries <= 0) {
            if (typeof console !== 'undefined') {
                console.warn('[i18n] Google Translate no respondio; el selector de idioma quedo inactivo.');
            }
            return;
        }
        setTimeout(function () { waitForCombo(tries - 1); }, COMBO_RETRY_MS);
    }

    function loadGoogleWidget() {
        var container = document.getElementById(CONTAINER_ID);
        if (!container) {
            container = document.createElement('div');
            container.id = CONTAINER_ID;
            container.className = 'skiptranslate';
            container.setAttribute('translate', 'no');
            document.body.appendChild(container);
        }

        window[CALLBACK] = function () {
            if (typeof google === 'undefined' || !google.translate) return;
            /* global google */
            new google.translate.TranslateElement({
                pageLanguage: pageLangGt(),
                includedLanguages: 'es,en,pt,fr,ru,zh-CN',
                autoDisplay: false
            }, CONTAINER_ID);

            pendingLang = detectLanguage();
            waitForCombo(COMBO_MAX_TRIES);
        };

        var script = document.createElement('script');
        script.src = 'https://translate.google.com/translate_a/element.js?cb=' + CALLBACK;
        script.async = true;
        script.onerror = function () {
            if (typeof console !== 'undefined') {
                console.warn('[i18n] No se pudo cargar el motor de traduccion.');
            }
        };
        document.body.appendChild(script);
    }

    function init() {
        if (initialized || document.getElementById(CONTAINER_ID)) return;
        initialized = true;
        injectCss();
        var lang = detectLanguage();
        ensureSelector(lang);
        loadGoogleWidget();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
