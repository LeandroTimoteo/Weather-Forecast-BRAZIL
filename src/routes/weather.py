from flask import Blueprint, jsonify, request
import requests
import json

weather_bp = Blueprint('weather', __name__)

# Lista de capitais dos estados brasileiros com suas coordenadas
BRAZILIAN_STATES = {
    'AC': {'name': 'Acre', 'capital': 'Rio Branco', 'lat': -9.9754, 'lon': -67.8249},
    'AL': {'name': 'Alagoas', 'capital': 'Maceió', 'lat': -9.6658, 'lon': -35.7353},
    'AP': {'name': 'Amapá', 'capital': 'Macapá', 'lat': 0.0389, 'lon': -51.0664},
    'AM': {'name': 'Amazonas', 'capital': 'Manaus', 'lat': -3.1190, 'lon': -60.0217},
    'BA': {'name': 'Bahia', 'capital': 'Salvador', 'lat': -12.9714, 'lon': -38.5014},
    'CE': {'name': 'Ceará', 'capital': 'Fortaleza', 'lat': -3.7319, 'lon': -38.5267},
    'DF': {'name': 'Distrito Federal', 'capital': 'Brasília', 'lat': -15.7942, 'lon': -47.8822},
    'ES': {'name': 'Espírito Santo', 'capital': 'Vitória', 'lat': -20.3155, 'lon': -40.3128},
    'GO': {'name': 'Goiás', 'capital': 'Goiânia', 'lat': -16.6869, 'lon': -49.2648},
    'MA': {'name': 'Maranhão', 'capital': 'São Luís', 'lat': -2.5387, 'lon': -44.2825},
    'MT': {'name': 'Mato Grosso', 'capital': 'Cuiabá', 'lat': -15.6014, 'lon': -56.0979},
    'MS': {'name': 'Mato Grosso do Sul', 'capital': 'Campo Grande', 'lat': -20.4697, 'lon': -54.6201},
    'MG': {'name': 'Minas Gerais', 'capital': 'Belo Horizonte', 'lat': -19.9191, 'lon': -43.9386},
    'PA': {'name': 'Pará', 'capital': 'Belém', 'lat': -1.4558, 'lon': -48.5044},
    'PB': {'name': 'Paraíba', 'capital': 'João Pessoa', 'lat': -7.1195, 'lon': -34.8450},
    'PR': {'name': 'Paraná', 'capital': 'Curitiba', 'lat': -25.4284, 'lon': -49.2733},
    'PE': {'name': 'Pernambuco', 'capital': 'Recife', 'lat': -8.0476, 'lon': -34.8770},
    'PI': {'name': 'Piauí', 'capital': 'Teresina', 'lat': -5.0892, 'lon': -42.8019},
    'RJ': {'name': 'Rio de Janeiro', 'capital': 'Rio de Janeiro', 'lat': -22.9068, 'lon': -43.1729},
    'RN': {'name': 'Rio Grande do Norte', 'capital': 'Natal', 'lat': -5.7945, 'lon': -35.2110},
    'RS': {'name': 'Rio Grande do Sul', 'capital': 'Porto Alegre', 'lat': -30.0346, 'lon': -51.2177},
    'RO': {'name': 'Rondônia', 'capital': 'Porto Velho', 'lat': -8.7612, 'lon': -63.9004},
    'RR': {'name': 'Roraima', 'capital': 'Boa Vista', 'lat': 2.8235, 'lon': -60.6758},
    'SC': {'name': 'Santa Catarina', 'capital': 'Florianópolis', 'lat': -27.5954, 'lon': -48.5480},
    'SP': {'name': 'São Paulo', 'capital': 'São Paulo', 'lat': -23.5505, 'lon': -46.6333},
    'SE': {'name': 'Sergipe', 'capital': 'Aracaju', 'lat': -10.9472, 'lon': -37.0731},
    'TO': {'name': 'Tocantins', 'capital': 'Palmas', 'lat': -10.1689, 'lon': -48.3317}
}

