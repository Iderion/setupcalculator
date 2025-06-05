// Internationalisierung
let currentLanguage = 'de';
let translations = {};

async function loadLanguage(lang) {
    currentLanguage = lang;
    try {
        const response = await fetch(`lang/${lang}.json`);
        translations = await response.json();
        applyTranslations();
    } catch (error) {
        console.error('Fehler beim Laden der Sprache:', error);
    }
}

function t(key) {
    return translations[key] || key;
}

function applyTranslations() {
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        element.textContent = t(key);
    });
    
    // Spezielle Elemente
    if (document.getElementById('welcome-title')) {
        document.getElementById('welcome-title').textContent = t('welcome');
    }
    if (document.getElementById('token-label')) {
        document.getElementById('token-label').textContent = t('token.prompt');
    }
}