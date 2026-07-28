# 🤠 Don Chucho Backend - Sistema de Chatbot con IA

Backend inteligente para Don Chucho, el arriero guía turístico del Eje Cafetero colombiano. Sistema completo con integración de WhatsApp Business API, OpenAI GPT-3.5, y MongoDB.

## 🚀 Características

- **🤖 IA con OpenAI GPT-3.5**: Respuestas inteligentes y contextualizadas
- **📱 WhatsApp Business API**: Comunicación bidireccional por WhatsApp
- **🗄️ MongoDB**: Almacenamiento de conversaciones y analíticas
- **🔔 Webhooks**: Recepción de mensajes en tiempo real
- **🎯 Fallback inteligente**: Respuestas locales cuando el backend falla
- **📊 Analíticas**: Tracking de conversaciones y escalaciones a humanos
- **🛡️ Seguridad**: Rate limiting y autenticación

## 📋 Requisitos Previos

### Cuentas Necesarias

1. **Meta for Developers** (Gratis)
   - Crear cuenta en https://developers.facebook.com/
   - Configurar WhatsApp Business API

2. **OpenAI API** (Pago)
   - Cuenta en https://platform.openai.com/
   - API Key para GPT-3.5-turbo (~$0.002/1K tokens)

3. **MongoDB Atlas** (Gratis hasta 512MB)
   - Cuenta en https://www.mongodb.com/atlas
   - Cluster gratuito M0

4. **Heroku/Vercel** (Gratis para desarrollo)
   - Para hosting del backend

### Instalación Local

```bash
# Clonar repositorio
git clone https://github.com/tu-usuario/don-chucho-backend.git
cd don-chucho-backend

# Instalar dependencias
npm install

# Configurar variables de entorno
cp .env.example .env
# Editar .env con tus credenciales reales

# Iniciar servidor
npm run dev
```

## 🔧 Configuración

### Variables de Entorno (.env)

```bash
# Servidor
PORT=3000
NODE_ENV=development
API_KEY=don-chucho-secret-key-2024

# WhatsApp Business API
WHATSAPP_PHONE_NUMBER_ID=tu_phone_number_id
WHATSAPP_ACCESS_TOKEN=tu_access_token
WHATSAPP_WEBHOOK_VERIFY_TOKEN=tu_token_secreto
WHATSAPP_API_VERSION=v18.0

# OpenAI API
OPENAI_API_KEY=tu_openai_api_key
OPENAI_MODEL=gpt-3.5-turbo

# MongoDB Atlas
MONGODB_URI=mongodb+srv://usuario:password@cluster.mongodb.net/don_chucho_db
DB_NAME=don_chucho_db

# Quindío Travel
QUINDIO_WHATSAPP=573174426044
QUINDIO_EMAIL=gerencia@quindiotravel.net

# Frontend URL (para CORS)
FRONTEND_URL=https://quindiotravel.com.co
```

### Estructura del Proyecto

```
don-chucho-backend/
├── server.js                    # Servidor principal Express
├── config/
│   └── database.js             # Configuración MongoDB
├── routes/
│   ├── webhook.js              # Rutas de WhatsApp webhooks
│   └── chat.js                 # API para chat web
├── services/
│   ├── whatsappService.js     # Lógica de WhatsApp
│   ├── openaiService.js        # Integración con OpenAI
│   └── knowledgeBase.js        # Base de conocimiento local
├── models/
│   └── Conversation.js          # Modelos de datos
├── middleware/
│   └── auth.js                 # Middleware de autenticación
├── .env.example                # Template de variables de entorno
├── package.json                 # Dependencias de Node.js
└── README.md                    # Este archivo
```

## 🚀 Despliegue

### Opción 1: Heroku (Recomendado)

```bash
# Instalar Heroku CLI
npm install -g heroku

# Login en Heroku
heroku login

# Crear aplicación
heroku create don-chucho-backend

# Configurar variables de entorno
heroku config:set PORT=3000
heroku config:set NODE_ENV=production
heroku config:set WHATSAPP_PHONE_NUMBER_ID=tu_id
heroku config:set WHATSAPP_ACCESS_TOKEN=tu_token
heroku config:set WHATSAPP_WEBHOOK_VERIFY_TOKEN=tu_token
heroku config:set WHATSAPP_API_VERSION=v18.0
heroku config:set OPENAI_API_KEY=tu_openai_key
heroku config:set OPENAI_MODEL=gpt-3.5-turbo
heroku config:set MONGODB_URI=tu_mongodb_uri
heroku config:set DB_NAME=don_chucho_db
heroku config:set QUINDIO_WHATSAPP=573174426044
heroku config:set FRONTEND_URL=https://quindiotravel.com.co

# Desplegar
git push heroku main
```

