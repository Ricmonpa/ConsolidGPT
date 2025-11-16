"""
ConsolidGPT - Co-Piloto de IA para agentes de viajes de Consolid.
"""
import random
from typing import Dict, List
from database_loader import DatabaseLoader


class ConsolidGPT:
    def __init__(self, database_path: str):
        self.db = DatabaseLoader(database_path)
        self.state = "INICIO"
        self.selected_package = None
        
    def calculate_commission(self, price: float, rate: float = 0.14) -> float:
        """Calcula la comisión sobre el precio."""
        return round(price * rate, 2)
    
    def format_price(self, price: float) -> str:
        """Formatea el precio en formato mexicano."""
        return f"${price:,.2f} MXN"
    
    def present_package(self, package: Dict) -> str:
        """Presenta un paquete de forma estructurada con información para tarjetas."""
        precio = package.get('precio', 0)
        comision = self.calculate_commission(precio)
        
        # Información del vuelo para activar tarjeta
        vuelo_info = f"Vuelo {package.get('vuelo_numero', 'AM540')} - {package.get('vuelo_aerolinea', 'Aeroméxico')}"
        horarios = package.get('vuelo_horarios', 'Salida: 1 Dic - 9:00 AM, Regreso: 7 Dic - 4:30 PM')
        
        # Información del hotel para activar tarjeta
        hotel_info = f"Hotel {package.get('hotel_nombre', 'Hyatt Ziva Cancún')} - {package.get('hotel_estrellas', '5 estrellas')}"
        
        output = f"\n**PAQUETE TODO INCLUIDO: {package['nombre']}**\n\n"
        
        output += f"✈️ **VUELO**\n"
        output += f"{vuelo_info}\n"
        output += f"{horarios}\n"
        output += f"Clase: Turista | Equipaje: 1 maleta incluida\n\n"
        
        output += f"🏨 **HOTEL ALL-INCLUSIVE**\n"
        output += f"{hotel_info}\n"
        output += f"Habitación: {package.get('habitacion', 'Doble')}\n"
        output += f"Ubicación: Zona Hotelera, Cancún\n"
        output += f"{package.get('detalles', 'Resort frente al mar con todas las amenidades')}\n\n"
        
        output += f"💰 **PRECIO TOTAL:** {self.format_price(precio)}\n"
        output += f"💼 **Tu Comisión (14%):** {self.format_price(comision)}\n\n"
        
        output += f"📋 Incluye: Vuelo redondo + Hotel + Traslados + All-Inclusive\n"
        
        return output
    
    def greet(self) -> str:
        """Saludo inicial."""
        return ("\n¡Hola! Soy ConsolidGPT, tu Co-Piloto de IA para Consolid. 🌴\n"
                "¿En qué puedo ayudarte hoy?\n")
    
    def search_packages(self, user_input: str) -> str:
        """Busca y presenta paquetes según la solicitud."""
        # Detectar si el usuario pide viaje a Cancún
        if "cancún" in user_input.lower() or "cancun" in user_input.lower():
            self.state = "PRESENTANDO_OPCIONES"
            
            response = "\n🔍 Entendido, buscando en nuestra base de datos...\n"
            response += "\n📋 He encontrado las siguientes opciones para tu viaje familiar a Cancún:\n"
            
            packages = self.db.get_all_packages()
            for i, package in enumerate(packages, 1):
                response += self.present_package(package)
            
            response += "\n¿Te gustaría conocer más detalles sobre algún paquete? "
            response += "(Ej: políticas de cancelación, kids club, etc.)\n"
            
            return response
        else:
            return "Por favor, indícame qué tipo de viaje necesitas cotizar."
    
    def handle_question(self, user_input: str) -> str:
        """Maneja preguntas específicas sobre los paquetes."""
        user_lower = user_input.lower()
        
        # Preguntas sobre políticas de cancelación
        if "cancelación" in user_lower or "cancelacion" in user_lower:
            response = "\n📜 **POLÍTICAS DE CANCELACIÓN:**\n\n"
            packages = self.db.get_all_packages()
            for package in packages:
                if 'politica_cancelacion' in package:
                    response += f"• **{package['hotel_nombre']}**: {package['politica_cancelacion']}\n\n"
            return response
        
        # Preguntas sobre kids club
        if "kids club" in user_lower or "niños" in user_lower or "ninos" in user_lower:
            response = "\n👶 **KIDS CLUB - INFORMACIÓN:**\n\n"
            packages = self.db.get_all_packages()
            for package in packages:
                detalles = package.get('detalles', '')
                if 'kids club' in detalles.lower() or 'playroom' in detalles.lower():
                    response += f"• **{package['hotel_nombre']}**: {detalles}\n\n"
            return response
        
        # Preguntas sobre un hotel específico
        if "hyatt" in user_lower:
            package = self.db.get_package_by_name("Caribe Familiar Deluxe")
            if package:
                return self.present_package(package)
        
        if "moon palace" in user_lower:
            package = self.db.get_package_by_name("Aventura Sol")
            if package:
                return self.present_package(package)
        
        # Búsqueda general
        result = self.db.search_in_content(user_input)
        if result and result != "No se encontró información sobre eso.":
            return f"\n📖 Información encontrada:\n{result}\n"
        
        return "¿Podrías ser más específico? Puedo ayudarte con políticas de cancelación, detalles del kids club, o información sobre los hoteles."
    
    def simulate_booking(self, package_name: str = None) -> str:
        """Simula una reserva."""
        # Generar códigos aleatorios
        pnr = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=6))
        hotel_id = f"HZ-{random.randint(10000, 99999)}"
        
        response = "\n" + "="*60 + "\n"
        response += "✅ ¡ACCIÓN! RESERVA CONFIRMADA\n"
        response += "="*60 + "\n\n"
        response += f"📌 **PNR Vuelo:** {pnr} (simulado)\n"
        response += f"🏨 **ID Hotel:** {hotel_id} (simulado)\n\n"
        response += "📧 He enviado la confirmación a tu sistema.\n"
        response += "="*60 + "\n"
        
        return response
    
    def process_input(self, user_input: str) -> str:
        """Procesa la entrada del usuario según el estado actual."""
        user_lower = user_input.lower()
        
        # Estado inicial
        if self.state == "INICIO":
            if any(word in user_lower for word in ["viaje", "cotizar", "paquete", "cancún", "cancun"]):
                return self.search_packages(user_input)
            else:
                return self.greet()
        
        # Estado presentando opciones
        elif self.state == "PRESENTANDO_OPCIONES":
            # Detectar intención de reserva
            if any(word in user_lower for word in ["reserva", "confirma", "reservar", "confirmar", "quiero"]):
                self.state = "RESERVADO"
                return self.simulate_booking()
            # Responder preguntas
            else:
                return self.handle_question(user_input)
        
        # Estado después de reserva
        elif self.state == "RESERVADO":
            return "La reserva ya ha sido confirmada. ¿Necesitas ayuda con algo más?"
        
        return "No entendí tu solicitud. ¿Puedes reformularla?"
