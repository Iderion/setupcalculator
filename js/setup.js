// Setup-Logik (Beispiel)
function initSetup() {
    console.log('Setup wird initialisiert...');
    
    // Hier kommt Ihre CRUD-Logik für Setup-Daten
    const setupContent = document.getElementById('setup-content');
    setupContent.innerHTML = `
        <div class="setup-item">
            <h2>${t('setup.current')}</h2>
            <p>${t('setup.description')}</p>
        </div>
    `;
    
    // Beispiel: Setup-Daten speichern
    const setupData = {
        items: [],
        lastUpdated: new Date().toISOString()
    };
    localStorage.setItem(`setup_${getToken()}`, JSON.stringify(setupData));
}

// setup.js
async function loadSetupTemplate() {
    const response = await fetch('assets/setup_template.json');
    return await response.json();
}

function generateSetupForm(template) {
    const container = document.getElementById('setup-values');
    container.innerHTML = '';
    
    Object.values(template.categories).forEach(category => {
        const categoryDiv = document.createElement('div');
        categoryDiv.className = 'setup-category';
        categoryDiv.innerHTML = `<h3>${category.name}</h3>`;
        
        Object.values(category.parameters).forEach(param => {
            const paramDiv = document.createElement('div');
            paramDiv.className = 'setup-item';
            paramDiv.innerHTML = `
                <label>${param.name}</label>
                <input type="number" id="${param.name.replace(/\s+/g, '_')}" 
                       min="${param.min}" max="${param.max}" 
                       step="${param.step}" value="${getDefaultForTrack(param)}">
                <span class="unit">${param.unit}</span>
            `;
            categoryDiv.appendChild(paramDiv);
        });
        
        container.appendChild(categoryDiv);
    });
}

function getDefaultForTrack(param) {
    const track = document.getElementById('track-select').value;
    return param.defaults[track] || Object.values(param.defaults)[0];
}