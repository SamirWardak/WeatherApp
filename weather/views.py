import requests

from django.shortcuts import render

from .models import City
from .forms import CityForm


def index(request):
    appid = 'd56f5d995fe947f196e92bc1debefefe'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    form = CityForm(request.POST)
    if "actions" in request.POST:
        actions = request.POST["actions"]

        if 'save' == actions:
            form.save()

        if 'remove_all' == actions:
            City.objects.all().delete()

        if 'remove' == actions and City.objects.filter(name=request.POST["name"]).exists():
            remove_city = City.objects.get(name=request.POST["name"])
            remove_city.delete()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        try:
            res = requests.get(url.format(city.name)).json()
            city_info = {
                'city': city.name,
                'temp': res["main"]["temp"],
                'icon': res["weather"][0]["icon"]
            }
            all_cities.append(city_info)
        except Exception as e:
            city_info = {
                'city': city.name,
                'temp': "Not found"
            }
            all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form
    }

    return render(
        request,
        'weather/index.html',
        context
    )
