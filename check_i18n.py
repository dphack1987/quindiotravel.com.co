import re, glob
from pathlib import Path
text = Path('assets/js/language-detector.js').read_text(encoding='utf-8')
obj = text.split('const translations = {',1)[1].rsplit('};',1)[0]
keys = set(re.findall(r"['\"]([a-z0-9_.]+)['\"]\s*:\s*['\"]", obj))
used = set()
pat = re.compile(r'data-i18n=["\']([^"\']+)["\']')
for fn in glob.glob('**/*.html', recursive=True):
    used |= set(pat.findall(Path(fn).read_text(encoding='utf-8')))
missing = sorted(used-keys)
print('translation keys:', len(keys))
print('used keys:', len(used))
print('missing keys:', len(missing))
for k in missing:
    print(k)
