# Guía de Despliegue - Subir Archivos al Servidor

## 📋 ARCHIVOS CRÍTICOS PARA SUBIR AL SERVIDOR

### 1. Archivos Estructurales (Raíz del servidor)
- `sitemap.xml` → Raíz del servidor (`/public_html/` o similar)
- `llms.txt` → Raíz del servidor
- `robots.txt` → Raíz del servidor
- `index.html` → Raíz del servidor (reemplazar existente)

### 2. Archivos de Estándar Emergente
- `.well-known/ai-metadata.json` → Directorio `.well-known/` en raíz

### 3. Archivos Generados (Ya existentes, verificar)
- `programmatic-pages/*.html` → Directorio `programmatic-pages/`
- `blog/*.html` → Directorio `blog/`

---

## 🚀 MÉTODOS DE SUBIDA (ELEGIR UNO)

### MÉTODO 1: FTP/SFTP (Más común)
**Requisitos:**
- Cliente FTP (FileZilla, WinSCP, Cyberduck)
- Credenciales FTP (host, usuario, contraseña, puerto)

**Pasos:**
1. Abrir cliente FTP
2. Conectar al servidor con credenciales
3. Navegar a directorio raíz (`/public_html/` o `/www/`)
4. Subir archivos:
   - `sitemap.xml`
   - `llms.txt`
   - `robots.txt`
   - `index.html` (sobrescribir)
5. Crear directorio `.well-known/` si no existe
6. Subir `.well-known/ai-metadata.json`

### MÉTODO 2: SSH/SCP (Para usuarios técnicos)
**Requisitos:**
- Acceso SSH al servidor
- Credenciales SSH

**Comandos:**
```bash
# Conectar al servidor
ssh usuario@servidor.com

# Navegar al directorio raíz
cd /ruta/al/sitio

# Subir archivos desde local
scp sitemap.xml usuario@servidor.com:/ruta/al/sitio/
scp llms.txt usuario@servidor.com:/ruta/al/sitio/
scp robots.txt usuario@servidor.com:/ruta/al/sitio/
scp index.html usuario@servidor.com:/ruta/al/sitio/

# Crear directorio y subir metadata
mkdir -p .well-known
scp .well-known/ai-metadata.json usuario@servidor.com:/ruta/al/sitio/.well-known/
```

### MÉTODO 3: Panel de Control (cPanel, Plesk)
**Requisitos:**
- Acceso al panel de control del hosting
- Credenciales del panel

**Pasos:**
1. Acceder al panel de control (cPanel/Plesk)
2. Abrir "Administrador de Archivos"
3. Navegar a directorio raíz
4. Subir archivos uno por uno
5. Crear directorio `.well-known/`
6. Subir archivo AI metadata

### MÉTODO 4: Git (Si el sitio está en Git)
**Requisitos:**
- Repositorio Git del sitio
- Acceso para hacer push

**Comandos:**
```bash
# Agregar archivos nuevos
git add sitemap.xml llms.txt robots.txt .well-known/ai-metadata.json index.html

# Commit
git commit -m "Add SEO optimization files for LLMs and Gemini"

# Push
git push origin main
```

---

## 📁 VERIFICACIÓN DE ESTRUCTURA

### Estructura esperada en el servidor:
```
/public_html/ (o /www/)
├── index.html (actualizado)
├── sitemap.xml (nuevo)
├── llms.txt (nuevo)
├── robots.txt (nuevo)
├── .well-known/
│   └── ai-metadata.json (nuevo)
├── programmatic-pages/
│   └── *.html (93 archivos)
├── blog/
│   └── *.html (20 archivos)
└── [otros archivos existentes]
```

---

## ✅ VERIFICACIÓN POST-DESPLEGUE

### 1. Verificar accesibilidad de archivos:
```
https://quindiotravel.com.co/sitemap.xml
https://quindiotravel.com.co/llms.txt
https://quindiotravel.com.co/robots.txt
https://quindiotravel.com.co/.well-known/ai-metadata.json
```

