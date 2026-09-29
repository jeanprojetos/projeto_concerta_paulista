const CACHE_NAME = 'concerta-paulista-v2';
const ARQUIVOS_ESSENCIAIS = [
    '/',
    '/static/core/css/style.css',
    '/static/core/js/theme.js',
    '/static/core/img/icon-192.png',
];

self.addEventListener('install', function (event) {
    event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            return cache.addAll(ARQUIVOS_ESSENCIAIS).catch(function () {
                /* se algum arquivo falhar, a instalação continua mesmo assim */
            });
        })
    );
});

self.addEventListener('activate', function (event) {
    event.waitUntil(
        caches.keys().then(function (nomes) {
            return Promise.all(
                nomes.filter(function (nome) { return nome !== CACHE_NAME; })
                     .map(function (nome) { return caches.delete(nome); })
            );
        })
    );
});

self.addEventListener('fetch', function (event) {
    if (event.request.method !== 'GET') return;

    event.respondWith(
        caches.match(event.request).then(function (resposta) {
            return resposta || fetch(event.request).catch(function () {
                return caches.match('/');
            });
        })
    );
});
