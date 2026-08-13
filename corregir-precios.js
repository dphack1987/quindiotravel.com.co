// Script para corregir precios según documento DOCX oficial PORTAFOLIO PLANES NACIONALES 2026.docx

const preciosOficiales = {
  plan1: {
    economico: { doble: 796000, triple: 668000, cuadruple: 602000 },
    intermedio: { doble: 815000, triple: 682000, cuadruple: 613000 },
    intermedio_vip: { doble: 962000, triple: 825000, cuadruple: 758000 },
    vip: { doble: 1020000, triple: 1164000, cuadruple: 1078000 }
  },
  plan2: {
    economico: { doble: 935000, triple: 805000, cuadruple: 735000 },
    intermedio: { doble: 972000, triple: 835000, cuadruple: 760000 },
    intermedio_vip: { doble: 1268000, triple: 1120000, cuadruple: 1045000 },
    vip: { doble: 2015000, triple: 1800000, cuadruple: 1685000 }
  },
  plan3: {
    economico: { doble: 1385000, triple: 1170000, cuadruple: 1050000 },
    intermedio: { doble: 1440000, triple: 1215000, cuadruple: 1150000 },
    intermedio_vip: { doble: 1885000, triple: 1650000, cuadruple: 1530000 },
    vip: { doble: 3000000, triple: 2660000, cuadruple: 2490000 }
  },
  plan4: {
    economico: { doble: 1495000, triple: 1250000, cuadruple: 1125000 },
    intermedio: { doble: 1550000, triple: 1295000, cuadruple: 1160000 },
    intermedio_vip: { doble: 1990000, triple: 1730000, cuadruple: 1590000 },
    vip: { doble: 3120000, triple: 2740000, cuadruple: 2550000 }
  },
  plan5: {
    economico: { doble: 1297000, triple: 1120000, cuadruple: 1020000 },
    intermedio: { doble: 1360000, triple: 1170000, cuadruple: 1060000 },
    intermedio_vip: { doble: 1795000, triple: 1590000, cuadruple: 1490000 },
    vip: { doble: 2920000, triple: 2600000, cuadruple: 2450000 }
  },
  plan6: {
    economico: { doble: 1800000, triple: 1520000, cuadruple: 1380000 },
    intermedio: { doble: 1880000, triple: 1580000, cuadruple: 1430000 },
    intermedio_vip: { doble: 2465000, triple: 2150000, cuadruple: 1995000 },
    vip: { doble: 3960000, triple: 3510000, cuadruple: 3280000 }
  }
};

console.log("Precios oficiales cargados según documento DOCX");
console.log("Plan 1:", preciosOficiales.plan1);
console.log("Plan 2:", preciosOficiales.plan2);
console.log("Plan 3:", preciosOficiales.plan3);
console.log("Plan 4:", preciosOficiales.plan4);
console.log("Plan 5:", preciosOficiales.plan5);
console.log("Plan 6:", preciosOficiales.plan6);