class KnowledgeBase {
    constructor() {
        this.baseDeConocimiento = {
            planes: {
                '3d': {
                    nombre: 'Plan 3 Días / 2 Noches',
                    precio: '$820.000',
                    incluye: [
                        'Parque del Café + entradas',
                        'PANACA + almuerzo',
                        'Alojamiento 2 noches en finca hotel',
                        'Transporte desde tu ciudad',
                        'Guía local'
                    ],
                    duracion: '3 días / 2 noches',
                    idealPara: 'Familias, primer vez al Eje Cafetero'
                },
                '4d': {
                    nombre: 'Plan 4 Días / 3 Noches',
                    precio: '$1.152.000',
                    incluye: [
                        'Valle de Cocora (senderismo)',
                        'Salento y Filandia',
                        'Parque del Café',
                        'Alojamiento 3 noches VIP',
                        'Transporte privado'
                    ],
                    duracion: '4 días / 3 noches',
                    idealPara: 'Experiencia completa, más tiempo'
                },
                '5d': {
                    nombre: 'Plan 5 Días / 4 Noches',
                    precio: '$1.473.000',
                    incluye: [
                        'Valle de Cocora + senderismo',
                        'Termales Santa Rosa',
                        'Parque del Café + PANACA',
                        'Todos los pueblos',
                        'Alojamiento 4 noches premium',
                        'Transporte exclusivo'
                    ],
                    duracion: '5 días / 4 noches',
                    idealPara: 'Experiencia definitiva, sin prisa'
                },
                'premium': {
                    nombre: 'Plan Premium VIP',
                    precio: '$1.800.000',
                    incluye: [
                        'Alojamiento VIP',
                        'Transporte exclusivo',
                        'Guías bilingües',
                        'Experiencias exclusivas',
                        'Servicio personalizado'
                    ],
                    duracion: 'Personalizable',
                    idealPara: 'Empresas, experiencias premium'
                },
                'empresarial': {
                    nombre: 'Plan Empresarial',
                    precio: 'Cotización personalizada',
                    incluye: [
                        'Team building',
                        'Conferencias',
                        'Actividades corporativas',
                        'Alimentación ejecutiva',
                        'Facturación oficial'
                    ],
                    duracion: 'Personalizable',
                    idealPara: 'Grupos, empresas, incentivos'
                }
            },
            destinos: {
                salento: {
                    nombre: 'Salento',
                    descripcion: 'Pueblo patrimonio con balcones coloridos y arquitectura tradicional. Fundado en 1842.',
                    highlights: [
                        'Mirador con vistas al Valle de Cocora',
                        'Artesanías locales',
                        'Café del municipio',
                        'Calle Real con arquitectura colonial'
                    ],
                    tips: [
                        'Sube al mirador al atardecer para fotos increíbles',
                        'Compra artesanías hechas a mano',
                        'Prueba el trucha asada en restaurantes locales',
                        'Caminar por la Calle Real es imperdible'
                    ],
                    actividades: ['Mirador', 'Compras', 'Fotografía', 'Gastronomía']
                },
                valle: {
                    nombre: 'Valle de Cocora',
                    descripcion: 'Valle natural con las palmas de cera más altas del mundo (hasta 60 metros).',
                    highlights: [
                        'Senderismo por bosque nuboso',
                        'Palmas de cera emblemáticas',
                        'Vistas panorámicas impresionantes',
                        'Humedad constante y neblina'
                    ],
                    tips: [
                        'Lleva calzado antideslizante',
                        'Lleva agua y snacks',
                        'Protector solar y repelente',
                        'Comienza temprano para evitar multitudes'
                    ],
                    actividades: ['Senderismo', 'Fotografía', 'Naturaleza', 'Avistamiento de aves']
                },
                cafe: {
                    nombre: 'Parque del Café',
                    descripcion: 'Parque temático del café con atracciones mecánicas, shows culturales y museo.',
                    highlights: [
                        'Museo del café interactivo',
                        'Shows culturales diarios',
                        'Atracciones mecánicas',
                        'Jardines botánicos de café'
                    ],
                    tips: [
                        'Compra pasaporte múltiple',
                        'Dedica todo el día',
                        'No te pierdas el show del café',
                        'Prueba el café especial en el restaurante'
                    ],
                    actividades: ['Museo', 'Shows', 'Atracciones', 'Degustación']
                },
                termales: {
                    nombre: 'Termales Santa Rosa',
                    descripcion: 'Aguas termales naturales con propiedades medicinales en Risaralda.',
                    highlights: [
                        'Piscinas termales naturales',
                        'Propiedades medicinales',
                        'Vistas panorámicas',
                        'Relax y bienestar'
                    ],
                    tips: [
                        'Lleva toalla y traje de baño',
                        'Dedica 3-4 horas',
                        'Ideal después de caminar',
                        'Reserva con anticipación en temporada alta'
                    ],
                    actividades: ['Relax', 'Baño termal', 'Naturaleza', 'Bienestar']
                },
                filandia: {
                    nombre: 'Filandia',
                    descripcion: 'Pueblo a 2.000msnm con mirador cóndor y tradición en artesanías de guadua.',
                    highlights: [
                        'Mirador cóndor (vistas 360°)',
                        'Artesanías en guadua',
                        'Iglesia colonial',
                        'Clima fresco durante todo el año'
                    ],
                    tips: [
                        'Lleva ropa abrigada (clima fresco)',
                        'Sube al mirador al amanecer',
                        'Compra artesanías de guadua',
                        'Prueba la gastronomía local'
                    ],
                    actividades: ['Mirador', 'Artesanías', 'Fotografía', 'Cultura']
                }
            },
            clima: {
                'mejor epoca': {
                    seco: ['Enero', 'Febrero', 'Julio', 'Agosto'],
                    lluvioso: ['Abril', 'Mayo', 'Octubre', 'Noviembre'],
                    recomendacion: 'Enero-febrero para clima perfecto, septiembre para menos turistas'
                },
                temperaturas: {
                    año: '18-25°C',
                    noche: '14-18°C',
                    valle_cocora: '12-18°C (más fresco)'
                },
                consejos: {
                    seco: 'Ideal para senderismo y actividades al aire libre',
                    lluvioso: 'Bueno para precios y menos turistas, prepare impermeable',
                    temp_alta: 'Reserva con anticipación, precios más altos'
                }
            },
            consejos: {
                empacar: {
                    esencial: [
                        'Protector solar',
                        'Repelente',
                        'Calzado cómodo para caminar',
                        'Ropa ligera y abrigable',
                        'Cámara'
                    ],
                    especifico: {
                        valle_cocora: 'Botas antideslizantes, agua, snacks',
                        termales: 'Toalla, traje de baño, chanclas',
                        pueblos: 'Dinero en efectivo, botella de agua'
                    }
                },
                seguridad: {
                    general: [
                        'Siempre usa guías locales certificados',
                        'No camines solo por senderismo desconocido',
                        'Copia documentos importantes',
                        'Tiene seguro de viaje'
                    ],
                    locales: [
                        'Evita mostrar objetos valiosos',
                        'Usa cajeros oficiales',
                        'Respeta normas locales',
                        'Contacta RNT 18152 para verificación'
                    ]
                },
                fotografía: {
                    mejores_horas: ['6-8 AM', '4-6 PM'],
                    mejores_lugares: ['Mirador Salento', 'Valle de Cocora', 'Parque del Café'],
                    consejos: [
                        'Lleva baterías extra',
                        'Usa tarjeta SD con espacio',
                        'Respecta a las personas al fotografiar',
                        'Pregunta permiso en comunidades indígenas'
                    ]
                }
            },
            precios: {
                temporada_baja: {
                    meses: ['Marzo', 'Mayo', 'Septiembre', 'Noviembre'],
                    descuento: '15-25%',
                    ventajas: ['Menos turistas', 'Mejores precios', 'Disponibilidad inmediata']
                },
                temporada_alta: {
                    meses: ['Diciembre', 'Enero', 'Puentes', 'Recesos'],
                    incremento: '20-30%',
                    consideraciones: ['Reserva con anticipación', 'Más turistas', 'Todo operativo']
                },
                adicionales: {
                    transporte: 'Incluido en precios base',
                    guias: 'Incluido certificados MINCIT',
                    entradas: 'Incluidas en parques',
                    alimentacion: 'Según plan (algunos todo incluido)'
                }
            }
        };
    }

