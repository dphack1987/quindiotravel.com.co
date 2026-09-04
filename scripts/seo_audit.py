"""Auditor SEO local, de solo lectura, para el sitio estático de Quindío Travel."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse
from xml.etree import ElementTree


SITE_URL = "https://quindiotravel.com.co/"
SKIP_DIRS = {".git", "node_modules", "dist", "components", "docs", "generated-pages", "documentation_archive"}
EXCLUDED_FILES = {"404.html", "500.html"}


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.h1_count = 0
        self.schema_count = 0
        self.schema_blocks: list[str] = []
        self.hreflang: dict[str, str] = {}
        self.links: list[str] = []
        self._in_title = False
        self._in_schema = False
        self._schema_buffer: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "script" and values.get("type", "").lower() == "application/ld+json":
            self.schema_count += 1
            self._in_schema = True
            self._schema_buffer = []
        elif tag == "meta":
            name = values.get("name", "").lower()
            if name == "description":
                self.description = values.get("content", "").strip()
            elif name == "robots":
                self.robots = values.get("content", "").strip().lower()
        elif tag == "link":
            rel = values.get("rel", "").lower()
            if rel == "canonical":
                self.canonical = values.get("href", "").strip()
            elif rel == "alternate" and values.get("hreflang") and values.get("href"):
                self.hreflang[values["hreflang"].lower()] = values["href"].strip()
        elif tag == "a" and values.get("href"):
            self.links.append(values["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self._in_title = False
        elif tag.lower() == "script" and self._in_schema:
            self.schema_blocks.append("".join(self._schema_buffer).strip())
            self._in_schema = False

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self.title += data
        if self._in_schema:
            self._schema_buffer.append(data)


def html_files(root: Path) -> list[Path]:
    pages = []
    for current, directories, filenames in os.walk(root):
        directories[:] = [directory for directory in directories if directory not in SKIP_DIRS]
        pages.extend(
            Path(current) / filename
            for filename in filenames
            if filename.endswith(".html") and filename not in EXCLUDED_FILES
        )
    return sorted(pages)


def page_url(relative: Path) -> str:
    relative_url = relative.as_posix()
    if relative.name == "index.html":
        parent = relative.parent.as_posix()
        return SITE_URL if parent == "." else f"{SITE_URL}{parent}/"
    return urljoin(SITE_URL, relative_url)


def normalize_link(raw: str, source_url: str) -> str | None:
    absolute = urljoin(source_url, raw)
    absolute, _ = urldefrag(absolute)
    parsed = urlparse(absolute)
    if parsed.scheme not in {"", "http", "https"}:
        return None
    if parsed.netloc and parsed.netloc != urlparse(SITE_URL).netloc:
        return None
    path = parsed.path or "/"
    return "index.html" if path == "/" else path.lstrip("/")


def load_sitemap_urls(root: Path) -> tuple[set[str], list[str], dict[str, int]]:
    urls: set[str] = set()
    errors: list[str] = []
    counts: Counter[str] = Counter()
    for sitemap in sorted(root.glob("*.xml")):
        try:
            tree = ElementTree.parse(sitemap)
        except ElementTree.ParseError as error:
            errors.append(f"{sitemap.name}: XML inválido ({error})")
            continue
        for loc in tree.findall(".//{*}loc"):
            if loc.text and loc.text.startswith(SITE_URL):
                url = loc.text.strip()
                urls.add(url)
                counts[url] += 1
    return urls, errors, counts


def parse_schema(block: str) -> bool:
    if not block:
        return False
    try:
        json.loads(block)
    except json.JSONDecodeError:
        return False
    return True


def audit(root: Path, published_only: bool = False) -> dict:
    sitemap_urls, sitemap_errors, sitemap_counts = load_sitemap_urls(root)
    sitemap_paths = {urlparse(url).path.lstrip("/") or "index.html" for url in sitemap_urls}
    if published_only:
        pages = [root / relative for relative in sorted(sitemap_paths) if (root / relative).is_file()]
        known_paths = sitemap_paths
    else:
        pages = html_files(root)
        known_paths = {path.relative_to(root).as_posix() for path in pages}
    details: dict[str, dict] = {}
    incoming = defaultdict(set)

    for path in pages:
        relative = path.relative_to(root)
        page = PageParser()
        page.feed(path.read_text(encoding="utf-8", errors="replace"))
        expected = page_url(relative)
        source_url = expected
        canonical = urljoin(expected, page.canonical) if page.canonical else ""
        broken_links: list[str] = []
        for raw_link in page.links:
            target = normalize_link(raw_link, source_url)
            if target and target.endswith(".html"):
                if target not in known_paths:
                    target_file = root / target
                    if not target_file.is_file():
                        broken_links.append(raw_link)
                    else:
                        incoming[target].add(relative.as_posix())
                else:
                    incoming[target].add(relative.as_posix())
        details[relative.as_posix()] = {
            "title": page.title.strip(),
            "description": page.description,
            "canonical": canonical,
            "expected_canonical": expected,
            "robots": page.robots,
            "h1_count": page.h1_count,
            "schema_count": page.schema_count,
            "schema_valid": all(parse_schema(block) for block in page.schema_blocks),
            "hreflang": page.hreflang,
            "broken_internal_links": sorted(set(broken_links)),
        }

    if published_only:
        for source in html_files(root):
            source_relative = source.relative_to(root).as_posix()
            if source_relative in details:
                continue
            content = source.read_text(encoding="utf-8", errors="replace")
            for raw_link in re.findall(r"href=[\"']([^\"']+)[\"']", content, re.IGNORECASE):
                target = normalize_link(raw_link, page_url(source.relative_to(root)))
                if target in details:
                    incoming[target].add(source_relative)

    titles = Counter(item["title"].casefold() for item in details.values() if item["title"])
    descriptions = Counter(item["description"].casefold() for item in details.values() if item["description"])
    issues = {"critical": [], "warning": [], "info": []}

    for relative, item in details.items():
        if not item["canonical"]:
            issues["critical"].append({"page": relative, "issue": "Falta canonical"})
        elif item["canonical"] != item["expected_canonical"]:
            issues["critical"].append({"page": relative, "issue": "Canonical no coincide con la URL del archivo", "canonical": item["canonical"]})
        if not item["description"]:
            issues["warning"].append({"page": relative, "issue": "Falta meta description"})
        elif not 70 <= len(item["description"]) <= 170:
            issues["info"].append({"page": relative, "issue": "Meta description requiere revisión editorial de longitud (heurística, no regla de ranking)", "length": len(item["description"])})
        if item["h1_count"] != 1:
            issues["warning"].append({"page": relative, "issue": f"Debe tener exactamente un H1 (actual: {item['h1_count']})"})
        if item["schema_count"] == 0:
            issues["info"].append({"page": relative, "issue": "No se encontró JSON-LD"})
        elif not item["schema_valid"]:
            issues["warning"].append({"page": relative, "issue": "JSON-LD inválido"})
        if item["hreflang"] and "x-default" not in item["hreflang"]:
            issues["info"].append({"page": relative, "issue": "Hreflang sin x-default"})
        if relative == "plan-exclusivo-meta-ads.html":
            content = (root / relative).read_text(encoding="utf-8", errors="replace").casefold()
            if not all(term in content for term in ("madrid", "barcelona", "españa", "280€")):
                issues["warning"].append({"page": relative, "issue": "Landing España sin señales geográficas/precio visibles completas"})
        if "noindex" in item["robots"]:
            issues["critical"].append({"page": relative, "issue": "Página marcada como noindex"})
        if item["broken_internal_links"]:
            issues["warning"].append({"page": relative, "issue": "Enlaces internos a archivos inexistentes", "links": item["broken_internal_links"]})

    for title, count in titles.items():
        if count > 1:
            issues["warning"].append({"issue": "Título duplicado", "title": title, "count": count})
    for description, count in descriptions.items():
        if count > 1:
            issues["info"].append({"issue": "Meta description duplicada", "description": description, "count": count})
    orphan_candidates = set(details) if published_only else known_paths
    for relative in sorted(orphan_candidates - {"index.html"}):
        if relative not in incoming:
            issues["warning"].append({"page": relative, "issue": "Posible página huérfana sin enlaces HTML entrantes"})
    if not published_only:
        for relative in sorted(known_paths - sitemap_paths):
            issues["info"].append({"page": relative, "issue": "HTML no incluido en los sitemaps raíz"})
    for sitemap_path in sorted(sitemap_paths - known_paths):
        issues["warning"].append({"page": sitemap_path, "issue": "URL del sitemap sin archivo HTML local equivalente"})
    issues["critical"].extend({"issue": error} for error in sitemap_errors)

    return {
        "site": SITE_URL,
        "pages_scanned": len(pages),
        "sitemap_urls_scanned": len(sitemap_urls),
        "sitemap_duplicate_urls": {url: count for url, count in sitemap_counts.items() if count > 1},
        "issues": issues,
        "pages": details,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audita SEO técnico sin modificar el sitio")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--json", type=Path, help="Guardar el informe completo en JSON")
    parser.add_argument("--published-only", action="store_true", help="Analizar solo las URLs presentes en los sitemaps raíz")
    args = parser.parse_args()
    report = audit(args.root.resolve(), published_only=args.published_only)
    if args.json:
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"SEO audit: {report['pages_scanned']} HTML, {report['sitemap_urls_scanned']} URLs únicas en sitemaps")
    print(f"sitemap duplicates: {len(report['sitemap_duplicate_urls'])}")
    for severity in ("critical", "warning", "info"):
        print(f"{severity}: {len(report['issues'][severity])}")
    if report["issues"]["critical"]:
        print("Primeros problemas críticos:")
        for issue in report["issues"]["critical"][:10]:
            print(f"- {issue}")
    return 1 if report["issues"]["critical"] else 0


if __name__ == "__main__":
    sys.exit(main())