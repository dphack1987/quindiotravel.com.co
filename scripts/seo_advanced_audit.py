#!/usr/bin/env python3
"""Auditor SEO avanzado y ético para el sitio.

Objetivo: detectar oportunidades de mejora técnica en páginas HTML sin borrar
contenido ni aplicar prácticas engañosas. El script produce un reporte con
métricas reales de indexación, semántica y entidades relevantes.
"""

from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from urllib.parse import urljoin

EXCLUDED_FILES = {"404.html", "500.html"}
SKIP_DIRS = {".git", "node_modules", "dist", ".devin", ".github", ".vscode"}


class PageSEOParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.meta_description = ""
        self.canonical = ""
        self.h1_count = 0
        self.h2_count = 0
        self.h3_count = 0
        self.links = 0
        self.internal_links = 0
        self.external_links = 0
        self.schema_blocks = 0
        self._inside_title = False
        self._inside_script = False
        self._inside_h1 = False
        self._inside_h2 = False
        self._inside_h3 = False
        self._is_og_image = False
        self._meta_properties: Dict[str, str] = {}
        self._attrs: Dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        values = {str(key).lower(): (value or "") for key, value in attrs}
        tag = tag.lower()

        if tag == "title":
            self._inside_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "h2":
            self.h2_count += 1
        if tag == "h3":
            self.h3_count += 1
        if tag == "a" and values.get("href"):
            self.links += 1
            href = values["href"].strip()
            if href.startswith("http"):
                self.external_links += 1
            elif href.startswith("#"):
                self.internal_links += 1
            else:
                self.internal_links += 1
        if tag == "meta":
            name = (values.get("name") or values.get("property") or "").lower().strip()
            content = values.get("content", "").strip()
            if name == "description":
                self.meta_description = content
            if name.startswith("og:"):
                self._meta_properties[name] = content
            if name == "twitter:image" and content:
                self._meta_properties["twitter:image"] = content
            if values.get("rel") == "canonical":
                self.canonical = values.get("href", "").strip()
        if tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self.schema_blocks += 1

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._inside_title = False

    def handle_data(self, data: str) -> None:
        if self._inside_title:
            self.title += data


class SEOIssueResult:
    def __init__(self, page: Path, score: int, issues: List[str]) -> None:
        self.page = page
        self.score = score
        self.issues = issues


def clean_text(value: str) -> str:
    return " ".join(value.split())


def read_html(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return path.read_text(encoding="latin-1", errors="replace")


def page_score(data: Dict[str, object]) -> int:
    score = 100
    if not data.get("title"):
        score -= 18
    if not data.get("meta_description"):
        score -= 15
    elif len(data["meta_description"]) < 70 or len(data["meta_description"]) > 170:
        score -= 8
    if not data.get("canonical"):
        score -= 15
    if int(data.get("h1_count") or 0) != 1:
        score -= 12
    if int(data.get("schema_blocks") or 0) == 0:
        score -= 10
    if not data.get("og_title"):
        score -= 7
    if not data.get("og_image"):
        score -= 6
    if int(data.get("links") or 0) == 0:
        score -= 5
    if score < 0:
        score = 0
    return score


def analyze_html(path: Path) -> Dict[str, object]:
    html = read_html(path)
    parser = PageSEOParser()
    parser.feed(html)

    title = clean_text(parser.title)
    desc = clean_text(parser.meta_description)
    og_title = ""
    og_image = ""
    for key, value in parser._meta_properties.items():
        if key == "og:title":
            og_title = value.strip()
        if key == "og:image":
            og_image = value.strip()

    data = {
        "page": str(path),
        "title": title,
        "meta_description": desc,
        "canonical": parser.canonical,
        "h1_count": parser.h1_count,
        "h2_count": parser.h2_count,
        "h3_count": parser.h3_count,
        "links": parser.links,
        "internal_links": parser.internal_links,
        "external_links": parser.external_links,
        "schema_blocks": parser.schema_blocks,
        "og_title": og_title,
        "og_image": og_image,
    }
    score = page_score(data)
    issues: List[str] = []

    if not title:
        issues.append("Sin <title> útil")
    if not desc:
        issues.append("Falta meta description")
    elif len(desc) < 70 or len(desc) > 170:
        issues.append("Meta description fuera del rango recomendado")
    if not parser.canonical:
        issues.append("Sin canonical URL")
    if parser.h1_count != 1:
        issues.append(f"H1 incorrecto: {parser.h1_count} encontrado(s)")
    if parser.schema_blocks == 0:
        issues.append("Sin JSON-LD de schema")
    if not og_title:
        issues.append("Falta og:title")
    if not og_image:
        issues.append("Falta og:image")
    if parser.links == 0:
        issues.append("Sin enlaces internos relevantes")

    return {"score": score, "issues": issues, **data}


def crawl_html(root: Path) -> List[Path]:
    files: List[Path] = []
    for path in root.rglob("*.html"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.name in EXCLUDED_FILES:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Auditor SEO técnico avanzado y ético")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", type=Path, default=None)
    parser.add_argument("--limit", type=int, default=12)
    args = parser.parse_args()

    root = args.root.resolve()
    pages = crawl_html(root)
    findings: List[Dict[str, object]] = []

    for page in pages:
        findings.append(analyze_html(page))

    findings.sort(key=lambda item: (item["score"], item["page"]))

    summary = {
        "pages_analyzed": len(findings),
        "avg_score": round(sum(item["score"] for item in findings) / len(findings), 2) if findings else 0,
        "low_score_pages": [
            {"page": item["page"], "score": item["score"], "issues": item["issues"][:4]}
            for item in findings[: args.limit]
            if item["score"] < 90
        ],
    }

    output = {"summary": summary, "pages": findings}

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Páginas analizadas: {summary['pages_analyzed']}")
    print(f"Promedio de score SEO: {summary['avg_score']}")
    print("Páginas con más oportunidad:")
    for item in summary["low_score_pages"]:
        print(f"- {item['page']} | score={item['score']} | issues={', '.join(item['issues'])}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