    buscarInformacion(categoria, clave) {
        if (this.baseDeConocimiento[categoria] && this.baseDeConocimiento[categoria][clave]) {
            return this.baseDeConocimiento[categoria][clave];
        }
        return null;
    }

    buscarPorPalabraClave(palabra) {
        const palabraLower = palabra.toLowerCase();
        const resultados = [];

        // Buscar en planes
        for (const [key, plan] of Object.entries(this.baseDeConocimiento.planes)) {
            if (palabraLower.includes(key) || 
                plan.nombre.toLowerCase().includes(palabraLower) ||
                plan.idealPara.toLowerCase().includes(palabraLower)) {
                resultados.push({ tipo: 'plan', key, data: plan });
            }
        }

        // Buscar en destinos
        for (const [key, destino] of Object.entries(this.baseDeConocimiento.destinos)) {
            if (palabraLower.includes(key) || 
                destino.nombre.toLowerCase().includes(palabraLower) ||
                destino.descripcion.toLowerCase().includes(palabraLower)) {
                resultados.push({ tipo: 'destino', key, data: destino });
            }
        }

        return resultados;
    }

    formatearRespuesta(resultados) {
        if (resultados.length === 0) {
            return null;
        }

        if (resultados.length === 1) {
            const resultado = resultados[0];
            if (resultado.tipo === 'plan') {
                return this.formatearPlan(resultado.data);
            } else if (resultado.tipo === 'destino') {
                return this.formatearDestino(resultado.data);
            }
        }

        // Múltiples resultados
        return this.formatearMultiplesResultados(resultados);
    }

