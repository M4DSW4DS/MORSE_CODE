const CACHE_VERSION = 'v3'; // Подняли версию, чтобы старый кэш сбросился
const CACHE_NAME = `morse-gadget-${CACHE_VERSION}`;
const URLS_TO_CACHE = [
  './',
  './index.html',
  './manifest.json',
  './icons/apple-touch-icon.png',
  './icons/favicon-96x96.png',
  './icons/web-app-manifest-192x192.png',
  './icons/web-app-manifest-512x512.png'
];
// ... дальше код без изменений