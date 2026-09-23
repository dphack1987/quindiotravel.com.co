# 🚀 Guía de Inicio Rápido - Sistema de Automatización de Leads

Guía paso a paso para comenzar a usar el sistema en menos de 15 minutos.

---

## ⏱️ **Tiempo Estimado: 10-15 minutos**

---

## 📋 **Requisitos Previos**

- ✅ Python 3.8+ instalado
- ✅ Acceso a internet (para instalar dependencias)
- ✅ Espacio en disco (~50MB)
- ✅ Número de WhatsApp Business (opcional para inicio)

---

## 🎯 **Objetivo de Esta Guía**

Configurar el sistema básico y procesar tu primer lead de prueba para ver cómo funciona el lead scoring automático.

---

## 🚀 **PASO 1: Instalación Automática (2 minutos)**

### **Opción A: Instalación Completa**
```bash
cd lead_automation_system
python install.py
```

El script verificará:
- ✅ Versión de Python compatible
- ✅ Estructura de archivos completa
- ✅ Dependencias instaladas
- ✅ Datos iniciales creados
- ✅ Pruebas del sistema ejecutadas

### **Opción B: Instalación Manual**
```bash
cd lead_automation_system
pip install -r requirements.txt
```

---

## 🎯 **PASO 2: Configuración Inicial (3 minutos)**

### **Opción A: Wizard Interactivo (Recomendado)**
```bash
python setup_wizard.py
```

El wizard te guiará a través de:
1. 📱 Configuración de WhatsApp (puedes dejar vacío al inicio)
2. 🏢 Información del negocio
3. 🎯 Umbrales de lead scoring
4. 📅 Programación de seguimientos
5. 📊 Objetivos de conversión

### **Opción B: Configuración Manual**
- Usa los valores por defecto en `config.py`
- El sistema funcionará sin configuración adicional

---

## 🎯 **PASO 3: Primera Prueba (2 minutos)**

### **Ejecutar Sistema en Modo Interactivo**
```bash
python main.py
```

Selecciona opción `1` para **Modo Interactivo**.

### **Procesar Lead de Prueba**
Selecciona opción `1` para **Procesar nuevo lead**.

Ingresa datos de prueba:
```
Nombre: Juan Pérez
Teléfono: 573000000000
Mensaje: Hola, estoy interesado en un plan al Valle de Cocora para 4 personas con presupuesto de 2 millones de pesos
Destino: Valle de Cocora
Fecha deseada: 2026-10-15
Número de personas: 4
Presupuesto: 2000000
```

### **Resultado Esperado**
```
📥 Procesando nuevo lead: Juan Pérez
🎯 Score: 85/100 - Categoría: hot_lead
🔮 Probabilidad de conversión: 75.5%
📅 Seguimientos programados: 4
📱 Mensaje lead caliente enviado: True
✅ Lead procesado y guardado: lead_20261023_123456
```

---

## 🎯 **PASO 4: Ver Dashboard (1 minuto)**

### **Abrir Dashboard**
Abre el archivo `dashboard.html` en tu navegador web.

### **Lo que Verás**
- 📊 Estadísticas del sistema
- 🔥 Leads calientes identificados
- 📈 Tasa de conversión
- 🚨 Alertas de alta prioridad
- ⚡ Botones de acciones rápidas

---

## 🎯 **PASO 5: Probar Integración Web (Opcional - 2 minutos)**

### **Iniciar API Web**
```bash
python web_integration.py
```

### **Agregar Script a Tu Sitio**
Agrega esta línea a tu `index.html` antes de `</body>`:
```html
<script src="assets/js/lead-automation-integration.js"></script>
```

### **Probar Formulario**
Completa tu formulario de cotización existente en el sitio web.
El sistema capturará automáticamente los datos y los procesará.

---

## 🎯 **PASO 6: Verificar Funcionamiento (1 minuto)**

### **Ejecutar Pruebas Rápidas**
```bash
python run_tests.py --quick
```

### **Resultado Esperado**
```
🧪 Ejecutando Pruebas Rápidas (Smoke Tests)
======================================================
test_hot_lead_scoring ... ok
test_warm_lead_scoring ... ok
test_cold_lead_scoring ... ok
test_conversion_rate_calculation ... ok
test_conversion_probability_prediction ... ok

🎉 ¡TODAS LAS PRUEBAS PASARON EXITOSAMENTE!
```

---

## 🎯 **PASO 7: Ver Backup Automático (1 minuto)**

### **Crear Backup Manual**
```bash
python utils/data_manager.py backup
```

### **Resultado Esperado**
```
✅ Backup creado exitosamente
📁 Archivo: backup_20261023_123456.zip
📊 Tamaño: 0.15 MB
```

---

## 🎯 **PASO 8: Revisar Estadísticas (1 minuto)**

### **Ver Estadísticas del Sistema**
```bash
python utils/data_manager.py stats
```

