# 📖 Ejemplo de Uso - ConsolidGPT

## Cómo Ejecutar

```bash
cd src
python3 main.py
```

## Ejemplo de Conversación Completa

```
==============================================================
   _____ ____  _   _  _____  ____  _      _____ _____ 
  / ____/ __ \| \ | |/ ____|/ __ \| |    |_   _|  __ \
 | |   | |  | |  \| | (___ | |  | | |      | | | |  | |
 | |   | |  | | . ` |\___ \| |  | | |      | | | |  | |
 | |___| |__| | |\  |____) | |__| | |____ _| |_| |__| |
  \_____\____/|_| \_|_____/ \____/|______|_____|_____/
                                                        
              ConsolidGPT - Tu Co-Piloto de IA         
==============================================================


¡Hola! Soy ConsolidGPT, tu Co-Piloto de IA para Consolid. 🌴
¿En qué puedo ayudarte hoy?


👤 Tú: Necesito un viaje familiar a Cancún, 2 adultos y 2 niños del 1 al 7 de diciembre

🤖 ConsolidGPT: 
🔍 Entendido, buscando en nuestra base de datos...

📋 He encontrado las siguientes opciones para tu viaje familiar a Cancún:

============================================================
**Paquete: Caribe Familiar Deluxe**
============================================================

✈️  **VUELO**
   Aerolínea: Aeroméxico
   No. Vuelo: AM540
   Horarios: Salida 01-Dic 9:00 AM, Regreso 07-Dic 4:30 PM

🏨 **HOTEL**
   Nombre: Hyatt Ziva Cancún
   Categoría: 5 Estrellas
   Habitación: Suite Familiar Vista al Mar
   Detalles: Todo Incluido, "Camp Hyatt" Kids Club (Confirmado).

💲 **PRECIO TOTAL (IVA incl.):** $124,500.00 MXN
💰 **COMISIÓN (14%):** $17,430.00 MXN

============================================================

============================================================
**Paquete: Aventura Sol**
============================================================

✈️  **VUELO**
   Aerolínea: Volaris
   No. Vuelo: Y4-702
   Horarios: Salida 01-Dic 7:30 AM, Regreso 07-Dic 2:00 PM

🏨 **HOTEL**
   Nombre: The Grand at Moon Palace
   Categoría: 5 Estrellas
   Habitación: Suite Familiar
   Detalles: Todo Incluido, "The Playroom" Kids Club (Confirmado).

💲 **PRECIO TOTAL (IVA incl.):** $115,000.00 MXN
💰 **COMISIÓN (14%):** $16,100.00 MXN

============================================================

¿Te gustaría conocer más detalles sobre algún paquete? (Ej: políticas de cancelación, kids club, etc.)


👤 Tú: ¿Cuáles son las políticas de cancelación?

🤖 ConsolidGPT: 
📜 **POLÍTICAS DE CANCELACIÓN:**

• **Hyatt Ziva Cancún**: Cancelación gratuita hasta 72 horas antes del check-in. Después de eso, penalización de 1 noche.

• **The Grand at Moon Palace**: Cancelación gratuita hasta 5 días antes del check-in.


👤 Tú: ¿Qué incluye el kids club?

🤖 ConsolidGPT: 
👶 **KIDS CLUB - INFORMACIÓN:**

• **Hyatt Ziva Cancún**: Todo Incluido, "Camp Hyatt" Kids Club (Confirmado).

• **The Grand at Moon Palace**: Todo Incluido, "The Playroom" Kids Club (Confirmado).


👤 Tú: Reserva el paquete Caribe Familiar Deluxe

🤖 ConsolidGPT: 
============================================================
✅ ¡ACCIÓN! RESERVA CONFIRMADA
============================================================

📌 **PNR Vuelo:** AXN45T (simulado)
🏨 **ID Hotel:** HZ-99812 (simulado)

📧 He enviado la confirmación a tu sistema.
============================================================


👤 Tú: salir

👋 ¡Hasta pronto! Que tengas un excelente día.
```

## Comandos Útiles

| Comando | Descripción |
|---------|-------------|
| `ayuda` o `help` | Muestra comandos disponibles |
| `salir`, `exit`, `quit` | Termina la aplicación |
| Ctrl+C | Salida rápida |

## Preguntas Frecuentes

**P: ¿Puedo agregar más paquetes?**  
R: Sí, edita el archivo `data/Base_de_Datos_Cancun.txt` siguiendo el formato existente.

**P: ¿Cómo cambio la tasa de comisión?**  
R: En `src/chatbot.py`, línea 13, modifica el valor `0.14` (14%) por el que necesites.

**P: ¿Los PNR son reales?**  
R: No, son simulados para demostración. Para producción, integrarías con tu sistema de reservas real.

**P: ¿Puedo agregar más destinos?**  
R: Sí, necesitarías crear archivos adicionales de base de datos y modificar la lógica del chatbot para soportar múltiples destinos.
