#!/usr/bin/env python3
"""
Script de demostración de ConsolidGPT
"""
import sys
sys.path.insert(0, 'src')

from chatbot import ConsolidGPT

# Inicializar el bot
bot = ConsolidGPT('data/Base_de_Datos_Cancun.txt')

print("\n" + "="*60)
print("   DEMO DE ConsolidGPT")
print("="*60 + "\n")

# Saludo
print("🤖 ConsolidGPT:", bot.greet())

# Solicitar viaje
print("\n👤 Usuario: Necesito un viaje familiar a Cancún, 2 adultos y 2 niños")
response = bot.process_input("viaje familiar a cancún")
print("\n🤖 ConsolidGPT:", response)

# Preguntar por políticas
print("\n👤 Usuario: ¿Cuáles son las políticas de cancelación?")
response = bot.process_input("políticas de cancelación")
print("\n🤖 ConsolidGPT:", response)

# Preguntar por kids club
print("\n👤 Usuario: ¿Qué incluye el kids club?")
response = bot.process_input("kids club")
print("\n🤖 ConsolidGPT:", response)

# Reservar
print("\n👤 Usuario: Reserva el paquete Caribe Familiar Deluxe")
response = bot.process_input("reserva")
print("\n🤖 ConsolidGPT:", response)

print("\n" + "="*60)
print("   FIN DE LA DEMO")
print("="*60 + "\n")
