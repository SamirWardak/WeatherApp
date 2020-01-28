from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    appid = 'd56f5d995fe947f196e92bc1debefefe'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if 'send' in request.POST:
        form = CityForm(request.POST)
        form.save()

    if 'delete_all' in request.POST:
        City.objects.all().delete()

    if 'delete_one' in request.POST:
        City.objects.filter(name=CityForm(request.POST)).delete()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {'city': city.name,
                     'temp': res["main"]["temp"],
                     'icon': res["weather"][0]["icon"]}

        all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
