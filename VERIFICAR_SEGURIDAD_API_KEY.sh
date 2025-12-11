#!/bin/bash
# Script de verificación de seguridad para API keys
# Asegura que ninguna API key esté expuesta en el repositorio

echo "🔒 Verificando seguridad de API keys..."
echo ""

ERRORS=0

# 1. Verificar que .env está en .gitignore
echo "1️⃣ Verificando que .env está en .gitignore..."
if grep -q "^\.env$" .gitignore; then
    echo "   ✅ .env está en .gitignore"
else
    echo "   ❌ .env NO está en .gitignore"
    ERRORS=$((ERRORS + 1))
fi

# 2. Verificar que .env no está tracked
echo ""
echo "2️⃣ Verificando que .env no está en git..."
if git ls-files --error-unmatch .env >/dev/null 2>&1; then
    echo "   ❌ .env está siendo tracked por git (PELIGRO)"
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ .env NO está tracked por git"
fi

# 3. Buscar API keys en archivos tracked
echo ""
echo "3️⃣ Buscando API keys en archivos tracked por git..."
if git grep -q "AIzaSy[A-Za-z0-9_-]\{35\}" -- ':(exclude).gitignore' 2>/dev/null; then
    echo "   ❌ Se encontraron API keys en archivos tracked"
    echo "   Archivos con posibles API keys:"
    git grep -l "AIzaSy[A-Za-z0-9_-]\{35\}" -- ':(exclude).gitignore' 2>/dev/null | sed 's/^/      - /'
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ No se encontraron API keys en archivos tracked"
fi

# 4. Verificar que no hay referencias a GOOGLE_API_KEY con valores reales
echo ""
echo "4️⃣ Verificando referencias a GOOGLE_API_KEY..."
if git grep -q "GOOGLE_API_KEY.*AIzaSy" -- ':(exclude).gitignore' 2>/dev/null; then
    echo "   ❌ Se encontraron asignaciones de API key en código"
    git grep -n "GOOGLE_API_KEY.*AIzaSy" -- ':(exclude).gitignore' 2>/dev/null | head -5 | sed 's/^/      /'
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ No hay asignaciones directas de API key en código"
fi

# 5. Verificar archivos de documentación
echo ""
echo "5️⃣ Verificando archivos de documentación..."
DOC_FILES=$(git ls-files | grep -E "\.(md|txt)$")
if echo "$DOC_FILES" | xargs grep -l "AIzaSy[A-Za-z0-9_-]\{35\}" 2>/dev/null; then
    echo "   ❌ Se encontraron API keys en archivos de documentación:"
    echo "$DOC_FILES" | xargs grep -l "AIzaSy[A-Za-z0-9_-]\{35\}" 2>/dev/null | sed 's/^/      - /'
    ERRORS=$((ERRORS + 1))
else
    echo "   ✅ No hay API keys en archivos de documentación"
fi

# Resumen
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
if [ $ERRORS -eq 0 ]; then
    echo "✅ Verificación completada: TODO SEGURO"
    echo ""
    echo "✓ Tu API key está protegida"
    echo "✓ Puedes continuar con seguridad"
    exit 0
else
    echo "❌ Verificación completada: SE ENCONTRARON $ERRORS PROBLEMA(S)"
    echo ""
    echo "⚠️  ACCIÓN REQUERIDA:"
    echo "   1. Revisa los problemas arriba"
    echo "   2. Elimina las API keys de los archivos indicados"
    echo "   3. Reemplázalas con 'TU_API_KEY_AQUI' o 'tu-api-key-aqui'"
    echo "   4. Vuelve a ejecutar este script"
    echo ""
    exit 1
fi

