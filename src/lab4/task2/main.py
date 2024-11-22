class Alive:
    split_age_array = [18, 25, 35, 45, 60, 80, 100]
    group = None

    @classmethod
    def initialize_group(cls):
        cls.group = cls.AgeGroup()

    @classmethod
    def set_split_age_array(cls, array):
        cls.split_age_array = array

    class AgeGroup:
        INFO = """
                У каждой возрастной группы есть элемент [начало]

                """

        @staticmethod
        def fix_age_array(array, template_if_bad):
            for i in range(len(array)):
                if array[i] < 0 or array[i] > 123:
                    array[i] = 0

            if len(array) == 0:
                return [template_if_bad]

            array = list(set(array))
            array.sort()
            return array

        def create_age_group(self, array: list[int]):

            array = self.fix_age_array(array, ["0-123"])

            array.append(-1)
            array = list(set(array))
            array.sort()

            if 0 in array:
                array.pop(0)

            age_group = []

            for i in range(len(array) - 1):
                tmp_str = f"{array[i] + 1}-{array[i + 1]}"
                age_group.append(tmp_str)

                if i == len(array) - 2:
                    age_group.append(f"{array[i + 1] + 1}+")
            return age_group

        def __init__(self):
            age_group_int_array = Alive.split_age_array
            self.age_group_for_view = self.create_age_group(age_group_int_array)
            self.age_group_for_index = self.fix_age_array(age_group_int_array, "0")
            self.start_elem = self.age_group_for_index[0]

        def stats(self):
            print(self.age_group_for_view, self.age_group_for_index)

        def which_group(self, age):
            if age < 0 or age > 123:
                return "(age error)"

            arr = self.age_group_for_index
            for index in range(len(arr)):
                if arr[index] >= age:
                    return self.age_group_for_view[index]
            return self.age_group_for_view[-1]

    class Human:
        def __init__(self, name="Ivan Ivanov", age=18):
            self.name = name
            self.age = age

            self.age_group = Alive.group.which_group(self.age) if Alive.group else "(no group)"

        def stats(self):
            print(self.name, self.age, self.age_group)


def main():
    users_array = []
    Alive.initialize_group()

    print("<name>, <age>")
    while True:
        string = input()
        if string.count(",") != 1:
            break
        input_arr = string.split(",")
        tmp_name = input_arr[0]
        tmp_age = int(input_arr[1])
        users_array.append(Alive.Human(tmp_name, tmp_age))

    group = Alive.AgeGroup().age_group_for_view
    for tmp_group in group:
        tmp_group_arr = []
        for user in users_array:
            if user.age_group == tmp_group:
                tmp_group_arr.append(f"{user.name} ({user.age})")
        if len(tmp_group_arr) != 0:
            print(f"{tmp_group}: {str(tmp_group_arr)[1:-1]}".replace("\'", ""))


def main_str(input_string):
    answer = ""
    users_array = []
    Alive.initialize_group()

    lines = input_string.strip().split("\n")

    for string in lines:
        if string.count(",") != 1:
            continue
        input_arr = string.split(",")
        tmp_name = input_arr[0].strip()
        tmp_age = int(input_arr[1].strip())
        users_array.append(Alive.Human(tmp_name, tmp_age))

    group = Alive.AgeGroup().age_group_for_view
    for tmp_group in group:
        tmp_group_arr = []
        for user in users_array:
            if user.age_group == tmp_group:
                tmp_group_arr.append(f"{user.name} ({user.age})")
        if len(tmp_group_arr) != 0:
            answer += f"{tmp_group}: {str(tmp_group_arr)[1:-1].replace("\'", "")}\n"
    return answer.replace("\n", "")


if __name__ == '__main__':

    main()
