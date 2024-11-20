class User:
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name


class Film:
    def __init__(self, film_id):
        self.ID = film_id
        try:
            self.name = Methods.film_by_id(film_id)
        except ValueError as e:
            self.name = None
            print(f"Ошибка при создании экземпляра класса: {e}")


class Methods:
    @staticmethod
    def count_strings(path):
        with open(path, "r") as file:
            return sum(1 for _ in file)

    @staticmethod
    def read_file_line(path: str, num: int) -> str:
        """Выводит содержимое строки num у файла"""
        with open(path, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if num >= len(lines):
                raise IndexError(f"Line number {num} out of range")
            return lines[num]

    @staticmethod
    def history_by_id(user_id):
        """Выводит список просмотров по ID пользователя"""

        try:
            film_str = Methods.read_file_line("history.txt", user_id)
            if film_str.count(",") == 0:
                return int(film_str)
            return list(map(int, film_str.split(",")))
        except IndexError:
            raise ValueError(f"Нет данных для user_id={user_id}")
        except FileNotFoundError:
            raise ValueError("Файл history.txt не найден")

    @staticmethod
    def film_by_id(film_id) -> str:
        """Выводит имя фильма по его ID"""
        try:
            film_str = Methods.read_file_line("films.txt", film_id)
            return film_str.split(",")[1]
        except IndexError:
            raise ValueError(f"Нет данных для film_id={film_id}")
        except FileNotFoundError:
            raise ValueError("Файл films.txt не найден")

    @staticmethod
    def half_coincide(arr_passive: list, arr_active: list):
        """надо, чтобы у passive совпадала половина с заданным массивом"""
        len_array = len(arr_passive)
        c = 0
        for elem in arr_passive:
            if elem in arr_active:
                c += 1
        return c / len_array >= 0.5

    @staticmethod
    def count_of_watch(film_id):
        with open("history.txt", "r") as file:
            return file.read().count(str(film_id))

    @staticmethod
    def recommendation_by_user(arr_films):
        """На вход подается экземпляр класса User"""


        recommends = set()
        for user_id in range(Methods.count_strings("history.txt")):
            if Methods.half_coincide(Methods.history_by_id(user_id), arr_films):
                recommends = recommends | (set(Methods.history_by_id(user_id)) - set(arr_films))

        recommends_arr = list(recommends)
        count = 0
        final_film_id = -1
        for index in range(len(recommends_arr)):
            tmp_film = recommends_arr[index]
            tmp_count = Methods.count_of_watch(tmp_film)
            if tmp_count > count:
                count = tmp_count
                final_film_id = tmp_film
        if final_film_id == -1:
            return "No recommend"
        return Methods.film_by_id(final_film_id)



print(Methods.recommendation_by_user([2, 4]))