### Opción 2: Vercel

```bash
# Instalar Vercel CLI
npm install -g vercel

# Login en Vercel
vercel login

# Desplegar
vercel
```

### Opción 3: Servidor VPS

```bash
# Instalar PM2 para proceso demonio
npm install -g pm2

# Iniciar con PM2
pm2 start server.js --name don-chucho

# Configurar para iniciar en boot
pm2 startup
pm2 save
```

## 🔌 Configuración de WhatsApp Business API

### Paso 1: Crear WhatsApp Business App

1. Ve a Meta for Developers
2. Crea nueva app > Business
3. Agrega "WhatsApp" al producto
4. Configura el número de teléfono

### Paso 2: Obtener Credenciales

1. En WhatsApp > Configuration:
   - Copia Phone Number ID
   - Genera Access Token (Permanent)
   - Configura Webhook URL: `https://tu-dominio.com/webhook/whatsapp`

### Paso 3: Configurar Webhook

1. URL: `https://tu-dominio.com/webhook/whatsapp`
2. Verify Token: tu_token_secreto
3. Suscribir a: `messages`, `message_status`

## 🧪 Testing

### Testing Local

```bash
# Iniciar servidor
npm run dev

# Verificar salud del servidor
curl http://localhost:3000/health

# Test de API de chat
curl -X POST http://localhost:3000/api/chat/session \
  -H "Content-Type: application/json" \
  -d '{"source":"web"}'

# Test de envío de mensaje
curl -X POST http://localhost:3000/api/chat/message \
  -H "Content-Type: application/json" \
  -d '{"message":"Hola Don Chucho","sessionId":"test123","conversationHistory":[]}'
```

### Testing con WhatsApp

1. Configura ngrok para tunneling local:
```bash
ngrok http 3000
```

2. Configura webhook en Meta con tu URL de ngrok

3. Envía mensaje de prueba al número de WhatsApp

## 📊 Monitoreo y Logs

### Logs de la Aplicación

```bash
# Ver logs en Heroku
heroku logs --tail

# Ver logs en tiempo real
heroku logs --tail --app don-chucho-backend
```

### MongoDB Atlas

1. Accede a MongoDB Atlas Dashboard
2. Observa las colecciones: `conversations`, `web_conversations`, `escalations`
3. Monitorea métricas de rendimiento

## 🔒 Seguridad

### Mejores de Seguridad Implementadas

- **Rate Limiting**: 30 requests por minuto por IP
- **API Key**: Autenticación básica para endpoints sensibles
- **Environment Variables**: Credenciales en .env, no en código
- **HTTPS**: Requerido para producción

### Recomendaciones Adicionales

- Implementar JWT para autenticación robusta
- Usar VPN para acceso a base de datos
- Configurar firewall para IPs específicas
- Implementar logging detallado de auditoría

## 🐛 Troubleshooting

### Errores Comunes

**Error: MongoDB Connection Failed**
- Verifica MONGODB_URI en .env
- Asegura que IP está whitelist en MongoDB Atlas
- Revisa usuario y contraseña

**Error: WhatsApp Webhook Verification Failed**
- Verifica que el verify token coincida exactamente
- Asegura que el servidor sea accesible públicamente
- Revisa que el endpoint GET `/webhook/whatsapp` responda correctamente

**Error: OpenAI API Rate Limit**
- Verifica que tienes créditos suficientes
- Implementa caching de respuestas frecuentes
- Considera modelo más económico (gpt-3.5-turbo)

**Error: CORS Policy**
- Verifica FRONTEND_URL en .env
- Asegura que el origen está permitido en middleware CORS

## 📈 Escalabilidad

### Carga Soportada

- **Desarrollo**: ~100 concurrentes
- **Producción**: ~1,000 concurrentes (con escalado horizontal)
- **Costo estimado**: $50-200/mes (Heroku + OpenAI + MongoDB)

### Mejoras de Escalabilidad

- Implementar Redis para caching
- Usar filas de mensajes para alta concurrencia
- Balanceador de carga (Nginx)
- CDN para recursos estáticos

## 🤝 Contribución

Este proyecto es propiedad de Quindío Travel (RNT 18152). Para contribuciones o sugerencias, contactar a gerencia@quindiotravel.net.

## 📄 Licencia

MIT License - Propiedad de Quindío Travel 2024

## 🎞 Soporte

Para soporte técnico, contactar al equipo de desarrollo o abrir issue en el repositorio.

---

**Desarrollado con ❤️ para el Eje Cafetero Colombiano**