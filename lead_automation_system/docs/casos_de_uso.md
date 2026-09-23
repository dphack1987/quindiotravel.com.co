# 📚 Casos de Uso - Sistema de Automatización de Leads

Documentación detallada de casos de uso para el sistema de automatización de leads de Quindío Travel.

---

## 🎯 Caso de Uso Principal: Lograr 4+ Reservas Mensuales

### **Actor Principal:** Operador Turístico (Álvaro Alzate Ortiz)
### **Objetivo:** Lograr mínimo 4 reservas confirmadas por mes mediante automatización inteligente de leads.

---

## 📋 Casos de Uso Específicos

### **CU-01: Captura y Calificación Automática de Leads**

**Descripción:** El sistema debe capturar automáticamente leads desde el sitio web y calificarlos según su probabilidad de conversión.

**Actor:** Sistema Python + Integración Web

**Precondiciones:**
- Sistema Python está ejecutándose
- Sitio web tiene el script de integración cargado
- API Flask está disponible

**Flujo Principal:**
1. Usuario completa formulario de cotización en el sitio web
2. Script JavaScript captura datos del formulario
3. Datos se envían a API Python (`POST /api/lead`)
4. Sistema calcula score del lead (0-100 puntos)
5. Sistema categoriza lead (Hot/Warm/Cold)
6. Sistema predice probabilidad de conversión
7. Sistema programa seguimientos automáticos
8. Sistema envía mensaje inicial por WhatsApp según categoría

**Postcondiciones:**
- Lead guardado en base de datos con score y predicción
- Seguimientos programados automáticamente
- Mensaje inicial enviado por WhatsApp
- Dashboard actualizado con nuevo lead

**Resultado Esperado:**
- Lead calificado en menos de 5 segundos
- Seguimientos programados sin intervención manual
- Prioridad de atención determinada automáticamente

---

### **CU-02: Seguimiento Automatizado por Tipo de Lead**

**Descripción:** El sistema debe ejecutar seguimientos personalizados según la categoría del lead.

**Actor:** Sistema Python (Motor de Follow-up)

**Precondiciones:**
- Lead previamente calificado y almacenado
- WhatsApp Business API configurada
- Plantillas de mensajes configuradas

**Flujo Principal:**

**Para Leads Calientes (Hot Lead - 70+ puntos):**
1. Sistema envía mensaje inmediato (mismo día)
2. Sistema programa seguimiento en 2 días
3. Sistema programa seguimiento en 1 semana
4. Sistema programa seguimiento en 2 semanas
5. Cada mensaje personalizado con nombre del cliente

**Para Leads Tibios (Warm Lead - 50-69 puntos):**
1. Sistema envía mensaje al día siguiente
2. Sistema programa seguimiento en 3 días
3. Sistema programa seguimiento en 1 semana
4. Sistema programa seguimiento en 2 semanas
5. Sistema programa seguimiento en 1 mes

**Para Leads Fríos (Cold Lead - <50 puntos):**
1. Sistema envía mensaje informativo en 1 semana
2. Sistema programa seguimiento en 2 semanas
3. Sistema programa seguimiento en 1 mes
4. Sistema programa seguimiento en 2 meses
5. Mensajes enfocados en nurturing y educación

**Postcondiciones:**
- Seguimientos ejecutados según programación
- Historial de comunicaciones registrado
- Estado del lead actualizado tras cada interacción

**Resultado Esperado:**
- 100% de leads reciben seguimiento oportuno
- Ningún lead es olvidado o perdido
- Personalización basada en categoría de lead

---

### **CU-03: Identificación de Leads de Alta Prioridad**

**Descripción:** El sistema debe identificar automáticamente leads que requieren atención inmediata y alertar al operador.

**Actor:** Sistema Python + Dashboard Web

**Precondiciones:**
- Sistema está ejecutándose tareas diarias
- Dashboard web está accesible
- Leads existen en base de datos

**Flujo Principal:**
1. Sistema ejecuta análisis diario (09:00, 14:00, 18:00)
2. Sistema identifica leads calientes creados en últimas 24 horas
3. Sistema calcula horas desde procesamiento
4. Sistema genera alerta de alta prioridad
5. Dashboard muestra alertas en tiempo real
6. Sistema recomienda acción específica

**Criterios de Alta Prioridad:**
- Score ≥ 70 puntos (Hot Lead)
- Creado en últimas 24 horas
- No ha recibido respuesta humana
- Presupuesto indicado ≥ $1M COP

**Postcondiciones:**
- Alertas visibles en dashboard
- Recomendaciones de acción específicas
- Sistema continúa monitoreando

