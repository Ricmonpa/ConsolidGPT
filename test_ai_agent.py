#!/usr/bin/env python3
"""
Script de prueba del Agente IA de ConsolidGPT
"""
import os
from dotenv import load_dotenv
import sys

# Cargar variables de entorno
load_dotenv()

# Agregar src al path
sys.path.insert(0, 'src')
from ai_agent import AIAgent

# Cargar base de datos
with open('data/Base_de_Datos_Cancun.txt', 'r', encoding='utf-8') as f:
    database_content = f.read()

# Obtener API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    print("❌ Error: GOOGLE_API_KEY no encontrada en .env")
    sys.exit(1)

print("\n" + "="*60)
print("   DEMO DEL AGENTE IA - ConsolidGPT")
print("   Powered by Google Gemini AI ✨")
print("="*60 + "\n")

# Inicializar el agente
print("🔄 Inicializando agente IA...")
agent = AIAgent(api_key, database_content)
print("✅ Agente IA listo!\n")

# Conversación de prueba
conversacion = [
    "Hola",
    "Necesito un viaje familiar a Cancún",
    "¿Cuál es mejor para niños pequeños?",
    "¿Cuáles son las políticas de cancelación?",
    "Reserva el Hyatt Ziva"
]

for i, mensaje in enumerate(conversacion, 1):
    print(f"\n{'='*60}")
    print(f"👤 Usuario ({i}/{len(conversacion)}): {mensaje}")
    print(f"{'='*60}\n")
    
    # Enviar mensaje al agente
    respuesta = agent.send_message(mensaje)
    
    print(f"🤖 ConsolidGPT:\n{respuesta}\n")
    
    # Pausa para leer
    if i < len(conversacion):
        input("Presiona Enter para continuar...")

print("\n" + "="*60)
print("   FIN DE LA DEMO")
print("="*60 + "\n")

print("💡 Historial de conversación:")
print(f"   Total de mensajes: {len(agent.get_history())}")
print("\n✨ El agente IA mantiene memoria de toda la conversación!")
