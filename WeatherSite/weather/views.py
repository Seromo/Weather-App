from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .models import City
from .forms import CityForm

#r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Johannesburg&units=metric&APPID=0ecca4fd6563b7746b4accf13dd6a9dc')
#response = r.json()
# Create your views here.
def index(request):

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
        #city = request.POST['city']
        

    form = CityForm()

    cities = City.objects.all()

    data = []
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=0ecca4fd6563b7746b4accf13dd6a9dc'

    for city in cities:

        response = requests.get(url.format(city)).json()

        weather = {'city_name': response['name'],
            "country_code": response['sys']['country'],
            'temp': str(response['main']['temp'])+ ' °C',
            "pressure": response['main']['pressure'],
            "humidity": response['main']['humidity'],
            'main': response['weather'][0]['main'],
            "condition":response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                
            }

        datab = City(name = city,
        country_code = response['sys']['country'],
        temperature = response['main']['temp'])
        datab.save()
        data.append(weather)
    
    context = {'weather_data' : data,'form':form}
    return render(request, 'weather/index.html',context)