### **Resultado Esperado**
```
📊 ESTADÍSTICAS DE DATOS
==================================================
Total leads: 1
Leads por categoría:
  - hot_lead: 1
  - warm_lead: 0
  - cold_lead: 0

Backups: 1 archivos
Exports: 0 archivos
Reports: 0 archivos
```

---

## 🎉 **¡SISTEMA LISTO PARA USAR!**

### **Lo que Has Logrado:**
- ✅ Sistema instalado y configurado
- ✅ Primer lead procesado y calificado
- ✅ Dashboard funcionando
- ✅ Backup automático activo
- ✅ Pruebas unitarias pasando

### **Próximos Pasos Recomendados:**

**Día 1:**
- Procesar 3-5 leads reales
- Revisar scores y ajustar reglas si es necesario
- Familiarizarte con el dashboard

**Semana 1:**
- Integrar completamente con tu sitio web
- Activar modo programado para automatización
- Monitorear primeras conversiones

**Mes 1:**
- Ajustar reglas de scoring según resultados
- Optimizar plantillas de mensajes
- Alcanzar 2-3 conversiones

---

## 🔧 **Comandos Útiles**

### **Operaciones Diarias:**
```bash
# Ejecutar tareas diarias manualmente
python main.py  # Modo interactivo > opción 2

# Ver leads de alta prioridad
python main.py  # Modo interactivo > opción 4

# Generar reporte mensual
python main.py  # Modo interactivo > opción 3
```

### **Gestión de Datos:**
```bash
# Crear backup
python utils/data_manager.py backup

# Exportar leads a CSV
python utils/data_manager.py export

# Ver estadísticas
python utils/data_manager.py stats

# Validar integridad
python utils/data_manager.py validate
```

### **Sistema de Backups:**
```bash
# Backup inmediato
python utils/backup_scheduler.py --mode immediate --type daily

# Ver estado de backups
python utils/backup_scheduler.py --mode status

# Programar backups automáticos
python utils/backup_scheduler.py --mode schedule
```

### **Pruebas:**
```bash
# Ejecutar todas las pruebas
python run_tests.py

# Ejecutar solo pruebas rápidas
python run_tests.py --quick

# Ejecutar pruebas de módulo específico
python run_tests.py --module test_lead_scoring
```

---

## 🚨 **Solución de Problemas Rápidos**

### **Problema: "No module named 'requests'"**
```bash
pip install requests
```

### **Problema: "Archivo config.py no encontrado"**
```bash
# Ejecuta el wizard de configuración
python setup_wizard.py
```

### **Problema: "Error al conectar con API"**
- Verifica que `web_integration.py` esté ejecutándose
- Verifica que el puerto 5000 esté disponible
- Revisa el firewall de tu computadora

### **Problema: "No se crean archivos de datos"**
```bash
# Ejecuta el instalador completo
python install.py --step structure
```

---

## 📊 **Expectativas Realistas**

### **Primeras 24 Horas:**
- Sistema instalado y funcionando
- 1-3 leads procesados
- Dashboard mostrando datos
- Seguimientos programados

### **Primera Semana:**
- 10-20 leads procesados
- Sistema aprendiendo tu patrón de leads
- 1-2 conversiones posibles
- Ajustes de scoring según resultados

### **Primer Mes:**
- 50+ leads procesados
- 2-3 conversiones esperadas
- Sistema optimizado
- Objetivo de 4 conversiones alcanzable

---

## 🎯 **Consejos para Éxito**

### **Para Lograr 4+ Reservas Mensales:**

1. **Calidad > Cantidad**
   - Enfócate en leads bien calificados
   - Prioriza leads calientes sobre volumen

2. **Respuesta Rápida**
   - Responde a leads calientes en <15 minutos
   - Usa las alertas del dashboard

3. **Personalización**
   - Ajusta plantillas de mensajes a tu estilo
   - Usa el nombre del cliente siempre

4. **Monitoreo Continuo**
   - Revisa el dashboard diariamente
   - Ajusta reglas según resultados

5. **Paciencia con el Sistema**
   - El sistema necesita datos para aprender
   - Los primeros días son de entrenamiento

---

## 🆘 **Soporte y Ayuda**

### **Documentación Disponible:**
- `README.md` - Documentación completa
- `docs/casos_de_uso.md` - Casos de uso detallados
- Comentarios en código - Documentación inline

### **Problemas Técnicos:**
- Revisa la sección de troubleshooting
- Ejecuta pruebas para identificar problemas
- Verifica logs del sistema

---

## 🎉 **¡Felicidades!**

Has completado la configuración inicial del Sistema de Automatización de Leads.

**El sistema está listo para ayudarte a lograr tu objetivo de 4+ reservas mensuales.**

**Siguiente paso:** Comienza a procesar leads reales y monitorea los resultados en el dashboard.

🚀 **¡Buena suerte con tus 4+ reservas mensuales!**