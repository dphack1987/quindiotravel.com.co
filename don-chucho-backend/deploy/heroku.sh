#!/bin/bash

# Script de despliegue para Heroku - Don Chucho Backend

echo "🤠 Iniciando despliegue de Don Chucho Backend..."

# Instalar Heroku CLI si no está instalado
if ! command -v heroku &> /dev/null; then
    echo "📦 Instalando Heroku CLI..."
    npm install -g heroku
fi

# Login en Heroku
echo "🔐 Login en Heroku..."
heroku login

# Crear aplicación Heroku
echo "🚀 Creando aplicación Heroku..."
heroku create don-chucho-backend

# Configurar variables de entorno
echo "⚙️  Configurando variables de entorno..."
heroku config:set PORT=3000
heroku config:set NODE_ENV=production
heroku config:set API_KEY=don-chucho-secret-key-2024

echo "⚠️  IMPORTANTE: Configura las siguientes variables manualmente:"
echo "   - WHATSAPP_PHONE_NUMBER_ID"
echo "   - WHATSAPP_ACCESS_TOKEN"
echo "   - WHATSAPP_WEBHOOK_VERIFY_TOKEN"
echo "   - OPENAI_API_KEY"
echo "   - MONGODB_URI"
echo "   - QUINDIO_WHATSAPP"
echo "   - FRONTEND_URL"

# Instalar dependencias de producción
echo "📦 Instalando dependencias..."
npm install --production

# Configurar buildpack
echo "🔧 Configurando buildpack..."
heroku buildpacks:set heroku/nodejs

# Desplegar código
echo "🚀 Desplegando código a Heroku..."
git push heroku main

# Escalar dynos (opcional)
echo "📊 Configurando dynos..."
heroku ps:scale web=1:standard

echo "✅ Despliegue completado!"
echo "🌐 URL de la aplicación: https://don-chucho-backend.herokuapp.com"
echo "📝 No olvides configurar el webhook en Meta con: https://don-chucho-backend.herokuapp.com/webhook/whatsapp"