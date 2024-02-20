from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests, json, os

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def weather(request):
    #client_ip = get_client_ip(request)
    client_ip = '24.48.0.1'
    API_KEY = os.environ.get('OPEN_WEATHER_API')  # Use the environment variable
    CITY_NAME = 'Greenville'
    URL_IP = f'http://ip-api.com/json/{client_ip}'
    response = requests.get(URL_IP)
    data_ip = response.json()

    lat = data_ip['lat']
    lon = data_ip['lon']
    
    URL_Weather = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
    response = requests.get(URL_Weather)
    data_weather = response.json()

    weather = {
        'description': data_weather['weather'][0]['description'],
        'temperature': data_weather['main']['temp'],
        'city': CITY_NAME
    }


    
    return render(request, 'weather.html', {'weather_data': json.dumps(data_weather, indent=4)})