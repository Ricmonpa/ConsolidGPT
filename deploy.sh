#!/bin/bash
# Script de deployment rápido para Vercel

echo "🚀 Deployando ConsolidGPT a Vercel..."
echo ""

# Verificar que vercel CLI esté instalado
if ! command -v vercel &> /dev/null
then
    echo "❌ Vercel CLI no está instalado"
    echo "Instálalo con: npm install -g vercel"
    exit 1
fi

echo "✅ Vercel CLI encontrado"
echo ""

# Verificar que exista .env
if [ ! -f .env ]; then
    echo "⚠️  Advertencia: No se encontró archivo .env"
    echo "Recuerda configurar GOOGLE_API_KEY en Vercel Dashboard"
    echo ""
fi

# Preguntar tipo de deployment
echo "¿Qué tipo de deployment deseas?"
echo "1) Preview (prueba)"
echo "2) Production (producción)"
read -p "Selecciona (1 o 2): " choice

case $choice in
    1)
        echo ""
        echo "📦 Deployando preview..."
        vercel
        ;;
    2)
        echo ""
        echo "🌐 Deployando a producción..."
        vercel --prod
        ;;
    *)
        echo "❌ Opción inválida"
        exit 1
        ;;
esac

echo ""
echo "✅ Deployment completado!"
echo ""
echo "📝 Recuerda:"
echo "   - Configurar GOOGLE_API_KEY en Vercel Dashboard"
echo "   - Probar la URL en móvil y desktop"
echo "   - Verificar que las tarjetas funcionen"
echo ""