### 2. Verificar contenido de sitemap:
- Abrir `https://quindiotravel.com.co/sitemap.xml`
- Debe mostrar 116 URLs

### 3. Verificar contenido de llms.txt:
- Abrir `https://quindiotravel.com.co/llms.txt`
- Debe mostrar información estructurada completa

### 4. Verificar contenido de robots.txt:
- Abrir `https://quindiotravel.com.co/robots.txt`
- Debe mostrar permisos correctos

---

## 🎯 PRÓXIMO PASO DESPUÉS DEL DESPLIEGUE

### Someter Sitemap a Google Search Console:
1. Acceder a Google Search Console
2. Seleccionar propiedad `quindiotravel.com.co`
3. Navegar a "Sitemaps"
4. Ingresar URL: `https://quindiotravel.com.co/sitemap.xml`
5. Hacer clic en "Enviar"
6. Monitorear indexación en "Estado de indexación"

---

## ⚠️ ADVERTENCIAS

### Precauciones:
1. **Hacer backup** de `index.html` antes de sobrescribir
2. **Verificar permisos** de archivos (644 para archivos, 755 para directorios)
3. **Verificar propietario** de archivos (www-data o usuario correcto)
4. **No interrumpir** procesos en curso durante subida

### Errores comunes:
- Subir archivos al directorio incorrecto
- Olvidar crear directorio `.well-known/`
- Permisos incorrectos en archivos
- Sobrescribir archivos sin backup

---

## 🚀 SCRIPT DE DESPLIEGUE AUTOMATIZADO (ADAPTAR)

Si tienes acceso SSH, puedes usar este script:

```bash
#!/bin/bash
# deployment.sh - Script de despliegue para Quindío Travel

# Configuración
SERVER="usuario@quindiotravel.com.co"
REMOTE_DIR="/ruta/al/sitio/public_html"
LOCAL_DIR="/path/to/local/files"

# Subir archivos críticos
scp $LOCAL_DIR/sitemap.xml $SERVER:$REMOTE_DIR/
scp $LOCAL_DIR/llms.txt $SERVER:$REMOTE_DIR/
scp $LOCAL_DIR/robots.txt $SERVER:$REMOTE_DIR/
scp $LOCAL_DIR/index.html $SERVER:$REMOTE_DIR/

# Crear directorio y subir metadata
ssh $SERVER "mkdir -p $REMOTE_DIR/.well-known"
scp $LOCAL_DIR/.well-known/ai-metadata.json $SERVER:$REMOTE_DIR/.well-known/

# Verificar accesibilidad
ssh $SERVER "chmod 644 $REMOTE_DIR/sitemap.xml"
ssh $SERVER "chmod 644 $REMOTE_DIR/llms.txt"
ssh $SERVER "chmod 644 $REMOTE_DIR/robots.txt"
ssh $SERVER "chmod 644 $REMOTE_DIR/index.html"
ssh $SERVER "chmod 644 $REMOTE_DIR/.well-known/ai-metadata.json"

echo "Despliegue completado exitosamente"
```

---

## 📞 SOPORTE

Si encuentras problemas:
1. Verificar credenciales de acceso
2. Verificar ruta del directorio en el servidor
3. Verificar permisos de archivos
4. Contactar soporte del hosting si es necesario

---

## 🎯 RESUMEN

**Archivos a subir:**
- `sitemap.xml` (27.5 KB)
- `llms.txt` (5.2 KB)
- `robots.txt` (1.1 KB)
- `index.html` (actualizado)
- `.well-known/ai-metadata.json` (2.3 KB)

**Ubicación:** Raíz del servidor (`/public_html/` o similar)

**Método recomendado:** FTP/SFTP o Panel de Control

**Verificación:** Acceder a URLs y verificar contenido

**Próximo paso:** Someter sitemap a Google Search Console