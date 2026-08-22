const fs = require('fs');
const path = require('path');

function fixLogoInDirectory(dir) {
    const files = fs.readdirSync(dir);
    
    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);
        
        if (stat.isDirectory()) {
            fixLogoInDirectory(filePath);
        } else if (file.endsWith('.html')) {
            try {
                const content = fs.readFileSync(filePath, 'utf8');
                
                // Fix logo paths
                let newContent = content
                    .replace(/src="\/logo_quindio_travel\.webp"/g, 'src="../assets/images/logo_quindio_travel.webp"')
                    .replace(/src="logo_quindio_travel\.webp"/g, 'src="../assets/images/logo_quindio_travel.webp"')
                    .replace(/"logo": "https:\/\/quindiotravel\.com\.co\/logo\.webp"/g, '"logo": "https://quindiotravel.com.co/assets/images/logo_quindio_travel.webp"')
                    .replace(/src="\/assets\/images\/logo_quindio_travel\.webp"/g, 'src="../assets/images/logo_quindio_travel.webp');
                
                if (content !== newContent) {
                    fs.writeFileSync(filePath, newContent);
                    console.log(`Fixed logo in: ${filePath}`);
                }
            } catch (error) {
                console.error(`Error processing ${filePath}:`, error);
            }
        }
    });
}

// Fix in generated-pages
const generatedPagesDir = path.join(__dirname, 'generated-pages');
if (fs.existsSync(generatedPagesDir)) {
    console.log('Fixing logos in generated-pages...');
    fixLogoInDirectory(generatedPagesDir);
}

// Fix in blog
const blogDir = path.join(__dirname, 'blog');
if (fs.existsSync(blogDir)) {
    console.log('Fixing logos in blog...');
    fixLogoInDirectory(blogDir);
}

console.log('Logo fix complete');