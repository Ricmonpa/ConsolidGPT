# 🚀 Deployment en Vercel - Guía Paso a Paso

## ✅ Pre-requisitos

Tu proyecto ya está listo para Vercel:
- ✅ `vercel.json` configurado
- ✅ `.gitignore` con `.env`
- ✅ `requirements.txt` actualizado
- ✅ Código optimizado

## 📋 Pasos para Deployar

### 1. Instalar Vercel CLI (si no lo tienes)

```bash
npm install -g vercel
```

### 2. Login en Vercel

```bash
vercel login
```

Esto abrirá tu navegador para autenticarte.

### 3. Deploy desde la Terminal

Desde la raíz de tu proyecto:

```bash
vercel
```

Responde las preguntas:
- **Set up and deploy?** → Yes
- **Which scope?** → Tu cuenta personal
- **Link to existing project?** → No (primera vez) o Yes (si ya existe)
- **Project name?** → `consolidgpt` (o el que prefieras)
- **Directory?** → `.` (punto, directorio actual)
- **Override settings?** → No

### 4. Configurar Variables de Entorno

**IMPORTANTE:** Debes agregar tu API key de Google en Vercel.

#### Opción A: Desde la Terminal
```bash
vercel env add GOOGLE_API_KEY
```
Pega tu API key cuando te lo pida.

#### Opción B: Desde el Dashboard de Vercel
1. Ve a tu proyecto en https://vercel.com/dashboard
2. Settings → Environment Variables
3. Agrega:
   - **Name:** `GOOGLE_API_KEY`
   - **Value:** Tu API key de Google
   - **Environment:** Production, Preview, Development

### 5. Re-deploy con las Variables

```bash
vercel --prod
```

## 🎯 Comandos Útiles

```bash
# Deploy de prueba (preview)
vercel

# Deploy a producción
vercel --prod

# Ver logs
vercel logs

# Ver información del proyecto
vercel inspect

# Eliminar deployment
vercel remove [deployment-url]
```

## 🌐 URLs Resultantes

Después del deploy obtendrás:
- **Preview URL:** `consolidgpt-xxx.vercel.app` (cada deploy)
- **Production URL:** `consolidgpt.vercel.app` (tu dominio principal)

## ⚙️ Configuración Adicional (Opcional)

### Dominio Personalizado

1. Ve a tu proyecto en Vercel Dashboard
2. Settings → Domains
3. Agrega tu dominio personalizado
4. Sigue las instrucciones para configurar DNS

### Variables de Entorno Adicionales

Si necesitas más variables:
```bash
vercel env add OTRA_VARIABLE
```

## 🔍 Verificar Deployment

1. Abre la URL que te dio Vercel
2. Prueba el chat
3. Verifica que las tarjetas aparezcan
4. Prueba en móvil

## 🐛 Troubleshooting

### Error: "Module not found"
```bash
# Verifica requirements.txt
cat requirements.txt

# Re-deploy
vercel --prod
```

### Error: "API Key not found"
```bash
# Verifica variables de entorno
vercel env ls

# Agrega la variable
vercel env add GOOGLE_API_KEY

# Re-deploy
vercel --prod
```

### Error: "Build failed"
```bash
# Ver logs detallados
vercel logs

# Verifica que app.py tenga encoding UTF-8
head -1 app.py
# Debe mostrar: # -*- coding: utf-8 -*-
```

## 📱 Probar en Móvil

Una vez deployado:
1. Abre la URL en tu móvil
2. Verifica que se vea a pantalla completa
3. Prueba las tarjetas interactivas
4. Verifica que el logo se vea bien

## 🔄 Actualizar Deployment

Cada vez que hagas cambios:

```bash
# Commit tus cambios (si usas git)
git add .
git commit -m "Actualización"
git push

# O deploy directo
vercel --prod
```

## 📊 Monitoreo

En el Dashboard de Vercel puedes ver:
- Número de requests
- Tiempo de respuesta
- Errores
- Logs en tiempo real

## 🎉 ¡Listo!

Tu ConsolidGPT estará disponible en:
```
https://consolidgpt.vercel.app
```

O la URL que Vercel te asigne.

---

## 🚨 Importante

- **NO subas** el archivo `.env` a git
- **SÍ configura** las variables en Vercel Dashboard
- **Prueba primero** con `vercel` (preview) antes de `vercel --prod`
- **Guarda** la URL de producción para compartir

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs: `vercel logs`
2. Verifica variables: `vercel env ls`
3. Consulta docs: https://vercel.com/docs
