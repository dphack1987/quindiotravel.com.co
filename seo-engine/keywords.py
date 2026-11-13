#!/usr/bin/env python3
"""Motor de keywords para Quindío Travel.

Expande la data maestra (pseo-master-data.json) en un universo de keywords
clasificadas por intención de búsqueda, con prioridad para la temporada
navideña. Salida: seo-engine/data/keyword-map.json + reporte Markdown.

Uso: python seo-engine/keywords.py
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MASTER = ROOT / "pseo-engine" / "pseo-master-data.json"
OUT_DIR = ROOT / "seo-engine" / "data"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# Modificadores por intención de búsqueda (es-CO, mercado turístico local)
# ---------------------------------------------------------------------------
INTENTS = {
    "transaccional": [
        "comprar", "reservar", "cotizar", "contratar", "agendar",
        "paquete turistico", "plan turistico", "tour", "excursion",
        "salida grupal", "cupos", "disponibilidad",
    ],
    "comercial": [
        "mejores", "top", "recomendados", "baratos", "economicos",
        "precio", "precios", "costo", "cuanto cuesta", "desde",
        "ofertas", "promociones", "descuentos", "promo", "last minute",
    ],
    "informacional": [
        "guia", "todo sobre", "que hacer", "que visitar", "como llegar",
        "como ir", "requisitos", "documentos", "que llevar", "clima",
        "mejor epoca", "temporada", "duracion", "itinerario",
    ],
    "navegacional": [
        "quindio travel", "hoteles en", "alojamiento en", "donde dormir",
        "fincas", "cabanas", "hostales",
    ],
    "temporada": [
        "diciembre", "navidad", "ano nuevo", "fin de ano", "vacaciones",
        "puente", "semana santa", "julio", "agosto", "octubre", "noviembre",
        "temporada alta", "temporada baja",
    ],
}

# Prioridad estacional: diciembre pesa más (temporada alta de reservas)
SEASONAL_WEIGHT = {
    "diciembre": 3.0, "navidad": 3.0, "ano nuevo": 3.0, "fin de ano": 3.0,
    "vacaciones": 2.0, "puente": 2.0, "temporada alta": 2.0,
}

STOPWORDS = {
    "en", "el", "la", "los", "las", "de", "del", "al", "un", "una",
    "y", "o", "para", "por", "con", "sin", "que", "como", "cual",
}


def norm(text: str) -> str:
    """Normaliza texto a slug-ish para deduplicar keywords."""
    t = text.lower().strip()
    t = re.sub(r"[^a-z0-9áéíóúñü ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def load_entities() -> dict:
    data = json.loads(MASTER.read_text(encoding="utf-8"))
    ents: dict[str, list[str]] = defaultdict(list)
    ents_meta: dict[str, dict] = {}

    for m in data.get("municipios", []):
        ents["destino"].append(m["nombre"])
        ents_meta[m["nombre"]] = {"tipo": "municipio", "slug": m["slug"],
                                  "keywords": m.get("keywords", [])}

    for a in data.get("atractivos", []):
        ents["atractivo"].append(a["nombre"])
        ents_meta[a["nombre"]] = {"tipo": "atractivo", "slug": a["slug"],
                                  "municipio": a.get("municipio"),
                                  "keywords": a.get("keywords", [])}

    for al in data.get("alojamientos", []):
        ents["alojamiento"].append(al["nombre"])
        ents_meta[al["nombre"]] = {"tipo": "alojamiento", "slug": al["slug"],
                                  "keywords": [al["nombre"].lower()]}

    for t in data.get("tiposViaje", []):
        ents["tipo"].append(t["nombre"])
        ents_meta[t["nombre"]] = {"tipo": "viaje", "slug": t["slug"],
                                  "keywords": t.get("keywords", [])}

    for am in data.get("amenidades", []):
        ents["amenidad"].append(am["nombre"])
        ents_meta[am["nombre"]] = {"tipo": "amenidad", "slug": am["slug"],
                                  "keywords": am.get("keywords", [])}

    return {"ents": ents, "meta": ents_meta}


def score(keyword: str, intent: str) -> float:
    """Score heurístico 0-100: intención comercial/transaccional y estacional pesan más."""
    score = 30.0
    weights = {
        "transaccional": 25, "comercial": 22, "temporada": 18,
        "informacional": 12, "navegacional": 8,
    }
    score += weights.get(intent, 10)
    kw = keyword.lower()
    for mod, w in SEASONAL_WEIGHT.items():
        if mod in kw:
            score += w * 10
    # Keywords multi-entidad (head + modificador) rankean mejor
    if len(keyword.split()) >= 4:
        score += 8
    if len(keyword.split()) <= 2:
        score -= 10  # muy genéricas, difícil competencia
    return round(min(score, 100), 1)


def main() -> None:
    data = load_entities()
    ents, meta = data["ents"], data["meta"]

    # Pool de términos "núcleo": nombre + keywords asociadas de cada entidad
    nucleo: dict[str, set[str]] = defaultdict(set)
    for nombre, m in meta.items():
        nucleo[nombre].add(nombre.lower())
        for k in m.get("keywords", []):
            nucleo[nombre].add(k.lower())

    keywords: dict[str, dict] = {}

    def add(kw: str, intent: str, entidades: list[str], pagina: str = ""):
        kw = norm(kw)
        if len(kw) < 4 or len(kw.split()) > 8:
            return
        entry = keywords.setdefault(kw, {
            "keyword": kw, "intenciones": set(), "entidades": set(),
            "paginas_sugeridas": set(), "score": 0.0,
        })
        entry["intenciones"].add(intent)
        entry["entidades"].update(entidades)
        if pagina:
            entry["paginas_sugeridas"].add(pagina)

    # 1) Keywords de la data maestra (ya mapeadas a páginas)
    combinaciones = json.loads(MASTER.read_text(encoding="utf-8")).get("combinacionesGeneradas", [])
    slug_a_kw = {}
    for c in combinaciones[:400]:  # muestra representativa para no explotar
        for kw in c.get("keywords", []):
            slug_a_kw.setdefault(norm(kw), c.get("slug", ""))

    for kw, slug in slug_a_kw.items():
        add(kw, "navegacional", [], slug)

    # 2) Expansión por intención: modificador × entidad
    entidades_planas = []
    for cat, nombres in ents.items():
        for n in nombres:
            entidades_planas.append((n, cat))

    # Priorizar destinos y atractivos (alto volumen turístico)
    prioridad = {"destino": 1, "atractivo": 2, "alojamiento": 3,
                 "tipo": 4, "amenidad": 5}
    entidades_planas.sort(key=lambda x: prioridad.get(x[1], 9))

    modificadores = {i: mods for i, mods in INTENTS.items()}

    for nombre, cat in entidades_planas:
        terminos = sorted(nucleo.get(nombre, {nombre.lower()}))
        # Usar el término más corto como base para no generar frases gigantes
        base = min(terminos, key=len)

        for intent, mods in modificadores.items():
            for mod in mods:
                if intent == "temporada" and mod not in SEASONAL_WEIGHT:
                    continue
                for template in (
                    f"{base} {mod}",
                    f"{mod} {base}",
                ):
                    add(template, intent, [nombre], "")

    # 3) Keywords navideñas específicas (temporada alta)
    destinos_top = [n for n, c in entidades_planas if c in ("destino", "atractivo")]
    for destino in destinos_top:
        for patron in (
            f"planes {destino} diciembre",
            f"viajes {destino} navidad",
            f"{destino} diciembre 2026",
            f"vacaciones {destino} fin de ano",
            f"plan navideno {destino}",
            f"que hacer en {destino} diciembre",
        ):
            add(patron, "temporada", [destino], "planes-especiales-diciembre-2026.html")

    # 4) Scoring y serialización
    for kw, e in keywords.items():
        mejor_intent = max(e["intenciones"],
                           key=lambda i: {"transaccional": 5, "comercial": 4,
                                          "temporada": 3, "informacional": 2,
                                          "navegacional": 1}.get(i, 0))
        e["score"] = score(kw, mejor_intent)
        e["intenciones"] = sorted(e["intenciones"])
        e["entidades"] = sorted(e["entidades"])
        e["paginas_sugeridas"] = sorted(e["paginas_sugeridas"])

    ranking = sorted(keywords.values(), key=lambda x: -x["score"])

    out = {
        "meta": {
            "total_keywords": len(ranking),
            "fuente": "pseo-engine/pseo-master-data.json",
            "generado": "2026-11-13",
        },
        "por_intencion": dict(Counter(
            i for e in ranking for i in e["intenciones"]
        )),
        "keywords": ranking,
    }
    (OUT_DIR / "keyword-map.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")

    # Reporte Markdown
    top = ranking[:60]
    lineas = [
        "# Mapa de Keywords — Quindío Travel",
        "",
        f"**Total generadas:** {len(ranking):,} keywords",
        f"**Por intención:** {out['por_intencion']}",
        "",
        "## Top 60 por score (intención + estacionalidad)",
        "",
        "| Score | Keyword | Intenciones | Entidades |",
        "|------:|---------|-------------|-----------|",
    ]
    for e in top:
        lineas.append(
            f"| {e['score']:.0f} | {e['keyword']} | {', '.join(e['intenciones'])} "
            f"| {', '.join(e['entidades'][:3])} |"
        )
    lineas += [
        "",
        "## Keywords navideñas prioritarias (temporada)",
        "",
    ]
    navidad = [e for e in ranking if "temporada" in e["intenciones"]]
    for e in navidad[:40]:
        lineas.append(f"- **{e['score']:.0f}** {e['keyword']}")

    (OUT_DIR / "keyword-report.md").write_text(
        "\n".join(lineas), encoding="utf-8")

    print(f"Keywords generadas: {len(ranking):,}")
    print(f"Por intención: {out['por_intencion']}")
    print(f"Salida: {OUT_DIR / 'keyword-map.json'}")
    print(f"Reporte: {OUT_DIR / 'keyword-report.md'}")


if __name__ == "__main__":
    sys.exit(main())
