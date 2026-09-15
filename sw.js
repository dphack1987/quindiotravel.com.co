/**
 * Quindío Travel Service Worker
 * Estrategia: Cache-First para estáticos, Network-First para HTML
 * v3 — Corregido: eliminado handler fetch duplicado y activate duplicado
 */

const CACHE_VERSION = 'v3';
const STATIC_CACHE = `quindio-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE = `quindio-dynamic-${CACHE_VERSION}`;
const IMAGE_CACHE = `quindio-images-${CACHE_VERSION}`;

const STATIC_URLS = [
  '/',
  '/index.html',
  '/planes.html',
  '/styles.min.css',
  '/assets/css/critical.min.css',
  '/assets/js/planes-data.js',
  '/assets/js/atractivos-data.js',
  '/logo_quindio_travel.png',
  '/favicon.ico',
  '/apple-touch-icon.png',
  '/site.webmanifest'
];

// Instalación: cachear recursos estáticos
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(STATIC_CACHE).then(cache => {
      return cache.addAll(STATIC_URLS).catch(err => {
        console.warn('SW: Error cacheando estáticos:', err);
      });
    })
  );
  self.skipWaiting();
});

// Activación: limpiar caches antiguos
self.addEventListener('activate', (event) => {
  const VALID_CACHES = [STATIC_CACHE, DYNAMIC_CACHE, IMAGE_CACHE];

  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames
          .filter(name => !VALID_CACHES.includes(name))
          .map(name => {
            console.log('SW: Eliminando cache antiguo:', name);
            return caches.delete(name);
          })
      );
    }).then(() => self.clients.claim())
  );
});

// Interceptación de requests — un solo handler
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;

  // No interceptar requests a otros dominios
  if (url.origin !== location.origin) return;

  // HTML: Network-First (siempre contenido fresco para crawlers)
  if (request.headers.get('accept')?.includes('text/html') ||
      url.pathname.endsWith('.html') ||
      url.pathname === '/') {
    event.respondWith(networkFirst(request, DYNAMIC_CACHE));
    return;
  }

  // Imágenes: Cache-First (agresivo)
  if (/\.(jpg|jpeg|png|gif|webp|avif|svg|ico)$/i.test(url.pathname)) {
    event.respondWith(cacheFirst(request, IMAGE_CACHE));
    return;
  }

  // CSS/JS/Fuentes: Stale-While-Revalidate (fresco pero rápido)
  if (/\.(css|js|woff2?|ttf|otf)$/i.test(url.pathname)) {
    event.respondWith(staleWhileRevalidate(request, STATIC_CACHE));
    return;
  }

  // Default: stale-while-revalidate
  event.respondWith(staleWhileRevalidate(request, DYNAMIC_CACHE));
});

// ── Estrategias de caching ──────────────────────────────────────

async function networkFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  try {
    const response = await fetch(request);
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  } catch {
    const cached = await cache.match(request);
    if (cached) return cached;
    return new Response('Offline', { status: 503 });
  }
}

async function cacheFirst(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);
  if (cached) {
    // Actualizar en background sin bloquear
    fetch(request).then(response => {
      if (response.ok) cache.put(request, response);
    }).catch(() => {});
    return cached;
  }
  const response = await fetch(request);
  if (response.ok) {
    cache.put(request, response.clone());
  }
  return response;
}

async function staleWhileRevalidate(request, cacheName) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(request);

  const fetchPromise = fetch(request).then(response => {
    if (response.ok) cache.put(request, response.clone());
    return response;
  }).catch(() => cached);

  return cached || fetchPromise;
}

// Push Notifications
self.addEventListener('push', (event) => {
  const options = {
    body: event.data ? event.data.text() : 'Nueva promoción disponible en Quindío Travel',
    icon: '/logo_quindio_travel.png',
    badge: '/favicon.ico',
    vibrate: [200, 100, 200],
    data: { url: '/' }
  };
  event.waitUntil(
    self.registration.showNotification('Quindío Travel', options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  event.waitUntil(clients.openWindow(event.notification.data?.url || '/'));
});

// Precache bajo demanda
self.addEventListener('message', (event) => {
  if (event.data?.type === 'CACHE_URLS') {
    event.waitUntil(
      caches.open(DYNAMIC_CACHE).then(cache => cache.addAll(event.data.urls))
    );
  }
});
