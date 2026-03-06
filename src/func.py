def state_list(self):
    """Возвращает все значения атрибутов самолёта"""
    states = []
    for i in [self.register_country, self.call_name, self.flight_speed,
              self.flight_height, self.is_on_ground]:
        states.append(i)
    return states


def filter_aeroplanes(aeroplanes: list, filter_words: str) -> list:
    """Возвращает самолёты только тех стран, которые есть в строке.
    Строка состоит из названий стран, разделённых пробелами"""
    filtered_aeroplanes = []
    for plane in aeroplanes:
        if plane.register_country in filter_words:
            filtered_aeroplanes.append(plane)
    return filtered_aeroplanes


def get_aeroplanes_by_altitude(aeroplanes: list, alt_start: float, alt_end: float) -> list:
    """Возвращает только те самолёты, высота полёта которых
    находится в промежутке двух указанных чисел"""
    ranged_aeroplanes = []
    for plane in aeroplanes:
        if alt_start <= plane.flight_height <= alt_end:
            ranged_aeroplanes.append(plane)
    return ranged_aeroplanes


def sort_aeroplanes(aeroplanes: list) -> list:
    """Сортирует самолёты по высоте в порядке убывания"""
    sorted_aeroplanes = sorted(aeroplanes, key=lambda x: x.flight_height, reverse=True)
    return sorted_aeroplanes


def get_top_aeroplanes(sorted_aeroplanes: list, top_n: int) -> list:
    """Возвращает указанное число самых высоко летящих самолётов
    из отсортированного списка"""
    top_aeroplanes = []
    for i in range(0, top_n):
        top_aeroplanes.append(sorted_aeroplanes[i])
    return top_aeroplanes
