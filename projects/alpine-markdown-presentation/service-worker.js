// Service Worker for Presentation Viewer PWA
// Version 1.0.1

const CACHE_VERSION = 'presentation-viewer-v1.0.1';
const CACHE_NAME = `pwa-presentation-${CACHE_VERSION}`;

// URLs to cache for offline functionality
const urlsToCache = [
  './',
  './index.html',
  './presentation-sample.md',
  './presentation-template.md',
  // CDN resources
  'https://cdn.jsdelivr.net/npm/marked/lib/marked.umd.js',
  'https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js',
  'https://cdn.jsdelivr.net/gh/gitbrent/pptxgenjs@3.12.0/dist/pptxgen.bundle.js'
];

// Install event - cache resources
self.addEventListener('install', (event) => {
  console.log('[Service Worker] Installing...');
  
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        console.log('[Service Worker] Caching app shell and content');
        return cache.addAll(urlsToCache);
      })
      .then(() => {
        console.log('[Service Worker] Install complete');
        return self.skipWaiting(); // Activate immediately
      })
      .catch((error) => {
        console.error('[Service Worker] Install failed:', error);
      })
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', (event) => {
  console.log('[Service Worker] Activating...');
  
  event.waitUntil(
    caches.keys()
      .then((cacheNames) => {
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (cacheName !== CACHE_NAME) {
              console.log('[Service Worker] Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        );
      })
      .then(() => {
        console.log('[Service Worker] Activation complete');
        return self.clients.claim(); // Take control immediately
      })
  );
});

// Fetch event - serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip cross-origin requests that aren't from our CDNs
  if (url.origin !== location.origin && 
      !url.hostname.includes('cdn.jsdelivr.net') &&
      !url.hostname.includes('unpkg.com')) {
    return;
  }
  
  event.respondWith(
    caches.match(request)
      .then((cachedResponse) => {
        // Return cached response if found
        if (cachedResponse) {
          console.log('[Service Worker] Serving from cache:', request.url);
          
          // For HTML and CDN resources, check for updates in background
          if (request.url.endsWith('.html') || 
              request.url.includes('cdn.jsdelivr.net') || 
              request.url.includes('unpkg.com')) {
            
            // Fetch update in background
            fetch(request)
              .then((response) => {
                if (response && response.status === 200) {
                  caches.open(CACHE_NAME).then((cache) => {
                    cache.put(request, response.clone());
                  });
                }
              })
              .catch(() => {
                // Silently fail - we have the cached version
              });
          }
          
          return cachedResponse;
        }
        
        // Not in cache, fetch from network
        console.log('[Service Worker] Fetching from network:', request.url);
        return fetch(request)
          .then((response) => {
            // Don't cache if not a valid response
            if (!response || response.status !== 200 || response.type === 'error') {
              return response;
            }
            
            // Clone the response
            const responseToCache = response.clone();
            
            // Cache for later
            caches.open(CACHE_NAME)
              .then((cache) => {
                cache.put(request, responseToCache);
              });
            
            return response;
          })
          .catch((error) => {
            console.error('[Service Worker] Fetch failed:', error);
            
            // Return offline page or fallback
            if (request.destination === 'document') {
              return caches.match('/presentation-viewer.html');
            }
            
            throw error;
          });
      })
  );
});

// Message event - handle commands from the app
self.addEventListener('message', (event) => {
  console.log('[Service Worker] Message received:', event.data);
  
  if (event.data.action === 'skipWaiting') {
    self.skipWaiting();
  }
  
  if (event.data.action === 'clearCache') {
    event.waitUntil(
      caches.delete(CACHE_NAME)
        .then(() => {
          console.log('[Service Worker] Cache cleared');
          // Notify the client
          event.ports[0].postMessage({ success: true });
        })
    );
  }
  
  if (event.data.action === 'getCacheStatus') {
    event.waitUntil(
      caches.has(CACHE_NAME)
        .then((exists) => {
          return caches.open(CACHE_NAME);
        })
        .then((cache) => {
          return cache.keys();
        })
        .then((requests) => {
          event.ports[0].postMessage({
            cached: true,
            count: requests.length,
            urls: requests.map(r => r.url)
          });
        })
        .catch((error) => {
          event.ports[0].postMessage({
            cached: false,
            error: error.message
          });
        })
    );
  }
});

// Background sync (for future enhancement)
self.addEventListener('sync', (event) => {
  console.log('[Service Worker] Background sync:', event.tag);
  
  if (event.tag === 'sync-presentations') {
    event.waitUntil(
      // Sync logic here
      Promise.resolve()
    );
  }
});

// Push notification (for future enhancement)
self.addEventListener('push', (event) => {
  console.log('[Service Worker] Push received');
  
  const options = {
    body: event.data ? event.data.text() : 'New update available',
    icon: '/icon-192.png',
    badge: '/badge-72.png'
  };
  
  event.waitUntil(
    self.registration.showNotification('Presentation Viewer', options)
  );
});

// Notification click handler
self.addEventListener('notificationclick', (event) => {
  console.log('[Service Worker] Notification clicked');
  
  event.notification.close();
  
  event.waitUntil(
    clients.openWindow('/')
  );
});

console.log('[Service Worker] Loaded and ready');
