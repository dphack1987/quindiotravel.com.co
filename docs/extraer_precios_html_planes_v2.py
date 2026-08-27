import re
import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
base = Path(r'c:\Users\user\Documents\www.quindiotravel.com')
for i in range(1, 7):
    plan = base / f'plan-{i}.html'
    html = plan.read_text(encoding='utf-8')
    print(f'\n===== plan-{i}.html =====')
    cats = [
        ('Economico', r'Econ.mico'),
        ('Intermedio', r'Intermedio(?! VIP)'),
        ('Intermedio VIP', r'Intermedio VIP'),
        ('VIP', r'VIP'),
    ]
    for label, pat_h3 in cats:
        regex = r'<h3[^>]*>[^<]*' + pat_h3 + r'[^<]*</h3>(.{0,2500}?)(?=<h3|$)'
        m = re.search(regex, html, re.DOTALL)
        if m:
            precios = re.findall(r'\$([\d\.,]+)', m.group(0))
            hoteles = re.findall(r'<p[^>]*0\.85rem[^>]*>(.*?)</p>', m.group(0), re.DOTALL)
            h = hoteles[0].strip() if hoteles else ''
            print(f'  [{label:16s}]  precios = {precios}    hoteles = {h}')
