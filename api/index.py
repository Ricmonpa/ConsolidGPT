# -*- coding: utf-8 -*-
"""
ConsolidGPT - Vercel Serverless Function
"""
import sys
import os

# Agregar el directorio raíz al path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

# Importar la app de Flask
from app import app

# Vercel necesita que la app se llame 'app' o se exporte como handler
# Flask app ya está lista para WSGI
