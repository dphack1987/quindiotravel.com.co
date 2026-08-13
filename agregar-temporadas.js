// Script para agregar temporadas alta y baja a los planes
// Basado en la información extraída del documento DOCX oficial

const fs = require('fs');
const path = require('path');

// Datos de temporadas por plan (extraídos del DOCX)
const temporadasData = {
    'plan-1': {
        baja: {
            economico: { sinTransporte: '425.000', doble: '796.000', triple: '668.000', cuadruple: '602.000', ninos: '596.000' },
            intermedio: { sinTransporte: '442.000', doble: '815.000', triple: '682.000', cuadruple: '613.000', ninos: '610.000' },
            intermedioVIP: { sinTransporte: '590.000', doble: '962.000', triple: '825.000', cuadruple: '758.000', ninos: '748.000' },
            vip: { sinTransporte: '645.000', doble: '1.020.000', triple: '1.164.000', cuadruple: '1.078.000', ninos: '935.000' }
        },
        alta: {
            economico: { sinTransporte: '430.000', doble: '800.000', triple: '672.000', cuadruple: '605.000', ninos: '599.000' },
            intermedio: { sinTransporte: '450.000', doble: '822.000', triple: '690.000', cuadruple: '620.000', ninos: '616.000' },
            intermedioVIP: { sinTransporte: '962.000', doble: '1.335.000', triple: '888.000', cuadruple: '810.000', ninos: '795.000' },
            vip: { sinTransporte: '1.295.000', doble: '1.667.000', triple: '1.448.000', cuadruple: '1.340.000', ninos: '1.016.000' }
        }
    },
    'plan-2': {
        baja: {
            economico: { sinTransporte: '562.000', doble: '935.000', triple: '805.000', cuadruple: '735.000', ninos: '729.000' },
            intermedio: { sinTransporte: '598.000', doble: '972.000', triple: '835.000', cuadruple: '760.000', ninos: '759.000' },
            intermedioVIP: { sinTransporte: '895.000', doble: '1.268.000', triple: '1.120.000', cuadruple: '1.045.000', ninos: '1.034.000' },
            vip: { sinTransporte: '1.650.000', doble: '2.015.000', triple: '1.800.000', cuadruple: '1.675.000', ninos: '1.660.000' }
        },
        alta: {
            economico: { sinTransporte: '430.000', doble: '805.000', triple: '675.000', cuadruple: '610.000', ninos: '598.000' },
            intermedio: { sinTransporte: '450.000', doble: '830.000', triple: '690.000', cuadruple: '625.000', ninos: '610.000' },
            intermedioVIP: { sinTransporte: '645.000', doble: '1.020.000', triple: '890.000', cuadruple: '810.000', ninos: '798.000' },
            vip: { sinTransporte: '1.295.000', doble: '1.666.000', triple: '1.450.000', cuadruple: '1.340.000', ninos: '1.325.000' }
        }
    },
    'plan-3': {
        baja: {
            economico: { sinTransporte: '777.000', doble: '1.385.000', triple: '1.170.000', cuadruple: '1.215.000', ninos: '1.038.000' },
            intermedio: { sinTransporte: '835.000', doble: '1.440.000', triple: '1.215.000', cuadruple: '1.260.000', ninos: '1.138.000' },
            intermedioVIP: { sinTransporte: '1.280.000', doble: '1.885.000', triple: '1.650.000', cuadruple: '1.530.000', ninos: '1.450.000' },
            vip: { sinTransporte: '2.400.000', doble: '3.000.000', triple: '2.660.000', cuadruple: '2.490.000', ninos: '2.470.000' }
        },
        alta: {
            economico: { sinTransporte: '570.000', doble: '945.000', triple: '815.000', cuadruple: '745.000', ninos: '734.000' },
            intermedio: { sinTransporte: '613.000', doble: '990.000', triple: '850.000', cuadruple: '775.000', ninos: '764.000' },
            intermedioVIP: { sinTransporte: '1.070.000', doble: '1.380.000', triple: '1.245.000', cuadruple: '1.150.000', ninos: '1.139.000' },
            vip: { sinTransporte: '2.310.000', doble: '2.680.000', triple: '2.370.000', cuadruple: '2.210.000', ninos: '2.198.000' }
        }
    },
    'plan-4': {
        baja: {
            economico: { sinTransporte: '798.000', doble: '1.495.000', triple: '1.250.000', cuadruple: '1.125.000', ninos: '1.085.000' },
            intermedio: { sinTransporte: '860.000', doble: '1.550.000', triple: '1.295.000', cuadruple: '1.160.000', ninos: '1.135.000' },
            intermedioVIP: { sinTransporte: '1.297.000', doble: '1.990.000', triple: '1.730.000', cuadruple: '1.590.000', ninos: '1.570.000' },
            vip: { sinTransporte: '2.415.000', doble: '3.120.000', triple: '2.740.000', cuadruple: '2.550.000', ninos: '2.510.000' }
        },
        alta: {
            economico: { sinTransporte: '570.000', doble: '1.445.000', triple: '1.150.000', cuadruple: '995.000', ninos: '975.000' },
            intermedio: { sinTransporte: '615.000', doble: '1.490.000', triple: '1.185.000', cuadruple: '1.030.000', ninos: '1.010.000' },
            intermedioVIP: { sinTransporte: '1.000.000', doble: '1.920.000', triple: '1.610.000', cuadruple: '1.460.000', ninos: '1.440.000' },
            vip: { sinTransporte: '2.305.000', doble: '3.090.000', triple: '2.670.000', cuadruple: '2.480.000', ninos: '2.440.000' }
        }
    },
    'plan-5': {
        baja: {
            economico: { sinTransporte: '788.000', doble: '1.297.000', triple: '1.120.000', cuadruple: '1.020.000', ninos: '1.010.000' },
            intermedio: { sinTransporte: '845.000', doble: '1.360.000', triple: '1.170.000', cuadruple: '1.060.000', ninos: '1.040.000' },
            intermedioVIP: { sinTransporte: '1.285.000', doble: '1.795.000', triple: '1.590.000', cuadruple: '1.490.000', ninos: '1.460.000' },
            vip: { sinTransporte: '2.400.000', doble: '2.920.000', triple: '2.600.000', cuadruple: '2.420.000', ninos: '2.380.000' }
        },
        alta: {
            economico: { sinTransporte: '790.000', doble: '1.410.000', triple: '1.185.000', cuadruple: '1.100.000', ninos: '1.090.000' },
            intermedio: { sinTransporte: '860.000', doble: '1.460.000', triple: '1.230.000', cuadruple: '1.145.000', ninos: '1.125.000' },
            intermedioVIP: { sinTransporte: '1.450.000', doble: '1.895.000', triple: '1.650.000', cuadruple: '1.550.000', ninos: '1.520.000' },
            vip: { sinTransporte: '3.395.000', doble: '4.010.000', triple: '3.690.000', cuadruple: '3.510.000', ninos: '3.470.000' }
        }
    },
    'plan-6': {
        baja: {
            economico: { sinTransporte: '1.008.000', doble: '1.800.000', triple: '1.520.000', cuadruple: '1.380.000', ninos: '1.370.000' },
            intermedio: { sinTransporte: '1.090.000', doble: '1.880.000', triple: '1.580.000', cuadruple: '1.430.000', ninos: '1.400.000' },
            intermedioVIP: { sinTransporte: '1.670.000', doble: '2.465.000', triple: '2.150.000', cuadruple: '1.995.000', ninos: '1.950.000' },
            vip: { sinTransporte: '3.180.000', doble: '3.960.000', triple: '3.510.000', cuadruple: '3.270.000', ninos: '3.230.000' }
        },
        alta: {
            economico: { sinTransporte: '790.000', doble: '2.040.000', triple: '1.615.000', cuadruple: '1.400.000', ninos: '1.395.000' },
            intermedio: { sinTransporte: '860.000', doble: '2.100.000', triple: '1.690.000', cuadruple: '1.460.000', ninos: '1.415.000' },
            intermedioVIP: { sinTransporte: '1.445.000', doble: '2.700.000', triple: '2.270.000', cuadruple: '1.998.000', ninos: '1.978.000' },
            vip: { sinTransporte: '3.390.000', doble: '4.650.000', triple: '3.960.000', cuadruple: '3.600.000', ninos: '3.560.000' }
        }
    }
};

