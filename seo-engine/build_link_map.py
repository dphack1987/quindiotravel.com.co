#!/usr/bin/env python3
"""Genera el mapa de enlazado contextual para Quindío Travel.

Lee todas las páginas HTML indexables, extrae entidades (destinos,
atractivos, alojamientos, temas) desde la data maestra y genera
seo-engine/data/related-links-map.json: página -> [páginas relacionadas].

Lo consume assets/js/related-links.js para inyectar el bloque
"Te puede interesar" en cada página.

Uso: python seo-engine/build_link_map.py
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "pseo-engine" / "pseo-master-data.json"
OUT = ROOT / "seo-engine" / "data" / "related-links-map.json"

SKIP_DIRS = {
    "node_modules", "dist", ".git", "tests", "scripts", "docs",
    "components", "competitive-engine", "pseo-engine", "seo-engine",
    "lead_automation_system", "don-chucho-backend", "directories_data",
    "outreach_data", "social_media_content", "datos",
    "documentation_archive", "backup-microdata-20260930-102216",
    "_redirects-pSEO", "generated-pages",
    "en", "zh",
}
EXCLUDE_FILES = {"404.html", "500.html", "gracias.html",
                 "auditoria_seo_quindio_travel.html"}


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def load_entities() -> dict[str, list[tuple[str, str]]]:
    """Devuelve {entidad_lower: [(slug_pagina, etiqueta)]} por categoría."""
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    ents: dict[str, list[tuple[str, str]]] = {}

    for m in data.get("municipios", []):
        ents.setdefault(strip_accents(m["nombre"].lower()), []).append(
            (m["slug"] + ".html", m["nombre"]))
        ents.setdefault(strip_accents(m["nombre"].lower() + " hotel"), []).append(
            (m["slug"] + ".html", f"Hoteles en {m['nombre']}"))

    for a in data.get("atractivos", []):
        ents.setdefault(strip_accents(a["nombre"].lower()), []).append(
            (a["slug"] + ".html", a["nombre"]))

    for al in data.get("alojamientos", []):
        ents.setdefault(strip_accents(al["nombre"].lower()), []).append(
            (al["slug"] + ".html", al["nombre"]))

    for t in data.get("tiposViaje", []):
        ents.setdefault(strip_accents(t["nombre"].lower()), []).append(
            ("planes-" + t["slug"].replace("viajes-", "") + "-quindio.html",
             t["nombre"]))

    # Temas transversales del sitio (solo matchean en filename/title,
    # no en cuerpo — si no, el footer los menciona en todas las páginas)
    temas = {
        "blog": [("blog.html", "Blog de viajes")],
        "planes": [("planes.html", "Todos los planes"),
                   ("comparar-planes.html", "Comparar planes")],
        "diciembre": [("planes-especiales-diciembre-2026.html",
                       "Planes especiales diciembre"),
                      ("promo-noviembre-2026.html", "Promoción vigente")],
        "salento": [("salento.html", "Guía de Salento")],
        "filandia": [("filandia.html", "Guía de Filandia")],
        "armenia": [("armenia.html", "Guía de Armenia")],
        "cocora": [("valle-de-cocora.html", "Valle de Cocora")],
        "panaca": [("panaca.html", "PANACA")],
        "termales": [("termales-santa-rosa.html", "Termales Santa Rosa")],
        "recuca": [("recuca.html", "RECUCA")],
        "mariposario": [("mariposario-quindio.html", "Mariposario")],
        "parque-cafe": [("parque-del-cafe.html", "Parque del Café")],
        "hoteles": [("alojamientos.html", "Alojamientos"),
                    ("finca-hoteles-en-el-quindio.html", "Fincas hoteles")],
        "familia": [("planes-familiares-quindio.html", "Planes familiares")],
        "parejas": [("planes-romanticos-para-parejas.html", "Planes románticos")],
        "grupos": [("planes-grupos-amigos-quindio.html", "Planes para grupos")],
        "whatsapp": [("cotizador-simplificado.html", "Cotizador")],
    }
    for k, v in temas.items():
        ents.setdefault("__temas__", {})[k] = v

    # Páginas pSEO actualizadas a calidad indexable (upgrade_pseo.py):
    # se registran como destinos por palabra clave temática para recibir
    # enlaces internos contextuales desde el resto del sitio.
    pseo_dest = {
        "cocora caminata": "programmatic-pages/valle-cocora-caminata-2026.html",
        "caminata cocora": "programmatic-pages/valle-cocora-caminata-2026.html",
        "cocora un dia": "programmatic-pages/valle-cocora-una-dia-2026.html",
        "cocora 1 dia": "programmatic-pages/valle-cocora-una-dia-2026.html",
        "cerro murillo": "programmatic-pages/valle-cocora-cerro-murillo-2026.html",
        "murillo": "programmatic-pages/valle-cocora-cerro-murillo-2026.html",
        "cocora aves": "programmatic-pages/valle-cocora-pajaros-2026.html",
        "cocora birdwatching": "programmatic-pages/valle-cocora-pajaros-2026.html",
        "aves cocora": "programmatic-pages/valle-cocora-pajaros-2026.html",
        "caminata nocturna cocora": "programmatic-pages/caminata-nocturna-valle-cocora-2026.html",
        "cocora nocturna": "programmatic-pages/caminata-nocturna-valle-cocora-2026.html",
        "cocora albergue": "programmatic-pages/valle-cocora-alberque-2026.html",
        "dormir cocora": "programmatic-pages/valle-cocora-alberque-2026.html",
        "salento bogota": "programmatic-pages/tour-salento-desde-bogota-2026.html",
        "salento desde bogota": "programmatic-pages/tour-salento-desde-bogota-2026.html",
        "tour privado salento": "programmatic-pages/tour-privado-salento-2026.html",
        "miradores salento": "programmatic-pages/miradores-salento-2026.html",
        "mirador filandia": "programmatic-pages/mirador-filandia-360-grados-2026.html",
        "filandia 360": "programmatic-pages/mirador-filandia-360-grados-2026.html",
        "miradores filandia": "programmatic-pages/mejores-miradores-filandia-2026.html",
        "guirrera": "programmatic-pages/visita-guirrera-salento-2026.html",
        "transporte barato eje": "programmatic-pages/transporte-barato-eje-cafetero-2026.html",
        "transporte barato": "programmatic-pages/transporte-barato-eje-cafetero-2026.html",
        "transporte colectivo eje": "programmatic-pages/transporte-colectivo-eje-cafetero-2026.html",
        "taxi eje cafetero": "programmatic-pages/transporte-taxi-eje-cafetero-2026.html",
        "taxi quindio": "programmatic-pages/transporte-taxi-eje-cafetero-2026.html",
        "tour sin transporte": "programmatic-pages/tour-eje-cafetero-sin-transporte-2026.html",
        "vuelo armenia": "programmatic-pages/vuelo-barato-armenia-2026.html",
        "vuelo a armenia": "programmatic-pages/vuelo-barato-armenia-2026.html",
        "vuelos armenia": "programmatic-pages/vuelo-barato-armenia-2026.html",
        "hotel familiar salento": "programmatic-pages/hoteles-familiares-salento-2026.html",
        "hoteles familiares salento": "programmatic-pages/hoteles-familiares-salento-2026.html",
        "hotel pet friendly salento": "programmatic-pages/hoteles-pet-friendly-salento-2026.html",
        "pet friendly salento": "programmatic-pages/hoteles-pet-friendly-salento-2026.html",
        "hotel 4 estrellas salento": "programmatic-pages/hoteles-4-estrellas-salento-2026.html",
        "hotel boutique quindio": "programmatic-pages/hoteles-boutique-quindio-2026.html",
        "hoteles boutique quindio": "programmatic-pages/hoteles-boutique-quindio-2026.html",
        "hotel campestre eje cafetero": "programmatic-pages/hoteles-campestres-eje-cafetero-2026.html",
        "hoteles campestres eje": "programmatic-pages/hoteles-campestres-eje-cafetero-2026.html",
        "alojamiento economico salento": "programmatic-pages/alojamiento-economico-salento-2026.html",
        "donde dormir barato salento": "programmatic-pages/alojamiento-economico-salento-2026.html",
        "fiestas diciembre quindio": "programmatic-pages/fiestas-diciembre-quindio-2026.html",
        "navidad quindio": "programmatic-pages/fiestas-diciembre-quindio-2026.html",
        "diciembre eje cafetero": "programmatic-pages/fiestas-diciembre-quindio-2026.html",
        "presupuesto viaje eje cafetero": "programmatic-pages/presupuesto-viaje-eje-cafetero-2026.html",
        "cuanto cuesta viaje eje cafetero": "programmatic-pages/presupuesto-viaje-eje-cafetero-2026.html",
        "viaje familiar quindio ninos": "programmatic-pages/viaje-familiar-quindio-ninos-2026.html",
        "quindio con ninos": "programmatic-pages/viaje-familiar-quindio-ninos-2026.html",
        "comida tipica quindio": "programmatic-pages/comida-tipica-quindio-2026.html",
        "gastronomia quindio": "programmatic-pages/comida-tipica-quindio-2026.html",
        "senderismo avanzado quindio": "programmatic-pages/senderismo-avanzado-quindio-2026.html",
        "senderismo quindio": "programmatic-pages/senderismo-avanzado-quindio-2026.html",
        "birdwatching eje cafetero": "programmatic-pages/birdwatching-eje-cafetero-2026.html",
        "observacion de aves eje": "programmatic-pages/birdwatching-eje-cafetero-2026.html",
        "luna de miel eje cafetero": "programmatic-pages/luna-de-miel-eje-cafetero-2026.html",
        "luna de miel quindio": "programmatic-pages/luna-de-miel-eje-cafetero-2026.html",
        "plan romantico quindio": "programmatic-pages/luna-de-miel-eje-cafetero-2026.html",
    }
    for key, slug in pseo_dest.items():
        fname = Path(slug).name
        # Etiqueta legible desde el slug
        label = fname.replace("-2026.html", "").replace("-", " ").title()
        ents.setdefault(key, []).append((slug, label))

    return ents


class TitleGrabber(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self._t = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._t = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._t = False

    def handle_data(self, d):
        if self._t:
            self.title += d


def is_indexable(path: Path) -> bool:
    if path.name in EXCLUDE_FILES:
        return False
    try:
        raw = path.read_bytes()
    except OSError:
        return False
    # Stubs de redirección pSEO (~800 bytes) y páginas casi vacías
    if len(raw) < 2500:
        return False
    head = raw.decode("utf-8", errors="replace")[:8000]
    if 'name="robots" content="noindex' in head:
        return False
    if "Redirigiendo a" in head[:3000]:
        return False
    return True


def main() -> None:
    ents = load_entities()
    temas_map = ents.pop("__temas__", {})
    pages: dict[str, dict] = {}

    for p in sorted(ROOT.rglob("*.html")):
        rel_parts = p.relative_to(ROOT).parts
        if any(part in SKIP_DIRS for part in rel_parts[:-1]):
            continue
        if not is_indexable(p):
            continue
        rel = str(p.relative_to(ROOT)).replace("\\", "/")
        html = p.read_text(encoding="utf-8", errors="replace")
        tg = TitleGrabber()
        tg.feed(html)
        title = re.sub(r"\s+", " ", tg.title).strip()

        # Prioridad 1: entidades en filename + title (señal fuerte de tema)
        hay_strong = strip_accents((rel + " " + title).lower())
        # Prioridad 2: entidades en el cuerpo (señal débil)
        hay_body = strip_accents(html[:40000].lower())

        matched: dict[str, tuple[int, str]] = {}  # slug -> (prioridad, etiqueta)

        def add_matches(ent_map: dict, hay: str, prio: int):
            for key, targets in ent_map.items():
                if not re.search(r"(?<![a-z0-9])" + re.escape(key) +
                                 r"(?![a-z0-9])", hay):
                    continue
                for slug, label in targets:
                    if slug == rel:
                        continue
                    if slug not in matched or matched[slug][0] > prio:
                        matched[slug] = (prio, label)

        # Fuertes (filename+title): entidades específicas + temas
        add_matches(ents, hay_strong, 1)
        add_matches(temas_map, hay_strong, 1)
        # Debiles (cuerpo): solo entidades específicas del master data
        add_matches(ents, hay_body, 2)

        # Ordenar: primero matches fuertes, luego alfabético; máx 6
        ordered = sorted(matched.items(), key=lambda kv: (kv[1][0], kv[0]))
        pages[rel] = {"title": title[:110],
                      "related": {s: l for s, (p_, l) in ordered}}

    # Convertir a formato JS: { "pagina.html": [["destino.html","Etiqueta"],...] }
    link_map = {}
    for rel, info in pages.items():
        rels = []
        for slug, label in list(info["related"].items())[:8]:
            dest = slug
            if dest not in pages and dest.endswith(".html"):
                alt = dest.replace(".html", "/index.html")
                if alt in pages:
                    dest = alt
            if dest in pages and dest != rel:
                rels.append([dest, label])
        if rels:
            link_map[rel] = rels[:6]

    OUT.write_text(json.dumps(link_map, ensure_ascii=False, indent=1),
                   encoding="utf-8")
    con_rel = sum(1 for v in link_map.values() if v)
    print(f"Páginas indexables: {len(pages)} | Con relacionadas: {con_rel}")
    print(f"Mapa: {OUT}")


if __name__ == "__main__":
    sys.exit(main())
