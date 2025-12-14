/**
 * Service Worker with Workbox
 * Implements offline caching for Alpine Resume PWA (Issues S3-004, S3-005, S3-007)
 * 
 * Features:
 * - Cache-first strategy for static assets and CDN resources
 * - Separate cache per CDN origin for better management
 * - Cache versioning for controlled updates (S3-007)
 * - 90-day expiration with max 30 entries per CDN cache
 * - Caches HTML, CSS, JS, and CDN libraries (Alpine.js, Tailwind CSS, Marked.js, Bootstrap Icons)
 * - Automatic old cache cleanup on service worker update (S3-007)
 * - Skip waiting and clients claim for immediate activation (S3-007)
 */

// Import Workbox from CDN
importScripts('https://storage.googleapis.com/workbox-cdn/releases/7.0.0/workbox-sw.js');

// Check if Workbox loaded successfully
if (workbox) {
  console.log('Workbox loaded successfully');
  
  // Cache versioning - Semantic versioning format (S3-007)
  const CACHE_VERSION = 'v1.0.0';
  
  // Configure Workbox
  workbox.setConfig({
    debug: false
  });
  
  // Precache and route the application shell
  workbox.precaching.precacheAndRoute([
    { url: '/', revision: CACHE_VERSION },
    { url: '/index.html', revision: CACHE_VERSION },
    { url: '/manifest.json', revision: CACHE_VERSION },
    { url: '/styles/theme.css', revision: CACHE_VERSION }
  ]);
  
  // Cache HTML files with NetworkFirst strategy (prefer fresh content)
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'document',
    new workbox.strategies.NetworkFirst({
      cacheName: `html-cache-${CACHE_VERSION}`,
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 10,
          maxAgeSeconds: 7 * 24 * 60 * 60, // 7 days
        }),
      ],
    })
  );
  
  // Cache CDN resources (Alpine.js, Tailwind CSS, Marked.js, Bootstrap Icons)
  // CacheFirst strategy with separate cache per CDN origin (Issue S3-005)
  // Each CDN gets its own cache for better organization and management
  
  const cdnOrigins = [
    { origin: 'https://cdn.jsdelivr.net', name: 'cdnjsdelivrnet' },
    { origin: 'https://cdn.tailwindcss.com', name: 'cdntailwindcsscom' },
    { origin: 'https://unpkg.com', name: 'unpkgcom' },
    { origin: 'https://storage.googleapis.com', name: 'storagegoogleapiscom' }
  ];
  
  cdnOrigins.forEach(({ origin, name }) => {
    workbox.routing.registerRoute(
      ({ url }) => url.origin === origin,
      new workbox.strategies.CacheFirst({
        cacheName: `cdn-${name}-${CACHE_VERSION}`,
        plugins: [
          new workbox.cacheableResponse.CacheableResponsePlugin({
            statuses: [0, 200], // Cache successful responses
          }),
          new workbox.expiration.ExpirationPlugin({
            maxEntries: 30,
            maxAgeSeconds: 90 * 24 * 60 * 60, // 90 days
          }),
        ],
      })
    );
  });
  
  // Cache CSS files
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'style',
    new workbox.strategies.CacheFirst({
      cacheName: `css-cache-${CACHE_VERSION}`,
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 10,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
        }),
      ],
    })
  );
  
  // Cache JavaScript files
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'script',
    new workbox.strategies.CacheFirst({
      cacheName: `js-cache-${CACHE_VERSION}`,
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 20,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
        }),
      ],
    })
  );
  
  // Cache images (icons, favicons, etc.)
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'image',
    new workbox.strategies.CacheFirst({
      cacheName: `image-cache-${CACHE_VERSION}`,
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 30,
          maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
        }),
      ],
    })
  );
  
  // Cache fonts
  workbox.routing.registerRoute(
    ({ request }) => request.destination === 'font',
    new workbox.strategies.CacheFirst({
      cacheName: `font-cache-${CACHE_VERSION}`,
      plugins: [
        new workbox.expiration.ExpirationPlugin({
          maxEntries: 10,
          maxAgeSeconds: 365 * 24 * 60 * 60, // 1 year
        }),
      ],
    })
  );
  
  // Catch-all route for other requests (NetworkFirst)
  workbox.routing.setDefaultHandler(
    new workbox.strategies.NetworkFirst({
      cacheName: `default-cache-${CACHE_VERSION}`,
    })
  );
  
  // Handle service worker activation (S3-007)
  self.addEventListener('activate', (event) => {
    console.log('Service Worker activated');
    
    // Clean up old caches - delete any cache that doesn't match current version
    const currentCaches = [
      `html-cache-${CACHE_VERSION}`,
      `cdn-cdnjsdelivrnet-${CACHE_VERSION}`,
      `cdn-cdntailwindcsscom-${CACHE_VERSION}`,
      `cdn-unpkgcom-${CACHE_VERSION}`,
      `cdn-storagegoogleapiscom-${CACHE_VERSION}`,
      `css-cache-${CACHE_VERSION}`,
      `js-cache-${CACHE_VERSION}`,
      `image-cache-${CACHE_VERSION}`,
      `font-cache-${CACHE_VERSION}`,
      `default-cache-${CACHE_VERSION}`,
      `workbox-precache-${CACHE_VERSION}`,
    ];
    
    event.waitUntil(
      caches.keys().then((cacheNames) => {
        // Delete old caches and claim clients for immediate activation
        return Promise.all(
          cacheNames.map((cacheName) => {
            if (!currentCaches.includes(cacheName) && !cacheName.startsWith('workbox-')) {
              console.log('Deleting old cache:', cacheName);
              return caches.delete(cacheName);
            }
          })
        ).then(() => {
          // Claim clients immediately so updates take effect without waiting
          console.log('Service Worker claiming clients');
          return self.clients.claim();
        });
      })
    );
  });
  
  // Handle service worker messages (S3-007)
  self.addEventListener('message', (event) => {
    // Support both message formats: { type: 'SKIP_WAITING' } and 'SKIP_WAITING'
    if (event.data === 'SKIP_WAITING' || (event.data && event.data.type === 'SKIP_WAITING')) {
      console.log('Service Worker: Skipping waiting');
      self.skipWaiting();
    }
  });
  
  console.log('Service Worker configuration complete');
  
} else {
  console.error('Workbox failed to load');
}
