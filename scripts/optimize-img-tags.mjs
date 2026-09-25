import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import sharp from 'sharp';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const rootDir = path.resolve(__dirname, '..');

const DRY = process.argv.includes('--dry');
const SKIP_DIRS = new Set(['dist', 'node_modules', '.git', '.vite']);

const cache = new Map(); // ruta absoluta -> {w,h} | null
async function dims(absPath) {
  if (cache.has(absPath)) return cache.get(absPath);
  let v = null;
  try {
    if (fs.existsSync(absPath) && /\.(jpe?g|png|webp|gif|avif)$/i.test(absPath)) {
      const m = await sharp(absPath, { failOn: 'none' }).metadata();
      if (m.width && m.height) v = { w: m.width, h: m.height };
    }
  } catch { /* no legible */ }
  cache.set(absPath, v);
  return v;
}

function walk(dir, out = []) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    if (e.isDirectory()) { if (!SKIP_DIRS.has(e.name)) walk(path.join(dir, e.name), out); continue; }
    if (e.name.endsWith('.html')) out.push(path.join(dir, e.name));
  }
  return out;
}

function resolveSrc(htmlFile, src) {
  if (!src) return null;
  if (/^(https?:)?\/\//i.test(src)) {
    const u = src.replace(/^https?:\/\/[^/]+/i, '');
    return path.join(rootDir, decodeURIComponent(u.replace(/^\//, '')));
  }
  if (src.startsWith('/')) return path.join(rootDir, decodeURIComponent(src.slice(1)));
  return path.join(path.dirname(htmlFile), decodeURIComponent(src));
}

function attr(tag, name) {
  const m = tag.match(new RegExp(`\\s${name}="([^"]*)"`, 'i'));
  return m ? m[1] : null;
}

function firstSourceFile(html, pictureStart) {
  const seg = html.slice(pictureStart);
  const m = seg.match(/<source\b[^>]*>/i);
  if (!m) return null;
  const tag = m[0];
  const s = attr(tag, 'src') || (attr(tag, 'srcset') || '').split(',')[0].trim().split(/\s+/)[0];
  return s || null;
}

function inHeader(html, idx) {
  const before = html.lastIndexOf('<header', idx);
  if (before === -1) return false;
  const close = html.indexOf('</header>', before);
  return close === -1 || idx < close;
}

let filesChanged = 0, imgsLazy = 0, imgsDim = 0, imgsSkip = 0, imgsErr = 0;
const report = [];

for (const file of walk(rootDir)) {
  const rawBuf = fs.readFileSync(file);
  const hasBom = rawBuf.length > 2 && rawBuf[0] === 0xef && rawBuf[1] === 0xbb && rawBuf[2] === 0xbf;
  const html = rawBuf.toString('utf8').replace(/^\uFEFF/, '');
  if (!/<img\b/i.test(html)) continue;

  const preloads = new Set();
  for (const m of html.matchAll(/<link\b[^>]*rel="preload"[^>]*>/gi)) {
    const h = attr(m[0], 'href');
    if (h && attr(m[0], 'as') === 'image') preloads.add(path.basename(h.split('?')[0]).toLowerCase());
  }

  const rel = path.relative(rootDir, file);
  const adds = [];

  for (const m of html.matchAll(/<img\b[^>]*>/gi)) {
    const tag = m[0];
    const idx = m.index;
    if (/\bloading=/i.test(tag)) continue;

    const style = attr(tag, 'style') || '';
    const src = attr(tag, 'src');
    const widthA = attr(tag, 'width'), heightA = attr(tag, 'height');

    if (/display\s*:\s*none/i.test(style) || (widthA === '1' && heightA === '1')) { imgsSkip++; continue; }

    const base = src ? path.basename(src.split('?')[0]).toLowerCase() : '';

    // <picture>: las fuentes tambien cuentan para decidir prioridad
    const picStart = html.lastIndexOf('<picture', idx);
    const picEnd = picStart !== -1 ? html.indexOf('</picture>', picStart) : -1;
    const inPic = picStart !== -1 && picEnd > idx;
    const picBases = [];
    if (inPic) {
      const picHtml = html.slice(picStart, picEnd);
      for (const s of picHtml.matchAll(/<source\b[^>]*>/gi)) {
        const direct = attr(s[0], 'src');
        const set = attr(s[0], 'srcset');
        const urls = [];
        if (direct) urls.push(direct);
        if (set) set.split(',').forEach(p => urls.push(p.trim().split(/\s+/)[0]));
        for (const u of urls) if (u) picBases.push(path.basename(u.split('?')[0]).toLowerCase());
      }
    }

    const prioritized = preloads.has(base) || picBases.some(b => preloads.has(b))
      || /\bfetchpriority=/i.test(tag) || inHeader(html, idx);

    const preloaded = preloads.has(base) || picBases.some(b => preloads.has(b));
    const keepEager = preloaded || /\bfetchpriority=/i.test(tag) || inHeader(html, idx);

    let out = tag;
    const open = () => out.replace(/>$/, '').replace(/\s*$/, '');
    if (keepEager) {
      // imagen criticada por preload/header: mantener eager; solo reforzar prioridad
      if (preloaded && !/\bfetchpriority=/i.test(out)) {
        out = open() + ' fetchpriority="high">';
        imgsLazy++;
      }
    } else {
      out = open() + ' loading="lazy" decoding="async">';
      imgsLazy++;
    }

    if (!widthA && !heightA) {
      // dentro de <picture>: usar el <source> como referencia de aspecto
      let probe = src;
      if (inPic) probe = firstSourceFile(html, picStart) || src;

      const probePath = resolveSrc(file, probe);
      const d1 = probePath ? await dims(probePath) : null;
      const srcPath = resolveSrc(file, src);
      const d2 = srcPath ? await dims(srcPath) : null;

      const use = d1 || d2;
      if (use) {
        // solo si el aspecto del source y del img coinciden
        if (!d1 || !d2 || Math.abs(d1.w / d1.h - d2.w / d2.h) < 0.02) {
          out = open() + ` width="${use.w}" height="${use.h}">`;
          imgsDim++;
        } else { imgsSkip++; }
      }
    }

    if (out !== tag) adds.push([tag, out]);
  }

  if (!adds.length) continue;
  let newHtml = html;
  for (const [from, to] of adds) newHtml = newHtml.replace(from, to);

  report.push(`  ${rel}: ${adds.length} img`);
  filesChanged++;
  if (!DRY) {
    const out = (hasBom ? Buffer.from([0xef, 0xbb, 0xbf]) : Buffer.concat([Buffer.alloc(0)]));
    fs.writeFileSync(file, Buffer.concat([out, Buffer.from(newHtml, 'utf8')]));
  }
}

console.log(`modo: ${DRY ? 'DRY-RUN' : 'ejecutar'}`);
console.log(`archivos modificados: ${filesChanged}`);
console.log(`img con prioridad/lazy anadido: ${imgsLazy}  |  con width/height: ${imgsDim}  |  omitidas: ${imgsSkip}`);
report.slice(0, 25).forEach(r => console.log(r));
if (report.length > 25) console.log(`  ... +${report.length - 25} archivos`);
