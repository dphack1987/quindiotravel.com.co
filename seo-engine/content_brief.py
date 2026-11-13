#!/usr/bin/env python3
"""Genera briefs de contenido para keywords sin página asignada.

Lee seo-engine/data/keyword-map.json, filtra keywords de alta prioridad
sin `paginas_sugeridas`, deduplica variantes (orden de palabras), y
produce seo-engine/data/content-briefs.md con briefs listos para redactar:
título, meta description, H1, estructura H2, entidades/precios del master
data, enlaces internos sugeridos y CTA.

Uso: python seo-engine/content_brief.py [--top 40] [--min-score 80]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KMAP = ROOT / "seo-engine" / "data" / "keyword-map.json"
MASTER = ROOT / "pseo-engine" / "pseo-master-data.json"
OUT = ROOT / "seo-engine" / "data" / "content-briefs.md"


def strip_accents(s: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", s)
                   if unicodedata.category(c) != "Mn")


def norm_words(kw: str) -> tuple[str, ...]:
    """Normaliza keyword a tupla de palabras ordenadas (dedupe de variantes)."""
    words = [w for w in re.findall(r"[a-z0-9]+", strip_accents(kw.lower()))
             if w not in {"el", "la", "los", "las", "de", "del", "en", "y",
                          "a", "para", "con", "por", "un", "una", "al"}]
    return tuple(sorted(set(words)))


def slugify(kw: str) -> str:
    s = strip_accents(kw.lower())
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)


def load_master() -> dict:
    """Mapa nombre-entidad (sin acentos) -> datos útiles."""
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    ent: dict[str, dict] = {}
    for m in data.get("municipios", []):
        ent[strip_accents(m["nombre"].lower())] = {
            "tipo": "municipio", "slug": m["slug"], "nombre": m["nombre"]}
    for a in data.get("atractivos", []):
        ent[strip_accents(a["nombre"].lower())] = {
            "tipo": "atractivo", "slug": a["slug"], "nombre": a["nombre"],
            "precio": a.get("precio")}
    for al in data.get("alojamientos", []):
        ent[strip_accents(al["nombre"].lower())] = {
            "tipo": "alojamiento", "slug": al["slug"], "nombre": al["nombre"],
            "precio": al.get("precio_desde") or al.get("precio")}
    for t in data.get("tiposViaje", []):
        ent[strip_accents(t["nombre"].lower())] = {
            "tipo": "tipoViaje", "slug": t["slug"], "nombre": t["nombre"]}
    for am in data.get("amenidades", []):
        nombre = am.get("nombre") or am.get("name") or ""
        if nombre:
            ent[strip_accents(nombre.lower())] = {
                "tipo": "amenidad", "slug": am.get("slug", ""),
                "nombre": nombre}
    return ent


def entity_hits(keyword: str, entidades: list, master: dict) -> list[dict]:
    hits = []
    for e in entidades:
        key = strip_accents(e.lower())
        if key in master:
            hits.append(master[key])
    return hits


def intent_label(intent_list: list) -> str:
    order = ["comercial", "transaccional", "temporada", "informacional"]
    for i in order:
        if i in intent_list:
            return i
    return intent_list[0] if intent_list else "general"


def h2_outline(intent: str, ents: list[dict]) -> list[str]:
    base = [
        "Qué es y por qué vale la pena",
        "Cómo llegar y mejor época para visitar",
        "Qué incluye y precios de referencia",
        "Itinerario sugerido paso a paso",
        "Consejos prácticos de operadores locales",
        "Preguntas frecuentes",
    ]
    if intent == "temporada":
        base[1] = "Fechas, clima y temporada alta"
        base.insert(2, "Qué pasa en diciembre y fin de año")
    if ents and ents[0]["tipo"] == "atractivo":
        base[0] = f"Qué es {ents[0]['nombre']} y qué lo hace único"
    return base


def internal_links(ents: list[dict], kw: str) -> list[str]:
    links = ["planes.html", "blog.html"]
    for e in ents:
        if e["tipo"] == "municipio":
            links.append(f"{e['slug']}.html")
        elif e["tipo"] == "atractivo":
            links.append(f"{e['slug']}.html")
    links.append("planes-especiales-diciembre-2026.html")
    # dedupe preservando orden
    seen, out = set(), []
    for l in links:
        if l not in seen:
            seen.add(l)
            out.append(l)
    return out[:6]


SMALL = {"de", "del", "la", "el", "los", "las", "en", "y", "a", "al",
         "con", "por", "para", "un", "una", "e"}


def kw_title(kw: str) -> str:
    """Title-case respetando preposiciones/artículos en minúscula."""
    words = kw.split()
    out = []
    for i, w in enumerate(words):
        lw = w.lower()
        if i > 0 and lw in SMALL:
            out.append(lw)
        else:
            out.append(lw.capitalize())
    return " ".join(out)


def build_brief(kw_item: dict, master: dict) -> str:
    kw = kw_item["keyword"]
    kt = kw_title(kw)
    ents = entity_hits(kw, kw_item.get("entidades", []), master)
    intent = intent_label(kw_item.get("intenciones", []))
    slug = slugify(kw)
    title = f"{kt} 2026 | Guía Completa | Quindío Travel"[:65]
    desc = (f"Todo sobre {kt} en el Quindío: cómo llegar, qué hacer, "
            f"precios reales y consejos de operadores locales RNT 18152.")[:155]
    links = internal_links(ents, kw)

    ent_lines = ""
    if ents:
        for e in ents:
            extra = f" — desde ${e['precio']:,}".replace(",", ".") \
                if e.get("precio") else ""
            ent_lines += f"- **{e['nombre']}** ({e['tipo']}){extra}\n"
    else:
        ent_lines = "- Sin entidad maestra asociada: investigar datos propios antes de publicar.\n"

    return f"""### {kw}

