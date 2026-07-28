#!/bin/bash

# Script para configurar ngrok para testing local de webhooks

echo "🔧 Configurando ngrok para Don Chucho Backend..."

# Instalar ngrok si no está instalado
if ! command -v ngrok &> /dev/null; then
    echo "📦 Instalando ngrok..."
    # Para Windows
    if [[ "$OSTYPE" == "msys" ]]; then
        # Descargar ngrok para Windows
        if [ ! -f "ngrok.zip" ]; then
            curl -s https://bin.equinox.io/c/4VmDzA7iaDbQPByAjKLJZrRt36h_t/pRJwBB9Xy9xNTE8z1p0/ngrok-stable-windows-amd64.zip -o ngrok.zip
            unzip ngrok.zip
        fi
    else
        # Para Linux/Mac
        curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | sudo tee /etc/apt/trusted.gpg >/dev/null
        sudo apt-key add /dev/stdin
        echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | sudo tee /etc/apt/sources.list.d/ngrok.list
        sudo apt update && sudo apt install ngrok
    fi
fi

# Iniciar ngrok
echo "🚀 Iniciando ngrok en puerto 3000..."
ngrok http 3000

echo "📝 Usa la URL generada para configurar el webhook en Meta:"
echo "   Webhook URL: https://TU-URL-NGROK/webhook/whatsapp"
echo "   Verify Token: tu_token_secreto"