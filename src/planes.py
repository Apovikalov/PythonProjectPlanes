class Aeroplane:
    """Класс для работы с информацией о самолётах"""
    __slots__ = ('__register_country', '__call_name', '__flight_speed',
                 '__flight_height', '__is_on_ground')
    __register_country: str   # страна регистрации
    __call_name: str   # позывной
    __flight_speed: float   # скорость полёта
    __flight_height: float   # высота полёта
    __is_on_ground: bool   # находится ли самолёт на земле

    def __init__(self, register_country, call_name, flight_speed,
                 flight_height, is_on_ground):
        self.__register_country = register_country
        self.__call_name = call_name
        if flight_speed <= 0:
            print("Скорость должна быть положительным числом")
            raise ValueError
        else:
            self.__flight_speed = flight_speed
        if flight_height <= 0:
            print("Высота должна быть положительным числом")
            raise ValueError
        else:
            self.__flight_height = flight_height
        self.__is_on_ground = is_on_ground

    def __eq__(self, other):
        return self.flight_height == other.flight_height

    def __gt__(self, other):
        return self.flight_height > other.flight_height

    def __lt__(self, other):
        return self.flight_height < other.flight_height

    @property
    def register_country(self):
        return self.__register_country

    @property
    def call_name(self):
        return self.__call_name

    @property
    def flight_speed(self):
        return self.__flight_speed

    @property
    def flight_height(self):
        return self.__flight_height

    @property
    def is_on_ground(self):
        return self.__is_on_ground

    @classmethod
    def from_dict(cls, dict_item: dict) -> object:
        """Создание объекта из словаря"""
        return cls(**dict_item)
