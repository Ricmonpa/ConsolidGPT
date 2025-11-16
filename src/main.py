#!/usr/bin/env python3
"""
ConsolidGPT - Aplicación Principal
Co-Piloto de IA para agentes de viajes de Consolid
"""
import sys
import os
from chatbot import ConsolidGPT


def print_header():
    """Imprime el header de la aplicación."""
    print("\n" + "="*60)
    print("   _____ ____  _   _  _____  ____  _      _____ _____  ")
    print("  / ____/ __ \\| \\ | |/ ____|/ __ \\| |    |_   _|  __ \\ ")
    print(" | |   | |  | |  \\| | (___ | |  | | |      | | | |  | |")
    print(" | |   | |  | | . ` |\\___ \\| |  | | |      | | | |  | |")
    print(" | |___| |__| | |\\  |____) | |__| | |____ _| |_| |__| |")
    print("  \\_____\\____/|_| \\_|_____/ \\____/|______|_____|_____/ ")
    print("                                                        ")
    print("              ConsolidGPT - Tu Co-Piloto de IA         ")
    print("="*60 + "\n")


def main():
    """Función principal."""
    # Determinar la ruta de la base de datos
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '..', 'data', 'Base_de_Datos_Cancun.txt')
    
    # Verificar que existe el archivo
    if not os.path.exists(db_path):
        print(f"❌ Error: No se encontró el archivo de base de datos en: {db_path}")
        sys.exit(1)
    
    # Inicializar el chatbot
    try:
        bot = ConsolidGPT(db_path)
    except Exception as e:
        print(f"❌ Error al inicializar ConsolidGPT: {e}")
        sys.exit(1)
    
    # Mostrar header
    print_header()
    
    # Saludo inicial
    print(bot.greet())
    
    # Loop principal
    while True:
        try:
            # Leer input del usuario
            user_input = input("\n👤 Tú: ").strip()
            
            # Comandos especiales
            if user_input.lower() in ['salir', 'exit', 'quit']:
                print("\n👋 ¡Hasta pronto! Que tengas un excelente día.\n")
                break
            
            if user_input.lower() in ['ayuda', 'help']:
                print("\n📚 COMANDOS DISPONIBLES:")
                print("  • Pide un viaje a Cancún para ver opciones")
                print("  • Pregunta sobre 'políticas de cancelación'")
                print("  • Pregunta sobre 'kids club'")
                print("  • Escribe 'reserva' o 'confirma' para simular una reserva")
                print("  • Escribe 'salir' para terminar\n")
                continue
            
            if not user_input:
                continue
            
            # Procesar input
            response = bot.process_input(user_input)
            print(f"\n🤖 ConsolidGPT: {response}")
            
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta pronto! Que tengas un excelente día.\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            continue


if __name__ == "__main__":
    main()
