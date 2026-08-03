from pathlib import Path
import re

nav_pattern = re.compile(r'class=["\']nav-menu["\']')
home_pattern = re.compile(r'href=["\'](?:index\.html|\./index\.html|/index\.html|/|\./)["\']', re.I)
missing_both = []
missing_nav = []
missing_home = []
files = sorted(Path('.').rglob('*.html'))
for p in files:
    text = p.read_text(encoding='utf-8', errors='ignore')
    has_nav = bool(nav_pattern.search(text))
    has_home = bool(home_pattern.search(text))
    if not has_nav:
        missing_nav.append(str(p))
    if not has_home:
        missing_home.append(str(p))
    if not has_nav and not has_home:
        missing_both.append(str(p))
print('TOTAL_HTML', len(files))
print('MISSING_NAV', len(missing_nav))
print('MISSING_HOME', len(missing_home))
print('MISSING_BOTH', len(missing_both))
for x in missing_both[:50]:
    print('MISSING_BOTH:', x)
