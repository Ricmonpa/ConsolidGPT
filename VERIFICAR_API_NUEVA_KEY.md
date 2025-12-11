# ✅ Verificar y Habilitar API para Nueva Key

## 🔑 Nueva API Key Configurada

Tu nueva API key ha sido actualizada en el archivo `.env`.

⚠️ **IMPORTANTE:** NUNCA subas tu API key a GitHub. Este archivo solo es una guía.

---

## 🔍 Verificar si Necesitas Habilitar la API

Cuando creas una nueva API key, es posible que necesites habilitar la API de Generative Language en el proyecto asociado.

### Paso 1: Identificar el Proyecto de la API Key

1. Ve a: **https://console.cloud.google.com/apis/credentials**
2. Busca tu API key en la lista
3. Nota el **nombre del proyecto** donde está creada
4. También puedes ver el **Project ID** o **Project Number**

### Paso 2: Verificar si la API Está Habilitada

**Opción A: Usando el Project ID directamente**

Si conoces el Project ID de tu nuevo proyecto, ve directamente a:

🔗 **https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com**

1. Selecciona el proyecto correcto (dropdown en la parte superior)
2. Verifica el estado:
   - ✅ **"API ENABLED"** o **"MANAGE"** = Ya está habilitada ✅
   - ❌ **"ENABLE"** = Necesitas habilitarla (click en el botón)

**Opción B: Desde la página de la API Key**

1. Ve a: **https://console.cloud.google.com/apis/credentials**
2. Busca tu API key y haz click en ella
3. Verás información sobre el proyecto asociado
4. Click en el nombre del proyecto para ir a su dashboard
5. Luego ve a: **APIs & Services → Library**
6. Busca "Generative Language API"
7. Si no está habilitada, click en **"ENABLE"**

---

## 🚀 Link Directo para Habilitar (Si es Necesario)

Si necesitas habilitar la API, estos son los links más comunes:

### Link Genérico (selecciona tu proyecto)
🔗 **https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com**

1. Selecciona tu proyecto en el dropdown superior
2. Si dice "ENABLE", haz click
3. Espera 1-2 minutos para que se propague

### Link desde API Library
🔗 **https://console.cloud.google.com/apis/library**

1. Busca "Generative Language API"
2. Asegúrate de tener el proyecto correcto seleccionado
3. Click en "ENABLE" si es necesario

---

## 🧪 Probar la Nueva API Key

Después de verificar/habilitar, prueba con este comando:

```bash
curl "https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key=TU_API_KEY_AQUI" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Hola, responde solo con OK"
      }]
    }]
  }'
```

Si funciona, verás una respuesta JSON con "OK" o similar.

---

## ⚠️ Si Aparece Error de "API Not Enabled"

Si al probar ves este error:
```
API has not been used in project... or it is disabled
```

**Solución:**
1. Ve al link: **https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com**
2. Asegúrate de tener el proyecto correcto seleccionado
3. Click en **"ENABLE"**
4. Espera 2-5 minutos
5. Prueba de nuevo

---

## ✅ Checklist Rápido

- [ ] API key actualizada en `.env` ✅
- [ ] Proyecto de la API key identificado
- [ ] API de Generative Language verificada/habilitada
- [ ] Prueba con curl ejecutada exitosamente
- [ ] Servidor reiniciado (si está corriendo)

---

## 🔄 Próximos Pasos

Una vez verificado:

1. **Reinicia el servidor** (si está corriendo):
   ```bash
   # Detener con Ctrl+C
   python app.py
   ```

2. **Prueba en el navegador:**
   - Ve a: http://localhost:5000
   - Envía un mensaje de prueba
   - Debería funcionar sin errores de cuota

3. **Cuando despliegues en Vercel:**
   - Actualiza también la variable de entorno `GOOGLE_API_KEY` en Vercel
   - Con tu nueva API key (reemplaza TU_API_KEY_AQUI)

---

## 📞 Recursos

- **Google Cloud Console:** https://console.cloud.google.com
- **API Library:** https://console.cloud.google.com/apis/library
- **Credentials:** https://console.cloud.google.com/apis/credentials
- **Generative Language API:** https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com

---

**¡Tu nueva API key está lista! 🎉**

