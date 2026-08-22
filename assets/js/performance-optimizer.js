/**
 * Quindío Travel Performance Optimizer
 * Optimización de Core Web Vitals y Edge Computing
 * Objetivo: >95 en Lighthouse y perfect score en CWV
 */

class PerformanceOptimizer {
  constructor() {
    this.initTime = performance.now();
    this.metrics = {};
    this.lazyLoadObserver = null;
    this.intersectionObserver = null;
  }

  init() {
    this.setupPreloading();
    this.setupLazyLoading();
    this.setupResourceHints();
    this.setupFontOptimization();
    this.setupScriptDeferral();
    this.setupImageOptimization();
    this.setupCLSPrevention();
    this.trackCoreWebVitals();
    this.optimizeAnimations();
    this.setupServiceWorker();
  }

  // Preconexiones críticas para edge computing
  setupPreloading() {
    // Preconectar a dominios externos críticos
    const criticalDomains = [
      'https://www.googletagmanager.com',
      'https://www.google-analytics.com',
      'https://fonts.googleapis.com',
      'https://fonts.gstatic.com',
      'https://wa.me'
    ];

    criticalDomains.forEach(domain => {
      const link = document.createElement('link');
      link.rel = 'preconnect';
      link.href = domain;
      document.head.appendChild(link);
    });

    // Precargar recursos críticos
    this.preloadCriticalResources();
  }

  preloadCriticalResources() {
    const criticalResources = [
      { href: '/assets/css/critical.css', as: 'style' },
      { href: '/assets/js/whatsapp-payload-builder.js', as: 'script' },
      { href: '/assets/images/logo.png', as: 'image' }
    ];

    criticalResources.forEach(resource => {
      // Validar que el recurso existe antes de intentar preload
      fetch(resource.href, { method: 'HEAD' })
        .then(response => {
          if (response.ok) {
            const link = document.createElement('link');
            link.rel = 'preload';
            link.href = resource.href;
            link.as = resource.as;
            
            if (resource.as === 'style') {
              link.onload = () => link.rel = 'stylesheet';
            }
            
            document.head.appendChild(link);
          } else {
            console.warn(`Recurso no encontrado para preload: ${resource.href}`);
          }
        })
        .catch(error => {
          console.warn(`Error validando recurso ${resource.href}:`, error);
        });
    });
  }

  // Lazy loading avanzado con Intersection Observer
  setupLazyLoading() {
    // Lazy loading para imágenes
    if ('IntersectionObserver' in window) {
      this.lazyLoadObserver = new IntersectionObserver(
        this.lazyLoadCallback.bind(this),
        {
          rootMargin: '50px 0px',
          threshold: 0.01
        }
      );

      // Observar todas las imágenes con data-src
      document.querySelectorAll('img[data-src]').forEach(img => {
        this.lazyLoadObserver.observe(img);
      });

      // Lazy loading para iframes (videos, mapas)
      document.querySelectorAll('iframe[data-src]').forEach(iframe => {
        this.lazyLoadObserver.observe(iframe);
      });
    } else {
      // Fallback para navegadores antiguos
      this.fallbackLazyLoading();
    }
  }

