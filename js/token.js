// Token-Generierung und Validierung
function generateToken() {
    return 'token-' + Math.random().toString(36).substr(2, 9) + 
           Date.now().toString(36).substr(4);
}

function validateToken(token) {
    return token && token.length >= 12 && /^[a-zA-Z0-9-]+$/.test(token);
}