**Resultado Esperado:**
- Operador identifica leads prometedores instantáneamente
- Tiempo de respuesta reducido a <15 minutos
- Priorización basada en datos, no intuición

---

### **CU-04: Análisis Predictivo de Conversión**

**Descripción:** El sistema debe predecir la probabilidad de conversión de cada lead basándose en datos históricos.

**Actor:** Sistema Python (Módulo Analytics)

**Precondiciones:**
- Histórico de conversiones disponible
- Lead nuevo capturado con datos completos
- Algoritmo de predicción entrenado

**Flujo Principal:**
1. Sistema recibe datos de nuevo lead
2. Sistema busca leads similares en historial
3. Sistema analiza patrones de conversión
4. Sistema calcula probabilidad de conversión (0-100%)
5. Sistema identifica factores que aumentan probabilidad
6. Sistema genera recomendación de acción

**Factores Analizados:**
- Presupuesto indicado vs. histórico
- Destino de interés vs. éxito histórico
- Número de personas vs. patrones
- Temporada de consulta vs. tendencias
- Comportamiento en sitio web
- Dispositivo utilizado

**Postcondiciones:**
- Probabilidad de conversión calculada
- Factores de conversión identificados
- Recomendación de acción generada

**Resultado Esperado:**
- Operador puede priorizar leads por probabilidad
- Enfoque en leads con mayor conversión esperada
- Optimización de tiempo y recursos

---

### **CU-05: Generación de Reportes de Conversión**

**Descripción:** El sistema debe generar reportes automáticos de rendimiento y progreso hacia objetivos.

**Actor:** Sistema Python + Dashboard Web

**Precondiciones:**
- Sistema tiene datos de leads y conversiones
- Período de análisis especificado
- Objetivos de conversión configurados

**Flujo Principal:**
1. Sistema ejecuta análisis de período especificado
2. Sistema calcula tasa de conversión
3. Sistema analiza períodos pico de alta conversión
4. Sistema calcula potencial de ingresos
5. Sistema genera recomendaciones estratégicas
6. Sistema compara vs. objetivos mensuales
7. Sistema guarda reporte en formato JSON

**Métricas Incluidas:**
- Tasa de conversión actual vs. objetivo
- Total leads vs. conversiones
- Leads por categoría (Hot/Warm/Cold)
- Períodos pico (mes, día, hora)
- Potencial de ingresos del pipeline
- Efectividad de seguimientos

**Postcondiciones:**
- Reporte generado y guardado
- Dashboard actualizado con métricas
- Recomendaciones disponibles

**Resultado Esperado:**
- Visibilidad clara del progreso hacia objetivo
- Decisiones basadas en datos
- Identificación de áreas de mejora

---

### **CU-06: Gestión de Backups Automatizados**

**Descripción:** El sistema debe crear backups automáticos de todos los datos con diferentes frecuencias.

**Actor:** Sistema Python (Backup Scheduler)

**Precondiciones:**
- Sistema de backup configurado
- Espacio en disco disponible
- Directorio de backups accesible

**Flujo Principal:**

**Backup Diario (02:00 AM):**
1. Sistema crea backup completo de datos
2. Sistema guarda con timestamp
3. Sistema limpia backups más antiguos de 7 días
4. Sistema registra operación en log

**Backup Semanal (Domingos 03:00 AM):**
1. Sistema crea backup completo
2. Sistema nombra como "weekly_backup_YYYYMMDD.zip"
3. Sistema limpia backups semanales más antiguos de 4 semanas
4. Sistema registra operación

**Backup Mensual (Día 1 04:00 AM):**
1. Sistema crea backup completo
2. Sistema nombra como "monthly_backup_YYYYMM.zip"
3. Sistema limpia backups mensuales más antiguos de 6 meses
4. Sistema registra operación

**Postcondiciones:**
- Backups creados según programación
- Espacio optimizado mediante limpieza
- Logs de operaciones disponibles

**Resultado Esperado:**
- Datos protegidos contra pérdida
- Recuperación posible en cualquier momento
- Espacio de disco optimizado

---

### **CU-07: Restauración Controlada de Datos**

**Descripción:** El sistema debe permitir restauración de datos con validación y opciones de rollback.

**Actor:** Operador + Sistema Python (Restore Manager)

**Precondiciones:**
- Backup disponible y validado
- Sistema no está procesando leads activos
- Espacio suficiente para restauración

