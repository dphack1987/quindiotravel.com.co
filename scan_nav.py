from pathlib import Path
import re

home_pattern = re.compile(r'href=["\'](?:index\.html|/|\./|https?://[^"\']*/index\.html)["\']', re.I)
nav_pattern = re.compile(r'class=["\']nav-menu["\']')
files = sorted(Path('.').rglob('*.html'))
missing_nav = []
missing_home = []
for p in files:
    text = p.read_text(encoding='utf-8', errors='ignore')
    if not nav_pattern.search(text):
        missing_nav.append(str(p))
    else:
        nav_start = nav_pattern.search(text).start()
        nav_end = text.find('</nav>', nav_start)
        nav_block = text[nav_start:nav_end+6] if nav_end != -1 else text[nav_start:]
        if not home_pattern.search(nav_block):
            missing_home.append(str(p))

with open('scan_nav_results.txt', 'w', encoding='utf-8') as f:
    f.write(f'TOTAL_HTML={len(files)}\n')
    f.write(f'MISSING_NAV={len(missing_nav)}\n')
    for x in missing_nav:
        f.write(f'MISSING_NAV:{x}\n')
    f.write(f'MISSING_HOME_IN_NAV={len(missing_home)}\n')
    for x in missing_home:
        f.write(f'MISSING_HOME:{x}\n')
print('Scan complete. Results saved to scan_nav_results.txt')
