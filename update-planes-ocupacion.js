const fs = require('fs');

const preciosPorPlan = {
    'plan-3.html': {
        economico: { doble: 1385000, triple: 1170000, cuadruple: 1050000 },
        intermedio: { doble: 1440000, triple: 1215000, cuadruple: 1150000 },
        intermedio_vip: { doble: 1865000, triple: 1650000, cuadruple: 1530000 },
        vip: { doble: 3000000, triple: 2660000, cuadruple: 2490000 }
    },
    'plan-4.html': {
        economico: { doble: 1495000, triple: 1250000, cuadruple: 1125000 },
        intermedio: { doble: 1550000, triple: 1295000, cuadruple: 1160000 },
        intermedio_vip: { doble: 1990000, triple: 1730000, cuadruple: 1590000 },
        vip: { doble: 3120000, triple: 2740000, cuadruple: 2550000 }
    },
    'plan-5.html': {
        economico: { doble: 1297000, triple: 1120000, cuadruple: 1020000 },
        intermedio: { doble: 1260000, triple: 1160000, cuadruple: 1060000 },
        intermedio_vip: { doble: 1795000, triple: 1590000, cuadruple: 1490000 },
        vip: { doble: 2920000, triple: 2600000, cuadruple: 2450000 }
    },
    'plan-6.html': {
        economico: { doble: 1800000, triple: 1520000, cuadruple: 1380000 },
        intermedio: { doble: 1880000, triple: 1580000, cuadruple: 1430000 },
        intermedio_vip: { doble: 2465000, triple: 2150000, cuadruple: 1995000 },
        vip: { doble: 3960000, triple: 3510000, cuadruple: 3280000 }
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