const fs = require('fs');

const indexHtml = 'index.html';
const content = fs.readFileSync(indexHtml, 'utf8');

// Eliminar estilos CSS de chatbot duplicados
const chatbotStylesPattern = /[\s\S]*?\.chatbot-header[\s\S]*?\.language-selector/;
const newContent = content.replace(chatbotStylesPattern, '\n    .language-selector');

if (content !== newContent) {
    fs.writeFileSync(indexHtml, newContent);
    console.log('Removed duplicate chatbot CSS styles');
} else {
    console.log('No chatbot CSS styles found to remove');
}