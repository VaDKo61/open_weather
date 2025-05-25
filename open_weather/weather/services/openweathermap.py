import requests
import json
import os

from dotenv import load_dotenv


def search_city(city_name: str) -> list[dict]:
    load_dotenv()
    api_key: str = os.getenv('API_KEY_OPENWEATHERKEY')
    limit_result: int = 5
    url_search_city: str = (f'http://api.openweathermap.org/geo/1.0/direct?'
                            f'q={city_name}&limit={limit_result}&appid={api_key}')
    response = requests.get(url_search_city)
    json_response: list[dict] = json.loads(response.text)
    return json_response


def get_weather_lat_lon(lat: str, lon: str) -> dict:
    load_dotenv()
    api_key: str = os.getenv('API_KEY_OPENWEATHERKEY')
    url_search_city: str = (f'https://api.openweathermap.org/data/2.5/weather?lat='
                            f'{lat}&lon={lon}&appid={api_key}')
    response = requests.get(url_search_city)
    json_response: list[dict] = json.loads(response.text)
    weather = {
        'city': json_response['name'],
        'temp': int(json_response['main']['temp'] - 273),
        'weather': json_response['weather'][0]['description']
    }
    return weather

# try:
#     api_response = requests.get(
#         f'https://api.openweathermap.org/data/2.5/forecast?lat={self.object.polygon.lat}&'
#         f'lon={self.object.polygon.lon}&appid={api_key}&units={units}&lang={lang}')
#     api_response.raise_for_status()
# except HTTPError:
#     context['error'] = True
# else:
#     json_response = json.loads(api_response.text)
#     weather_dict = {}
#     date_game = str(self.object.date)
#     for dict_weather in json_response['list']:
#         if dict_weather['dt_txt'][:10] == date_game:
#             weather_dict[f'time_{dict_weather["dt_txt"][11:13]}'] = {
#                 'description': dict_weather['weather'][0]['description'],
#                 'temp': round(dict_weather['main']['temp']),
#                 'feels_like': round(dict_weather['main']['feels_like']),
#                 'visibility': dict_weather['visibility'] // 1000,
#                 'speed': round(dict_weather['wind']['speed'], 1),
#                 'gust': round(dict_weather['wind']['gust'], 1),
#                 'pop': round(dict_weather['pop'] * 100),
#                 'rain': dict_weather.get('rain', False),
#                 'snow': dict_weather.get('snow', False),
#                 'time': dict_weather["dt_txt"][11:16]
#             }
#     context['weather_dict'] = weather_dict
