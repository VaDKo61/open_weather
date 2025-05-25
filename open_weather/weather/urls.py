from django.urls import path

from weather.views import get_title_page, get_city, get_weather

urlpatterns = [
    path('', get_title_page, name='title_page'),
    path('search', get_city, name='search_city'),
    path('weather/<str:lat>&<str:lon>', get_weather, name='weather_city'),
]
