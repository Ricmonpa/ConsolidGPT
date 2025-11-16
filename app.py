# -*- coding: utf-8 -*-
"""
ConsolidGPT - Web Application
Flask API para el agente conversacional de viajes con IA
"""
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import sys
import os

# Cargar variables de entorno
load_dotenv()

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from ai_agent import AIAgent

app = Flask(__name__)
CORS(app)

# Configuración
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
if not GOOGLE_API_KEY:
    raise Exception("❌ GOOGLE_API_KEY no encontrada en .env")

# Cargar base de datos
db_path = os.path.join(os.path.dirname(__file__), 'data', 'Base_de_Datos_Cancun.txt')
with open(db_path, 'r', encoding='utf-8') as f:
    database_content = f.read()

# Almacenar sesiones de usuarios (en producción usa Redis o similar)
user_sessions = {}


@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')


@app.route('/favicon.ico')
def favicon():
    """Favicon."""
    from flask import send_from_directory
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Endpoint para procesar mensajes del chat con IA."""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        session_id = data.get('session_id', 'default')
        
        if not user_message:
            return jsonify({'error': 'Mensaje vacío'}), 400
        
        # Obtener o crear sesión del agente IA para este usuario
        if session_id not in user_sessions:
            user_sessions[session_id] = AIAgent(GOOGLE_API_KEY, database_content)
        
        agent = user_sessions[session_id]
        
        # Procesar mensaje con IA
        response = agent.send_message(user_message)
        
        return jsonify({
            'response': response,
            'history': agent.get_history()
        })
    
    except Exception as e:
        print(f"Error en /api/chat: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/reset', methods=['POST'])
def reset():
    """Reinicia la sesión del chat con IA."""
    try:
        data = request.json
        session_id = data.get('session_id', 'default')
        
        # Reiniciar sesión con nuevo agente IA
        user_sessions[session_id] = AIAgent(GOOGLE_API_KEY, database_content)
        
        # Obtener saludo inicial
        greeting = user_sessions[session_id].reset_conversation()
        
        return jsonify({
            'message': 'Sesión reiniciada',
            'greeting': greeting
        })
    
    except Exception as e:
        print(f"Error en /api/reset: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/api/health', methods=['GET'])
def health():
    """Health check para Vercel."""
    return jsonify({'status': 'ok', 'service': 'ConsolidGPT'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
