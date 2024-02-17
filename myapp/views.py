from django.http import HttpResponse
from django.template import loader
import requests, json, os

def home(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def weather(request):
    API_KEY = os.environ.get('OPENWEATHER_API_KEY', '')  # Use the environment variable
    CITY_NAME = 'Greenville'
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}'
    
    response = requests.get(URL)
    data = response.json()
    print(data)
    
    weather = {
        'description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'city': CITY_NAME
    }
    
    return render(request, 'your_app/weather.html', {'weather_data': json.dumps(data, indent=4)})