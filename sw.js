/**
 * Quindío Travel Service Worker
 * Edge Computing y Caching Inteligente
 * Estrategia: Cache-First para estáticos, Network-First para dinámicos
 */

const CACHE_NAME = 'quindio-travel-v3';
const STATIC_CACHE = 'quindio-static-v3';
const DYNAMIC_CACHE = 'quindio-dynamic-v3';
const IMAGE_CACHE = 'quindio-images-v3';

// URLs que deben cachearse estáticamente
const STATIC_URLS = [
  '/',
  '/index.html',
  '/planes.html',
  '/styles.css',
  '/assets/css/critical.css',
  '/assets/js/planes-data.js',
  '/assets/js/atractivos-data.js',
  '/assets/js/whatsapp-payload-builder.js',
  '/assets/js/performance-optimizer.js',
  '/logo_quindio_travel.webp',
  '/favicon.ico',
  '/apple-touch-icon.webp',
  '/site.webmanifest'
];

// Estrategias de caching
const CACHE_STRATEGIES = {
  // Cache-First: Ideal para assets estáticos
  cacheFirst: async (request, cacheName) => {
    const cache = await caches.open(cacheName);
    const cached = await cache.match(request);
    
    if (cached) {
      // Actualizar cache en background
      fetch(request).then(response => {
        if (response.ok) {
          cache.put(request, response.clone());
        }
      });
      return cached;
    }
    
    const response = await fetch(request);
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  },

  // Network-First: Ideal para contenido dinámico
  networkFirst: async (request, cacheName) => {
    const cache = await caches.open(cacheName);
    
    try {
      const response = await fetch(request);
      if (response.ok) {
        cache.put(request, response.clone());
      }
      return response;
    } catch (error) {
      const cached = await cache.match(request);
      if (cached) {
        return cached;
      }
      throw error;
    }
  },

  // Stale-While-Revalidate: Balance entre velocidad y frescura
  staleWhileRevalidate: async (request, cacheName) => {
    const cache = await caches.open(cacheName);
    const cached = await cache.match(request);
    
    const fetchPromise = fetch(request).then(response => {
      if (response.ok) {
        cache.put(request, response.clone());
      }
      return response;
    });
    
    return cached || fetchPromise;
  },

  // Network-Only: Para contenido que nunca debe cachearse
  networkOnly: async (request) => {
    return fetch(request);
  }
};

// Instalación del Service Worker
self.addEventListener('install', (event) => {
  console.log('Service Worker: Instalando...');
  
  event.waitUntil(
    Promise.all([
      // Cachear recursos estáticos
      caches.open(STATIC_CACHE).then(cache => {
        console.log('Service Worker: Cacheando recursos estáticos');
        return cache.addAll(STATIC_URLS);
      }),
      // Cachear imágenes principales
      caches.open(IMAGE_CACHE).then(cache => {
        return cache.addAll([
          '/assets/images/paisajes/valle-cocora-hero-banner.webp',
          '/assets/images/paisajes/eje-cafetero-aerial-view.webp'
        ]);
      })
    ])
  );
  
  // Forzar activación inmediata
  self.skipWaiting();
});

