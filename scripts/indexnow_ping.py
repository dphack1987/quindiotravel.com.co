#!/usr/bin/env python3
"""Ping IndexNow para indexación instantánea en Bing, Yandex, Naver,
Seznam y otros motores que soportan el protocolo.

Uso:
    python scripts/indexnow_ping.py                 # envía todas las URLs del sitemap
    python scripts/indexnow_ping.py URL1 URL2 ...   # envía URLs específicas
"""

from __future__ import annotations

import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOST = "quindiotravel.com.co"
KEY = "26aa624b592cb5ed21726d978b12fc6d"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"
SITEMAP = ROOT / "sitemap-main.xml"


def sitemap_urls() -> list[str]:
    xml = SITEMAP.read_text(encoding="utf-8")
    return re.findall(r"<loc>(https://quindiotravel\.com\.co/[^<]+)</loc>", xml)


def ping(urls: list[str]) -> int:
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls[:10000],
    }
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            print(f"IndexNow: HTTP {r.status} — {len(urls)} URLs enviadas")
            return r.status
    except urllib.error.HTTPError as e:
        print(f"IndexNow: HTTP {e.code} — {e.read()[:300]}")
        return e.code


def main() -> int:
    if len(sys.argv) > 1:
        urls = [u if u.startswith("http") else f"https://{HOST}/{u.lstrip('/')}"
                for u in sys.argv[1:]]
    else:
        urls = sitemap_urls()
    print(f"URLs a notificar: {len(urls)}")
    return 0 if ping(urls) in (200, 202) else 1


if __name__ == "__main__":
    sys.exit(main())
