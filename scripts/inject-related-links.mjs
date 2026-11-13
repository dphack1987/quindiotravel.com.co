// Inyecta assets/js/related-links.js en las páginas indexables
// listadas en assets/data/related-links-map.json.
// Uso: node scripts/inject-related-links.mjs [--dry]
import { readFileSync, writeFileSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..');
const DRY = process.argv.includes('--dry');
const MARK = 'related-links.js';

const map = JSON.parse(
  readFileSync(join(ROOT, 'assets/data/related-links-map.json'), 'utf8'));

let modified = 0, skipped = 0, missing = 0;

for (const rel of Object.keys(map)) {
  const file = join(ROOT, rel);
  let html;
  try {
    html = readFileSync(file, 'utf8');
  } catch {
    missing++;
    continue;
  }
  if (html.includes(MARK)) { skipped++; continue; }
  if (!/<\/body>/i.test(html)) { missing++; continue; }

  const depth = rel.split('/').length - 1;
  const base = depth === 0 ? '' : '../'.repeat(depth);
  const tag = `<script src="${base}assets/js/related-links.js" defer></script>`;
  const out = html.replace(/<\/body>/i, `    ${tag}\n</body>`);

  if (!DRY) writeFileSync(file, out, 'utf8');
  modified++;
}

console.log(`${DRY ? '[dry-run] ' : ''}Inyectadas: ${modified} | Ya existían: ${skipped} | Sin archivo/body: ${missing}`);
