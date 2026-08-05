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

# helper to find nested keys sequentially

def check_nested(js_text, segments):
    pos=0
    for seg in segments:
        m=re.search(r'\b'+re.escape(seg)+r"\b\s*:\s*", js_text[pos:])
        if not m:
            return False
        # advance pos to after this match
        pos = pos + m.end()
    return True

missing=[]
for k in keys_sorted:
    segs=k.split('.')
    if not check_nested(js, segs):
        missing.append(k)

out=(root/'i18n_audit_v2.txt')
with out.open('w',encoding='utf-8') as f:
    f.write('Total HTML keys: %d\n' % len(keys_sorted))
    f.write('\n'.join(keys_sorted))
    f.write('\n\nMissing (nested check) in language-detector.js: %d\n' % len(missing))
    for m in missing:
        f.write(m+'\n')
print('Audit v2 written to', out)
