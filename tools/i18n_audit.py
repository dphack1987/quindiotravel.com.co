import re
from pathlib import Path
root=Path(__file__).resolve().parent.parent
html_files=list(root.glob('*.html'))
keys=set()
for p in html_files:
    s=p.read_text(encoding='utf-8')
    keys |= set(re.findall(r'data-i18n="([^"]+)"', s))
keys_sorted=sorted(keys)
js=(root/'assets/js/language-detector.js').read_text(encoding='utf-8')
missing=[]
for k in keys_sorted:
    if k not in js:
        missing.append(k)
out=(root/'i18n_audit.txt')
with out.open('w',encoding='utf-8') as f:
    f.write('Total HTML keys: %d\n' % len(keys_sorted))
    f.write('\n'.join(keys_sorted))
    f.write('\n\nMissing in language-detector.js: %d\n' % len(missing))
    for m in missing:
        f.write(m+'\n')
print('Audit written to', out)
