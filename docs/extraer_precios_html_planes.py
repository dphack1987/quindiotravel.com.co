import re
from pathlib import Path

base = Path(r"c:\Users\user\Documents\www.quindiotravel.com")
planes = [base / f"plan-{i}.html" for i in range(1, 7)]

for plan in planes:
    html = plan.read_text(encoding="utf-8")
    print(f"\n{'='*80}")
    print(f"📄 {plan.name}")
    print(f"{'='*80}")
    # Buscar las 4 tarjetas de categoría (secciones Económica, Intermedio, VIP...)
    patrones_categorias = [
        ("💰 Económico", r"💰.*?Econ.mico.*?</div>", False),
        ("⭐ Intermedio", r"⭐[^<]*Intermedio(?! VIP).*?</div>", False),
        ("⭐⭐ Intermedio VIP", r"⭐⭐[^<]*Intermedio VIP.*?</div>", False),
        ("👑 VIP", r"👑 VIP.*?</div>", False),
    ]
    # Extraer precios dentro del rango 320-450 de líneas por archivo por archivo es variable
    for cat_name, pat, _ in patrones_categorias:
        matches = re.findall(pat, html, re.DOTALL)
        if not matches:
            # Patrón alternativo: busca <h3>...</h3> + siguientes 2000 chars conteniendo precios
            alt_pat = rf"<h3[^>]*>[^<]*{cat_name.split()[-1] if len(cat_name.split())>1 else cat_name[:3]}[^<]*</h3>.*?</div>\s*</div>"
            matches = re.findall(alt_pat, html, re.DOTALL)
        if matches:
            bloque = matches[0]
            # Extraer todos los precios con formato $X.XXX.XXX
            precios = re.findall(r"\$([\d\.,]+)", bloque)
            # Extraer última fila (nombres hoteles)
            ult_p = re.findall(r"<p[^>]*font-size:\s*0\.85rem[^>]*>(.*?)</p>", bloque, re.DOTALL)
            print(f"  ▶ {cat_name}:  precios_html = {precios}  | hoteles = {ult_p[-1].strip() if ult_p else 'N/A'}")
