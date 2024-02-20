from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import requests, json, os

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def weather(request):
    # API_KEY = 'e87eb99c5ab7bd9404658726884e70ec'
    API_KEY = os.environ.get('OPEN_WEATHER_API')  # Use the environment variable
    CITY_NAME = 'Greenville'
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'
    
    response = requests.get(URL)
    data = response.json()
    print(data)
    print(os.environ.get('OPENWEATHER_API_KEY'))
    
    weather = {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'city': CITY_NAME
    }
    
    return render(request, 'weather.html', {'weather_data': json.dumps(data, indent=4)})