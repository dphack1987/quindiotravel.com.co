// Inyecta la temática de diciembre (CSS + JS) en todas las páginas HTML.
// Uso: node scripts/inject-diciembre-theme.mjs [--dry]
import { readdirSync, readFileSync, writeFileSync, statSync } from 'node:fs';
import { join, relative, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DRY = process.argv.includes('--dry');

const EXCLUDE_DIRS = new Set([
  'node_modules', 'dist', '.git', 'tests', 'scripts', 'docs',
  'backup-microdata-20260930-102216', 'documentation_archive',
  'lead_automation_system', 'don-chucho-backend', 'directories_data',
  'outreach_data', 'social_media_content', 'datos'
]);

const MARK = 'diciembre-theme';
let modified = 0, skipped = 0, noHead = 0;

function walk(dir) {
  for (const entry of readdirSync(dir, { withFileTypes: true })) {
    const full = join(dir, entry.name);
    if (entry.isDirectory()) {
      if (!EXCLUDE_DIRS.has(entry.name)) walk(full);
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.html')) {
      processFile(full);
    }
  }
}

function processFile(file) {
  const html = readFileSync(file, 'utf8');
  if (html.includes(MARK)) { skipped++; return; }

  const depth = relative(ROOT, dirname(file)).split(/[\\/]/).filter(Boolean).length;
  const base = depth === 0 ? '' : '../'.repeat(depth);
  const css = `<link rel="stylesheet" href="${base}assets/css/diciembre-theme.css">`;
  const js = `<script src="${base}assets/js/diciembre-theme.js" defer></script>`;

  let out = html;
  let ok = true;

  if (/<\/head>/i.test(out)) {
    out = out.replace(/<\/head>/i, `    ${css}\n</head>`);
  } else { ok = false; }

  if (/<\/body>/i.test(out)) {
    out = out.replace(/<\/body>/i, `    ${js}\n</body>`);
  } else { ok = false; }

  if (!ok) { noHead++; console.log('SIN </head> o </body>, omitido:', relative(ROOT, file)); return; }

  if (!DRY) writeFileSync(file, out, 'utf8');
  modified++;
}

walk(ROOT);
console.log(`${DRY ? '[dry-run] ' : ''}Modificados: ${modified} | Ya tenían el tema: ${skipped} | Omitidos: ${noHead}`);