**Flujo Principal:**
1. Operador selecciona backup a restaurar
2. Sistema valida integridad del backup
3. Sistema crea backup de seguridad
4. Sistema muestra preview del contenido
5. Operador confirma restauración
6. Sistema ejecuta restauración
7. Sistema valida datos restaurados
8. Sistema registra operación en log

**Opciones Disponibles:**
- Restauración completa
- Restauración selectiva (archivos específicos)
- Restauración con validación
- Rollback desde backup de seguridad

**Postcondiciones:**
- Datos restaurados correctamente
- Validación de integridad completada
- Backup de seguridad disponible
- Operación registrada en log

**Resultado Esperado:**
- Recuperación de datos sin pérdida
- Opción de reversión disponible
- Confianza en el proceso de restauración

---

### **CU-08: Monitoreo en Tiempo Real via Dashboard**

**Descripción:** El sistema debe proporcionar visibilidad en tiempo real del estado de leads y conversión.

**Actor:** Operador + Dashboard Web

**Precondiciones:**
- Dashboard web accesible
- API Python ejecutándose
- Navegador web moderno

**Flujo Principal:**
1. Operador accede a dashboard
2. Sistema carga estadísticas principales
3. Sistema muestra leads recientes
4. Sistema muestra alertas de alta prioridad
5. Sistema muestra tasa de conversión
6. Sistema actualiza datos cada 5 minutos
7. Operador puede ejecutar acciones rápidas

**Funcionalidades del Dashboard:**
- Estadísticas en tiempo real (leads, conversiones, categorías)
- Tabla de leads recientes con scores
- Alertas de alta prioridad con recomendaciones
- Gráfico de progreso hacia objetivo mensual
- Botones para acciones rápidas (ejecutar tareas, generar reportes)
- Actualización automática cada 5 minutos

**Postcondiciones:**
- Visibilidad completa del pipeline
- Alertas de oportunidades disponibles
- Acciones ejecutables desde dashboard

**Resultado Esperado:**
- Toma de decisiones informada
- Respuesta rápida a oportunidades
- Monitoreo continuo sin esfuerzo manual

---

### **CU-09: Exportación e Importación de Datos**

**Descripción:** El sistema debe permitir exportación e importación de datos para análisis externo y migración.

**Actor:** Operador + Sistema Python (Data Manager)

**Precondiciones:**
- Datos disponibles en sistema
- Permisos de archivo otorgados
- Formato de archivo compatible

**Flujo Principal (Exportación):**
1. Operador solicita exportación
2. Sistema selecciona datos a exportar
3. Sistema convierte a formato CSV
4. Sistema guarda archivo en directorio de exports
5. Sistema confirma exportación completada

**Flujo Principal (Importación):**
1. Operador selecciona archivo CSV
2. Sistema valida formato del archivo
3. Sistema procesa datos del archivo
4. Sistema detecta duplicados (si merge)
5. Sistema integra datos existentes con nuevos
6. Sistema confirma importación completada

**Opciones Disponibles:**
- Exportar todos los leads o filtrados
- Importar con merge o reemplazo
- Validación de integridad antes de importar
- Preview de datos antes de importar

**Postcondiciones:**
- Datos exportados en formato estándar
- Datos importados validados e integrados
- Historial de operaciones registrado

**Resultado Esperado:**
- Flexibilidad para análisis externo
- Capacidad de migración entre sistemas
- Integridad de datos mantenida

---

### **CU-10: Ejecución de Pruebas de Calidad**

**Descripción:** El sistema debe permitir ejecución de pruebas automáticas para verificar funcionamiento correcto.

**Actor:** Desarrollador + Sistema Python (Test Suite)

**Precondiciones:**
- Sistema de pruebas instalado
- Dependencias de prueba disponibles
- Ambiente de prueba configurado

**Flujo Principal:**
1. Operador ejecuta script de pruebas
2. Sistema carga suite de pruebas
3. Sistema ejecuta pruebas unitarias
4. Sistema genera reporte de resultados
5. Sistema muestra pruebas exitosas y fallidas
6. Sistema indica estado general del sistema

**Categorías de Pruebas:**
- Lead Scoring Engine
- Analytics Module
- Followup Engine
- Data Management
- Backup/Restore System

**Opciones Disponibles:**
- Ejecutar todas las pruebas
- Ejecutar pruebas de módulo específico
- Ejecutar pruebas rápidas (smoke tests)
- Ejecución con reporte detallado

**Postcondiciones:**
- Estado del sistema verificado
- Problemas identificados
- Confianza en funcionamiento

**Resultado Esperado:**
- Detección temprana de problemas
- Confianza en estabilidad del sistema
- Documentación de calidad del código

