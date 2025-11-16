# 🎨 Guía de Tarjetas Interactivas - ConsolidGPT

## ✅ Implementación Completada

Se han implementado **tarjetas interactivas** en el chat que se activan automáticamente cuando el bot menciona:

### 1. ✈️ Tarjetas de Vuelo
**Se activan cuando el bot menciona:**
- Códigos de vuelo: `AM540`, `VOLARIS`, `VIVA AEROBUS`
- Palabras clave: `vuelo`, `aerolínea`

**Información mostrada:**
- Aerolínea y código de vuelo
- Horarios de salida y llegada
- Fechas del viaje
- Origen y destino (CDMX → Cancún)
- Duración del vuelo
- Clase y equipaje incluido
- Precio por persona
- **Botón "Reservar Vuelo"**

---

### 2. 🏨 Tarjetas de Hotel
**Se activan cuando el bot menciona:**
- Nombres de hoteles: `HYATT ZIVA`, `HOTEL`, `RESORT`
- Palabras clave: `ALL-INCLUSIVE`

**Información mostrada:**
- Nombre del hotel y estrellas
- Ubicación (Zona Hotelera, Cancún)
- Features: All-Inclusive, Frente al mar, Kids Club, Albercas, Bares
- Política de cancelación destacada
- Precio total por noches
- **Botón "Reservar"**

---

### 3. 🎁 Tarjetas de Paquete
**Se activan cuando el bot menciona:**
- Palabras clave: `PAQUETE`, `TODO INCLUIDO`, `PACKAGE`

**Información mostrada:**
- Badge especial "PAQUETE ESPECIAL"
- Título y descripción del paquete
- Lista de inclusiones:
  - Vuelo redondo
  - Noches de hotel
  - All-Inclusive Premium
  - Traslados
  - Kids Club
  - Actividades
- Precio total con ahorro calculado
- **Botón "Reservar Paquete"**

---

## 🎯 Cómo Funciona

### Detección Automática
El sistema detecta automáticamente en las respuestas del bot:

```javascript
// Detecta vuelos
const flightPattern = /vuelo[s]?.*?(AM\d+|VOLARIS|VIVA\s*AEROBUS|AEROMEXICO)/gi;

// Detecta hoteles
const hotelPattern = /(HYATT\s*ZIVA|HOTEL|RESORT|ALL[\s-]*INCLUSIVE)/gi;

// Detecta paquetes
const packagePattern = /(PAQUETE|PACKAGE|TODO\s*INCLUIDO.*VUELO)/gi;
```

### Extracción de Datos
Las tarjetas extraen información del texto:
- **Códigos de vuelo**: `AM540`, `VOLARIS 123`
- **Horarios**: `9:00 AM`, `4:30 PM`
- **Fechas**: `1 Dic`, `7 Dic`
- **Precios**: `$8,500`, `$12,500`
- **Noches**: `6 noches`

---

## 🚀 Prueba las Tarjetas

### Opción 1: Archivo de Prueba
Abre en tu navegador:
```bash
open test_cards.html
```

Este archivo muestra todas las tarjetas con ejemplos estáticos.

### Opción 2: En el Chat Real
1. Inicia la aplicación:
```bash
python app.py
```

2. Pregunta al bot:
```
"Necesito un viaje familiar a Cancún"
```

3. El bot responderá con información que activará las tarjetas automáticamente.

---

## 🎨 Diseño Implementado

### Sidebar Oscuro
- Fondo: `#1a1d2e` (azul oscuro)
- Navegación con iconos
- Logo "CONSOLID" con icono
- Items: Dashboard, New Search, History, Settings
- Footer con info del agente

### Tarjetas
- **Vuelos**: Borde azul (`#3b82f6`)
- **Hoteles**: Borde verde (`#10b981`)
- **Paquetes**: Borde morado (`#8b5cf6`) con fondo degradado

### Botones de Reservar
- Gradientes según tipo
- Iconos SVG
- Efectos hover con elevación
- Funcionales con `onclick`

---

## 🔧 Personalización

### Modificar Colores
En `static/style.css`:

