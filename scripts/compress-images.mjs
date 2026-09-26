import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const MIN_ARG = process.argv.find(a => a.startsWith('--min='));
const MIN_BYTES = MIN_ARG ? parseInt(MIN_ARG.split('=')[1], 10) : 1_000_000;
const MAX_WIDTH = 1920;           // no ampliar (full-width hero / retina razonable)
const QUALITY  = 80;
// Seguridad: modo dry-run por defecto para evitar cambios accidentales
const DRY = !process.argv.includes('--execute');

const IMAGE_RE = /\.(jpe?g|png|webp)$/i;
const SKIP_DIRS = new Set(['dist', 'node_modules', '.git', '.vite']);

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      walk(path.join(dir, e.name), out);
    } else if (IMAGE_RE.test(e.name)) {
      out.push(path.join(dir, e.name));
    }
  }
  return out;
}

function collectRefs() {
  const refs = new Set();
  const FILE_RE = /[\w\-./%]+\.(?:jpe?g|png|webp|svg|gif|avif)/gi;
  const scanDirs = ['', 'assets', 'blog', 'en', 'zh', 'planes', 'experiencias', 'programmatic-pages', 'generated-pages'];
  for (const d of scanDirs) {
    const base = path.join(rootDir, d);
    if (!fs.existsSync(base)) continue;
    const stack = [base];
    while (stack.length) {
      const cur = stack.pop();
      for (const e of fs.readdirSync(cur, { withFileTypes: true })) {
        const p = path.join(cur, e.name);
        if (e.isDirectory()) { if (!SKIP_DIRS.has(e.name)) stack.push(p); continue; }
        if (!/\.(?:html|js|css|json|xml|md|svg)$/i.test(e.name)) continue;
        try {
          const txt = fs.readFileSync(p, 'utf8');
          for (const m of txt.matchAll(FILE_RE)) refs.add(m[0].split('/').pop().toLowerCase());
        } catch { /* binarios */ }
      }
    }
  }
  return refs;
}

const files = walk(rootDir);
const targets = files.filter(f => fs.statSync(f).size > MIN_BYTES);
const refs = collectRefs();

// Ya recomprimadas en una pasada anterior -> no re-codificar (perdida de 2a generacion)
const already = new Set();
try {
  const raw = execSync('git status --porcelain -z', { cwd: rootDir, encoding: 'utf8', maxBuffer: 1e8 });
  for (const e of raw.split('\0')) {
    if (/^[ MADRCU?!]{2} /.test(e)) already.add(e.slice(3).replace(/\\/g, '/'));
  }
} catch { /* sin git: sin guarda */ }

console.log(`imagenes .jpg/.jpeg/.png/.webp: ${files.length}  |  >${MIN_BYTES} bytes: ${targets.length}  |  ya comprimidas: ${already.size}  |  modo: ${DRY ? 'DRY-RUN (agrega --execute para aplicar cambios)' : 'ejecutar'}\n`);

let before = 0, after = 0, done = 0, skipped = 0, failed = 0;
const unused = [];

for (const file of targets) {
  const rel = path.relative(rootDir, file);
  const b0 = fs.statSync(file).size;
  before += b0;
  if (!refs.has(path.basename(file).toLowerCase())) unused.push(rel);

  if (already.has(rel.split(path.sep).join('/'))) {
    after += b0; skipped++;
    if (!DRY) console.log(`  2gen  ${(b0 / 1e6).toFixed(2)} MB (ya comprimida en pasada anterior)  ${rel}`);
    continue;
  }

  if (DRY) { after += b0; continue; }

  try {
    // Buffer en memoria: libvips mantiene abierto el archivo de entrada y
    // sobrescribirlo desde disco provoca sharing violation en Windows.
    const input = fs.readFileSync(file);
    const img = sharp(input, { failOn: 'none' }).rotate();
    const meta = await img.metadata();
    const pipeline = (meta.width && meta.width > MAX_WIDTH)
      ? img.resize({ width: MAX_WIDTH, withoutEnlargement: true })
      : img;

    let out = pipeline;
    if (meta.format === 'png') {
      // PNG: solo lossless (paletas degradan fotos)
      out = pipeline.png({ compressionLevel: 9, adaptiveFiltering: true });
    } else if (meta.format === 'webp') {
      out = pipeline.webp({ quality: QUALITY, effort: 5 });
    } else {
      out = pipeline.jpeg({ quality: QUALITY, mozjpeg: true, chromaSubsampling: '4:2:0' });
    }
    const buf = await out.toBuffer();

    if (buf.length > 0 && buf.length < b0 * 0.9) {
      fs.writeFileSync(file, buf);
      const check = await sharp(fs.readFileSync(file)).metadata();
      if (check.format !== meta.format || !check.width) throw new Error('verificacion post-escritura fallo');
      after += buf.length; done++;
      console.log(`  ok   ${(b0 / 1e6).toFixed(2)} -> ${(buf.length / 1e6).toFixed(2)} MB  (-${Math.round(100 - (100 * buf.length) / b0)}%)  ${check.width}x${check.height}  ${rel}`);
    } else {
      after += b0; skipped++;
      console.log(`  skip ${(b0 / 1e6).toFixed(2)} MB (no mejora)  ${rel}`);
    }
  } catch (e) {
    failed++;
    after += b0;
    console.log(`  FAIL ${rel}: ${e.message}`);
  }
}

console.log(`\n== RESULTADO ==`);
console.log(`procesadas: ${targets.length} | recomprimidas: ${done} | sin mejora: ${skipped} | fallos: ${failed}`);
console.log(`peso antes: ${(before / 1e6).toFixed(1)} MB | despues: ${(after / 1e6).toFixed(1)} MB | ahorrado: ${((before - after) / 1e6).toFixed(1)} MB`);

if (unused.length) {
  console.log(`\n== IMAGENES >1 MB SIN REFERENCIAS EN HTML/JS/CSS (${unused.length}) ==`);
  unused.slice(0, 40).forEach(f => console.log(`  ${f}`));
  if (unused.length > 40) console.log(`  ... +${unused.length - 40}`);
}
