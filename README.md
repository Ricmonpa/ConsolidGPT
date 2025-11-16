# ConsolidGPT 🌴✈️🧠

**Agente Conversacional Inteligente para Viajes - Powered by Google Gemini AI**

ConsolidGPT es un agente de IA con conversaciones naturales que cotiza y reserva viajes familiares a Cancún. Usa Google Gemini para respuestas inteligentes y contextuales, manteniendo toda la información de tu base de datos.

## ✨ Nuevo: Inteligencia Artificial Real

- 🧠 **Conversaciones Naturales** - Habla como un humano, no como un bot
- 🎯 **Entiende Contexto** - Recuerda toda la conversación
- 💡 **Respuestas Inteligentes** - Sugiere, compara y recomienda
- 🤝 **Personalidad Profesional** - Tono amigable y experto
- 📚 **Memoria de Conversación** - Mantiene el hilo de la charla
- ⚡ **API REST Directa** - Sin dependencias problemáticas

## 🎯 Características

- ✅ **Agente IA Conversacional** - Powered by Google Gemini
- ✅ **Interfaz Web Moderna** - UI diseñada y responsive
- ✅ Consulta de paquetes de viaje desde base de datos local
- ✅ Presentación estructurada de opciones (Vuelo + Hotel)
- ✅ Cálculo automático de comisiones (14%)
- ✅ Respuestas inteligentes sobre políticas y kids clubs
- ✅ Simulación de reservas con PNR y códigos de hotel
- ✅ **Deploy en Vercel** - Comparte con tus clientes

## 📁 Estructura del Proyecto

```
consolid-gpt/
├── data/
│   └── Base_de_Datos_Cancun.txt    # Base de datos de paquetes
├── src/
│   ├── ai_agent.py                  # Agente IA con Google Gemini
│   ├── main.py                      # CLI (opcional)
│   ├── chatbot.py                   # Chatbot simple (legacy)
│   └── database_loader.py           # Cargador de base de datos
├── .env                             # Variables de entorno (API keys)
├── templates/
│   └── index.html                   # UI principal
├── static/
│   ├── style.css                    # Estilos
│   └── script.js                    # JavaScript
├── app.py                           # Flask web app
├── vercel.json                      # Config para Vercel
├── requirements.txt
└── README.md
```

## 🚀 Instalación

1. **Verificar Python** (requiere Python 3.7+)
   ```bash
   python3 --version
   ```

2. **Instalar dependencias**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Configurar API Key de Google**
   
   El archivo `.env` ya está creado con tu API key. Si necesitas cambiarla:
   ```bash
   # Edita .env
   GOOGLE_API_KEY=tu-api-key-aqui
   ```

## 💻 Uso Local

### Ejecutar la Web App (Recomendado)

```bash
python3 app.py
```

Luego abre tu navegador en: **http://localhost:5000**

### Ejecutar CLI (Opcional)

```bash
cd src
python3 main.py
```

## 🌐 Deploy en Vercel

### Opción 1: Deploy Rápido con CLI

```bash
# Instalar Vercel CLI
npm install -g vercel

# Deploy
vercel

# Deploy a producción
vercel --prod
```

### Opción 2: Deploy desde GitHub

1. Sube tu proyecto a GitHub
2. Ve a [vercel.com/new](https://vercel.com/new)
3. Importa tu repositorio
4. Click en "Deploy"

**¡Listo!** Tendrás una URL como: `https://consolid-gpt.vercel.app`

📖 **Guía completa de deploy:** Ver `DEPLOY_VERCEL.md`

## 🎨 Interfaz Web

La interfaz incluye:
- 💬 Chat en tiempo real con el bot
- 🎯 Botones de acciones rápidas
- 📱 Diseño responsive (móvil y desktop)
- 🎨 UI moderna con gradientes y animaciones
- ⌨️ Atajos de teclado (Enter para enviar)
- 🔄 Botón de reiniciar conversación

## 📋 Flujo de Uso

1. **Abre la web app** en tu navegador
2. **Usa los botones rápidos** o escribe tu consulta
3. **El bot presenta opciones** de paquetes con precios y comisiones
4. **Haz preguntas** sobre políticas, kids club, etc.
5. **Simula la reserva** escribiendo "reserva" o "confirma"

## 🔧 Personalización

### Agregar Nuevos Paquetes

Edita el archivo `data/Base_de_Datos_Cancun.txt` siguiendo el formato existente:

```
**Paquete: "Nombre del Paquete"**
* Vuelo: Aerolínea (Código), Horarios
* Hotel: Nombre (Estrellas)
* Habitación: Tipo
* Detalles: Características
* Precio Total (4pax): $XXX,XXX.XX MXN
* Política de Cancelación: Descripción
```

### Modificar Tasa de Comisión

En `src/chatbot.py`, línea 13:
```python
def calculate_commission(self, price: float, rate: float = 0.14):
    # Cambia 0.14 por la tasa deseada (ej: 0.15 para 15%)
```

## 🎨 Roadmap

- [x] Interfaz web con Flask
- [x] Deploy en Vercel
- [x] **Integración con Google Gemini AI** ✨ NUEVO
- [x] **Conversaciones naturales e inteligentes** ✨ NUEVO
- [ ] Soporte para múltiples destinos
- [ ] Base de datos SQL para mejor escalabilidad
- [ ] Exportación de cotizaciones a PDF
- [ ] Sistema de autenticación para agentes
- [ ] Integración con sistemas de reservas reales
- [ ] Analytics y dashboard de métricas

## 🧠 Sobre la IA

ConsolidGPT usa **Google Gemini Pro** para:
- Generar respuestas naturales y contextuales
- Mantener conversaciones fluidas
- Entender intenciones del usuario
- Sugerir y recomendar activamente

**Regla de Oro**: El agente NUNCA inventa información. Solo usa datos del archivo `Base_de_Datos_Cancun.txt`

📖 **Más info:** Ver `UPGRADE_IA.md`

## 📝 Notas Importantes

- Los PNR y códigos de hotel generados son simulados (para demostración)
- Los precios incluyen IVA y TUA según la base de datos
- La API de Google Gemini tiene límites gratuitos (60 req/min, 1500 req/día)
- Para producción, configura la API key en Vercel como variable de entorno

## 📄 Licencia

Proyecto interno de Consolid.

---

**Desarrollado para Consolid** 🌴✈️
