// Songbook PWA Service Worker
const CACHE = 'songbook-v2';
const ASSETS_TO_CACHE = [
    './',
    './index.html',
    'https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js',
    'https://cdn.jsdelivr.net/npm/marked/marked.min.js'
];

// Install event - precache assets; wait for existing clients to close or SKIP_WAITING
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE).then((cache) => cache.addAll(ASSETS_TO_CACHE))
    );
});

// Activate event - delete old caches, then take control
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys()
            .then((names) => Promise.all(
                names.filter((name) => name !== CACHE).map((name) => caches.delete(name))
            ))
            .then(() => self.clients.claim())
    );
});

// Let the page activate a waiting worker before all existing clients close
self.addEventListener('message', (event) => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

// Fetch event
self.addEventListener('fetch', (event) => {
    const request = event.request;
    if (request.method !== 'GET') {
        return;
    }

    // Navigations: network-first, revalidating past the 10-minute HTTP cache
    if (request.mode === 'navigate') {
        event.respondWith(
            fetch(request.url, { cache: 'no-cache' })
                .then((response) => {
                    if (response.ok) {
                        const copy = response.clone();
                        caches.open(CACHE).then((cache) => cache.put(request, copy));
                    }
                    return response;
                })
                .catch(() =>
                    caches.match(request).then((cached) => cached || caches.match('./index.html'))
                )
        );
        return;
    }

    // Other assets: cache-first (up to ~10 minute delay on GitHub Pages is acceptable)
    event.respondWith(
        caches.match(request).then((cached) => {
            if (cached) {
                return cached;
            }
            return fetch(request)
                .then((response) => {
                    const cacheable = response.ok &&
                        (response.type === 'basic' || request.url.includes('cdn.jsdelivr.net'));
                    if (cacheable) {
                        const copy = response.clone();
                        caches.open(CACHE).then((cache) => cache.put(request, copy));
                    }
                    return response;
                })
                .catch(() => new Response('Offline', { status: 503 }));
        })
    );
});

// Background sync for future enhancements
self.addEventListener('sync', (event) => {
    if (event.tag === 'sync-collection') {
        // Future: sync collection when online
        console.log('Background sync triggered');
    }
});
