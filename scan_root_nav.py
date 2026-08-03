from pathlib import Path
import re
root = Path('.')
root_html = sorted([p for p in root.glob('*.html')])
nav_pattern = re.compile(r'class=["\']nav-menu["\']', re.I)
hamburger_pattern = re.compile(r'hamburger-btn', re.I)
home_pattern = re.compile(r'href=["\'](?:index\.html|/|\./|/index\.html)["\']', re.I)
print('ROOT_HTML_COUNT', len(root_html))
for p in root_html:
    text = p.read_text(encoding='utf-8', errors='ignore')
    print(p.name, 'nav_menu=', bool(nav_pattern.search(text)), 'hamburger=', bool(hamburger_pattern.search(text)), 'home_link=', bool(home_pattern.search(text)))
