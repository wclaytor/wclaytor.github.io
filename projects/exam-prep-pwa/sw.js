const sw = self;
const CACHE_PREFIX = "exam-prep-pwa-";
const CACHE_NAME = `${CACHE_PREFIX}${"ce294e7f7586"}`;
sw.addEventListener("install", (event) => {
	event.waitUntil(caches.open(CACHE_NAME).then((cache) => cache.addAll(["./","./assets/index-RmcP2V_b.js","./assets/style-q3aoCSe-.css","./index.html","./fonts/ibm-plex-mono-latin-400-normal.woff2","./fonts/ibm-plex-mono-latin-500-normal.woff2","./fonts/ibm-plex-sans-latin-400-normal.woff2","./fonts/ibm-plex-sans-latin-500-normal.woff2","./fonts/ibm-plex-sans-latin-600-normal.woff2","./icons/apple-touch-icon.png","./icons/icon-192.png","./icons/icon-512.png","./icons/icon-maskable-512.png","./icons/icon.svg","./manifest.webmanifest"].map((url) => new Request(url, { cache: "reload" })))));
});
sw.addEventListener("activate", (event) => {
	event.waitUntil((async () => {
		const names = await caches.keys();
		// Only this app's old caches: other projects share the origin (§4.7).
		await Promise.all(names.filter((n) => n.startsWith(CACHE_PREFIX) && n !== CACHE_NAME).map((n) => caches.delete(n)));
		await sw.clients.claim();
	})());
});
sw.addEventListener("fetch", (event) => {
	const request = event.request;
	if (request.method !== "GET") return;
	const url = new URL(request.url);
	if (url.origin !== sw.location.origin) return;
	event.respondWith((async () => {
		const cache = await caches.open(CACHE_NAME);
		const cached = await cache.match(request, { ignoreSearch: request.mode === "navigate" });
		if (cached) return cached;
		if (request.mode === "navigate") {
			const shell = await cache.match("./index.html") ?? await cache.match("./");
			if (shell) return shell;
		}
		return fetch(request);
	})());
});
sw.addEventListener("message", (event) => {
	const data = event.data;
	if (data?.type === "GET_VERSION") {
		event.ports[0]?.postMessage({
			version: "0.1.0",
			buildId: "ce294e7f7586"
		});
	} else if (data?.type === "SKIP_WAITING") {
		void sw.skipWaiting();
	}
});
