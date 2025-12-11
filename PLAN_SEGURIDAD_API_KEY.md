# 🔒 Plan de Seguridad para API Keys

## ⚠️ PROBLEMA CRÍTICO

Las API keys de Google están siendo expuestas en archivos de documentación que se suben a GitHub público. Google detecta esto y marca las keys como "leaked", revocándolas.

---

## ✅ CHECKLIST DE SEGURIDAD

### Antes de cada commit:

- [ ] **Ejecutar script de verificación:**
  ```bash
  ./VERIFICAR_SEGURIDAD_API_KEY.sh
  ```
  Si hay errores, NO hacer commit hasta corregirlos.

- [ ] **Verificar que .env está en .gitignore**
  ```bash
  grep "^\.env$" .gitignore
  ```
  Debe mostrar `.env`

- [ ] **Verificar que .env no está tracked:**
  ```bash
  git ls-files | grep "^\.env$"
  ```
  No debe mostrar nada

- [ ] **Buscar API keys en archivos que se van a commitear:**
  ```bash
  git diff --cached | grep -i "AIzaSy"
  ```
  No debe mostrar nada

---

## 📋 REGLAS ABSOLUTAS

### ✅ SÍ PUEDES hacer:

1. **Guardar la API key en `.env` local** (ya está en .gitignore)
2. **Guardar la API key en Vercel** (Environment Variables)
3. **Usar placeholders en documentación:**
   - `GOOGLE_API_KEY=tu-api-key-aqui`
   - `GOOGLE_API_KEY=TU_API_KEY_AQUI`
   - `GOOGLE_API_KEY=AIzaSyEjemplo123456789NuevaKey` (solo si es claramente un ejemplo)

### ❌ NUNCA hagas:

1. **Subir `.env` a GitHub** (aunque ya está en .gitignore, verifica)
2. **Poner API keys reales en archivos `.md`, `.txt`, `.py`, `.js`, etc.**
3. **Comentar código con API keys reales**
4. **Usar API keys reales en ejemplos de documentación**
5. **Hacer commit sin verificar primero**

---

## 🔧 PASOS PARA AGREGAR UNA NUEVA API KEY

### 1. Obtener la nueva API key
- Ve a: https://console.cloud.google.com/apis/credentials
- Crea nueva API key

### 2. Actualizar LOCALMENTE (.env)
```bash
# Edita .env
nano .env

# Actualiza la línea:
GOOGLE_API_KEY=tu-nueva-api-key-real-aqui

# Guarda y cierra
```

### 3. Actualizar en Vercel
- Ve a: https://vercel.com/dashboard
- Tu proyecto → Settings → Environment Variables
- Busca `GOOGLE_API_KEY`
- Click "Edit" → Reemplaza con nueva key
- Guarda

### 4. Verificar seguridad ANTES de commitear
```bash
# Ejecuta el script
./VERIFICAR_SEGURIDAD_API_KEY.sh

# Si hay errores, NO hagas commit
```

### 5. Si todo está bien, haz commit
```bash
git add .
git commit -m "Tu mensaje"
git push
```

---

## 🛡️ ARCHIVOS QUE NUNCA DEBEN CONTENER API KEYS

- ✅ `.env` (está en .gitignore, pero verifica)
- ✅ Cualquier `.md` (markdown)
- ✅ Cualquier `.txt`
- ✅ Cualquier `.py`, `.js`, `.html` (código fuente)
- ✅ `README.md`
- ✅ Archivos de documentación
- ✅ Comentarios en código
- ✅ Ejemplos de código

---

## 🚨 QUÉ HACER SI EXPONES UNA API KEY

1. **INMEDIATAMENTE revoca la key en Google Cloud:**
   - https://console.cloud.google.com/apis/credentials
   - Encuentra la key → Click en los 3 puntos → "Delete" o "Regenerate"

2. **Elimina la key del código:**
   ```bash
   # Buscar todas las referencias
   git grep "TU_API_KEY_EXPUESTA"
   
   # Eliminar de archivos
   # Reemplazar con placeholder
   ```

3. **Si ya hiciste commit pero NO push:**
   ```bash
   # Reset del último commit (mantiene cambios)
   git reset --soft HEAD~1
   
   # Corrige los archivos
   # Vuelve a hacer commit
   ```

4. **Si ya hiciste push:**
   - La key ya está comprometida
   - Revoca la key en Google Cloud
   - Crea una nueva key
   - **NO puedes eliminar del historial de git fácilmente** (quedaría en el historial)

---

## 📝 PLACEHOLDERS PERMITIDOS EN DOCUMENTACIÓN

Usa estos formatos para ejemplos:

```
GOOGLE_API_KEY=tu-api-key-aqui
GOOGLE_API_KEY=TU_API_KEY_AQUI
GOOGLE_API_KEY=AIzaSyEjemplo123456789NuevaKey
GOOGLE_API_KEY=sk-... (para OpenAI)
```

**NUNCA uses una API key real, incluso si está "ofuscada" o "parcialmente visible".**

---

## ✅ VERIFICACIÓN AUTOMÁTICA

Ejecuta esto antes de cada commit:

```bash
# Script completo de verificación
./VERIFICAR_SEGURIDAD_API_KEY.sh

# Si muestra ✅ TODO SEGURO → Puedes hacer commit
# Si muestra ❌ PROBLEMAS → Corrige antes de commitear
```

---

## 🔄 WORKFLOW RECOMENDADO

```bash
# 1. Hacer cambios
git add .

# 2. VERIFICAR SEGURIDAD (OBLIGATORIO)
./VERIFICAR_SEGURIDAD_API_KEY.sh

# 3. Si todo está bien, commit
git commit -m "Tu mensaje"

# 4. Push
git push
```

---

## 📞 RECURSOS

- **Google Cloud Console:** https://console.cloud.google.com/apis/credentials
- **Vercel Environment Variables:** https://vercel.com/dashboard → Tu proyecto → Settings → Environment Variables
- **Script de verificación:** `./VERIFICAR_SEGURIDAD_API_KEY.sh`

---

**🔒 SEGURIDAD PRIMERO. Sin excepciones.**

