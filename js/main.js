// Gemeinsame Hilfsfunktionen
function getToken() {
    return localStorage.getItem('token');
}

function saveToken(token) {
    localStorage.setItem('token', token);
}

function redirectIfNoToken() {
    if (!getToken()) {
        window.location.href = 'index.html';
    }
}

function redirectIfTokenExists() {
    if (getToken()) {
        window.location.href = 'setup.html';
    }
}