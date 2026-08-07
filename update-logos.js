const fs = require('fs');

const planFiles = [
    'plan-1.html',
    'plan-2.html', 
    'plan-3.html',
    'plan-4.html',
    'plan-5.html',
    'plan-6.html'
];

planFiles.forEach(file => {
    try {
        const content = fs.readFileSync(file, 'utf8');
        const newContent = content.replace(
            /src="logo_quindio_travel\.png"/g,
            'src="assets/images/logo_quindio_travel.png"'
        );
        
        if (content !== newContent) {
            fs.writeFileSync(file, newContent);
            console.log(`Updated logo in ${file}`);
        } else {
            console.log(`No logo changes needed in ${file}`);
        }
    } catch (error) {
        console.error(`Error processing ${file}:`, error);
    }
});

console.log('Logo update complete');