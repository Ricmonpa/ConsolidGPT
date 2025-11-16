# -*- coding: utf-8 -*-
"""
ConsolidGPT - Vercel Serverless Function
"""
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Importar la app de Flask
from app import app

# Exportar para Vercel
handler = app
