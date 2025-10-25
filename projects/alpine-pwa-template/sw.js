// sw.js - minimal cache for app shell + Markdown files
const VERSION = 'v1';
const CACHE = `alpine-pwa-${VERSION}`;
const APP_SHELL = [
  './',
  './index.html', // helpful for local dev; GitHub Pages also serves index.html
  // Add pinned CDN URLs here if you want them pre-cached.
  // Local repo content (optional): './files.json', './files/example.md',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(APP_SHELL)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (e) => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const sameOrigin = url.origin === location.origin;
  const isRepoMd = sameOrigin && url.pathname.includes('/files/') && url.pathname.endsWith('.md');

  // Cache-first for same-origin (your app shell) and Markdown under /files/
  if (sameOrigin || isRepoMd) {
    e.respondWith(
      caches.match(req).then(cached =>
        cached || fetch(req).then(resp => {
          const clone = resp.clone();
          caches.open(CACHE).then(c => c.put(req, clone));
          return resp;
        }).catch(() => caches.match('./index.html'))
      )
    );
  }
});
