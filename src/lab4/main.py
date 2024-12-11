import re


class Shop:
    path_input = "orders.txt"
    path_output_error = "non_valid_orders.txt"
    orders_array_not_ru = []
    orders_array_ru = []
    orders_array = None

    input_array = None

    def read_order(self):
        """массив из массивов"""
        file = open(self.path_input, "r", encoding="utf-8")
        lines = file.readlines()
        file.close()
        array = []
        for line in lines:
            array.append(line.split(";"))
        self.input_array = array

    def clear_error_file(self):
        file = open(self.path_output_error, "w", encoding="utf-8")
        file.write("")
        file.close()

    def sort(self):
        """Быстрая сортировка сначала по priority, затем по country"""

        def swap(array, i, j):
            array[i], array[j] = array[j], array[i]

        def partition_country(array, left, right):
            x = array[left].order_country
            less_then = left
            grow_then = right
            i = left + 1

            while i <= grow_then:
                if array[i].order_country < x:
                    swap(array, less_then, i)
                    less_then += 1
                    i += 1
                elif array[i].order_country > x:
                    swap(array, grow_then, i)
                    grow_then -= 1
                else:
                    i += 1
            return grow_then, less_then

        def partition_prioritet(array, left, right):
            x = array[left].order_prioritet
            less_then = left
            grow_then = right
            i = left + 1

            while i <= grow_then:
                if array[i].order_prioritet < x:
                    swap(array, less_then, i)
                    less_then += 1
                    i += 1
                elif array[i].order_prioritet > x:
                    swap(array, grow_then, i)
                    grow_then -= 1
                else:
                    i += 1
            return grow_then, less_then

        def quicksort_prioritet(array, left, right):
            if len(array) == 0:
                return
            if left < right:
                grow_then, less_then = partition_prioritet(array, left, right)
                quicksort_prioritet(array, left, less_then - 1)
                quicksort_prioritet(array, grow_then + 1, right)

        def quicksort_country(array, left, right):
            if len(array) == 0:
                return
            if left < right:
                grow_then, less_then = partition_country(array, left, right)
                quicksort_country(array, left, less_then - 1)
                quicksort_country(array, grow_then + 1, right)

        def quicksort(array, left, right):
            quicksort_prioritet(array, left, right)
            quicksort_country(array, left, right)

        quicksort(self.orders_array_not_ru, 0, len(self.orders_array_not_ru) - 1)
        quicksort_prioritet(self.orders_array_ru, 0, len(self.orders_array_ru) - 1)
        self.orders_array = self.orders_array_ru + self.orders_array_not_ru

    def __init__(self, from_file=True, array=None):
        self.orders_array_not_ru = []
        self.orders_array_ru = []
        self.orders_array = None

        if from_file:
            self.read_order()
            self.clear_error_file()
        else:
            self.input_array = array

        for order in self.input_array:
            order_elem = self.Order(order)

            if order_elem.is_valid:
                if order_elem.order_country == "Россия":
                    self.orders_array_ru.append(order_elem)
                else:
                    self.orders_array_not_ru.append(order_elem)
            else:
                if from_file:
                    file = open(self.path_output_error, "a", encoding="utf-8")
                    file.write(order_elem.error_text)
                    file.close()

        self.sort()

        if from_file:
            self.write()

    def info(self):
        """id, counry, priority"""
        for order in self.orders_array:
            print(order.order_id, order.order_country, order.order_prioritet)


    def write(self):
        """
        Формат сохранения:
        <Номер заказа>;
        <Набор продуктов>;
        <ФИО заказчика>;
        <Адрес доставки>;
        <Номер телефона>;
        <Приоритет доставки>
        """
        with open("order_country.txt", "w", encoding="utf-8") as file:
            file.write("")

        with open("order_country.txt", "a", encoding="utf-8") as file:
            for order in self.orders_array:
                if order.order_prioritet == 0:
                    prioritet = "MAX"
                elif order.order_prioritet == 1:
                    prioritet = "MIDDLE"
                else:
                    prioritet = "LOW"
                answer_line = f"{order.order_id};{order.order_products};{order.order_name};{order.order_adress_without_country};{order.order_phone_number};{prioritet}\n"

                file.write(answer_line)

    class Order:
        """класс отдельного заказа"""
        order_id = None
        order_products = None
        order_name = None
        order_adress = None
        order_phone_number = None
        order_prioritet = None
        order_country = None
        order_adress_without_country = None

        is_valid = None
        error_text = ""

        path_output_error = "non_valid_orders.txt"

        def error_write(self, error_id, error_text):
            """error_id - 0:no error; 1: adress; 2:phone"""

            if error_text == "":
                error_text = "no data"
            self.error_text += f"{self.order_id};{error_id};{error_text}\n"

        def check_errors(self):
            """
            ___Адрес доставки___ == ___<Страна>. <Регион>. <Город>. <Улица>___.
            ___Номер телефона___ - == +x-xxx-xxx-xx-xx, где x - любая цифра 0-9
            """

            address_pattern = r"^[^.]+\. [^.]+\. [^.]+\. [^.]+$"

            phone_pattern = r"^\+\d-\d{3}-\d{3}-\d{2}-\d{2}$"

            is_address_valid = re.match(address_pattern, self.order_adress) is not None
            is_phone_valid = re.match(phone_pattern, self.order_phone_number) is not None

            if not is_address_valid:
                self.error_write(1, self.order_adress)
            if not is_phone_valid:
                self.error_write(2, self.order_phone_number)

            self.is_valid = is_address_valid and is_phone_valid

        def __init__(self, array):
            """массив из read_order"""

            if len(array) != 6:
                print("error len order_array")

            self.order_id = array[0]
            self.order_products = array[1]
            self.order_name = array[2]
            self.order_adress = array[3]
            self.order_phone_number = array[4]

            if "MAX" in array[5]:
                self.order_prioritet = 0
            elif "MIDDLE" in array[5]:
                self.order_prioritet = 1
            else:
                self.order_prioritet = 2

            self.check_errors()
            if self.is_valid:
                self.order_country = self.order_adress.split(".")[0]
                self.order_adress_without_country = self.order_adress[len(self.order_country) + 2:]



if __name__ == '__main__':
    Shop()