| Campo | Valor |
|---|---|
| **Keyword** | `{kw}` |
| **Intención** | {intent} (score {kw_item['score']}) |
| **URL sugerida** | `programmatic-pages/{slug}-2026.html` |
| **Title** | {title} |
| **Meta description** | {desc} |
| **H1** | {kt} en el Quindío: guía 2026 |

**Entidades (master data):**
{ent_lines}
**Estructura H2:**
""" + "\n".join(f"{i+1}. {h}" for i, h in enumerate(h2_outline(intent, ents))) + f"""

**Enlaces internos sugeridos:** {', '.join(f'`{l}`' for l in links)}
**CTA:** WhatsApp con mensaje "Hola Quindío Travel, me interesa {kw}"
**Checklist:** precio real verificado · foto propia o con licencia · FAQ con 4+ preguntas · canonical propio · `index,follow`
"""


SEASON_WORDS = {"fin", "ano", "nuevo", "diciembre", "navidad", "navideno",
                "navidena", "navidenas", "puente", "temporada", "festivo",
                "christmas", "holiday", "vacaciones", "finde"}

# Preferencia de keyword representativa dentro del mismo grupo
KW_PREFERENCE = ["diciembre", "navidad", "fin de ano", "ano nuevo",
                 "temporada", "vacaciones"]


def group_key(kw: str, intent: str) -> tuple:
    """Agrupa variantes estacionales del mismo tema: quita palabras de
    temporada para no generar páginas que se canibalicen entre sí."""
    words = [w for w in re.findall(r"[a-z0-9]+", strip_accents(kw.lower()))
             if w not in {"el", "la", "los", "las", "de", "del", "en", "y",
                          "a", "para", "con", "por", "un", "una", "al"}
             and w not in SEASON_WORDS]
    return (tuple(sorted(set(words))), intent_label(intent))


def kw_rank(kw: str) -> int:
    k = " " + strip_accents(kw.lower()) + " "
    for i, pref in enumerate(KW_PREFERENCE):
        if pref in k:
            return i
    return len(KW_PREFERENCE)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=40)
    ap.add_argument("--min-score", type=float, default=80)
    args = ap.parse_args()

    km = json.loads(KMAP.read_text(encoding="utf-8"))
    master = load_master()

    # Keywords sin página, score mínimo; dedupe por set de palabras y
    # luego por grupo entidad+intención (colapsa variantes de temporada)
    seen: dict[tuple, dict] = {}
    for k in km["keywords"]:
        if k.get("paginas_sugeridas"):
            continue
        if k["score"] < args.min_score:
            continue
        # Descartar keywords que solo combinan amenidades + temporada
        # ("wifi fin de ano", "gatos diciembre"): no sostienen página de calidad
        ents = k.get("entidades", [])
        if ents and all(
                strip_accents(e.lower()) in master
                and master[strip_accents(e.lower())]["tipo"] == "amenidad"
                for e in ents):
            continue
        key = norm_words(k["keyword"])
        if not key:
            continue
        if key not in seen or k["score"] > seen[key]["score"]:
            seen[key] = k

    groups: dict[tuple, dict] = {}
    for k in seen.values():
        gk = group_key(k["keyword"], k.get("intenciones", []))
        cur = groups.get(gk)
        if (cur is None
                or k["score"] > cur["score"]
                or (k["score"] == cur["score"]
                    and kw_rank(k["keyword"]) < kw_rank(cur["keyword"]))):
            groups[gk] = k

    briefed = sorted(groups.values(), key=lambda x: -x["score"])[:args.top]

    header = f"""# Content Briefs — Keywords sin página ({len(briefed)} grupos únicos con score ≥ {args.min_score})

Generado por `seo-engine/content_brief.py`. Cada brief es la base para una
página indexable de calidad (ver checklist al final de cada uno).

"""
    body = "\n---\n\n".join(build_brief(k, master) for k in briefed)
    OUT.write_text(header + body, encoding="utf-8")
    print(f"Briefs generados: {len(briefed)} (únicas: {len(seen)})")
    print(f"Salida: {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
