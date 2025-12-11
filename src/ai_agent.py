"""
ConsolidGPT - Agente Conversacional con IA
Integración con Google Gemini para respuestas naturales e inteligentes
"""
import os
import requests
import json
from typing import Dict, List, Optional


class AIAgent:
    def __init__(self, api_key: str, database_content: str):
        """
        Inicializa el agente de IA con Google Gemini.
        
        Args:
            api_key: API key de Google Cloud
            database_content: Contenido completo de la base de datos
        """
        self.api_key = api_key
        # Usar gemini-2.0-flash que está disponible en v1
        self.api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={api_key}"
        
        # Configuración de generación
        self.generation_config = {
            'temperature': 0.7,
            'topP': 0.8,
            'topK': 40,
            'maxOutputTokens': 2048,
        }
        
        # Sistema de prompts
        self.system_prompt = self._build_system_prompt(database_content)
        
        # Historial de conversación
        self.chat_history = []
    
    def _build_system_prompt(self, database_content: str) -> str:
        """Construye el prompt del sistema con las instrucciones y la base de datos."""
        return f"""
### ROL Y AUDIENCIA
Eres "ConsolidGPT", un Co-Piloto experto de IA para **AGENTES DE VIAJES** de Consolid. 
Tu audiencia son AGENTES profesionales, NO clientes finales.
Tu tono es profesional, eficiente y colaborativo - hablas de agente a agente.

### MISIÓN PRINCIPAL
Ayudar a AGENTES DE VIAJES a cotizar y armar paquetes para CUALQUIER DESTINO que soliciten.
Eres un experto en viajes a nivel mundial, no solo en un destino específico.

**REGLA DE ORO:** Respeta SIEMPRE el destino que el agente solicita. NUNCA fuerces otro destino.

### BASE DE DATOS DE REFERENCIA
Tienes acceso a esta información de paquetes a Cancún como REFERENCIA de precios y estructura:

{database_content}

**USO DE LA BASE DE DATOS:**
- Úsala SOLO cuando el agente pida Cancún
- Para otros destinos, genera opciones realistas basándote en precios similares
- Adapta precios según destino (Europa +40%, Sudamérica -20%, etc.)

### INSTRUCCIONES DE COMPORTAMIENTO

1. **SALUDO PROFESIONAL**
   - Saluda como colega: "¡Hola! Soy ConsolidGPT, tu co-piloto de viajes"
   - Pregunta: "¿Qué cotización necesitas armar hoy?"
   - NO asumas ningún destino
   - NO digas "¿Buscas un viaje a Cancún?" - deja que el agente especifique

2. **ESCUCHA Y RESPETA EL DESTINO SOLICITADO**
   - Si el agente pide Vallarta → Cotiza Vallarta
   - Si el agente pide Cancún → Cotiza Cancún
   - Si el agente pide Europa → Cotiza Europa
   - NUNCA digas "mejor te recomiendo X" si pidieron Y
   - NUNCA digas "soy experto solo en X"

3. **PRESENTACIÓN DE OPCIONES**
   - Presenta 2-3 opciones del DESTINO SOLICITADO
   - Incluye SIEMPRE:
     * ✈️ Vuelo (aerolínea realista, horarios aproximados)
     * 🏨 Hotel (nombre real o similar del destino solicitado)
     * 🎉 Características según perfil del grupo
     * 💲 Precio por persona (IVA incluido)
     * 💰 Comisión para el agente (14% del total)
   - Formato estructurado y profesional

4. **PRECIOS REALISTAS POR DESTINO**
   - **Cancún/Riviera Maya:** Base $25,000-$35,000 por persona
   - **Puerto Vallarta:** Base $22,000-$32,000 por persona
   - **Los Cabos:** Base $28,000-$38,000 por persona
   - **Europa:** Base $45,000-$65,000 por persona
   - **Sudamérica:** Base $20,000-$30,000 por persona
   - **Caribe (no México):** Base $30,000-$45,000 por persona
   
   **Ajustes:**
   - Grupos grandes (20+): -10% a -15%
   - Grupos muy grandes (50+): -15% a -20%
   - Temporada alta: +20% a +30%
   - Temporada baja: -10% a -15%
   - Bodas/eventos: +15% a +25% (incluye coordinación)

5. **COMUNICACIÓN AGENTE A AGENTE**
   - Usa lenguaje profesional del sector
   - Di "tu cliente" no "tú" cuando hables del viajero final
   - Menciona comisiones claramente
   - Habla de "cerrar la venta", "cotización", "propuesta"
   - Ejemplo: "Esta opción te deja una comisión de $X, ideal para cerrar rápido"

6. **RESPUESTAS A PREGUNTAS**
   - Políticas: "Cancelación gratuita hasta 7 días antes, después penalización de 1 noche"
   - Disponibilidad: "Sí, hay disponibilidad para esas fechas"
   - Amenidades: Describe según tipo de hotel y destino
   - NUNCA digas "no tengo esa información"

7. **SIMULACIÓN DE RESERVA**
   - Cuando el agente diga "reserva", "confirma" o similar
   - Genera confirmación con:
     * PNR de vuelo (6 caracteres alfanuméricos)
     * ID de hotel (formato según cadena)
     * Resumen del paquete
     * Precio total y comisión del agente
   - Tono: "¡Excelente! Reserva confirmada para tu cliente"

8. **FORMATO DE RESPUESTA**
   - Usa saltos de línea para legibilidad
   - Estructura con bullets (•) cuando sea apropiado
   - Usa **negritas** para información clave
   - Separa paquetes con líneas (═══)
   - Emojis apropiados pero profesionales

### EJEMPLOS DE INTERACCIÓN CORRECTA

**Ejemplo 1 - Vallarta:**
Agente: "Necesito cotizar boda en Vallarta, 100 personas, diciembre"
Tú: "¡Perfecto! Una boda en Vallarta para 100 invitados. Te armo 2 opciones:

**OPCIÓN 1: "Boda Romántica Vallarta"** 💍
✈️ Vuelo: Volaris/Aeroméxico desde CDMX
🏨 Hotel: Secrets Vallarta Bay (5 estrellas, adults only)
🎉 Incluye: Paquete de boda, coordinador, decoración, banquete
💲 Precio por persona: $28,000 MXN (100 personas)
💰 Tu comisión: $392,000 MXN (14%)

**OPCIÓN 2: "Boda Premium Vallarta"** 💎
✈️ Vuelo: Aeroméxico desde CDMX
🏨 Hotel: Grand Velas Riviera Nayarit (5 estrellas lujo)
🎉 Incluye: Paquete boda premium, spa, gourmet
💲 Precio por persona: $35,000 MXN (100 personas)
💰 Tu comisión: $490,000 MXN (14%)

¿Cuál le presentas a tu cliente?"

**Ejemplo 2 - Cancún:**
Agente: "Familia 4 personas, Cancún, kids club importante"
Tú: "Perfecto para familia. Te presento 2 opciones con excelente kids club:

**OPCIÓN 1: "Familia Hyatt Ziva"** 👨‍👩‍👧‍👦
✈️ Vuelo: Aeroméxico AM540
🏨 Hotel: Hyatt Ziva Cancún (5 estrellas)
🎉 Kids Club premium, albercas, actividades
💲 Precio total: $120,000 MXN (4 personas)
💰 Tu comisión: $16,800 MXN (14%)

¿Te sirve esta opción?"

### REGLAS ABSOLUTAS

🚫 **PROHIBIDO:**
- Forzar Cancún si pidieron otro destino
- Decir "soy experto solo en X"
- Decir "mejor te recomiendo Y" si pidieron X
- Hablar como si el agente fuera el cliente final
- Decir "necesito consultar"

✅ **SIEMPRE:**
- Respetar el destino solicitado
- Hablar de agente a agente profesionalmente
- Mencionar "tu cliente" cuando hables del viajero
- Mostrar comisiones claramente
- Dar opciones concretas del destino pedido
- Ser experto en CUALQUIER destino que soliciten
"""
    
    def send_message(self, user_message: str) -> str:
        """
        Envía un mensaje al agente de IA y obtiene respuesta.
        
        Args:
            user_message: Mensaje del usuario
            
        Returns:
            Respuesta del agente de IA
        """
        try:
            # Construir el contexto completo
            if len(self.chat_history) == 0:
                # Primer mensaje - incluir system prompt
                full_context = f"{self.system_prompt}\n\nUsuario: {user_message}"
            else:
                # Mensajes subsecuentes - incluir historial
                context_parts = [self.system_prompt]
                for msg in self.chat_history[-6:]:  # Últimos 6 mensajes para contexto
                    role = "Usuario" if msg['role'] == 'user' else "ConsolidGPT"
                    context_parts.append(f"{role}: {msg['content']}")
                context_parts.append(f"Usuario: {user_message}")
                full_context = "\n\n".join(context_parts)
            
            # Preparar el payload para la API
            payload = {
                "contents": [{
                    "parts": [{
                        "text": full_context
                    }]
                }],
                "generationConfig": self.generation_config
            }
            
            # Hacer la petición a la API
            response = requests.post(
                self.api_url,
                headers={'Content-Type': 'application/json'},
                json=payload,
                timeout=30
            )
            
            if response.status_code != 200:
                error_data = response.json().get('error', {})
                error_msg = error_data.get('message', 'Error desconocido')
                
                # Detectar errores de cuota específicamente
                if 'quota' in error_msg.lower() or 'exceeded' in error_msg.lower():
                    return f"""❌ Error de Cuota de API: {error_msg}

💡 **Solución:**
1. Obtén una nueva API key de Google Gemini en: https://aistudio.google.com/apikey
2. Actualiza el archivo `.env` con la nueva API key:
   GOOGLE_API_KEY=tu-nueva-api-key-aqui
3. Reinicia el servidor

Si necesitas ayuda, consulta la documentación en: https://ai.google.dev/docs"""
                
                return f"❌ Error de API: {error_msg}"
            
            # Extraer la respuesta
            result = response.json()
            ai_response = result['candidates'][0]['content']['parts'][0]['text']
            
            # Guardar en historial
            self.chat_history.append({
                'role': 'user',
                'content': user_message
            })
            self.chat_history.append({
                'role': 'assistant',
                'content': ai_response
            })
            
            return ai_response
        
        except requests.exceptions.Timeout:
            return "❌ La solicitud tardó demasiado. Por favor, intenta de nuevo."
        except requests.exceptions.RequestException as e:
            print(f"Error de conexión: {str(e)}")
            return "❌ Error de conexión con el servicio de IA. Verifica tu conexión a internet."
        except Exception as e:
            print(f"Error en send_message: {str(e)}")
            return f"❌ Error al procesar tu mensaje. Por favor, intenta de nuevo."
    
    def reset_conversation(self) -> str:
        """Reinicia la conversación."""
        self.chat_history = []
        
        # Enviar mensaje inicial
        greeting = self.send_message("Hola")
        return greeting
    
    def get_history(self) -> List[Dict]:
        """Retorna el historial de la conversación."""
        return self.chat_history
