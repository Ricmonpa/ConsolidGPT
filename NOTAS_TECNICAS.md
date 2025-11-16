# 📝 Notas Técnicas - ConsolidGPT

## 🔧 Implementación de la IA

### Decisión de Arquitectura: API REST Directa

**Problema Original:**
La librería `google-generativeai` tenía conflictos de versiones y dependencias incompatibles en Python 3.8.

**Solución Implementada:**
Usar la API REST de Google Gemini directamente con `requests`, sin dependencias adicionales.

### Ventajas de esta Aproximación

1. **Sin Conflictos de Dependencias**
   - Solo requiere `requests` (librería estándar)
   - No hay problemas de versiones
   - Funciona en cualquier versión de Python 3.7+

2. **Mayor Control**
   - Control total sobre los requests
   - Mejor manejo de errores
   - Timeouts configurables

3. **Más Ligero**
   - Menos dependencias = menos problemas
   - Instalación más rápida
   - Menor tamaño del proyecto

4. **Más Transparente**
   - Puedes ver exactamente qué se envía a la API
   - Fácil de debuggear
   - Logs más claros

### Cómo Funciona

```python
# URL de la API
api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={api_key}"

# Payload
payload = {
    "contents": [{
        "parts": [{
            "text": "Tu mensaje aquí"
        }]
    }],
    "generationConfig": {
        "temperature": 0.7,
        "topP": 0.8,
        "topK": 40,
        "maxOutputTokens": 2048
    }
}

# Request
response = requests.post(api_url, json=payload)
result = response.json()
ai_response = result['candidates'][0]['content']['parts'][0]['text']
```

### Configuración de Generación

| Parámetro | Valor | Descripción |
|-----------|-------|-------------|
| `temperature` | 0.7 | Creatividad (0.0 = conservador, 1.0 = creativo) |
| `topP` | 0.8 | Nucleus sampling |
| `topK` | 40 | Top-k sampling |
| `maxOutputTokens` | 2048 | Máximo de tokens en respuesta |

### Manejo de Contexto

El agente mantiene contexto incluyendo:
- System prompt (instrucciones)
- Últimos 6 mensajes de la conversación
- Base de datos completa

Esto permite conversaciones naturales y coherentes.

### Manejo de Errores

```python
try:
    response = requests.post(api_url, json=payload, timeout=30)
    if response.status_code != 200:
        # Manejar error de API
    # Procesar respuesta
except requests.exceptions.Timeout:
    # Timeout
except requests.exceptions.RequestException:
    # Error de conexión
except Exception:
    # Otros errores
```

### Límites y Consideraciones

**Google Gemini Free Tier:**
- 60 requests/minuto
- 1,500 requests/día
- Timeout de 30 segundos por request

**Optimizaciones:**
- Caché de respuestas frecuentes (futuro)
- Rate limiting por usuario (futuro)
- Fallback a respuestas predefinidas si API falla

### Seguridad

1. **API Key Protegida**
   - Almacenada en `.env`
   - No se expone al frontend
   - No se sube a GitHub

2. **Validación de Input**
   - Mensajes vacíos rechazados
   - Timeout para prevenir ataques

3. **Rate Limiting**
   - Implementar en producción
   - Prevenir abuso

### Testing

```bash
# Test del agente IA
python3 test_ai_agent.py

# Test de API directamente
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hola", "session_id": "test"}'
```

### Monitoreo

**Logs a Revisar:**
- Errores de API (status != 200)
- Timeouts
- Errores de conexión
- Uso de tokens

**Métricas Importantes:**
- Tiempo de respuesta promedio
- Tasa de error
- Uso de API (requests/día)
- Satisfacción del usuario

### Escalabilidad

**Para Producción:**

1. **Base de Datos Real**
   - Migrar de .txt a PostgreSQL/MongoDB
   - Caché con Redis

2. **Rate Limiting**
   - Por IP
   - Por usuario
   - Por sesión

3. **Load Balancing**
   - Múltiples instancias
   - Queue de requests

4. **Monitoring**
   - Sentry para errores
   - Google Analytics
   - Custom dashboard

### Alternativas Consideradas

1. **google-generativeai (librería oficial)**
   - ❌ Conflictos de dependencias
   - ❌ Versiones incompatibles
   - ✅ Más features

2. **API REST Directa (implementada)**
   - ✅ Sin conflictos
   - ✅ Más control
   - ✅ Más ligero
   - ⚠️ Menos features

3. **OpenAI API**
   - ✅ Más maduro
   - ❌ Más caro
   - ❌ Requiere tarjeta de crédito

### Migración Futura

Si en el futuro quieres usar la librería oficial:

```python
# Instalar versión específica
pip install google-generativeai==0.8.0

# Código
import google.generativeai as genai
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
response = model.generate_content("Hola")
```

### Debugging

**Ver requests completos:**
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Ver payload enviado:**
```python
print(json.dumps(payload, indent=2))
```

**Ver respuesta completa:**
```python
print(json.dumps(response.json(), indent=2))
```

### Performance

**Tiempos Típicos:**
- Primera llamada: 2-5 segundos (inicialización)
- Llamadas subsecuentes: 1-3 segundos
- Con caché: < 100ms (futuro)

**Optimizaciones Aplicadas:**
- Timeout de 30s
- Contexto limitado a últimos 6 mensajes
- Payload mínimo necesario

### Conclusión

La implementación con API REST directa es:
- ✅ Más confiable
- ✅ Más fácil de mantener
- ✅ Más fácil de debuggear
- ✅ Sin problemas de dependencias

Es la mejor solución para este proyecto.
