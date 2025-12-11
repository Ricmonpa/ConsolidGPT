# 🔒 Guía: Configurar Restricciones en API Key de Google Gemini

## 🎯 Configuración Recomendada para Vercel

Cuando creas tu API key en Google Cloud Console, aquí están las mejores prácticas:

---

## ✅ Restricciones de API (OBLIGATORIO)

### **SÍ, debes restringir tu API key**

1. En "Restricciones de API", selecciona **"Restringir clave"**
2. Busca y marca **"Generative Language API"** (o "Gemini API")
3. **NO marques otras APIs** (solo la que necesitas)

**¿Por qué?**
- Previene que alguien use tu key para otras APIs de Google
- Si tu key se filtra, solo puede usarse para Gemini
- Es una buena práctica de seguridad

---

## ⚠️ Restricciones de Aplicación (Para Vercel)

### **Puedes dejar "Ninguno"**

**Para Vercel, la configuración recomendada es:**

```
Restricciones de Aplicación: Ninguno
```

**¿Por qué?**
- ✅ Las llamadas a la API vienen del **backend (serverless)** de Vercel
- ✅ NO vienen directamente del navegador del usuario
- ✅ Las IPs de Vercel son **dinámicas** (cambian constantemente)
- ✅ Restringir por dominio web no aplica para llamadas desde servidor

### ❌ Por qué NO funciona restringir por sitio web:
- Tu app en Vercel hace llamadas desde funciones serverless
- Estas funciones tienen IPs que cambian constantemente
- Google no puede verificar el dominio desde donde se llama (es el servidor)

### ❌ Por qué NO funciona restringir por IP:
- Vercel usa un rango de IPs muy amplio y dinámico
- Cada deployment puede usar IPs diferentes
- Puede fallar en cualquier momento sin aviso

---

## 📋 Configuración Final Recomendada

Cuando creas tu API key, usa esta configuración:

```
┌─────────────────────────────────────┐
│ Nombre: consolid API 2             │
│                                     │
│ ✅ Restricciones de API:            │
│    [x] Restringir clave             │
│    [x] Generative Language API      │
│                                     │
│ ⚠️ Restricciones de Aplicación:     │
│    [ ] Ninguno  ← SELECCIONA ESTO   │
│                                     │
│ [Crear] [Cancelar]                  │
└─────────────────────────────────────┘
```

---

## 🔐 Seguridad Adicional

Aunque no puedas restringir por aplicación, tu API key está protegida por:

1. **Variables de Entorno**: La key está en el servidor, no en el código público
2. **Backend Serverless**: Las llamadas van desde Vercel, no del navegador
3. **Restricción de API**: Solo funciona para Gemini
4. **CORS**: Tu backend controla quién puede hacer requests

---

## 🚨 Si tu Key se Filtra

Si accidentalmente expones tu API key:

1. Ve a Google Cloud Console → Credentials
2. Encuentra tu API key
3. Click en los 3 puntos → **"Eliminar"** o **"Regenerar"**
4. Crea una nueva key
5. Actualiza `.env` y Vercel con la nueva key

---

## ✅ Resumen Rápido

**Para tu deployment en Vercel:**
- ✅ **SÍ** restringe por API (solo Generative Language API)
- ✅ **SÍ** deja "Ninguno" en restricciones de aplicación
- ✅ **SÍ** guarda tu key como variable de entorno (nunca en código)

¡Con esta configuración estarás listo para desplegar en Vercel! 🚀