    formatearPlan(plan) {
        return `🗺️ **${plan.nombre}**\n\n💰 Precio: ${plan.precio}\n⏰ Duración: ${plan.duracion}\n✨ Ideal para: ${plan.idealPara}\n\n📋 Incluye:\n${plan.incluye.map(item => `• ${item}`).join('\n')}\n\n¿Te gustaría cotizar este plan?`;
    }

    formatearDestino(destino) {
        return `🏛️ **${destino.nombre}**\n\n${destino.descripcion}\n\n✨ Destacados:\n${destino.highlights.map(item => `• ${item}`).join('\n')}\n\n💡 Tips:\n${destino.tips.map(item => `• ${item}`).join('\n')}\n\n¿Quieres incluirlo en tu viaje?`;
    }

    formatearMultiplesResultados(resultados) {
        let respuesta = "Encontré varias opciones:\n\n";
        
        resultados.forEach((resultado, index) => {
            if (resultado.tipo === 'plan') {
                respuesta += `${index + 1}. 🗺️ ${resultado.data.nombre} - ${resultado.data.precio}\n`;
            } else if (resultado.tipo === 'destino') {
                respuesta += `${index + 1}. 🏛️ ${resultado.data.nombre}\n`;
            }
        });

        respuesta += "\n¿Cuál te interesa más?";
        return respuesta;
    }

    obtenerRespuestaCotizacion(datos) {
        return `Perfecto, viajero! 🤠 Para cotizar tu viaje necesito:\n\n👤 Personas: ${datos.personas || '¿Cuántas?'}\n📅 Fecha: ${datos.fecha || '¿Cuándo?'}\n🎯 Intereses: ${datos.intereses || '¿Qué prefieres?'}\n\nCuéntame estos detalles y te preparo una cotización especial con descuento.`;
    }
}

module.exports = new KnowledgeBase();