import pytest
import requests

from .configuration import API_KEY, URL_NEAREST_STATION, URL_SCHEDULE, PARAMS_PENZA

@pytest.mark.api
def test_nearest_station_penza():
    # Отправляем запрос для поиска ближайшего вокзала к Пензе
    response = requests.get(URL_NEAREST_STATION, params=PARAMS_PENZA)
    assert response.status_code == 200, 'Wrong status code'

    # Получаем данные из ответа
    data = response.json()

    # Проверяем, что список станций не пуст
    assert 'stations' in data, 'List of stations not found in response'
    assert len(
        data['stations']) > 2, 'There are not enough stations in 50km'

    # Получаем третий ближайший вокзал
    third_station = data['stations'][2]
    station_code = third_station['code']

    # Проверяем, что мы получили код станции
    assert station_code, 'Failed to get third station code'

@pytest.mark.api
def test_schedule_third_station(third_station_code):
    # Параметры для получения расписания
    PARAMS_SCHEDULE = {
        'apikey': API_KEY,
        'format': 'json',
        'station': third_station_code,
        'transport_types': 'suburban',
        'lang': 'ru_RU'
    }

    # Отправляем запрос для получения расписания
    response = requests.get(URL_SCHEDULE, params=PARAMS_SCHEDULE)
    assert response.status_code == 200, 'Wrong status code'

    # Получаем данные из ответа
    data = response.json()

    # Проверяем наличие необходимых элементов в ответе
    required_elements = [
        'date',
        'pagination',
        'station',
        'schedule',
        'schedule_direction',
        'directions'
    ]
    for element in required_elements:
        assert element in data, f'"{element}" not found'

    # Проверяем структуру массива schedule
    assert 'schedule' in data, 'Schedule not found in data'
    for thread in data['schedule']:
        assert 'thread' in thread, 'Thread not found in schedule'
        assert 'number' in thread['thread'] and thread['thread']['number'], 'Number is missing or empty in thread'
        assert 'title' in thread['thread'] and thread['thread']['title'], 'Title is missing or empty in thread'
        assert 'uid' in thread['thread'] and thread['thread']['uid'], 'UID is missing or empty in thread'
