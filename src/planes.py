class Aeroplane:
    """Класс для работы с информацией о самолётах"""
    register_country: str   # страна регистрации
    call_name: str   # позывной
    flight_speed: float   # скорость полёта
    flight_height: float   # высота полёта
    is_on_ground: bool   # находится ли самолёт на земле

    def __init__(self, register_country, call_name, flight_speed, flight_height, is_on_ground):
        self.register_country = register_country
        self.call_name = call_name
        self.flight_speed = flight_speed
        self.flight_height = flight_height
        self.is_on_ground = is_on_ground

    @classmethod
    def from_dict(cls, dict_item: dict) -> object:
        """Создание объекта из словаря"""
        return cls(**dict_item)
