import os

from dotenv import load_dotenv

load_dotenv()
# Ключ API для Яндекс.Расписаний
API_KEY = os.getenv('API_KEY')

# URL для поиска ближайшего вокзала
URL_NEAREST_STATION = 'https://api.rasp.yandex.net/v3.0/nearest_stations/'

# URL для получения расписания
URL_SCHEDULE = 'https://api.rasp.yandex.net/v3.0/schedule/'

# Параметры для поиска ближайшего вокзала к Пензе
PARAMS_PENZA = {
    'apikey': API_KEY,
    'lat': 53.2007,
    'lng': 45.0046,
    'distance': 50,
    'transport_types': 'train',
    'station_types': 'station'
}