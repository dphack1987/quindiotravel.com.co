(function () {
  const prices = {
    1: {
      low: [[425000, 796000, 668000, 602000, 596000], [442000, 815000, 682000, 613000, 610000], [590000, 962000, 825000, 758000, 748000], [645000, 1020000, 1164000, 1078000, 935000]],
      high: [[430000, 800000, 672000, 605000, 599000], [450000, 822000, 690000, 620000, 616000], [962000, 1335000, 888000, 810000, 795000], [1235000, 1667000, 1448000, 1340000, 1016000]]
    },
    2: {
      low: [[562000, 935000, 805000, 735000, 729000], [598000, 972000, 835000, 760000, 759000], [895000, 1268000, 1120000, 1045000, 1034000], [1650000, 2015000, 1800000, 1685000, 1674000]],
      high: [[570000, 945000, 815000, 745000, 734000], [613000, 990000, 850000, 775000, 764000], [1070000, 1380000, 1245000, 1150000, 1139000], [2310000, 2680000, 2370000, 2210000, 2198000]]
    },
    3: {
      low: [[777000, 1385000, 1170000, 1050000, 1038000], [835000, 1440000, 1215000, 1150000, 1138000], [1280000, 1865000, 1650000, 1530000, 1515000], [2400000, 3000000, 2660000, 2490000, 2470000]],
      high: [[790000, 1410000, 1185000, 1100000, 1088000], [860000, 1485000, 1290000, 1200000, 1180000], [1450000, 2060000, 1850000, 1690000, 1670000], [3395000, 3998000, 3520000, 3290000, 3270000]]
    },
    4: {
      low: [[798000, 1495000, 1250000, 1125000, 1110000], [860000, 1550000, 1295000, 1160000, 1145000], [1297000, 1990000, 1730000, 1590000, 1160000], [2415000, 3120000, 2740000, 2550000, 1510000]],
      high: [[820000, 1514000, 2270000, 1135000, 1120000], [880000, 1575000, 1320000, 1180000, 1160000], [1470000, 2160000, 1920000, 1750000, 1735000], [3420000, 4131000, 3525000, 3350000, 3335000]]
    },
    5: {
      low: [[788000, 1297000, 1120000, 1020000, 998000], [845000, 1260000, 1160000, 1060000, 1040000], [1285000, 1795000, 1590000, 1490000, 1460000], [2400000, 2920000, 2600000, 2450000, 2430000]],
      high: [[798000, 1310000, 1135000, 1040000, 1010000], [870000, 1390000, 1190000, 1080000, 1050000], [1460000, 1965000, 1780000, 1645000, 1630000], [3398000, 3910000, 3460000, 3250000, 3230000]]
    },
    6: {
      low: [[1008000, 1800000, 1520000, 1380000, 1360000], [1090000, 1880000, 1580000, 1430000, 1400000], [1670000, 2465000, 2150000, 1995000, 1950000], [3180000, 3960000, 3510000, 3280000, 3240000]],
      high: [[1020000, 1820000, 1550000, 1410000, 1385000], [1120000, 1920000, 1610000, 1460000, 1410000], [1898000, 2690000, 2430000, 2210000, 2180000], [4490000, 5290000, 4650000, 4330000, 4325000]]
    }
  };
  const categories = ['Económico', 'Intermedio', 'Intermedio VIP', 'VIP'];
  const labels = ['Sin transporte', 'Doble', 'Triple', 'Cuádruple', 'Niños 2-10 años'];
  const money = value => '$' + value.toLocaleString('es-CO') + ' COP';
  const render = (plan, season, rows) => '<div class="plan-price-table-wrap" style="overflow-x:auto; margin: 20px 0 35px;"><table class="plan-price-table" style="width:100%; border-collapse:collapse; min-width:720px; background:white; border-radius:10px; overflow:hidden;"><thead><tr style="background:var(--verde-cafe); color:white;"><th style="padding:12px; text-align:left;">Categoría</th>' + labels.map(label => '<th style="padding:12px; text-align:right;">' + label + '</th>').join('') + '</tr></thead><tbody>' + rows.map((row, index) => '<tr><th scope="row" style="padding:12px; text-align:left; border-bottom:1px solid #e5e5e5;">' + categories[index] + '</th>' + row.map(value => '<td style="padding:12px; text-align:right; border-bottom:1px solid #e5e5e5; white-space:nowrap;">' + money(value) + '</td>').join('') + '</tr>').join('') + '</tbody></table></div>';
  document.addEventListener('DOMContentLoaded', function () {
    const plan = Number(document.body.dataset.plan);
    const target = document.getElementById('tabla-precios-completa');
    if (!target || !prices[plan]) return;
    target.innerHTML = '<h2 style="color:var(--verde-cafe); margin-bottom:10px;">Valores y acomodaciones</h2><p>Precios oficiales por persona en pesos colombianos. Incluyen las opciones de temporada baja y alta.</p><h3 style="color:var(--verde-cafe);">Temporada baja</h3>' + render(plan, 'low', prices[plan].low) + '<h3 style="color:var(--verde-cafe);">Temporada alta</h3>' + render(plan, 'high', prices[plan].high);
  });
})();
