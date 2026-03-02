from abc import ABC, abstractmethod

from requests import get


class Parser(ABC):

    @abstractmethod
    def get_aeroplanes(self, country: str):
        pass


class APIAdapter(Parser):

    def __init__(self) -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        headers_nominatim = {
            'User-Agent': 'test-app',
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        data = response.json()

        # Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        # Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.opensky_url, params=params)

        # Пример ответа от opensky-network можно посмотреть в задании курсовой.
        self.aeroplanes = response.json()


api = APIAdapter()
print(api.get_aeroplanes('Canada'))
