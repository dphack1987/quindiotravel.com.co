# Guía de Configuración: Google Analytics 4

## Paso 1: Crear cuenta de Google Analytics

1. Accede a [https://analytics.google.com](https://analytics.google.com)
2. Inicia sesión con tu cuenta de Google (gerencia@quindiotravel.net)
3. Haz clic en "Empezar a medir"
4. Ingresa el nombre de la cuenta: "Quindío Travel"
5. Crea una propiedad: "Sitio Web Quindío Travel"
6. Selecciona zona horaria: "Colombia - Bogota"
7. Selecciona moneda: "Peso colombiano (COP)"

## Paso 2: Configurar flujo de datos web

1. Ingresa la URL del sitio: `https://quindiotravel.com.co/`
2. Nombre del flujo de datos: "Sitio Web Principal"
3. Mejora de medición: Actívala (recomendado)
4. Haz clic en "Crear flujo de datos"

## Paso 3: Instalar etiqueta de seguimiento

### Opción A: Google Tag Manager (Recomendado)
1. Copia el ID de medición (G-XXXXXXXXXX)
2. Actualiza el código GA4 existente en `index.html`
3. Verifica que esté en el `<head>` del sitio

### Opción B: Etiqueta Global de Sitio (gtag.js)
1. Copia el código de seguimiento proporcionado
2. Pégalo en el `<head>` de todas las páginas
3. Asegúrate de estar antes de cualquier otro script

## Paso 4: Verificar instalación

1. Usa la "Asistente de etiquetas" de GA4
2. Instala la extensión de Chrome "Google Tag Assistant"
3. Navega por el sitio y verifica que se registren eventos
4. Espera 24-48 horas para que aparezcan datos en GA4

## Paso 5: Configurar conversiones

### Eventos de conversión automáticos
GA4 configura automáticamente estos eventos:
- `page_view`: Cada vez que se visita una página
- `session_start`: Cuando comienza una sesión
- `first_visit`: Primera visita del usuario
- `user_engagement`: Interacción con el sitio

### Eventos personalizados a configurar
1. Ve a "Configurar" > "Eventos"
2. Crea eventos personalizados para:
   - `whatsapp_click`: Clic en botón de WhatsApp
   - `plan_view`: Visualización de planes individuales
   - `contact_form_submit`: Envío de formulario de contacto
   - `language_change`: Cambio de idioma

## Paso 6: Configurar objetivos de conversión

1. Ve a "Configurar" > "Conversiones"
2. Marca como conversiones los eventos clave:
   - `whatsapp_click` (contacto directo)
   - `contact_form_submit` (generación de leads)
   - `first_visit` (adquisición de usuarios)

## Paso 7: Configurar audiencias

1. Ve a "Configurar" > "Definiciones de audiencia"
2. Crea audiencias útiles:
   - "Usuarios interesados en planes turísticos"
   - "Visitantes de páginas de destinos"
   - "Usuarios que cambiaron idioma"
   - "Visitantes recurrentes"

## Paso 8: Configurar enlaces de atribución

1. Ve a "Configurar" > "Enlaces de atribución"
2. Activa "Google Ads" si usas publicidad
3. Configura modelo de atribución: "Basado en datos" (recomendado)

## Paso 9: Configurar exportación de datos

1. Ve a "Administrador" > "Configuración de exportación de datos"
2. Conecta con BigQuery si necesitas análisis avanzado
3. Configura exportaciones automáticas si lo requieres

## Paso 10: Configurar informes personalizados

### Informes de exploración
1. Ve a "Explorar" en el menú izquierdo
2. Crea informes personalizados:
   - "Rendimiento por destino"
   - "Conversión por idioma"
   - "Tráfico móvil vs desktop"
   - "Rutas de conversión"

### Informes de ciclo de vida
1. Ve a "Ciclo de vida" en el menú izquierdo
2. Configura:
   - **Adquisición**: Fuentes de tráfico, campañas
   - **Compromiso**: Tiempo en página, páginas por sesión
   **Monetización**: Valor de conversiones (si aplica)
   **Retención**: Usuarios recurrentes

## Métricas clave a monitorear

### Adquisición
- **Usuarios**: Número de usuarios únicos
- **Sesiones**: Número de visitas al sitio
- **Tasa de rebote**: Porcentaje de sesiones de una sola página
- **Fuentes de tráfico**: Organic, Direct, Referral, Social

### Compromiso
- **Tiempo de compromiso promedio**: Tiempo que pasan en el sitio
- **Eventos por sesión**: Interacciones por visita
- **Páginas por sesión**: Profundidad de navegación
- **Tasa de retención**: Usuarios que regresan

### Conversión
- **Tasa de conversión**: Porcentaje de conversiones
- **Ingresos** (si aplica): Valor de conversiones
- **Eventos de conversión**: Número de conversiones
- **Valor de conversión**: Valor promedio por conversión

### Técnico
- **Dispositivos**: Móvil vs Desktop vs Tablet
- **Navegadores**: Chrome, Safari, Firefox, etc.
- **Sistemas operativos**: iOS, Android, Windows, etc.
- **Ubicación**: Países, ciudades de origen

## Integración con Google Search Console

1. Ve a "Administrador" > "Configuración de propiedad"
2. Selecciona "Vinculación de Search Console"
3. Vincula tu propiedad de GSC ya configurada
4. Esto permite ver datos de SEO combinados con GA4

## Frecuencia recomendada de revisión

- **Diaria**: Revisar tráfico general y conversiones
- **Semanal**: Analizar fuentes de tráfico y comportamiento
- **Mensual**: Revisar informes de ciclo de vida completo
- **Trimestral**: Auditoría de configuración y objetivos

## Dashboards recomendados

### Dashboard principal
- Usuarios totales últimos 30 días
- Sesiones por fuente de tráfico
- Tasa de conversión general
- Rendimiento por dispositivo

### Dashboard de SEO
- Tráfico orgánico vs total
- Palabras clave principales
- Páginas con más tráfico orgánico
- Tasa de rebote por página

### Dashboard de conversión
- Eventos de conversión principales
- Tasa de conversión por fuente
- Valor de conversión por canal
- Rutas de conversión

## Troubleshooting común

### Sin datos en el informe
- Verificar que la etiqueta esté instalada correctamente
- Esperar 24-48 horas para la primera aparición de datos
- Revisar que no haya bloqueadores de anuncios activos
- Verificar filtros de fecha en el informe

### Datos inexactos
- Revisar configuración de zona horaria
- Verificar que no haya duplicación de etiquetas
- Comprobar filtros aplicados en el informe
- Revisar configuración de exclusión de referencia

### Baja tasa de conversión
- Revisar que los eventos de conversión estén configurados
- Verificar que los botones de contacto funcionen
- Analizar UX móvil para mejorar conversiones
- Revisar funnels de conversión

## Integración con otras herramientas

### Google Ads
1. Vincular cuenta de Google Ads
2. Importar conversiones de GA4
3. Configurar audiencias para remarketing

### Google Tag Manager
1. Crear contenedor GTM
2. Migrar etiquetas GA4 a GTM
3. Configurar activadores y variables
4. Publicar contenedor

### Search Ads 360
1. Vincular cuenta de SA360
2. Importar datos de conversión
3. Configurar atribución avanzada

## Recursos adicionales

- [Documentación oficial GA4](https://support.google.com/analytics/answer/9304126)
- [Centro de ayuda de Google Analytics](https://support.google.com/analytics)
- [Guía de migración a GA4](https://support.google.com/analytics/answer/9356318)