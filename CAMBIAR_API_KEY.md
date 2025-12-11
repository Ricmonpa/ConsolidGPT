# 🔑 Cómo Cambiar la API Key de Google Gemini

## 🎯 Problema: Cuota Excedida

Si ves este error:
```
❌ Error de API: You exceeded your current quota, please check your plan and billing details.
```

Significa que tu API key actual se quedó sin cuota gratuita.

---

## ✅ Solución: Actualizar la API Key

### Paso 1: Obtener Nueva API Key

1. Ve a: https://aistudio.google.com/apikey
2. Inicia sesión con tu cuenta de Google
3. Click en **"Create API Key"** o **"Get API Key"**
4. Selecciona o crea un proyecto de Google Cloud
5. Copia la nueva API key que te dan

### Paso 2: Actualizar el Archivo `.env`

1. Abre el archivo `.env` en la raíz del proyecto
2. Busca la línea:
   ```
   GOOGLE_API_KEY=tu-api-key-anterior
   ```
3. Reemplázala con tu nueva API key:
   ```
   GOOGLE_API_KEY=tu-nueva-api-key-aqui
   ```
4. Guarda el archivo

### Paso 3: Reiniciar el Servidor

Si el servidor está corriendo, detenlo (Ctrl+C) y vuelve a iniciarlo:

```bash
python app.py
```

---

## 🔄 Alternativa: Usar Variable de Entorno Directamente

También puedes definir la variable de entorno sin editar el archivo:

**En Mac/Linux:**
```bash
export GOOGLE_API_KEY=tu-nueva-api-key-aqui
python app.py
```

**En Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="tu-nueva-api-key-aqui"
python app.py
```

---

## 📝 Ejemplo Completo

1. Obtienes tu nueva API key: `AIzaSyEjemplo123456789NuevaKey`
2. Actualizas `.env`:
   ```
   GOOGLE_API_KEY=tu-api-key-aqui
   ```
3. Reinicias el servidor
4. ¡Listo! Debería funcionar con la nueva cuota

---

## ⚠️ Notas Importantes

- Cada API key de Google Gemini tiene un límite gratuito (varía según el plan)
- Puedes crear múltiples proyectos en Google Cloud para tener múltiples API keys
- Si estás en Vercel u otro hosting, también debes actualizar la variable de entorno allí

---

## 🌐 Si Estás en Vercel

1. Ve a tu proyecto en https://vercel.com
2. Settings → Environment Variables
3. Busca `GOOGLE_API_KEY`
4. Click en los 3 puntos → Edit
5. Actualiza con tu nueva API key
6. Guarda y haz un nuevo deploy

---

## ✅ Verificar que Funciona

Después de cambiar la API key, prueba enviando un mensaje en el chat. Si no aparece el error de cuota, ¡está funcionando correctamente!

---

## 🔒 Configuración de Restricciones (Para Vercel)

Cuando crees tu API key, aquí están las recomendaciones:

### ✅ Restricciones de API (RECOMENDADO)

**Sí, debes restringir:**

1. Selecciona **"Restringir clave"**
2. Busca y selecciona: **"Generative Language API"** o **"Gemini API"**
3. Esto asegura que la key solo funcione para Gemini y no otras APIs de Google

### ⚠️ Restricciones de Aplicación

**Para Vercel, puedes dejarlo en "Ninguno"** porque:
- Las llamadas vienen del backend (serverless) de Vercel, no directamente del navegador
- Las IPs de Vercel son dinámicas y cambian constantemente
- Restringir por dominio web no aplica para llamadas desde servidor

**Si quieres más seguridad (opcional):**
- Puedes restringir por IP, pero necesitarías agregar el rango de IPs de Vercel (complicado y puede fallar)
- **Recomendación:** Deja "Ninguno" para desarrollo y producción en Vercel

### 📋 Resumen de Configuración Recomendada

```
✅ Restricciones de API: SÍ → Solo "Generative Language API"
⚠️ Restricciones de Aplicación: Ninguno (para Vercel)
```

Esto te da seguridad sin complicaciones para el deployment.