```css
/* Cambiar color de tarjeta de vuelo */
.flight-card {
    border-left: 4px solid #TU_COLOR;
}

/* Cambiar color del botón */
.reserve-btn {
    background: linear-gradient(135deg, #COLOR1 0%, #COLOR2 100%);
}
```

### Agregar Más Información
En `static/script.js`, función `createFlightCard()`:

```javascript
// Agregar más filas de información
card.innerHTML += `
    <div class="flight-info-row">
        <span class="flight-info-label">Nueva Info</span>
        <span class="flight-info-value">Valor</span>
    </div>
`;
```

---

## 📱 Responsive

Las tarjetas son completamente responsive:
- En desktop: Layout horizontal
- En móvil: Layout vertical apilado
- Botones se expanden al 100% en móvil

---

## 🎯 Funcionalidad de Botones

Cuando se hace clic en "Reservar":

```javascript
function handleReservation(type, identifier) {
    // Incrementa contador de reservas
    stats.reservas++;
    
    // Envía mensaje automático al bot
    const message = `Quiero reservar el ${type} ${identifier}`;
    sendMessage();
}
```

El bot procesará la reserva y generará un PNR simulado.

---

## 🌟 Características Especiales

### 1. Animaciones
- Entrada suave de tarjetas (`slideIn`)
- Hover con elevación
- Transiciones fluidas

### 2. Iconos
- SVG inline para mejor rendimiento
- Iconos personalizados por tipo
- Emojis para features

### 3. Políticas Destacadas
- Box amarillo para políticas de cancelación
- Fácil de identificar para agentes

### 4. Precios Destacados
- Tamaño grande y color distintivo
- Comisión calculada automáticamente
- Ahorro mostrado en paquetes

---

## 📊 Integración con Backend

El chatbot en `src/chatbot.py` ya está actualizado para generar respuestas compatibles:

```python
def present_package(self, package: Dict) -> str:
    # Genera texto que activa las tarjetas
    output = f"Vuelo {package.get('vuelo_numero', 'AM540')}"
    output += f"Hotel {package.get('hotel_nombre', 'Hyatt Ziva')}"
    # ...
```

---

## ✅ Checklist de Implementación

- [x] Sidebar oscuro estilo ConsolidGPT
- [x] Tarjetas de vuelo con detalles completos
- [x] Tarjetas de hotel con políticas
- [x] Tarjetas de paquetes con inclusiones
- [x] Botones de reservar funcionales
- [x] Detección automática en respuestas
- [x] Extracción de datos del texto
- [x] Diseño responsive
- [x] Animaciones y efectos hover
- [x] Integración con backend
- [x] Archivo de prueba (test_cards.html)

---

## 🎓 Para Agentes de Viajes

### Ventajas del Nuevo UI:
1. **Visual**: Los clientes ven información clara y profesional
2. **Rápido**: Un clic para reservar
3. **Completo**: Toda la info importante visible
4. **Profesional**: Diseño moderno tipo Amadeus/Sabre
5. **Comisiones**: Siempre visibles para el agente

### Flujo de Trabajo:
1. Cliente pregunta por viaje
2. Bot muestra tarjetas interactivas
3. Agente revisa detalles en tarjetas
4. Clic en "Reservar"
5. Sistema genera PNR
6. Confirmación enviada

---

## 🚀 Próximos Pasos Sugeridos

1. **Conectar con API real** de vuelos/hoteles
2. **Agregar más tipos de tarjetas**: Tours, seguros, traslados
3. **Filtros interactivos**: Por precio, fecha, aerolínea
4. **Comparador**: Mostrar múltiples opciones lado a lado
5. **Calendario visual**: Para seleccionar fechas
6. **Mapa interactivo**: Ubicación de hoteles

---

## 📞 Soporte

Si necesitas modificar algo:
- CSS: `static/style.css` (línea 600+)
- JavaScript: `static/script.js` (funciones `create*Card()`)
- HTML: `templates/index.html`
- Backend: `src/chatbot.py`

¡Disfruta tu nuevo UI profesional! 🎉
