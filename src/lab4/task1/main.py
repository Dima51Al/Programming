class Methods:
    @staticmethod
    def read_file_line(path: str, num: int) -> str:
        line = open(path, "r").readlines()[num]
        return line

    @staticmethod
    def history_by_id(user_id):
        array = Methods.read_file_line("history.txt", user_id).split(",")
        return list(map(int, array))

    @staticmethod
    def film_by_id(film_id) -> str:
        return Methods.read_file_line("films.txt", film_id).split(",")[1]


class User:
    def __init__(self, user_id, user_name):
        self.ID = user_id
        self.user_name = user_name


class Film:
    def __init__(self, film_id):
        self.ID = film_id
        self.name = Methods.film_by_id(film_id)
