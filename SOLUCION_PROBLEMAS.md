# 🔧 Solución de Problemas - ConsolidGPT

## ❌ Errores Comunes y Soluciones

### Error: "module 'google.generativeai' has no attribute 'GenerativeModel'"

**Causa:** Versión incorrecta de la librería de Google Generative AI

**Solución:**
```bash
pip3 install --upgrade google-generativeai
```

Verifica que la versión sea >= 0.7.0:
```bash
pip3 show google-generativeai
```

---

### Error: "GOOGLE_API_KEY no encontrada"

**Causa:** Archivo `.env` no existe o está mal configurado

**Solución:**
1. Verifica que existe el archivo `.env` en la raíz del proyecto
2. Abre `.env` y verifica que contenga:
   ```
   GOOGLE_API_KEY=tu-api-key-aqui
   ```
3. Reinicia el servidor

---

### Error: "Failed to load resource: 404 (NOT FOUND) favicon.ico"

**Causa:** Navegador busca favicon que no existe

**Solución:** Ya está solucionado. El archivo `static/favicon.ico` fue creado.

Si persiste, limpia el caché del navegador (Cmd+Shift+R en Mac)

---

### Error: "500 (INTERNAL SERVER ERROR) /api/chat"

**Causas posibles:**

1. **API Key inválida**
   - Verifica que la API key en `.env` sea correcta
   - Verifica que la API key esté activa en Google Cloud Console

2. **Límite de API excedido**
   - Revisa tu uso en: https://console.cloud.google.com
   - Free tier: 60 req/min, 1500 req/día

3. **Error en el código**
   - Revisa los logs del servidor en la terminal
   - Busca el mensaje de error específico

**Solución general:**
```bash
# Detener servidor (Ctrl+C)
# Reinstalar dependencias
pip3 install -r requirements.txt --upgrade
# Reiniciar servidor
python3 app.py
```

---

### Error: "Connection refused" o "Cannot connect to server"

**Causa:** Servidor Flask no está corriendo

**Solución:**
```bash
# Iniciar servidor
python3 app.py

# O usar el script
./START.sh
```

Verifica que veas:
```
* Running on http://127.0.0.1:5000
```

---

### Error: "Port 5000 already in use"

**Causa:** Otro proceso está usando el puerto 5000

**Solución:**
```bash
# Encontrar el proceso
lsof -i :5000

# Matar el proceso (reemplaza PID con el número que aparece)
kill -9 PID

# O cambiar el puerto en app.py (última línea):
app.run(debug=True, host='0.0.0.0', port=5001)
```

---

### Error: "ModuleNotFoundError: No module named 'flask'"

**Causa:** Dependencias no instaladas

**Solución:**
```bash
pip3 install -r requirements.txt
```

---

### Error: Respuestas lentas del agente IA

**Causa:** Primera llamada a la API de Google Gemini

**Solución:** 
- Es normal que la primera respuesta tarde 2-5 segundos
- Las siguientes respuestas son más rápidas
- Si persiste, verifica tu conexión a internet

---

### Error: Agente IA responde en inglés

**Causa:** System prompt no está siendo aplicado correctamente

**Solución:**
Edita `src/ai_agent.py` y asegúrate de que el system prompt incluya:
```python
Tu tono es profesional, amigable, eficiente y proactivo. 
Hablas español de forma natural y cercana.
```

---

### Error: "Generative Language API has not been used" o "API is disabled"

**Causa:** La API de Google Gemini no está habilitada en tu proyecto

**Solución:**
1. Abre este link: https://console.developers.google.com/apis/api/generativelanguage.googleapis.com/overview?project=429013278512
2. Click en "ENABLE" (Habilitar)
3. Espera 1-2 minutos
4. Recarga tu app

**Alternativa - Usar Google AI Studio:**
1. Ve a: https://makersuite.google.com/app/apikey
2. Crea una nueva API key
3. Actualiza `.env` con la nueva key
4. Reinicia el servidor

📖 **Guía completa:** Ver `HABILITAR_API_GOOGLE.md`

---

### Error: "models/gemini-pro is not found for API version v1beta"

