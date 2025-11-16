# 🚀 Deploy ConsolidGPT a Vercel - AHORA

## Opción 1: Deploy Rápido con GitHub (RECOMENDADO)

### Paso 1: Sube tu código a GitHub

```bash
# Inicializar git (si no lo has hecho)
git init

# Agregar todos los archivos
git add .

# Commit
git commit -m "ConsolidGPT con tarjetas interactivas"

# Crear repositorio en GitHub y conectar
git remote add origin https://github.com/TU_USUARIO/consolidgpt.git
git branch -M main
git push -u origin main
```

### Paso 2: Conectar con Vercel

1. Ve a https://vercel.com
2. Click en "Add New" → "Project"
3. Importa tu repositorio de GitHub
4. Vercel detectará automáticamente que es Python/Flask
5. Click en "Deploy"

### Paso 3: Configurar Variable de Entorno

1. En tu proyecto en Vercel, ve a "Settings"
2. Click en "Environment Variables"
3. Agrega:
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** (pega tu API key de Google)
   - **Environment:** Marca todas (Production, Preview, Development)
4. Click "Save"

### Paso 4: Re-deploy

1. Ve a "Deployments"
2. Click en los 3 puntos del último deployment
3. Click "Redeploy"

¡Listo! Tu app estará en: `https://tu-proyecto.vercel.app`

---

## Opción 2: Deploy con Vercel CLI

### Paso 1: Instalar Vercel CLI

```bash
npm install -g vercel
```

Si no tienes npm, instala Node.js desde: https://nodejs.org

### Paso 2: Login

```bash
vercel login
```

### Paso 3: Deploy

```bash
# Desde la raíz del proyecto
vercel
```

Responde:
- Set up and deploy? → **Yes**
- Which scope? → Tu cuenta
- Link to existing project? → **No**
- Project name? → **consolidgpt**
- Directory? → **.** (punto)
- Override settings? → **No**

### Paso 4: Agregar API Key

```bash
vercel env add GOOGLE_API_KEY
```

Pega tu API key cuando te lo pida.

Selecciona: **Production, Preview, Development** (todas)

### Paso 5: Deploy a Producción

```bash
vercel --prod
```

---

## Opción 3: Deploy Manual (Sin CLI)

### Paso 1: Crear cuenta en Vercel

Ve a https://vercel.com y crea una cuenta.

### Paso 2: Comprimir tu proyecto

```bash
# Crear un zip SIN node_modules, .env, __pycache__
zip -r consolidgpt.zip . -x "*.git*" "*.env*" "*__pycache__*" "*node_modules*" "*.DS_Store"
```

### Paso 3: Subir a Vercel

1. En Vercel Dashboard, click "Add New" → "Project"
2. Click "Upload"
3. Arrastra tu archivo `consolidgpt.zip`
4. Vercel lo procesará automáticamente

### Paso 4: Configurar Variables

1. Settings → Environment Variables
2. Agrega `GOOGLE_API_KEY` con tu API key
3. Redeploy

---

## ⚡ Método Más Rápido (GitHub)

Si ya tienes GitHub:

```bash
# 1. Sube a GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/TU_USUARIO/consolidgpt.git
git push -u origin main

# 2. Ve a vercel.com
# 3. Import from GitHub
# 4. Deploy
# 5. Agrega GOOGLE_API_KEY en Settings
# 6. Redeploy
```

**Tiempo total: 5 minutos** ⚡

---

## 🔑 Tu API Key de Google

Tu API key está en el archivo `.env`:

```bash
cat .env | grep GOOGLE_API_KEY
```

Copia ese valor para usarlo en Vercel.

---

## ✅ Verificar Deployment

Una vez deployado:

1. Abre la URL que te dio Vercel
2. Prueba el chat
3. Verifica que aparezcan las tarjetas
4. Prueba en móvil

---

## 🐛 Si algo falla

### Error: "Module not found"
- Verifica que `requirements.txt` esté en la raíz
- Re-deploy

### Error: "API Key not found"
- Verifica que agregaste `GOOGLE_API_KEY` en Vercel
- Redeploy después de agregar la variable

### Error: "Build failed"
- Revisa los logs en Vercel Dashboard
- Verifica que `app.py` tenga `# -*- coding: utf-8 -*-` al inicio

---

## 📱 Compartir tu App

Una vez deployada, comparte:
```
https://consolidgpt.vercel.app
```

O el dominio que Vercel te asigne.

---

## 🎉 ¡Listo!

Tu ConsolidGPT estará disponible 24/7 en internet con:
- ✅ Tarjetas interactivas
- ✅ Logo personalizado
- ✅ Responsive móvil
- ✅ System prompt corregido
- ✅ SSL automático (HTTPS)
- ✅ CDN global

**¿Cuál método prefieres usar?**
