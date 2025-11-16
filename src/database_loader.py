"""
Módulo para cargar y parsear la base de datos de paquetes de viaje.
"""
import re
from typing import Dict, List, Optional


class DatabaseLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.raw_content = ""
        self.packages = []
        self.general_policies = ""
        self.load_database()
    
    def load_database(self):
        """Carga el archivo de base de datos."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.raw_content = f.read()
            self._parse_content()
        except FileNotFoundError:
            raise Exception(f"No se encontró el archivo: {self.filepath}")
    
    def _parse_content(self):
        """Parsea el contenido del archivo."""
        # Separar paquetes y políticas generales
        parts = self.raw_content.split('### POLÍTICAS GENERALES ###')
        packages_section = parts[0]
        self.general_policies = parts[1].strip() if len(parts) > 1 else ""
        
        # Extraer paquetes individuales
        package_pattern = r'\*\*Paquete: "(.*?)"\*\*(.*?)(?=\*\*Paquete:|---|\Z)'
        matches = re.findall(package_pattern, packages_section, re.DOTALL)
        
        for name, content in matches:
            package = self._parse_package(name, content)
            self.packages.append(package)
    
    def _parse_package(self, name: str, content: str) -> Dict:
        """Parsea un paquete individual."""
        package = {'nombre': name}
        
        # Extraer información del vuelo
        vuelo_match = re.search(r'Vuelo: (.*?)\((.*?)\), (.*)', content)
        if vuelo_match:
            package['vuelo_aerolinea'] = vuelo_match.group(1).strip()
            package['vuelo_numero'] = vuelo_match.group(2).strip()
            package['vuelo_horarios'] = vuelo_match.group(3).strip()
        
        # Extraer información del hotel
        hotel_match = re.search(r'Hotel: (.*?)\((.*?)\)', content)
        if hotel_match:
            package['hotel_nombre'] = hotel_match.group(1).strip()
            package['hotel_estrellas'] = hotel_match.group(2).strip()
        
        # Extraer habitación
        habitacion_match = re.search(r'Habitación: (.*)', content)
        if habitacion_match:
            package['habitacion'] = habitacion_match.group(1).strip()
        
        # Extraer detalles
        detalles_match = re.search(r'Detalles: (.*)', content)
        if detalles_match:
            package['detalles'] = detalles_match.group(1).strip()
        
        # Extraer precio
        precio_match = re.search(r'Precio Total.*?: \$?([\d,]+\.?\d*)', content)
        if precio_match:
            precio_str = precio_match.group(1).replace(',', '')
            package['precio'] = float(precio_str)
        
        # Extraer política de cancelación
        politica_match = re.search(r'Política de Cancelación.*?: (.*?)(?=\n\*|\n\n|\Z)', content, re.DOTALL)
        if politica_match:
            package['politica_cancelacion'] = politica_match.group(1).strip()
        
        return package
    
    def get_all_packages(self) -> List[Dict]:
        """Retorna todos los paquetes disponibles."""
        return self.packages
    
    def get_package_by_name(self, name: str) -> Optional[Dict]:
        """Busca un paquete por nombre."""
        for package in self.packages:
            if name.lower() in package['nombre'].lower():
                return package
        return None
    
    def get_general_policies(self) -> str:
        """Retorna las políticas generales."""
        return self.general_policies
    
    def search_in_content(self, query: str) -> str:
        """Busca una palabra clave en todo el contenido."""
        lines = self.raw_content.split('\n')
        results = []
        for line in lines:
            if query.lower() in line.lower():
                results.append(line.strip())
        return '\n'.join(results) if results else "No se encontró información sobre eso."
