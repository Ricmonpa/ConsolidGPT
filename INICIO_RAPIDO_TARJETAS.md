# 🚀 Inicio Rápido - Nuevas Tarjetas UI

## ⚡ En 3 Pasos

### 1️⃣ Inicia la aplicación
```bash
python app.py
```

### 2️⃣ Abre en tu navegador
```
http://localhost:5000
```

### 3️⃣ Pregunta al bot
```
"Necesito un viaje familiar a Cancún"
```

**¡Listo!** Las tarjetas aparecerán automáticamente. ✨

---

## 🎨 Ver Demo de Tarjetas (Sin Backend)

Si solo quieres ver cómo se ven las tarjetas:

```bash
open test_cards.html
```

O arrastra el archivo `test_cards.html` a tu navegador.

---

## 📱 Navegación

### Sidebar (Izquierda):
- **Dashboard**: Estadísticas y resumen
- **New Search**: Chat principal (aquí aparecen las tarjetas)
- **History**: Historial de conversaciones
- **Settings**: Configuración

### En Móvil:
- Toca el icono **☰** para abrir el menú

---

## 💬 Frases que Activan Tarjetas

### Para ver tarjeta de VUELO:
- "Necesito un vuelo a Cancún"
- "¿Qué vuelos hay disponibles?"
- "Muéstrame opciones de vuelo"

### Para ver tarjeta de HOTEL:
- "¿Qué hoteles tienen disponibles?"
- "Cuéntame sobre el Hyatt Ziva"
- "Necesito un hotel all-inclusive"

### Para ver tarjeta de PAQUETE:
- "Necesito un viaje familiar a Cancún"
- "¿Tienen paquetes todo incluido?"
- "Quiero un paquete completo"

---

## 🎯 Cómo Reservar

1. El bot muestra las tarjetas
2. Revisa la información
3. Haz clic en el botón **"Reservar"**
4. El bot procesa la reserva
5. Recibes confirmación con PNR

---

## 🎨 Características Visuales

### Tarjetas:
- **Azul** = Vuelos ✈️
- **Verde** = Hoteles 🏨
- **Morado** = Paquetes 🎁

### Sidebar:
- **Oscuro** = Profesional
- **Iconos** = Fácil navegación
- **Responsive** = Funciona en móvil

---

## 🔧 Si Algo No Funciona

### Las tarjetas no aparecen:
1. Verifica que el bot mencione palabras clave:
   - "vuelo", "AM540", "Aeroméxico"
   - "hotel", "Hyatt Ziva", "all-inclusive"
   - "paquete", "todo incluido"

2. Abre la consola del navegador (F12)
3. Busca errores en JavaScript

### El sidebar no se ve oscuro:
1. Refresca la página (Ctrl+R o Cmd+R)
2. Limpia caché del navegador
3. Verifica que `style.css` se cargó correctamente

### Los botones no funcionan:
1. Verifica que `script.js` se cargó
2. Abre consola (F12) y busca errores
3. Intenta refrescar la página

---

## 📊 Dashboard

En el Dashboard verás:
- **Consultas Hoy**: Contador de mensajes
- **Reservas Simuladas**: Cuántas veces se hizo clic en "Reservar"
- **Comisión Potencial**: Calculada automáticamente (14%)
- **Paquetes Disponibles**: Total en base de datos

---

## 🎓 Tips para Agentes

### Mejores Prácticas:
1. **Sé específico**: "Viaje familiar 2 adultos 2 niños a Cancún"
2. **Pregunta detalles**: "¿Cuál es la política de cancelación?"
3. **Compara opciones**: "¿Qué diferencia hay entre los paquetes?"
4. **Confirma antes**: Revisa toda la info en la tarjeta antes de reservar

### Información Siempre Visible:
- ✈️ Horarios y códigos de vuelo
- 🏨 Estrellas y ubicación del hotel
- 💰 Precios totales
- 💼 Tu comisión (14%)
- 📜 Políticas de cancelación
- ✨ Inclusiones del paquete

---

## 🌟 Funciones Especiales

### Botones Rápidos:
En el mensaje de bienvenida hay 3 botones:
- **✈️ Viaje a Cancún**: Inicia búsqueda de paquetes
- **📜 Políticas**: Consulta políticas de cancelación
- **👶 Kids Club**: Info sobre servicios para niños

### Auto-scroll:
El chat hace scroll automático al final cuando:
- Envías un mensaje
- El bot responde
- Aparece una tarjeta

### Contador de Stats:
Automáticamente cuenta:
- Cada mensaje que envías
- Cada vez que haces clic en "Reservar"
- Comisión acumulada

---

## 📱 Responsive

### Desktop (>768px):
- Sidebar fijo a la izquierda
- Tarjetas en layout horizontal
- Máximo ancho 900px para chat

### Móvil (<768px):
- Sidebar oculto (abre con ☰)
- Tarjetas en layout vertical
- Botones al 100% de ancho
- Touch-friendly

---

## 🎉 ¡Disfruta!

Tu chat ahora tiene:
- ✅ Tarjetas interactivas profesionales
- ✅ Sidebar oscuro moderno
- ✅ Botones de reserva funcionales
- ✅ Diseño responsive
- ✅ Detección automática
- ✅ Animaciones suaves

**Todo funciona automáticamente. Solo usa el chat normalmente.** 🚀

---

## 📞 Archivos de Ayuda

- `GUIA_TARJETAS_UI.md` - Documentación completa
- `RESUMEN_UI_TARJETAS.md` - Resumen de implementación
- `EJEMPLO_VISUAL_CHAT.md` - Ejemplos visuales
- `test_cards.html` - Demo de tarjetas

---

## 🔄 Reiniciar Chat

Si quieres empezar de nuevo:
1. Haz clic en el botón **"Reiniciar"** (arriba a la derecha)
2. O refresca la página

---

**¡Listo para cotizar viajes como un profesional!** ✈️🏨🎁
