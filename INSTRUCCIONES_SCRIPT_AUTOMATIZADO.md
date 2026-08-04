# Instrucciones: Script de Despliegue Automatizado

## 🚀 EJECUTAR EL SCRIPT AUTOMATIZADO

### MÉTODO 1: EJECUCIÓN SIMPLE (Recomendado)

#### Paso 1: Abrir terminal
1. Presiona `Win + R`
2. Escribe `cmd` y presiona Enter
3. O busca "Símbolo del sistema" en el menú inicio

#### Paso 2: Navegar al directorio del proyecto
```bash
cd C:\Users\user\Documents\www.quindiotravel.com
```

#### Paso 3: Ejecutar el script
```bash
python deployment_automated.py
```

#### Paso 4: Ingresar credenciales cuando pregunte
- **Host FTP:** `quindiotravel.com.co` (o tu servidor FTP)
- **Usuario FTP:** Tu usuario FTP
- **Contraseña FTP:** Tu contraseña FTP (no se mostrará por seguridad)
- **Puerto FTP:** `21` (default) o tu puerto específico
- **Directorio remoto:** `public_html` (default) o tu directorio raíz

#### Paso 5: Esperar a que termine
- El script conectará al servidor
- Subirá los 5 archivos automáticamente
- Verificará que los archivos existan en el servidor
- Generará un reporte de despliegue

#### Paso 6: Verificar el reporte
- El script creará `deployment_report.txt`
- Revisa el reporte para ver el estado del despliegue

---

## ✅ VERIFICACIÓN POST-DESPLEGUE

### Abrir estas URLs en tu navegador:
```
https://quindiotravel.com.co/sitemap.xml
https://quindiotravel.com.co/llms.txt
https://quindiotravel.com.co/robots.txt
https://quindiotravel.com.co/.well-known/ai-metadata.json
```

### Esperado:
- **sitemap.xml:** Debe mostrar XML con 116 URLs
- **llms.txt:** Debe mostrar información de la empresa
- **robots.txt:** Debe mostrar permisos de crawlers
- **ai-metadata.json:** Debe mostrar metadata en JSON

---

## 🎯 PRÓXIMO PASO

### Someter sitemap a Google Search Console:
1. Acceder a https://search.google.com/search-console
2. Seleccionar propiedad `quindiotravel.com.co`
3. Navegar a "Sitemaps"
4. Ingresar: `sitemap.xml`
5. Hacer clic en "Enviar"

---

## ⚠️ SOLUCIÓN DE PROBLEMAS

### Error: "Error de conexión FTP"
- Verificar que el host sea correcto
- Verificar que el puerto sea correcto (21 o 22)
- Verificar que el usuario y contraseña sean correctos
- Verificar que el servidor acepte conexiones FTP

### Error: "Error navegando al directorio"
- Verificar que el directorio remoto sea correcto
- Intentar con `public_html` o `www`
- Consultar con tu hosting el directorio correcto

### Error: "Algunos archivos locales faltan"
- Verificar que estés en el directorio correcto
- Ejecutar el script desde `C:\Users\user\Documents\www.quindiotravel.com\`

### Error: "Error subiendo archivos"
- Verificar permisos de escritura en el servidor
- Verificar que haya espacio disponible
- Verificar que el directorio sea escribible

---

## 📞 AYUDA ADICIONAL

### Si el script falla:
1. Revisa el archivo `deployment_report.txt` para ver errores específicos
2. Consulta con tu hosting sobre credenciales FTP correctas
3. Intenta subir archivos manualmente por FTP como alternativa

### Si no tienes credenciales FTP:
- Consulta con tu hosting
- Busca en el panel de control del hosting
- Revisa emails de bienvenida del hosting

---

## ⏱️ TIEMPO ESTIMADO
- **Ejecución del script:** 5-10 minutos
- **Verificación post-despliegue:** 2-3 minutos
- **Google Search Console:** 3-5 minutos
- **Total:** 10-18 minutos