---

## 🎯 Escenarios de Uso Completos

### **Escenario 1: Día Típico de Operación**

**Contexto:** Operador comienza su día laboral.

**Flujo:**
1. **08:00 AM** - Operador revisa dashboard
2. **08:05 AM** - Sistema muestra 3 leads de alta prioridad
3. **08:10 AM** - Operador llama a lead más prometedor
4. **08:30 AM** - Lead convierte en reserva (1/4 objetivo)
5. **09:00 AM** - Sistema ejecuta tareas diarias automáticamente
6. **09:05 AM** - Sistema envía 5 seguimientos programados
7. **10:00 AM** - Operador recibe nuevo lead via formulario web
8. **10:01 AM** - Sistema califica lead automáticamente (Hot Lead)
9. **10:02 AM** - Sistema envía mensaje WhatsApp inmediato
10. **14:00 PM** - Sistema ejecuta tareas diarias (segunda ronda)
11. **18:00 PM** - Sistema ejecuta tareas diarias (tercera ronda)
12. **20:00 PM** - Operador revisa dashboard del día
13. **20:05 PM** - Sistema muestra progreso: 1/4 conversiones

**Resultado:** Lead calificado automáticamente, seguimientos ejecutados sin intervención, 1 reserva confirmada.

---

### **Escenario 2: Recuperación de Datos**

**Contexto:** Error del sistema causó corrupción de datos.

**Flujo:**
1. Operador detecta problema en datos
2. Operador accede a restore manager
3. Sistema lista backups disponibles
4. Operador selecciona backup más reciente
5. Sistema valida integridad del backup
6. Sistema crea backup de seguridad
7. Sistema muestra preview del contenido
8. Operador confirma restauración
9. Sistema ejecuta restauración
10. Sistema valida datos restaurados
11. Sistema confirma restauración exitosa
12. Operador verifica funcionamiento normal

**Resultado:** Datos restaurados completamente, sistema operativo, cero pérdida de información.

---

### **Escenario 2: Optimización Mensual**

**Contexto:** Fin de mes, análisis de rendimiento.

**Flujo:**
1. Sistema genera reporte mensual automáticamente
2. Operador accede a dashboard
3. Sistema muestra tasa de conversión: 8.5%
4. Sistema muestra 4 conversiones logradas (objetivo cumplido)
5. Sistema identifica períodos pico: viernes 15:00-17:00
6. Sistema recomienda incrementar disponibilidad esos horarios
7. Operador ajusta configuración de scoring según insights
8. Sistema aplica nuevos pesos de scoring
9. Operador exporta datos para análisis externo
10. Sistema limpia backups antiguos automáticamente

**Resultado:** Objetivo mensual cumplido, insights para optimización siguiente mes.

---

## 📊 Métricas de Éxito del Sistema

### **KPIs Principales:**
- **Reservas mensuales:** 4+ conversiones
- **Tasa de conversión:** 8-12% (vs 2-3% sin sistema)
- **Tiempo de respuesta:** <15 minutos para leads calientes
- **Seguimientos ejecutados:** 100% de leads programados
- **Leads calificados:** 100% de leads capturados

### **KPIs Operativos:**
- **Backups automáticos:** 100% de programaciones ejecutadas
- **Uptime del sistema:** >99%
- **Pruebas unitarias:** 100% pasando
- **Dashboard disponible:** 24/7

---

## 🔒 Consideraciones de Seguridad

### **Protección de Datos:**
- Todos los datos almacenados localmente
- Tokens de API en variables de entorno
- Backups encriptados opcionales
- Logs de acceso registrados

### **Recuperación de Desastres:**
- Backups diarios/semanales/mensuales
- Validación de integridad de backups
- Proceso de restauración con rollback
- Sistema de logs de operaciones

---

## 🚀 Roadmap de Implementación

### **Fase 1: Prueba (Mes 1)**
- Instalación y configuración básica
- Prueba de lead scoring manual
- Validación de seguimientos
- Objetivo: 2-3 reservas

### **Fase 2: Integración (Mes 2)**
- Integración con sitio web
- Activación de dashboard
- Optimización de reglas
- Objetivo: 3-4 reservas

### **Fase 3: Producción (Mes 3+)**
- Sistema completamente automatizado
- Análisis predictivo activo
- Optimización continua
- Objetivo: 4+ reservas consistentes

---

Esta documentación proporciona una guía completa para entender y utilizar el sistema de automatización de leads para lograr el objetivo de 4+ reservas mensuales.