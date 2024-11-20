class Methods:
    @staticmethod
    def read_file_line(path: str, num: int) -> str:
        """Выводит содержимое строки num у файла"""
        with open(path, "r").readlines() as line:
            if num >= len(line):
                raise IndexError(f"Line number {num} out of range")
            return line[num]

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


class User:
    def __init__(self, user_id, user_name):
        self.ID = user_id
        self.user_name = user_name


class Film:
    def __init__(self, film_id):
        self.ID = film_id
        try:
            self.name = Methods.film_by_id(film_id)
        except ValueError as e:
            self.name = None
            print(f"Ошибка при создании экземпляра класса: {e}")