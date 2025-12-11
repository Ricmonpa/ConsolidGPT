# 🚨 URGENTE: Revocar API Key Expuesta

## ❌ LA API KEY FUE EXPUESTA EN GITHUB

La API key `AIzaSyA-8GLqKz9rqkBuqCSk83oQERNg3D9cn6A` fue encontrada en GitHub por Google.

**YA FUE ELIMINADA** del código, pero necesitas **REVOCARLA INMEDIATAMENTE**.

---

## 🔴 ACCIÓN REQUERIDA AHORA MISMO

### 1. Revoca la API key expuesta:

1. Ve a: https://console.cloud.google.com/apis/credentials
2. Busca la API key: `AIzaSyA-8GLqKz9rqkBuqCSk83oQERNg3D9cn6A`
3. Click en los **3 puntos (⋯)** a la derecha
4. Selecciona **"Delete"** o **"Regenerate"** (Re-generar)
5. Confirma la eliminación

### 2. Crea una NUEVA API key:

1. En la misma página (Credentials)
2. Click en **"CREATE CREDENTIALS"** → **"API Key"**
3. Nombre: "ConsolidGPT Production v2" (o el que prefieras)
4. Configura restricciones:
   - **API restrictions:** Solo "Generative Language API"
   - **Application restrictions:** Ninguno (para Vercel)
5. Copia la nueva API key

### 3. Actualiza en Vercel:

1. Ve a: https://vercel.com/dashboard
2. Tu proyecto → Settings → Environment Variables
3. Busca `GOOGLE_API_KEY`
4. Click en "Edit"
5. Reemplaza con la NUEVA API key
6. Guarda

### 4. Actualiza `.env` local:

```bash
# Edita .env
nano .env

# Actualiza la línea:
GOOGLE_API_KEY=tu-nueva-api-key-aqui

# Guarda (Ctrl+X, luego Y, luego Enter)
```

### 5. Haz redeploy en Vercel:

1. Ve a Deployments
2. Click en los 3 puntos del deployment más reciente
3. Click en "Redeploy"

---

## ⚠️ IMPORTANTE

**NO uses la API key expuesta nunca más.** Está comprometida y Google la revocará automáticamente.

---

## 🔒 PREVENCIÓN FUTURA

**NUNCA más:**
- ❌ Poner API keys reales en archivos de documentación
- ❌ Poner API keys reales en ningún archivo que se suba a git
- ❌ Incluir API keys en ejemplos

**Siempre:**
- ✅ Usar placeholders: `tu-api-key-aqui` o `TU_API_KEY_AQUI`
- ✅ Ejecutar `./VERIFICAR_SEGURIDAD_API_KEY.sh` antes de cada commit
- ✅ Verificar que `.env` esté en `.gitignore`

---

**DISCLPA POR EL ERROR. REVOCA LA KEY AHORA MISMO.**

