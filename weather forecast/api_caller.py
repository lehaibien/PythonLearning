import requests

def get_weather():
    response = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude=10.97&longitude=106.82&hourly=temperature_2m&daily=temperature_2m_max,temperature_2m_min&timezone=Asia%2FBangkok')
    response_dictionary = response.json()
    min_temperature = response_dictionary['daily']['temperature_2m_min'][0]
    max_temperature = response_dictionary['daily']['temperature_2m_max'][0]
    temperature = response_dictionary['hourly']['temperature_2m'][0:24]
    return {
        'min_temperature': min_temperature,
        'max_temperature': max_temperature,
        'temperature': temperature
    }
