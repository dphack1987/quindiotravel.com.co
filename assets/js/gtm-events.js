(function () {
    'use strict';

    function ensureDataLayer() {
        if (!Array.isArray(window.dataLayer)) {
            window.dataLayer = [];
        }
        return window.dataLayer;
    }

    // Extraer el nombre del plan de la URL o título
    function getPlanName() {
        const path = window.location.pathname;
        if (path.includes('plan-1')) return 'Escapada Cafetera (2D/1N)';
        if (path.includes('plan-2')) return 'Aventura Natural (3D/2N)';
        if (path.includes('plan-3')) return 'Experiencia Completa (4D/3N)';
        if (path.includes('plan-4')) return 'Termales Santa Rosa (4D/3N)';
        if (path.includes('plan-5')) return 'Tradición y Raíces (4D/3N)';
        if (path.includes('plan-6')) return 'Experiencia Premium (5D/4N)';
        return null;
    }

    // Track vista de página de plan
    function trackPlanView() {
        const planName = getPlanName();
        if (planName) {
            ensureDataLayer().push({
                event: 'view_plan',
                plan_name: planName,
                page_path: window.location.pathname,
                page_title: document.title
            });
        }
    }

    // Track clic en card de plan
    function trackPlanCardClick(e) {
        const card = e.target.closest('.qt-plan-card, .plan-card, [data-plan-id]');
        if (card) {
            const planId = card.getAttribute('data-plan-id') || card.querySelector('.plan-title')?.textContent || '';
            ensureDataLayer().push({
                event: 'click_plan_card',
                plan_id: planId,
                plan_name: planId,
                page_path: window.location.pathname
            });
        }
    }

    // Track uso de filtros
    function trackFilterUse(e) {
        const filter = e.target.closest('.filter-select, .filter-checkbox, [data-filter]');
        if (filter) {
            const filterType = filter.getAttribute('data-filter-type') || filter.getAttribute('name') || 'unknown';
            const filterValue = filter.value || filter.textContent || '';
            ensureDataLayer().push({
                event: 'use_filter',
                filter_type: filterType,
                filter_value: filterValue,
                page_path: window.location.pathname
            });
        }
    }

    // Track toggle de desglose de precios
    function trackPriceToggle(e) {
        const toggle = e.target.closest('[id*="toggle-precios"], [id*="price-toggle"], .price-toggle-btn');
        if (toggle) {
            const isOpen = toggle.getAttribute('aria-expanded') === 'true';
            ensureDataLayer().push({
                event: 'toggle_price_details',
                action: isOpen ? 'open' : 'close',
                page_path: window.location.pathname,
                plan_name: getPlanName()
            });
        }
    }

    // Track scroll depth
    function trackScrollDepth() {
        const thresholds = [25, 50, 75, 100];
        const trackedDepths = new Set();

        window.addEventListener('scroll', function () {
            const scrollTop = window.scrollY || document.documentElement.scrollTop;
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercent = Math.round((scrollTop / docHeight) * 100);

            thresholds.forEach(threshold => {
                if (scrollPercent >= threshold && !trackedDepths.has(threshold)) {
                    trackedDepths.add(threshold);
                    ensureDataLayer().push({
                        event: 'scroll_depth',
                        scroll_percent: threshold,
                        page_path: window.location.pathname,
                        page_title: document.title,
                        plan_name: getPlanName()
                    });
                }
            });
        });
    }

    // Track time on page (30s, 60s, 120s)
    function trackTimeOnPage() {
        const intervals = [30, 60, 120];
        intervals.forEach(seconds => {
            setTimeout(() => {
                ensureDataLayer().push({
                    event: 'time_on_page',
                    time_seconds: seconds,
                    page_path: window.location.pathname,
                    page_title: document.title,
                    plan_name: getPlanName()
                });
            }, seconds * 1000);
        });
    }

    // Track clic en enlace de comparación
    function trackComparisonClick(e) {
        const link = e.target.closest('a[href*="comparar-planes"], .compare-btn');
        if (link) {
            ensureDataLayer().push({
                event: 'click_comparison',
                page_path: window.location.pathname,
                page_title: document.title
            });
        }
    }

    // Inicializar tracking
    document.addEventListener('DOMContentLoaded', function () {
        // Track vista de plan al cargar
        trackPlanView();

        // Track scroll depth
        trackScrollDepth();

        // Track time on page
        trackTimeOnPage();

        // Event listeners
        document.addEventListener('click', function (e) {
            trackPlanCardClick(e);
            trackFilterUse(e);
            trackPriceToggle(e);
            trackComparisonClick(e);
        }, true);
    });

})();