// Activación del Service Worker
self.addEventListener('activate', (event) => {
  console.log('Service Worker: Activando...');
  
  event.waitUntil(
    Promise.all([
      // Limpiar caches antiguos
      caches.keys().then(cacheNames => {
        return Promise.all(
          cacheNames.map(cacheName => {
            if (cacheName !== CACHE_NAME && 
                cacheName !== STATIC_CACHE && 
                cacheName !== DYNAMIC_CACHE && 
                cacheName !== IMAGE_CACHE) {
              console.log('Service Worker: Eliminando cache antiguo:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      }),
      // Reclamar clientes inmediatamente
      self.clients.claim()
    ])
  );
});

// Interceptación de requests
self.addEventListener('fetch', (event) => {
  const request = event.request;
  const url = new URL(request.url);
  
  // Ignorar requests que no son GET
  if (request.method !== 'GET') {
    return;
  }
  
  // Ignorar requests a otros dominios (excepto CDN y APIs permitidas)
  if (url.origin !== location.origin && 
      !url.hostname.includes('googletagmanager.com') &&
      !url.hostname.includes('google-analytics.com') &&
      !url.hostname.includes('fonts.googleapis.com') &&
      !url.hostname.includes('fonts.gstatic.com')) {
    return;
  }
  
  // Estrategia según el tipo de recurso
  let strategy;
  
  // CSS y JS estáticos
  if (request.url.match(/\.(css|js)$/)) {
    strategy = CACHE_STRATEGIES.staleWhileRevalidate(request, STATIC_CACHE);
  }
  // Imágenes
  else if (request.url.match(/\.(jpg|jpeg|png|gif|webp|svg)$/)) {
    strategy = CACHE_STRATEGIES.cacheFirst(request, IMAGE_CACHE);
  }
  // HTML
  else if (request.url.match(/\.html$/)) {
    strategy = CACHE_STRATEGIES.networkFirst(request, DYNAMIC_CACHE);
  }
  // Fuentes
  else if (request.url.match(/\.(woff|woff2|ttf|otf)$/)) {
    strategy = CACHE_STRATEGIES.cacheFirst(request, STATIC_CACHE);
  }
  // Páginas principales
  else if (url.pathname === '/' || url.pathname === '/index.html') {
    strategy = CACHE_STRATEGIES.networkFirst(request, DYNAMIC_CACHE);
  }
  // APIs y contenido dinámico
  else if (request.url.includes('/api/') || request.url.includes('/data/')) {
    strategy = CACHE_STRATEGIES.networkFirst(request, DYNAMIC_CACHE);
  }
  // Default: Stale-While-Revalidate
  else {
    strategy = CACHE_STRATEGIES.staleWhileRevalidate(request, DYNAMIC_CACHE);
  }
  
  event.respondWith(strategy);
});

// Background Sync reservado para flujos propios del dominio.
// Se desactiva la sincronización a WhatsApp porque `wa.me` no expone
// un endpoint POST compatible con Background Sync del navegador.
self.addEventListener('sync', (event) => {
  console.log('Service Worker: Background Sync ignorado:', event.tag);
});

// Push Notifications
self.addEventListener('push', (event) => {
  console.log('Service Worker: Push recibido');
  
  const options = {
    body: event.data ? event.data.text() : 'Nueva promoción disponible en Quindío Travel',
    icon: '/logo_quindio_travel.webp',
    badge: '/favicon.ico',
    vibrate: [200, 100, 200],
    data: {
      url: '/'
    },
    actions: [
      {
        action: 'explore',
        title: 'Ver Promoción',
        icon: '/logo_quindio_travel.webp'
      },
      {
        action: 'close',
        title: 'Cerrar',
        icon: '/favicon.ico'
      }
    ]
  };
  
  event.waitUntil(
    self.registration.showNotification('Quindío Travel', options)
  );
});

// Click en notificaciones
self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  
  if (event.action === 'explore') {
    event.waitUntil(
      clients.openWindow(event.notification.data.url || '/')
    );
  }
});

// Cache dinámico inteligente
async function cacheDynamicResponse(request, response) {
  const cache = await caches.open(DYNAMIC_CACHE);
  
  // Solo cachear respuestas exitosas
  if (response.ok) {
    // Clonar la respuesta antes de cachearla
    const responseToCache = response.clone();
    
    // Determinar tiempo de expiración según el tipo de contenido
    const url = new URL(request.url);
    let maxAge = 3600; // 1 hora por defecto
    
    if (url.pathname.includes('/api/')) {
      maxAge = 300; // 5 minutos para APIs
    } else if (url.pathname.includes('/planes/')) {
      maxAge = 7200; // 2 horas para planes
    }
    
    // Agregar headers de cache
    const headers = new Headers(responseToCache.headers);
    headers.set('Cache-Control', `max-age=${maxAge}`);
    
    const cachedResponse = new Response(responseToCache.body, {
      status: responseToCache.status,
      statusText: responseToCache.statusText,
      headers: headers
    });
    
    await cache.put(request, cachedResponse);
  }
  
  return response;
}

// Precaching inteligente de páginas visitadas
self.addEventListener('message', (event) => {
  if (event.data && event.data.type === 'CACHE_URLS') {
    event.waitUntil(
      caches.open(DYNAMIC_CACHE).then(cache => {
        return cache.addAll(event.data.urls);
      })
    );
  }
});

// Limpieza periódica de cache
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          // Eliminar caches que no se han usado recientemente
          return caches.open(cacheName).then(cache => {
            return cache.keys().then(keys => {
              if (keys.length === 0) {
                return caches.delete(cacheName);
              }
            });
          });
        })
      );
    })
  );
});

// Estadísticas de cache (desactivado en producción para mejor rendimiento)
if (location.hostname === 'localhost' || location.hostname === '127.0.0.1') {
  self.addEventListener('fetch', (event) => {
    // Logging de cache hits/misses para debugging
    event.respondWith(
      (async () => {
        const cache = await caches.open(DYNAMIC_CACHE);
        const cached = await cache.match(event.request);
        
        if (cached) {
          console.log('Cache HIT:', event.request.url);
          return cached;
        }
        
        console.log('Cache MISS:', event.request.url);
        const response = await fetch(event.request);
        
        if (response.ok) {
          await cache.put(event.request, response.clone());
        }
        
        return response;
      })()
    );
  });
}

console.log('Service Worker: Cargado correctamente');
