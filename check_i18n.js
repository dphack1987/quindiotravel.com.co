const fs = require('fs');
const path = require('path');
const glob = require('glob');
const text = fs.readFileSync(path.join('assets','js','language-detector.js'), 'utf8');
const obj = text.split('const translations = {',1)[1].split('};').slice(0,-1).join('};');
const keys = new Set(obj.match(/['"]([a-z0-9_.]+)['"]\s*:/gi).map(m => m.replace(/['"]|\s*:/g, '')));
const used = new Set();
const files = glob.sync('**/*.html');
const re = /data-i18n=["']([^"']+)["']/g;
for (const f of files) {
  const c = fs.readFileSync(f, 'utf8');
  let m;
  while ((m = re.exec(c)) !== null) {
    used.add(m[1]);
  }
}
const missing = [...used].filter(k => !keys.has(k)).sort();
console.log('translation keys:', keys.size);
console.log('used keys:', used.size);
console.log('missing keys:', missing.length);
console.log(missing.join('\n'));
