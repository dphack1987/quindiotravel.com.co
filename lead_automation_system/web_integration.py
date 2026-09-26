"""
Integración Web del Sistema de Automatización de Leads
API Flask para conectar el sitio web con el sistema Python
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os
import sys
from datetime import datetime

# Agregar directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from main import LeadAutomationSystem

app = Flask(__name__)
# Restringir CORS al dominio del proyecto para seguridad
CORS(app, origins=['https://quindiotravel.com.co', 'http://localhost:3000', 'http://127.0.0.1:3000'])

# Inicializar sistema de automatización
automation_system = LeadAutomationSystem()

@app.route('/api/lead', methods=['POST'])
def create_lead():
    """API para crear un nuevo lead desde el sitio web"""
    try:
        lead_data = request.json
        
        # Agregar datos adicionales del request
        lead_data['inquiry_time'] = datetime.now().isoformat()
        lead_data['source'] = 'website'
        lead_data['ip_address'] = request.remote_addr
        lead_data['user_agent'] = request.headers.get('User-Agent', '')
        
        # Procesar lead a través del sistema
        result = automation_system.process_new_lead(lead_data)
        
        return jsonify({
            'success': True,
            'lead_id': result['lead_id'],
            'score': result['score'],
            'prediction': result['prediction'],
            'message': 'Lead procesado exitosamente'
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/lead/<lead_id>', methods=['GET'])
def get_lead(lead_id):
    """API para obtener información de un lead específico"""
    try:
        lead = next((l for l in automation_system.leads_db if l.get('id') == lead_id), None)
        
        if not lead:
            return jsonify({
                'success': False,
                'error': 'Lead no encontrado'
            }), 404
        
        return jsonify({
            'success': True,
            'lead': lead
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/leads', methods=['GET'])
def get_leads():
    """API para obtener todos los leads con filtros opcionales"""
    try:
        # Filtros opcionales
        category = request.args.get('category')
        limit = int(request.args.get('limit', 50))
        
        leads = automation_system.leads_db
        
        # Filtrar por categoría si se especifica
        if category:
            leads = [l for l in leads if l.get('score', {}).get('category') == category]
        
        # Limitar resultados
        leads = leads[:limit]
        
        return jsonify({
            'success': True,
            'leads': leads,
            'total': len(leads)
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/leads/high-priority', methods=['GET'])
def get_high_priority_leads():
    """API para obtener leads de alta prioridad"""
    try:
        high_priority_leads = automation_system.identify_high_priority_leads()
        
        return jsonify({
            'success': True,
            'leads': high_priority_leads,
            'total': len(high_priority_leads)
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/followup', methods=['POST'])
def create_followup():
    """API para crear un seguimiento manual"""
    try:
        data = request.json
        lead_id = data.get('lead_id')
        message = data.get('message')
        priority = data.get('priority', 'normal')
        
        followup = automation_system.followup_engine.add_manual_followup(
            lead_id, message, priority
        )
        
        return jsonify({
            'success': True,
            'followup': followup
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analytics/conversion-rate', methods=['GET'])
def get_conversion_rate():
    """API para obtener tasa de conversión"""
    try:
        period_days = int(request.args.get('period_days', 30))
        conversion_rate = automation_system.analytics.calculate_conversion_rate(period_days)
        
        return jsonify({
            'success': True,
            'conversion_rate': conversion_rate
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analytics/report', methods=['GET'])
def get_analytics_report():
    """API para obtener reporte analítico completo"""
    try:
        report = automation_system.analytics.generate_conversion_report()
        
        return jsonify({
            'success': True,
            'report': report
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/analytics/predict', methods=['POST'])
def predict_conversion():
    """API para predecir probabilidad de conversión de un lead"""
    try:
        lead_data = request.json
        prediction = automation_system.analytics.predict_conversion_probability(lead_data)
        
        return jsonify({
            'success': True,
            'prediction': prediction
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats', methods=['GET'])
def get_system_stats():
    """API para obtener estadísticas del sistema"""
    try:
        stats = {
            'total_leads': len(automation_system.leads_db),
            'hot_leads': len([l for l in automation_system.leads_db if l.get('score', {}).get('category') == 'hot_lead']),
            'warm_leads': len([l for l in automation_system.leads_db if l.get('score', {}).get('category') == 'warm_lead']),
            'cold_leads': len([l for l in automation_system.leads_db if l.get('score', {}).get('category') == 'cold_lead']),
            'followup_stats': automation_system.followup_engine.get_followup_stats(),
            'whatsapp_messages': automation_system.whatsapp_bot.daily_message_count
        }
        
        return jsonify({
            'success': True,
            'stats': stats
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tasks/daily', methods=['POST'])
def execute_daily_tasks():
    """API para ejecutar tareas diarias manualmente"""
    try:
        results = automation_system.execute_daily_tasks()
        
        return jsonify({
            'success': True,
            'results': results
        }), 200
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """API para verificar estado del sistema"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'system': 'Lead Automation System - Quindío Travel'
    }), 200

# Integración con el formulario de cotización existente
@app.route('/api/quote', methods=['POST'])
def process_quote():
    """API específica para procesar cotizaciones del sitio web"""
    try:
        quote_data = request.json
        
        # Convertir datos de cotización a formato de lead
        lead_data = {
            'nombre': quote_data.get('name', ''),
            'telefono': quote_data.get('phone', ''),
            'mensaje': f"Cotización para {quote_data.get('destination', 'Eje Cafetero')}",
            'destino': quote_data.get('destination', ''),
            'fecha_deseada': quote_data.get('date', ''),
            'num_personas': quote_data.get('passengers', ''),
            'presupuesto': quote_data.get('budget', ''),
            'source': 'quote_form',
            'inquiry_time': datetime.now().isoformat(),
            'device': 'desktop',
            'page_views': 3,
            'time_on_site': 5,
            'is_return_visitor': False
        }
        
        # Procesar lead
        result = automation_system.process_new_lead(lead_data)
        
        return jsonify({
            'success': True,
            'lead_id': result['lead_id'],
            'score': result['score'],
            'message': 'Cotización procesada exitosamente'
        }), 201
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("🚀 API de Integración Web - Sistema de Automatización de Leads")
    print("📡 Servidor ejecutándose en http://localhost:5000")
    print("🔗 Endpoints disponibles:")
    print("   POST /api/lead - Crear nuevo lead")
    print("   GET  /api/lead/<id> - Obtener lead específico")
    print("   GET  /api/leads - Obtener todos los leads")
    print("   GET  /api/leads/high-priority - Leads de alta prioridad")
    print("   POST /api/followup - Crear seguimiento manual")
    print("   GET  /api/analytics/conversion-rate - Tasa de conversión")
    print("   GET  /api/analytics/report - Reporte analítico")
    print("   POST /api/analytics/predict - Predecir conversión")
    print("   GET  /api/stats - Estadísticas del sistema")
    print("   POST /api/tasks/daily - Ejecutar tareas diarias")
    print("   GET  /api/health - Verificar estado")
    print("   POST /api/quote - Procesar cotización")
    
    app.run(debug=False, host='0.0.0.0', port=5000)