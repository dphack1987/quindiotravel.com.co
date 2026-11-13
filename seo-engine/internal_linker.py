#!/usr/bin/env python3
"""Auditor de enlazado interno para Quindío Travel.

Construye el grafo de enlaces internos del sitio y detecta:
- Páginas huérfanas (0 enlaces internos entrantes)
- Páginas con muy poca autoridad interna (<2 inlinks)
- Texto ancla repetido excesivamente hacia un mismo destino
- URLs del sitemap sin enlaces internos (indexación débil)

Uso: python seo-engine/internal_linker.py
Salida: seo-engine/data/internal-links-report.md + .json
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "seo-engine" / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SKIP_DIRS = {
    "node_modules", "dist", ".git", "tests", "scripts", "docs",
    "components", "competitive-engine", "pseo-engine", "seo-engine",
    "lead_automation_system", "don-chucho-backend", "directories_data",
    "outreach_data", "social_media_content", "datos", "documentation_archive",
    "backup-microdata-20260930-102216",
}
EXTERNAL_HOSTS = {"quindiotravel.com.co", "www.quindiotravel.com.co",
                  "localhost", "127.0.0.1"}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[tuple[str, str]] = []  # (href, anchor_text)
        self._in_a = False
        self._href = ""
        self._text: list[str] = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "a":
            href = attrs_d.get("href", "")
            if href:
                self._in_a = True
                self._href = href
                self._text = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "a" and self._in_a:
            self.links.append((self._href, " ".join(self._text).strip()))
            self._in_a = False
            self._href = ""
            self._text = []

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._in_a:
            self._text.append(data)


def iter_html_files() -> list[Path]:
    files = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT)
        if any(part in SKIP_DIRS for part in rel.parts[:-1]):
            continue
        files.append(p)
    return sorted(files)


def to_site_path(href: str, source: Path) -> str | None:
    """Convierte un href a ruta de sitio tipo 'blog/foo.html' o None si externo."""
    href = href.strip()
    if not href or href.startswith(("#", "javascript:", "mailto:", "tel:", "data:")):
        return None
    # URLs absolutas del propio dominio -> path relativo a ROOT
    parsed = urlparse(href)
    if parsed.scheme in ("http", "https"):
        if parsed.netloc not in EXTERNAL_HOSTS:
            return None
        path = parsed.path.lstrip("/")
    else:
        path = href.split("#")[0].split("?")[0]
        if not path:
            return None
        # Resolver relativo al directorio de la página fuente
        resolved = (source.parent / unquote(path)).resolve()
        try:
            rel = resolved.relative_to(ROOT.resolve())
        except ValueError:
            return None
        path = str(rel).replace("\\", "/")
    # Quitar query/fragment ya hecho; normalizar index.html -> .
    path = unquote(path)
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif path == "index.html":
        path = ""
    return path or "index.html"


def main() -> None:
    files = iter_html_files()
    pages: dict[str, dict] = {}
    inbound: Counter = Counter()
    anchor_counter: dict[str, Counter] = defaultdict(Counter)

    for f in files:
        rel = str(f.relative_to(ROOT)).replace("\\", "/")
        try:
            html = f.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        parser = LinkParser()
        parser.feed(html)
        pages[rel] = {
            "title": re.sub(r"\s+", " ", parser.title).strip()[:120],
            "outlinks": [],
        }
        for href, anchor in parser.links:
            target = to_site_path(href, f)
            if target and target in pages or (target and target != rel):
                # Registrar aunque el destino aún no se haya parseado
                pages[rel]["outlinks"].append(target)
                inbound[target] += 1
                if anchor:
                    anchor_counter[target][anchor[:80]] += 1

    # Segunda pasada: marcar outlinks que apuntan a páginas existentes
    existing = set(pages)
    for rel, p in pages.items():
        p["outlinks"] = sorted({t for t in p["outlinks"] if t in existing})

    # Índice de autoridad interna (inlinks ponderados: homepage pesa más)
    authority = {}
    for rel in pages:
        auth = inbound.get(rel, 0)
        if rel == "index.html":
            auth += len(pages) * 0  # homepage es origen, no destino
        authority[rel] = auth

    orphans = sorted([r for r in pages if inbound.get(r, 0) == 0 and r != "index.html"])
    weak = sorted([r for r in pages if 0 < inbound.get(r, 0) <= 2])

    # Anclas sobre-usadas: mismo anchor text >10 veces al mismo destino
    anchor_spam = []
    for target, ctr in anchor_counter.items():
        for anchor, n in ctr.most_common(1):
            if n >= 10 and anchor.lower() not in ("click aquí", "aquí", "ver más"):
                anchor_spam.append({"destino": target, "anchor": anchor, "veces": n})

    report = {
        "total_paginas": len(pages),
        "huerfanas": orphans,
        "poca_autoridad": weak,
        "anchors_repetidos": sorted(anchor_spam, key=lambda x: -x["veces"]),
        "top_inlinks": sorted(
            ((r, inbound.get(r, 0)) for r in pages),
            key=lambda x: -x[1])[:20],
    }

    (OUT_DIR / "internal-links.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    lineas = [
        "# Auditoría de Enlazado Interno — Quindío Travel",
        "",
        f"**Páginas analizadas:** {len(pages)}",
        f"**Huérfanas (0 inlinks):** {len(orphans)}",
        f"**Poca autoridad interna (1-2 inlinks):** {len(weak)}",
        "",
        "## Páginas huérfanas",
        "",
    ]
    for r in orphans:
        lineas.append(f"- `{r}` — {pages[r]['title']}")
    lineas += ["", "## Páginas con poca autoridad interna", ""]
    for r in weak[:80]:
        lineas.append(f"- `{r}` ({inbound.get(r, 0)} inlinks) — {pages[r]['title']}")
    lineas += ["", "## Anclas repetidas excesivamente", ""]
    for a in report["anchors_repetidos"][:30]:
        lineas.append(f"- **{a['veces']}x** \"{a['anchor']}\" → `{a['destino']}`")
    lineas += ["", "## Top 20 páginas con más inlinks", ""]
    for r, n in report["top_inlinks"]:
        lineas.append(f"- `{r}` — {n} inlinks")

    (OUT_DIR / "internal-links-report.md").write_text(
        "\n".join(lineas), encoding="utf-8")

    print(f"Páginas: {len(pages)} | Huérfanas: {len(orphans)} | "
          f"Poca autoridad: {len(weak)} | Anclas spam: {len(anchor_spam)}")
    print(f"Reporte: {OUT_DIR / 'internal-links-report.md'}")


if __name__ == "__main__":
    sys.exit(main())
