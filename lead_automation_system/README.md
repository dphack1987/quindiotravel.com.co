# 🚀 Sistema de Automatización de Leads - Quindío Travel

Sistema Python avanzado para lograr **4+ reservas confirmadas al mes** mediante automatización inteligente de leads, lead scoring y seguimiento personalizado.

## 🎯 Objetivo del Sistema

Lograr mínimo **4 reservas confirmadas por mes** optimizando:
- **Calificación automática de leads** (Lead Scoring)
- **Seguimiento personalizado** por tipo de lead
- **Integración WhatsApp Business API** para comunicación automatizada
- **Análisis predictivo** de probabilidad de conversión
- **Alertas prioritarias** para leads de alta conversión

## 📁 Estructura del Sistema

```
lead_automation_system/
├── main.py                 # Orquestador principal
├── config.py               # Configuración del sistema
├── requirements.txt        # Dependencias Python
├── README.md              # Esta documentación
├── data/
│   ├── leads_db.json       # Base de datos de leads
│   ├── conversion_data.json # Datos históricos de conversiones
│   ├── scoring_rules.json   # Reglas de calificación
│   └── reports/           # Reportes generados
├── modules/
│   ├── lead_scoring.py     # Motor de lead scoring
│   ├── whatsapp_bot.py     # Integración WhatsApp Business API
│   ├── followup_engine.py  # Motor de follow-up automatizado
│   └── analytics.py        # Análisis de datos y métricas
└── utils/
    └── message_templates.json # Plantillas de mensajes
```

## 🛠️ Instalación y Configuración

