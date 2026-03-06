class Aeroplane:
    """Класс для работы с информацией о самолётах"""
    __register_country: str   # страна регистрации
    __call_name: str   # позывной
    __flight_speed: float   # скорость полёта
    __flight_height: float   # высота полёта
    __is_on_ground: bool   # находится ли самолёт на земле

    def __init__(self, register_country, call_name, flight_speed,
                 flight_height, is_on_ground):
        self.__register_country = register_country
        self.__call_name = call_name
        self.__flight_speed = flight_speed
        self.__flight_height = flight_height
        self.__is_on_ground = is_on_ground

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
