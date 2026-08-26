# Quindío Travel - Sitio Web Oficial

Operador turístico oficial RNT 18152 especializado en turismo del Eje Cafetero colombiano.

## 🌐 Estructura del Proyecto

- **Páginas principales:** index.html, planes.html, finca-hoteles-en-el-quindio.html
- **Destinos:** salento.html, filandia.html
- **Alojamientos:** Múltiples páginas de hoteles y finca hoteles
- **Blog:** +30 artículos sobre turismo en el Quindío
- **Landing pages:** +100 páginas programáticas para captación de tráfico específico
- **Componentes:** Estructura modular en carpeta components/

## 🚀 Despliegue con GitHub Pages

### Configuración Inicial (Requiere acceso a interfaz web de GitHub)

1. **Ir al repositorio en GitHub:**
   - Accede a https://github.com/dphack1987/quindiotravel.com.co

2. **Habilitar GitHub Pages:**
   - Ve a Settings → Pages
   - En "Source", selecciona "Deploy from a branch"
   - En "Branch", selecciona "main" y carpeta "/" (root)
   - Haz clic en "Save"

3. **Dominio personalizado:**
   - En "Custom domain", ingresa: quindiotravel.com.co
   - GitHub generará registros DNS que debes configurar en tu proveedor de dominio

### Configuración DNS

Agrega estos registros en tu proveedor de dominio:

```
A    @         185.199.108.153
A    @         185.199.109.153  
A    @         185.199.110.153
A    @         185.199.111.153
CNAME www      dphack1987.github.io
```

### Verificación

Una vez configurado, el sitio estará disponible en:
- **Temporal:** https://dphack1987.github.io/quindiotravel.com.co/
- **Final:** https://quindiotravel.com.co/

## 📝 Actualizaciones

Cada vez que hagas push a la rama `main`, GitHub Pages se actualizará automáticamente:

```bash
git add .
git commit -m "Descripción de cambios"
git push origin main
```

## 🎯 Landing Pages

El proyecto incluye +100 landing pages programáticas optimizadas para SEO, ubicadas en:
- `programmatic-pages/` - Páginas generadas automáticamente
- `promo-agosto-2026.html` - Promociones específicas
- `en/booking-*.html` - Landing pages de reservas internacionales

## 📞 Contacto

- **Gerente:** Álvaro Alzate Ortiz
- **Celular/WhatsApp:** (317) 442-6044
- **Correo:** gerencia@quindiotravel.net
- **RNT:** 18152

---
© 2026 Quindío Travel. Todos los derechos reservados.