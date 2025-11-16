# 🚀 Inicio Rápido - ConsolidGPT con IA

## ✨ NUEVO: Ahora con Inteligencia Artificial

ConsolidGPT usa Google Gemini AI para conversaciones naturales e inteligentes.

---

## ⚡ Opción 1: Script Automático (Más Fácil)

```bash
./START.sh
```

Luego abre: **http://localhost:5000**

---

## 🔧 Opción 2: Manual

### 1. Instalar dependencias (incluye Google AI)

```bash
pip3 install -r requirements.txt
```

### 2. Verificar API Key

El archivo `.env` ya tiene tu API key configurada. Si necesitas cambiarla:
```bash
# Edita .env
GOOGLE_API_KEY=tu-api-key-aqui
```

### 3. Iniciar servidor

```bash
python3 app.py
```

### 4. Abrir en navegador

Abre: **http://localhost:5000**

---

## 🌐 Para Compartir con Clientes (Deploy en Vercel)

### Método Rápido:

```bash
# Instalar Vercel CLI (solo una vez)
npm install -g vercel

# Deploy
vercel --prod
```

Te dará una URL como: `https://consolid-gpt-xxxxx.vercel.app`

**¡Comparte esa URL con tus clientes!** 🎉

---

## 📱 Cómo Usar la App

1. **Abre la web** en tu navegador
2. **Conversa naturalmente** con el agente IA:
   - 💬 "Hola, necesito un viaje a Cancún"
   - 💬 "¿Cuál es mejor para niños pequeños?"
   - 💬 "Compara los dos hoteles"
   - 💬 "¿Qué incluye el kids club?"
3. **El agente IA responde** de forma inteligente y contextual
4. **Mantén la conversación** - recuerda todo lo que has dicho
5. **Reserva** cuando estés listo

---

## 🎨 Características

- 🧠 **Agente IA Inteligente** - Conversaciones naturales con Google Gemini
- 💬 Chat en tiempo real con memoria de contexto
- 📱 Funciona en móvil y desktop
- 🎯 Botones de acciones rápidas
- ⌨️ Atajos: Enter para enviar, Shift+Enter para nueva línea
- 🔄 Botón de reiniciar conversación
- 🎨 Diseño moderno con gradientes

---

## ❓ Problemas Comunes

**"No se puede conectar al servidor"**
- Verifica que el servidor esté corriendo
- Revisa que estés en http://localhost:5000

**"Module not found"**
- Ejecuta: `pip3 install -r requirements.txt`

**"Port 5000 already in use"**
- Detén otros servicios en el puerto 5000
- O cambia el puerto en `app.py` (línea final)

---

## 📞 Siguiente Paso

Una vez que funcione en local, sigue la guía `DEPLOY_VERCEL.md` para ponerlo en línea y compartirlo con tus clientes.
