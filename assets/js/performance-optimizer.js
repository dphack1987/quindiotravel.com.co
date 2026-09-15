/**
 * Quindío Travel Performance Optimizer v2
 * Core Web Vitals: LCP <1.5s, INP <100ms, CLS <0.05
 * v2 — Corregido: CLS, preloading, async/defer, font optimization
 */

class PerformanceOptimizer {
  constructor() {
    this.metrics = {};
    this.lazyLoadObserver = null;
  }

  init() {
    this.setupPreloading();
    this.setupLazyLoading();
    this.setupResourceHints();
    this.setupImageOptimization();
    this.setupCLSPrevention();
    this.trackCoreWebVitals();
    this.optimizeAnimations();
    this.setupServiceWorker();
  }

  // ── Preconexiones críticas (solo DOM, sin fetch HEAD) ─────────
  setupPreloading() {
    const criticalDomains = [
      'https://www.googletagmanager.com',
      'https://www.google-analytics.com',
      'https://fonts.googleapis.com',
      'https://fonts.gstatic.com'
    ];

    criticalDomains.forEach(domain => {
      const link = document.createElement('link');
      link.rel = 'preconnect';
      link.href = domain;
      link.crossOrigin = 'anonymous';
      document.head.appendChild(link);
    });

    // Preload critical CSS (sin fetch HEAD — directo)
    const preloadCSS = document.createElement('link');
    preloadCSS.rel = 'preload';
    preloadCSS.href = '/assets/css/critical.min.css';
    preloadCSS.as = 'style';
    preloadCSS.onload = () => { preloadCSS.rel = 'stylesheet'; };
    document.head.appendChild(preloadCSS);
  }

  // ── Lazy loading con Intersection Observer ────────────────────
  setupLazyLoading() {
    if (!('IntersectionObserver' in window)) {
      this.fallbackLazyLoading();
      return;
    }

    this.lazyLoadObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            if (el.tagName === 'IMG') this.loadImage(el);
            else if (el.tagName === 'IFRAME') this.loadIframe(el);
            this.lazyLoadObserver.unobserve(el);
          }
        });
      },
      { rootMargin: '200px 0px', threshold: 0.01 }
    );

    document.querySelectorAll('img[data-src], iframe[data-src]').forEach(el => {
      this.lazyLoadObserver.observe(el);
    });
  }

  loadImage(img) {
    const src = img.getAttribute('data-src');
    const srcset = img.getAttribute('data-srcset');
    if (src) {
      img.src = src;
      img.onload = () => img.classList.add('loaded');
    }
    if (srcset) img.srcset = srcset;
    img.removeAttribute('data-src');
    img.removeAttribute('data-srcset');
  }

  loadIframe(iframe) {
    const src = iframe.getAttribute('data-src');
    if (src) {
      iframe.src = src;
      iframe.removeAttribute('data-src');
    }
  }

  fallbackLazyLoading() {
    const lazyImages = document.querySelectorAll('img[data-src]');
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          this.loadImage(entry.target);
          observer.unobserve(entry.target);
        }
      });
    });
    lazyImages.forEach(img => observer.observe(img));
  }

  // ── Resource hints (DNS prefetch) ────────────────────────────
  setupResourceHints() {
    const secondaryDomains = [
      'https://facebook.com',
      'https://instagram.com',
      'https://wa.me'
    ];

    secondaryDomains.forEach(domain => {
      const link = document.createElement('link');
      link.rel = 'dns-prefetch';
      link.href = domain;
      document.head.appendChild(link);
    });
  }

  // ── Lazy loading de imágenes ─────────────────────────────────
  setupImageOptimization() {
    const images = document.querySelectorAll('img');
    images.forEach((img, index) => {
      // Solo las primeras 2 imágenes son above-the-fold
      if (index >= 2) {
        if (!img.hasAttribute('loading')) {
          img.setAttribute('loading', 'lazy');
        }
        img.setAttribute('decoding', 'async');
      }
    });
  }

  // ── Prevención de CLS (versión corregida) ────────────────────
  setupCLSPrevention() {
    // NO forzar aspect-ratio 16/9 en todo — eso causa shifts
    // Solo marcar imágenes sin dimensiones con un ratio razonable
    const images = document.querySelectorAll('img:not([width]):not([height])');
    images.forEach(img => {
      // Usar object-fit para preservar relación de aspecto sin forzar 16/9
      img.style.width = '100%';
      img.style.height = 'auto';
      img.style.objectFit = 'cover';
    });

    // Reservar espacio para iframes (videos, mapas)
    const iframes = document.querySelectorAll('iframe:not([width]):not([height])');
    iframes.forEach(iframe => {
      iframe.style.aspectRatio = '16/9';
      iframe.style.width = '100%';
      iframe.style.height = 'auto';
    });
  }

  // ── Track Core Web Vitals ────────────────────────────────────
  trackCoreWebVitals() {
    this.trackLCP();
    this.trackINP();
    this.trackCLS();
    this.trackFCP();
    this.trackTTFB();
  }

  trackLCP() {
    if (!('PerformanceObserver' in window)) return;
    try {
      const observer = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
      });
      observer.observe({ entryTypes: ['largest-contentful-paint'] });
    } catch {}
  }

  trackINP() {
    if (!('PerformanceObserver' in window)) return;
    try {
      const observer = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const longest = entries.reduce((max, entry) => {
          const duration = entry.duration;
          return duration > max.duration ? entry : max;
        }, entries[0]);
        if (longest) {
          this.metrics.inp = longest.duration;
        }
      });
      observer.observe({ entryTypes: ['event'] });
    } catch {}
  }

  trackCLS() {
    if (!('PerformanceObserver' in window)) return;
    try {
      let clsValue = 0;
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) {
            clsValue += entry.value;
          }
        }
        this.metrics.cls = clsValue;
      });
      observer.observe({ entryTypes: ['layout-shift'] });
    } catch {}
  }

  trackFCP() {
    if (!('PerformanceObserver' in window)) return;
    try {
      const observer = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        this.metrics.fcp = entries[0].startTime;
      });
      observer.observe({ entryTypes: ['paint'] });
    } catch {}
  }

  trackTTFB() {
    const navigation = performance.getEntriesByType('navigation')[0];
    if (navigation) {
      this.metrics.ttfb = navigation.responseStart - navigation.requestStart;
    }
  }

  // ── Animaciones optimizadas ──────────────────────────────────
  optimizeAnimations() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      document.body.classList.add('reduced-motion');
    }

    document.querySelectorAll('[data-animate]').forEach(el => {
      el.style.willChange = 'transform, opacity';
    });
  }

  // ── Service Worker ───────────────────────────────────────────
  setupServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').catch(() => {});
      });
    }
  }

  // ── Métricas para debugging ──────────────────────────────────
  getPerformanceMetrics() {
    const navigation = performance.getEntriesByType('navigation')[0];
    return {
      lcp: this.metrics.lcp,
      inp: this.metrics.inp,
      cls: this.metrics.cls,
      fcp: this.metrics.fcp,
      ttfb: this.metrics.ttfb,
      totalLoadTime: navigation ? navigation.loadEventEnd - navigation.fetchStart : null
    };
  }
}

// Inicializar
const performanceOptimizer = new PerformanceOptimizer();

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => performanceOptimizer.init());
} else {
  performanceOptimizer.init();
}

window.performanceOptimizer = performanceOptimizer;
