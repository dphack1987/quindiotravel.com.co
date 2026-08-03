from pathlib import Path
import re

files = sorted(Path('.').rglob('*.html'))
nav_re = re.compile(r'<nav\b', re.I)
home_re = re.compile(r'href=["\'](?:index\.html|/|\./|\.\./index\.html|/index\.html)["\']', re.I)

results = []
for p in files:
    text = p.read_text(encoding='utf-8', errors='ignore')
    has_nav = bool(nav_re.search(text))
    has_home = bool(home_re.search(text))
    results.append((str(p), has_nav, has_home))

missing_nav = [r for r in results if not r[1]]
missing_home = [r for r in results if not r[2]]
missing_both = [r for r in results if not r[1] and not r[2]]
with open('scan_navigation_broad.txt', 'w', encoding='utf-8') as f:
    f.write(f'TOTAL_HTML={len(results)}\n')
    f.write(f'MISSING_NAV={len(missing_nav)}\n')
    for r in missing_nav:
        f.write('MISSING_NAV:' + r[0] + '\n')
    f.write(f'MISSING_HOME={len(missing_home)}\n')
    for r in missing_home:
        f.write('MISSING_HOME:' + r[0] + '\n')
    f.write(f'MISSING_BOTH={len(missing_both)}\n')
    for r in missing_both:
        f.write('MISSING_BOTH:' + r[0] + '\n')
print('Done. Wrote scan_navigation_broad.txt')
