# 🔑 Habilitar API de Google Gemini

## ✅ Ya Habilitaste la API

Si acabas de habilitar la API, **espera 2-5 minutos** para que Google propague los cambios.

---

## 🕐 Mientras Esperas

### Verifica que la API esté habilitada:

1. Ve a: https://console.cloud.google.com/apis/library/generativelanguage.googleapis.com?project=429013278512

2. Deberías ver un botón que dice **"MANAGE"** o **"API HABILITADA"**

3. Si dice "ENABLE", haz click para habilitar

---

## 🧪 Cómo Probar

### Opción 1: Espera 2-5 minutos y recarga la página

```
http://localhost:5000
```

Luego intenta enviar un mensaje al chat.

### Opción 2: Prueba con curl

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=AIzaSyC5UAimCkhMrdWZ12YrI4chzchSfwQBbJY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Hola"
      }]
    }]
  }'
```

Si funciona, verás una respuesta JSON con el texto generado.

---

## ❌ Si Sigue Sin Funcionar Después de 5 Minutos

### 1. Verifica el Proyecto Correcto

Asegúrate de que estás en el proyecto correcto:
- ID del proyecto: `429013278512`
- Ve a: https://console.cloud.google.com

### 2. Verifica la API Key

La API key debe estar asociada al proyecto correcto:
- Ve a: https://console.cloud.google.com/apis/credentials?project=429013278512
- Verifica que tu API key esté listada
- Si no está, crea una nueva

### 3. Verifica Cuotas

Ve a: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas?project=429013278512

Deberías ver:
- **Requests per minute:** 60
- **Requests per day:** 1,500

### 4. Verifica Facturación (Opcional)

Aunque Gemini tiene free tier, algunos proyectos requieren facturación habilitada:
- Ve a: https://console.cloud.google.com/billing?project=429013278512
- Verifica que haya una cuenta de facturación asociada

---

## 🔄 Reiniciar el Servidor

Después de habilitar la API, reinicia el servidor:

```bash
# Detener (Ctrl+C)
# Reiniciar
python3 app.py
```

---

## 🎯 Checklist de Verificación

- [x] API de Generative Language habilitada
- [ ] Esperaste 2-5 minutos
- [ ] Proyecto correcto (429013278512)
- [ ] API key correcta en `.env`
- [ ] Servidor reiniciado
- [ ] Página recargada en el navegador

---

## 💡 Tip: Crear Nueva API Key

Si sigues teniendo problemas, crea una nueva API key:

1. Ve a: https://console.cloud.google.com/apis/credentials?project=429013278512

2. Click en **"CREATE CREDENTIALS"** → **"API Key"**

3. Copia la nueva key

4. Actualiza tu `.env`:
   ```
   GOOGLE_API_KEY=tu-nueva-api-key-aqui
   ```

5. Reinicia el servidor

---

## 🚀 Una Vez Que Funcione

Verás respuestas del agente IA como:

```
🤖 ConsolidGPT: ¡Hola! 👋 Soy ConsolidGPT, tu asistente 
de viajes de Consolid. ¿En qué puedo ayudarte hoy? 
¿Buscas un viaje a Cancún? 🌴
```

---

## 📞 Recursos Útiles

- **Google Cloud Console:** https://console.cloud.google.com
- **API Library:** https://console.cloud.google.com/apis/library
- **Credentials:** https://console.cloud.google.com/apis/credentials
- **Quotas:** https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/quotas

---

## ⏰ Tiempo de Propagación

**Normal:** 2-5 minutos  
**Máximo:** 10-15 minutos  

Si después de 15 minutos sigue sin funcionar, revisa los pasos anteriores.

---

**¡La API debería estar funcionando en unos minutos! 🎉**