  lazyLoadCallback(entries, observer) {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const element = entry.target;
        
        if (element.tagName === 'IMG') {
          this.loadImage(element);
        } else if (element.tagName === 'IFRAME') {
          this.loadIframe(element);
        }
        
        observer.unobserve(element);
      }
    });
  }

  loadImage(img) {
    const src = img.getAttribute('data-src');
    const srcset = img.getAttribute('data-srcset');
    
    if (src) {
      img.src = src;
      img.onload = () => img.classList.add('loaded');
    }
    
    if (srcset) {
      img.srcset = srcset;
    }
    
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
    // Lazy loading simple para navegadores sin Intersection Observer
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    const lazyLoad = () => {
      const lazyImageObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            this.loadImage(entry.target);
            lazyImageObserver.unobserve(entry.target);
          }
        });
      });

      lazyImages.forEach(img => lazyImageObserver.observe(img));
    };

    if (document.readyState === 'complete') {
      lazyLoad();
    } else {
      window.addEventListener('load', lazyLoad);
    }
  }

  // Resource hints para mejor rendimiento
  setupResourceHints() {
    // DNS prefetch para dominios no críticos
    const secondaryDomains = [
      'https://facebook.com',
      'https://instagram.com',
      'https://twitter.com'
    ];

    secondaryDomains.forEach(domain => {
      const link = document.createElement('link');
      link.rel = 'dns-prefetch';
      link.href = domain;
      document.head.appendChild(link);
    });
  }

  // Optimización de fuentes
  setupFontOptimization() {
    // Usar font-display: swap para fuentes
    const fontLinks = document.querySelectorAll('link[href*="fonts.googleapis.com"]');
    fontLinks.forEach(link => {
      link.rel = 'preload';
      link.as = 'style';
      link.onload = () => {
        link.rel = 'stylesheet';
        document.body.classList.add('fonts-loaded');
      };
    });

    // Fallback para fuentes del sistema si tardan
    setTimeout(() => {
      document.body.classList.add('fonts-fallback');
    }, 3000);
  }

  // Diferir scripts no críticos
  setupScriptDeferral() {
    const nonCriticalScripts = [
      '/assets/js/cotizador.js'
    ];

    nonCriticalScripts.forEach(src => {
      const script = document.createElement('script');
      script.src = src;
      script.defer = true;
      script.async = true;
      document.body.appendChild(script);
    });
  }

  // Optimización de imágenes modernas
  setupImageOptimization() {
    // Agregar atributos loading="lazy" a imágenes below-the-fold
    const images = document.querySelectorAll('img');
    images.forEach((img, index) => {
      if (index > 3) { // Las primeras 3 imágenes son above-the-fold
        img.setAttribute('loading', 'lazy');
        img.setAttribute('decoding', 'async');
      }
    });

    // Usar WebP si es compatible
    this.setupWebPImages();
  }

  setupWebPImages() {
    if (this.supportsWebP()) {
      const images = document.querySelectorAll('img[data-webp]');
      images.forEach(img => {
        const webpSrc = img.getAttribute('data-webp');
        if (webpSrc) {
          img.src = webpSrc;
        }
      });
    }
  }

  supportsWebP() {
    return document.createElement('canvas').toDataURL('image/webp').indexOf('data:image/webp') === 0;
  }

  // Prevención de CLS (Cumulative Layout Shift)
  setupCLSPrevention() {
    // Reservar espacio para imágenes y videos
    const mediaElements = document.querySelectorAll('img, iframe, video');
    mediaElements.forEach(element => {
      if (!element.hasAttribute('width') || !element.hasAttribute('height')) {
        // Establecer dimensiones por defecto si no están especificadas
        element.style.aspectRatio = '16/9';
        element.style.width = '100%';
        element.style.height = 'auto';
      }
    });

    // Reservar espacio para fuentes
    document.body.style.fontDisplay = 'swap';
  }

  // Track Core Web Vitals
  trackCoreWebVitals() {
    // LCP (Largest Contentful Paint)
    this.trackLCP();
    
    // FID (First Input Delay)
    this.trackFID();
    
    // CLS (Cumulative Layout Shift)
    this.trackCLS();
    
    // FCP (First Contentful Paint)
    this.trackFCP();
    
    // TTFB (Time to First Byte)
    this.trackTTFB();
  }

  trackLCP() {
    if ('PerformanceObserver' in window) {
      const lcpObserver = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        this.metrics.lcp = lastEntry.renderTime || lastEntry.loadTime;
        
        console.log('LCP:', this.metrics.lcp);
        
        // Enviar a analytics si está disponible
        if (typeof gtag !== 'undefined') {
          gtag('event', 'LCP', {
            'event_category': 'Web Vitals',
            'value': this.metrics.lcp,
            'non_interaction': true
          });
        }
      });
      
      lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });
    }
  }

  trackFID() {
    if ('PerformanceObserver' in window) {
      const fidObserver = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const fid = entries[0].processingStart - entries[0].startTime;
        this.metrics.fid = fid;
        
        console.log('FID:', fid);
        
        if (typeof gtag !== 'undefined') {
          gtag('event', 'FID', {
            'event_category': 'Web Vitals',
            'value': fid,
            'non_interaction': true
          });
        }
      });
      
      fidObserver.observe({ entryTypes: ['first-input'] });
    }
  }

  trackCLS() {
    let clsValue = 0;
    let clsEntries = [];
    
    if ('PerformanceObserver' in window) {
      const clsObserver = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (!entry.hadRecentInput) {
            clsValue += entry.value;
            clsEntries.push(entry);
          }
        }
        
        this.metrics.cls = clsValue;
        
        console.log('CLS:', clsValue);
        
        if (typeof gtag !== 'undefined') {
          gtag('event', 'CLS', {
            'event_category': 'Web Vitals',
            'value': clsValue,
            'non_interaction': true
          });
        }
      });
      
      clsObserver.observe({ entryTypes: ['layout-shift'] });
    }
  }

  trackFCP() {
    if ('PerformanceObserver' in window) {
      const fcpObserver = new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const fcp = entries[0].startTime;
        this.metrics.fcp = fcp;
        
        console.log('FCP:', fcp);
        
        if (typeof gtag !== 'undefined') {
          gtag('event', 'FCP', {
            'event_category': 'Web Vitals',
            'value': fcp,
            'non_interaction': true
          });
        }
      });
      
      fcpObserver.observe({ entryTypes: ['paint'] });
    }
  }

  trackTTFB() {
    const navigation = performance.getEntriesByType('navigation')[0];
    if (navigation) {
      const ttfb = navigation.responseStart - navigation.requestStart;
      this.metrics.ttfb = ttfb;
      
      console.log('TTFB:', ttfb);
      
      if (typeof gtag !== 'undefined') {
        gtag('event', 'TTFB', {
          'event_category': 'Web Vitals',
          'value': ttfb,
          'non_interaction': true
        });
      }
    }
  }

  // Optimización de animaciones
  optimizeAnimations() {
    // Reducir animaciones en dispositivos con preferencia de reducción de movimiento
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
    
    if (prefersReducedMotion.matches) {
      document.body.classList.add('reduced-motion');
    }
    
    // Usar transform y opacity en lugar de propiedades que causan reflow
    const animatedElements = document.querySelectorAll('[data-animate]');
    animatedElements.forEach(element => {
      element.style.willChange = 'transform, opacity';
    });
  }

  // Service Worker para edge computing
  setupServiceWorker() {
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
          .then(registration => {
            console.log('Service Worker registrado:', registration.scope);
          })
          .catch(error => {
            console.log('Service Worker error:', error);
          });
      });
    }
  }

  // Métricas de rendimiento personalizadas
  getPerformanceMetrics() {
    const navigation = performance.getEntriesByType('navigation')[0];
    
    return {
      // Core Web Vitals
      lcp: this.metrics.lcp,
      fid: this.metrics.fid,
      cls: this.metrics.cls,
      
      // Timing metrics
      domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart,
      loadComplete: navigation.loadEventEnd - navigation.loadEventStart,
      totalLoadTime: navigation.loadEventEnd - navigation.fetchStart,
      
      // Resource metrics
      resourceCount: performance.getEntriesByType('resource').length,
      
      // Memory (si está disponible)
      memory: performance.memory ? {
        usedJSHeapSize: performance.memory.usedJSHeapSize,
        totalJSHeapSize: performance.memory.totalJSHeapSize,
        jsHeapSizeLimit: performance.memory.jsHeapSizeLimit
      } : null
    };
  }

  // Optimización de scroll
  setupScrollOptimization() {
    let ticking = false;
    
    window.addEventListener('scroll', () => {
      if (!ticking) {
        window.requestAnimationFrame(() => {
          this.handleScroll();
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
  }

  handleScroll() {
    // Lógica de scroll optimizada
    const scrollY = window.scrollY;
    
    // Cargar recursos cuando el usuario hace scroll
    if (scrollY > 500) {
      this.loadSecondaryResources();
    }
  }

  loadSecondaryResources() {
    // Cargar recursos secundarios después del scroll inicial
    const secondaryResources = document.querySelectorAll('[data-load-on-scroll]');
    secondaryResources.forEach(resource => {
      if (resource.tagName === 'SCRIPT') {
        resource.src = resource.getAttribute('data-src');
      } else if (resource.tagName === 'LINK') {
        resource.href = resource.getAttribute('data-href');
      }
      resource.removeAttribute('data-load-on-scroll');
    });
  }

  // Optimización de memoria
  optimizeMemory() {
    // Limpiar event listeners no usados
    // Implementar debouncing/throttling
    // Usar object pooling para elementos frecuentes
  }

  // Reporte de rendimiento
  generatePerformanceReport() {
    const metrics = this.getPerformanceMetrics();
    const report = {
      timestamp: new Date().toISOString(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      metrics: metrics,
      score: this.calculatePerformanceScore(metrics)
    };
    
    console.log('Performance Report:', report);
    return report;
  }

  calculatePerformanceScore(metrics) {
    let score = 100;
    
    // Penalizar según métricas
    if (metrics.lcp > 2500) score -= 10;
    if (metrics.fid > 100) score -= 10;
    if (metrics.cls > 0.1) score -= 10;
    if (metrics.totalLoadTime > 3000) score -= 15;
    
    return Math.max(0, score);
  }
}

// Inicializar optimizador de rendimiento
const performanceOptimizer = new PerformanceOptimizer();

// Iniciar cuando el DOM esté listo
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    performanceOptimizer.init();
  });
} else {
  performanceOptimizer.init();
}

// Exponer para debugging
window.performanceOptimizer = performanceOptimizer;

// Generar reporte de rendimiento después de 5 segundos
setTimeout(() => {
  const report = performanceOptimizer.generatePerformanceReport();
  
  // Enviar reporte a analytics si está disponible
  if (typeof gtag !== 'undefined') {
    gtag('event', 'performance_report', {
      'event_category': 'Performance',
      'value': report.score,
      'custom_map': {
        'metric_lcp': report.metrics.lcp,
        'metric_fid': report.metrics.fid,
        'metric_cls': report.metrics.cls
      }
    });
  }
}, 5000);