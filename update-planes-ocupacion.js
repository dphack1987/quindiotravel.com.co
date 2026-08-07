const fs = require('fs');

const preciosPorPlan = {
    'plan-3.html': {
        economico: { doble: 1150000, triple: 1050000, cuadruple: 979000 },
        intermedio: { doble: 1150000, triple: 1050000, cuadruple: 979000 },
        intermedio_vip: { doble: 1150000, triple: 1050000, cuadruple: 979000 },
        vip: { doble: 1150000, triple: 1050000, cuadruple: 979000 }
    },
    'plan-4.html': {
        economico: { doble: 1270000, triple: 1120000, cuadruple: 979000 },
        intermedio: { doble: 1270000, triple: 1120000, cuadruple: 979000 },
        intermedio_vip: { doble: 1270000, triple: 1120000, cuadruple: 979000 },
        vip: { doble: 1270000, triple: 1120000, cuadruple: 979000 }
    },
    'plan-5.html': {
        economico: { doble: 1200000, triple: 1080000, cuadruple: 950000 },
        intermedio: { doble: 1200000, triple: 1080000, cuadruple: 950000 },
        intermedio_vip: { doble: 1200000, triple: 1080000, cuadruple: 950000 },
        vip: { doble: 1200000, triple: 1080000, cuadruple: 950000 }
    },
    'plan-6.html': {
        economico: { doble: 1650000, triple: 1550000, cuadruple: 1473000 },
        intermedio: { doble: 1650000, triple: 1550000, cuadruple: 1473000 },
        intermedio_vip: { doble: 1650000, triple: 1550000, cuadruple: 1473000 },
        vip: { doble: 1650000, triple: 1550000, cuadruple: 1473000 }
    }
};

function formatPrice(price) {
    return new Intl.NumberFormat('es-CO').format(price);
}

function generatePrecioHTML(categoria, precios) {
    return `
                <div style="margin-bottom: 15px;">
                    <p style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">Doble:</p>
                    <p style="font-size: 1.5rem; font-weight: 700; color: var(--marron-madera);">$${formatPrice(precios.doble)}</p>
                </div>
                <div style="margin-bottom: 15px;">
                    <p style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">Triple:</p>
                    <p style="font-size: 1.5rem; font-weight: 700; color: var(--marron-madera);">$${formatPrice(precios.triple)}</p>
                </div>
                <div style="margin-bottom: 15px;">
                    <p style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">Cuádruple:</p>
                    <p style="font-size: 1.5rem; font-weight: 700; color: var(--marron-madera);">$${formatPrice(precios.cuadruple)}</p>
                </div>`;
}

function updatePlanFile(filename) {
    const content = fs.readFileSync(filename, 'utf8');
    const precios = preciosPorPlan[filename];
    
    // Reemplazar cada categoría con sus precios por ocupación
    const categorias = ['Económico', 'Intermedio', 'Intermedio VIP', 'VIP'];
    const categoriasClave = ['economico', 'intermedio', 'intermedio_vip', 'vip'];
    
    let newContent = content;
    
    categoriasClave.forEach((cat, index) => {
        const oldPattern = new RegExp(`<h3 style="color: var\\(--verde-cafe\\); margin-bottom: 15px; font-size: 1\\.3rem;">.*?${categorias[index]}<\\/h3>[\\s\\S]*?<\\/div>`, 'g');
        const catPrecios = precios[cat];
        const newHTML = `<h3 style="color: var(--verde-cafe); margin-bottom: 15px; font-size: 1.3rem;">${getBadge(categorias[index])} ${categorias[index]}</h3>${generatePrecioHTML(categorias[index], catPrecios)}`;
        newContent = newContent.replace(oldPattern, newHTML);
    });
    
    fs.writeFileSync(filename, newContent);
    console.log(`Updated ${filename} successfully`);
}

function getBadge(categoria) {
    const badges = {
        'Económico': '💰',
        'Intermedio': '⭐',
        'Intermedio VIP': '⭐⭐',
        'VIP': '👑'
    };
    return badges[categoria] || '';
}

// Actualizar cada archivo
Object.keys(preciosPorPlan).forEach(updatePlanFile);

console.log('All plan files updated successfully');