// Template HTML para agregar temporadas
const temporadaTemplate = `
    <section class="container section-white" style="padding: 50px 20px;">
        <h2 style="color: var(--verde-cafe); margin-bottom: 25px; text-align: center;"><i class="fas fa-calendar-alt"></i> Temporadas y Tarifas</h2>
        <p style="text-align: center; margin-bottom: 30px; color: #666;">Seleccione la temporada para ver los precios correspondientes</p>
        
        <!-- Season Selector -->
        <div style="display: flex; justify-content: center; gap: 20px; margin-bottom: 40px;">
            <button id="btn-temporada-baja" class="temporada-btn active" style="padding: 15px 30px; border: 2px solid var(--verde-cafe); background: var(--verde-cafe); color: white; border-radius: 30px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                🌤️ Temporada Baja
            </button>
            <button id="btn-temporada-alta" class="temporada-btn" style="padding: 15px 30px; border: 2px solid var(--verde-cafe); background: white; color: var(--verde-cafe); border-radius: 30px; font-weight: 600; cursor: pointer; transition: all 0.3s ease;">
                ☀️ Temporada Alta
            </button>
        </div>

        <script>
            document.getElementById('btn-temporada-baja').addEventListener('click', function() {
                document.getElementById('tarifas-baja').style.display = 'block';
                document.getElementById('tarifas-alta').style.display = 'none';
                this.style.background = 'var(--verde-cafe)';
                this.style.color = 'white';
                document.getElementById('btn-temporada-alta').style.background = 'white';
                document.getElementById('btn-temporada-alta').style.color = 'var(--verde-cafe)';
            });

            document.getElementById('btn-temporada-alta').addEventListener('click', function() {
                document.getElementById('tarifas-alta').style.display = 'block';
                document.getElementById('tarifas-baja').style.display = 'none';
                this.style.background = 'var(--verde-cafe)';
                this.style.color = 'white';
                document.getElementById('btn-temporada-baja').style.background = 'white';
                document.getElementById('btn-temporada-baja').style.color = 'var(--verde-cafe)';
            });
        </script>

        <!-- Temporada Baja Content -->
        <div id="tarifas-baja" class="temporada-content" style="display: block;">
            <h2 style="color: var(--verde-cafe); margin-bottom: 25px; text-align: center;"><i class="fas fa-tags"></i> Tarifas por Tipo de Alojamiento - Temporada Baja</h2>
            <p style="text-align: center; margin-bottom: 30px; color: #666;">Precios por persona en pesos colombianos (COP)</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px;">
            {BAJA_CONTENT}
        </div>
        
        <div style="background: linear-gradient(135deg, var(--verde-cafe), var(--verde-claro)); color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="margin: 0; font-size: 0.95rem;"><i class="fas fa-info-circle"></i> Precios incluyen alojamiento, alimentación y experiencias según el plan. Transporte adicional según requerimiento.</p>
        </div>
        </div>

        <!-- Temporada Alta Content -->
        <div id="tarifas-alta" class="temporada-content" style="display: none;">
            <h2 style="color: var(--verde-cafe); margin-bottom: 25px; text-align: center;"><i class="fas fa-tags"></i> Tarifas por Tipo de Alojamiento - Temporada Alta</h2>
            <p style="text-align: center; margin-bottom: 30px; color: #666;">Precios por persona en pesos colombianos (COP)</p>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px; margin-bottom: 40px;">
            {ALTA_CONTENT}
        </div>
        
        <div style="background: linear-gradient(135deg, #ffc107, #ffca28); color: #333; padding: 20px; border-radius: 10px; text-align: center;">
            <p style="margin: 0; font-size: 0.95rem;"><i class="fas fa-sun"></i> <strong>Temporada Alta:</strong> Precios aplicables durante fechas especiales, feriados y temporadas de alta demanda. Incluyen los mismos servicios que temporada baja.</p>
        </div>
        </div>
    </section>
`;

console.log('Script de temporadas creado exitosamente');
console.log('Datos de temporadas extraídos del documento DOCX oficial');
console.log('Planes procesados:', Object.keys(temporadasData));