**Causa:** Versión incorrecta de la API o modelo no disponible

**Solución:** Ya está arreglado en el código. Usamos `gemini-1.5-flash` con API v1.

Si persiste:
1. Verifica que `src/ai_agent.py` use:
   ```python
   self.api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
   ```
2. Reinicia el servidor
3. Recarga la página

---

### Error: "API quota exceeded"

**Causa:** Has superado el límite gratuito de Google Gemini

**Solución:**
1. Espera a que se reinicie el contador (diario/mensual)
2. O actualiza tu plan en Google Cloud Console
3. Monitorea tu uso en: https://console.cloud.google.com

---

### Error: Agente IA inventa información

**Causa:** Temperature muy alta o system prompt no claro

**Solución:**
Edita `src/ai_agent.py`, línea ~25:
```python
self.generation_config = {
    'temperature': 0.5,  # Reduce de 0.7 a 0.5 para más precisión
    'top_p': 0.8,
    'top_k': 40,
}
```

Y refuerza en el system prompt:
```python
NUNCA debes inventar información, precios, hoteles, aerolíneas u horarios 
que no estén explícitamente en la base de datos.
```

---

### Error: Deploy en Vercel falla

**Causas posibles:**

1. **Variable de entorno no configurada**
   - Ve a Vercel Dashboard → Settings → Environment Variables
   - Agrega `GOOGLE_API_KEY`

2. **requirements.txt incorrecto**
   - Verifica que todas las dependencias estén listadas
   - Verifica las versiones

3. **Archivos faltantes**
   - Asegúrate de que todos los archivos estén en el repo
   - Verifica que `vercel.json` esté configurado

**Solución:**
```bash
# Ver logs de Vercel
vercel logs

# Redeploy
vercel --prod
```

---

### Error: Chat no mantiene contexto

**Causa:** Sesiones no se están guardando correctamente

**Solución:**
Verifica que en `app.py` las sesiones se estén creando:
```python
if session_id not in user_sessions:
    user_sessions[session_id] = AIAgent(GOOGLE_API_KEY, database_content)
```

---

### Error: Botones rápidos no funcionan

**Causa:** JavaScript no se está cargando

**Solución:**
1. Abre la consola del navegador (F12)
2. Busca errores en la pestaña "Console"
3. Verifica que `static/script.js` se esté cargando
4. Limpia caché del navegador (Cmd+Shift+R)

---

## 🔍 Debugging

### Ver logs del servidor
Los logs aparecen en la terminal donde ejecutaste `python3 app.py`

### Ver logs del navegador
1. Abre DevTools (F12 o Cmd+Option+I)
2. Ve a la pestaña "Console"
3. Ve a la pestaña "Network" para ver requests

### Probar API directamente
```bash
# Health check
curl http://localhost:5000/api/health

# Enviar mensaje
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola", "session_id": "test123"}'
```

---

## 📞 Soporte Adicional

Si ninguna solución funciona:

1. **Revisa los logs** completos del servidor
2. **Copia el error exacto** que aparece
3. **Verifica tu versión de Python**: `python3 --version` (debe ser 3.7+)
4. **Reinstala todo desde cero**:
   ```bash
   pip3 uninstall -y Flask flask-cors google-generativeai python-dotenv
   pip3 install -r requirements.txt
   ```

---

## ✅ Checklist de Verificación

Antes de reportar un problema, verifica:

- [ ] Python 3.7+ instalado
- [ ] Todas las dependencias instaladas (`pip3 install -r requirements.txt`)
- [ ] Archivo `.env` existe con `GOOGLE_API_KEY`
- [ ] Servidor Flask corriendo sin errores
- [ ] Puerto 5000 disponible
- [ ] Navegador actualizado
- [ ] Conexión a internet estable
- [ ] API key de Google válida y activa

---

**Si todo falla, reinicia desde cero:**

```bash
# 1. Detener servidor (Ctrl+C)
# 2. Reinstalar dependencias
pip3 install -r requirements.txt --upgrade --force-reinstall
# 3. Verificar .env
cat .env
# 4. Reiniciar servidor
python3 app.py
# 5. Abrir navegador en http://localhost:5000
```
