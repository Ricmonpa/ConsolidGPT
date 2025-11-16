#!/bin/bash

# ConsolidGPT - Script de Inicio Rápido

echo "🌴 ConsolidGPT - Iniciando..."
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 no está instalado"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Instalar dependencias si no están instaladas
echo "📦 Verificando dependencias..."
pip3 install -q -r requirements.txt

echo ""
echo "🚀 Iniciando ConsolidGPT Web App..."
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "   Abre tu navegador en: http://localhost:5000"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Presiona Ctrl+C para detener el servidor"
echo ""

# Iniciar Flask
python3 app.py
