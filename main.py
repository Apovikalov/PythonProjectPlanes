# Создание экземпляра класса для работы с API сайтов с самолетами
from src.api import APIAdapter
from src.func import filter_aeroplanes, state_list, get_aeroplanes_by_altitude, sort_aeroplanes, get_top_aeroplanes
from src.json_saver import JSONSaver
from src.planes import Aeroplane

api = APIAdapter()

# Получение информации о самолетах с opensky-network.org
aeroplanes = api.get_aeroplanes('Spain')

# Преобразование набора данных в список объектов
if aeroplanes.type is not None:
    aeroplanes = state_list(aeroplanes)

# Пример работы конструктора класса с одним самолетом
aeroplane = Aeroplane("United States", "UAL1621", 268.79, 10203.18, False)

# Сохранение информации в файл
json_saver = JSONSaver()
json_saver.dump_to_file(aeroplane)
json_saver.delete_from_file()

# Функция для взаимодействия с пользователем
def user_interaction():
    country = input("Введите название страны: ")
    top_n = int(input("Введите количество самолетов для вывода в топ N: "))
    filter_words = input("Введите названия стран для фильтрации по стране регистрации: ").split()
    altitude_range = input("Введите диапазон высот полета: ") # Пример: 100000 - 150000
    alt_start, alt_end = altitude_range.split(" - ")

    filtered_aeroplanes = filter_aeroplanes(aeroplanes, filter_words)

    ranged_aeroplanes = get_aeroplanes_by_altitude(aeroplanes, float(alt_start), float(alt_end))

    sorted_aeroplanes = sort_aeroplanes(ranged_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_aeroplanes, top_n)
    print(top_aeroplanes)


if __name__ == "__main__":
    user_interaction()
