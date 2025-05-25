from django.shortcuts import render

from .services import search_city
from .services import get_weather_lat_lon


def get_title_page(request):
    return render(request, 'weather/base.html')


def get_city(request):
    city: str = request.GET['search']
    cities: list[dict] = search_city(city)
    return render(request, 'weather/search_city.html', context={'cities': cities})


def get_weather(request, lat: str, lon: str):
    weather = get_weather_lat_lon(lat, lon)
    return render(request, 'weather/weather.html', context={'weather': weather})
