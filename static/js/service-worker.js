// Nombre del caché actualizado para cada nueva versión
const CACHE_NAME = 'my-cache-v2'; // Cambia este nombre cuando actualices los archivos

// Instalación del Service Worker
self.addEventListener('install', function(event) {
    console.log('📦 Instalando Service Worker...');
    self.skipWaiting(); // Activación inmediata para reemplazar el Service Worker anterior
    event.waitUntil(
        caches.open(CACHE_NAME).then(function(cache) {
            return cache.addAll([
                '/',
                '/static/css/styles.css',
                '/static/js/scripts.js',
                '/static/img/icono192.png',
                '/static/img/icono512.png',
                '/static/img/icono144.png'
            ]);
        }).catch(function(error) {
            console.error('❌ Error al abrir el caché durante la instalación:', error);
        })
    );
});

// Activación del Service Worker (borrar cachés antiguos si cambia la versión)
self.addEventListener('activate', function(event) {
    console.log('⚙️ Activando nuevo Service Worker...');
    event.waitUntil(
        caches.keys().then(function(keys) {
            return Promise.all(
                keys.filter(function(key) {
                    return key !== CACHE_NAME; // No eliminar el nuevo caché
                }).map(function(key) {
                    console.log('🗑️ Borrando caché antiguo:', key);
                    return caches.delete(key); // Eliminar cachés antiguos
                })
            );
        })
    );
    self.clients.claim(); // Control inmediato de las páginas abiertas
});

// Intercepción de solicitudes
self.addEventListener('fetch', function(event) {
    event.respondWith(
        (async function() {
            try {
                const cachedResponse = await caches.match(event.request);
                // Si el recurso está en caché, devolverlo desde allí
                if (cachedResponse) {
                    return cachedResponse;
                }
                // Si no está en caché, realizar una solicitud de red
                const networkResponse = await fetch(event.request);
                return networkResponse;
            } catch (error) {
                console.error('❌ Error en fetch:', error);
                // Responder con un error si ocurre un problema con la red
                return new Response('Error al recuperar el recurso.', {
                    status: 500,
                    statusText: 'Error interno del Service Worker'
                });
            }
        })()
    );
});