### 1. Requisitos Previos
- Python 3.8+
- Token de WhatsApp Business API (obtener en [Facebook Developers](https://developers.facebook.com/docs/whatsapp/business-api))
- Número de WhatsApp Business (+57 317 442 6044)

### 2. Instalación de Dependencias
```bash
cd lead_automation_system
pip install -r requirements.txt
```

### 3. Configuración de Variables de Entorno
Crear archivo `.env` con las siguientes variables:
```env
WHATSAPP_API_TOKEN=tu_token_de_whatsapp_business_api
WHATSAPP_BUSINESS_ID=tu_business_id
```

### 4. Inicialización del Sistema
El sistema se inicializa automáticamente en la primera ejecución, creando:
- Estructura de directorios
- Archivos de datos base
- Plantillas de mensajes
- Reglas de scoring

## 🚀 Uso del Sistema

### Modo Interactivo
```bash
python main.py
```
Seleccionar opción `1` para modo interactivo.

Comandos disponibles:
1. Procesar nuevo lead
2. Ejecutar tareas diarias
3. Generar reporte mensual
4. Ver leads de alta prioridad
5. Ver estadísticas
6. Salir

### Modo Programado (Automático)
```bash
python main.py
```
Seleccionar opción `2` para modo programado.

Tareas automáticas:
- Ejecución diaria: 09:00, 14:00, 18:00
- Reporte mensual: Primer día de cada mes

## 📊 Funcionalidades Principales

### 1. Lead Scoring Inteligente
El sistema califica cada lead en 3 categorías:
- **Hot Lead (70+ puntos)**: Llamada inmediata, seguimiento intensivo
- **Warm Lead (50-69 puntos)**: Seguimiento personalizado en 24 horas
- **Cold Lead (<50 puntos)**: Seguimiento estándar, campañas de nurturing

**Factores de scoring:**
- Señales de interés (mención de plan, fecha, presupuesto)
- Señales de calidad (destino relevante, presupuesto razonable)
- Señales de comportamiento (páginas vistas, tiempo en sitio)
- Señales de timing (hora de consulta, temporada)

### 2. WhatsApp Business API Integration
Automatización de comunicación:
- Envío de mensajes personalizados por tipo de lead
- Seguimientos programados automáticamente
- Plantillas de mensajes dinámicas
- Tracking de entregas y lecturas

### 3. Motor de Follow-up Automatizado
Programación inteligente de seguimientos:
- **Hot Lead**: Hoy, 2 días, 1 semana, 2 semanas
- **Warm Lead**: Mañana, 3 días, 1 semana, 2 semanas, 1 mes
- **Cold Lead**: 1 semana, 2 semanas, 1 mes, 2 meses

### 4. Análisis Predictivo
Predicción de probabilidad de conversión:
- Análisis de leads similares históricos
- Identificación de factores de conversión
- Recomendaciones de acción basadas en probabilidad

### 5. Alertas Prioritarias
Sistema de alertas para leads de alta prioridad:
- Identificación automática de leads calientes
- Recomendaciones de acción inmediata
- Sistema de priorización basado en score

## 📈 Métricas y KPIs

### Objetivos del Sistema
- **Reservas mensuales**: 4+ conversiones
- **Tasa de conversión objetivo**: 8%
- **Leads necesarios**: 50 leads/mes
- **Lead de alto valor**: Presupuesto > $1M COP

### Métricas Rastreadas
- Tasa de conversión por período
- Tiempo de respuesta a leads
- Efectividad de seguimientos
- Probabilidad de conversión por lead
- Ingresos potenciales del pipeline

## 🔧 Personalización

### Modificar Reglas de Scoring
Editar `data/scoring_rules.json` para ajustar pesos de calificación:
```json
{
  "interest_signals": {
    "specific_plan_mentioned": 15,
    "date_range_provided": 12,
    ...
  }
}
```

### Personalizar Plantillas de Mensajes
Editar `utils/message_templates.json` para ajustar mensajes:
```json
{
  "hot_lead": {
    "immediate": [
      "🌟 ¡Hola {nombre}! Gracias por tu interés...",
      ...
    ]
  }
}
```

### Ajustar Configuración
Editar `config.py` para modificar:
- Umbrales de scoring
- Horarios de envío
- Límites de mensajes diarios
- Objetivos de conversión

## 🚨 Configuración WhatsApp Business API

### Obtener Token
1. Crear cuenta en [Meta for Developers](https://developers.facebook.com/)
2. Crear aplicación WhatsApp Business
3. Obtener Access Token y Business ID
4. Configurar webhooks para recibir mensajes

### Configurar Webhook
El sistema puede integrarse con webhooks para:
- Recibir mensajes de clientes
- Actualizar estado de mensajes
- Sincronizar conversaciones en tiempo real

## 📊 Reportes Generados

### Reportes Diarios
Guardados en `data/reports/daily_YYYYMMDD.json`:
- Progreso de objetivos
- Estadísticas de seguimientos
- Mensajes enviados
- Leads de alta prioridad

### Reportes Mensuales
Guardados en `data/reports/monthly_YYYYMM.json`:
- Análisis completo de conversión
- Períodos pico de alta conversión
- Potencial de ingresos
- Recomendaciones estratégicas

## 🔒 Seguridad y Privacidad

- Datos almacenados localmente en JSON
- Tokens de API en variables de entorno
- No se comparten datos personales con terceros
- Cumplimiento con regulaciones de privacidad

## 🚀 Próximas Mejoras

- [ ] Integración con CRM existente
- [ ] Interfaz web para administración
- [ ] Dashboard en tiempo real
- [ ] Integración con Google Analytics
- [ ] Sistema de tickets de soporte
- [ ] Predicción de cancelaciones
- [ ] Optimización de precios dinámica

## 📞 Soporte

Para problemas o consultas:
- WhatsApp: +57 317 442 6044
- Email: gerencia@quindiotravel.net
- RNT: 18152

## 📄 Licencia

Sistema propietario de Quindío Travel - RNT 18152

---

**Quindío Travel - Operador Turístico Certificado RNT 18152**
🌿 Especialistas en turismo del Eje Cafetero
📱 +57 317 442 6044
🌐 https://quindiotravel.com.co