from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from .forms import CityForm

#r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Johannesburg&units=metric&APPID=0ecca4fd6563b7746b4accf13dd6a9dc')
#response = r.json()
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        form = CityForm(request.POST) # add actual request data to form for processing
        form.save() #
        

        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=0ecca4fd6563b7746b4accf13dd6a9dc'

        response = requests.get(url.format(city)).json()
        

        weather = {'city_name': city,
        "country_code": response['sys']['country'],
        'temp': round(response['main']['temp'],0),
        "pressure": response['main']['pressure'],
        "humidity": response['main']['humidity'],
        'main': response['weather'][0]['main'],
        "condition":response['weather'][0]['description'],
        'icon': response['weather'][0]['icon'],
        
     }

    else:
        weather ={}

    form = CityForm()
    
    context = {'weather_data' :[weather], 'form' : form}
    return render(request, 'weather/index.html',context)