def get_weather_data_openmeteo(lat, lon):
    """
    Obtém dados meteorológicos usando a API Open-Meteo (gratuita)
    """
    try:
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            'latitude': lat,
            'longitude': lon,
            'current': 'temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m',
            'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum,precipitation_probability_max,weather_code',
            'timezone': 'America/Sao_Paulo',
            'forecast_days': 7
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Mapear códigos de clima para descrições em português
        weather_codes = {
            0: "Céu limpo",
            1: "Principalmente limpo",
            2: "Parcialmente nublado",
            3: "Nublado",
            45: "Neblina",
            48: "Neblina com geada",
            51: "Garoa leve",
            53: "Garoa moderada",
            55: "Garoa intensa",
            61: "Chuva leve",
            63: "Chuva moderada",
            65: "Chuva intensa",
            80: "Pancadas de chuva leves",
            81: "Pancadas de chuva moderadas",
            82: "Pancadas de chuva intensas",
            95: "Tempestade",
            96: "Tempestade com granizo leve",
            99: "Tempestade com granizo intenso"
        }
        
        current = data.get('current', {})
        daily = data.get('daily', {})
        
        # Dados atuais
        current_weather = {
            'temperature': current.get('temperature_2m'),
            'humidity': current.get('relative_humidity_2m'),
            'apparent_temperature': current.get('apparent_temperature'),
            'precipitation': current.get('precipitation'),
            'wind_speed': current.get('wind_speed_10m'),
            'description': weather_codes.get(current.get('weather_code'), "Desconhecido")
        }
        
        # Previsão para os próximos dias
        forecast = []
        if daily:
            for i in range(len(daily.get('time', []))):
                forecast.append({
                    'date': daily['time'][i],
                    'max_temp': daily['temperature_2m_max'][i],
                    'min_temp': daily['temperature_2m_min'][i],
                    'precipitation': daily['precipitation_sum'][i],
                    'precipitation_probability': daily['precipitation_probability_max'][i],
                    'description': weather_codes.get(daily['weather_code'][i], "Desconhecido")
                })
        
        return {
            'current': current_weather,
            'forecast': forecast,
            'success': True
        }
        
    except Exception as e:
        return {
            'error': str(e),
            'success': False
        }

@weather_bp.route('/states', methods=['GET'])
def get_states():
    """
    Retorna a lista de estados brasileiros
    """
    return jsonify({
        'states': BRAZILIAN_STATES,
        'success': True
    })

@weather_bp.route('/weather/<state_code>', methods=['GET'])
def get_weather_by_state(state_code):
    """
    Obtém dados meteorológicos para um estado específico
    """
    state_code = state_code.upper()
    
    if state_code not in BRAZILIAN_STATES:
        return jsonify({
            'error': 'Estado não encontrado',
            'success': False
        }), 404
    
    state_info = BRAZILIAN_STATES[state_code]
    weather_data = get_weather_data_openmeteo(state_info['lat'], state_info['lon'])
    
    if weather_data['success']:
        return jsonify({
            'state': state_info,
            'weather': weather_data,
            'success': True
        })
    else:
        return jsonify({
            'error': weather_data['error'],
            'success': False
        }), 500

@weather_bp.route('/weather/all', methods=['GET'])
def get_all_weather():
    """
    Obtém dados meteorológicos para todos os estados
    """
    all_weather = {}
    
    for state_code, state_info in BRAZILIAN_STATES.items():
        weather_data = get_weather_data_openmeteo(state_info['lat'], state_info['lon'])
        
        if weather_data['success']:
            all_weather[state_code] = {
                'state': state_info,
                'weather': weather_data
            }
        else:
            all_weather[state_code] = {
                'state': state_info,
                'weather': {'error': weather_data['error'], 'success': False}
            }
    
    return jsonify({
        'data': all_weather,
        'success': True
    })

