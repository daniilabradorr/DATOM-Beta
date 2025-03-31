if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/static/js/service-worker.js')
        .then(function(registration) {
            console.log('✅ Service Worker registrado con éxito:', registration);
        })
        .catch(function(error) {
            console.error('❌ Error al registrar el Service Worker:', error);
        });
}
