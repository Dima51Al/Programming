import unittest
from src.lab4.main import Shop


class CalculatorTestCase(unittest.TestCase):

    def test_should_order_init(self):
        #given
        order_array_1 = ['42856', 'Сыр, Яблоки, Вода, Хлеб', 'Соболева Мария Петровна', 'Япония. Токио. Гиндза',
                         '+8-3-234-56-78', 'LOW']
        order_array_2 = ['73241', 'Печенье, Макароны, Сок, Чай', 'Чернов Владимир Александрович',
                         'Испания. Валенсия. Пласа-де-ла-Рейна', '+34-96-1234-567', 'MIDDLE']
        order_array_3 = ['68592', 'Хлеб, Молоко, Кофе, Печенье', 'Романова Елена Николаевна',
                         'Германия. Франкфурт. Цайль', '+4-69-234-56-78', 'MAX']
        order_array_4 = ['53987', 'Яблоки, Чай, Сок, Колбаса', 'Семенова Татьяна Андреевна',
                         'Италия. Венеция. Сан-Марко', '+3-041-234-56-78', 'LOW']
        order_array_5 = ['84761', 'Вода, Сыр, Макароны, Печенье', 'Поляков Алексей Викторович',
                         'Франция. Париж. Монмартр', '+3-214-020-51-51', 'MIDDLE']

        #when
        order_1 = Shop.Order(order_array_1)
        order_2 = Shop.Order(order_array_2)
        order_3 = Shop.Order(order_array_3)
        order_4 = Shop.Order(order_array_4)
        order_5 = Shop.Order(order_array_5)

        # then
        self.assertEqual(order_1.order_id, '42856')
        self.assertEqual(order_1.order_products, 'Сыр, Яблоки, Вода, Хлеб')
        self.assertEqual(order_1.order_name, 'Соболева Мария Петровна')
        self.assertEqual(order_1.order_adress, 'Япония. Токио. Гиндза')
        self.assertEqual(order_1.order_phone_number, '+8-3-234-56-78')

        self.assertEqual(order_2.order_id, '73241')
        self.assertEqual(order_2.order_products, 'Печенье, Макароны, Сок, Чай')
        self.assertEqual(order_2.order_name, 'Чернов Владимир Александрович')
        self.assertEqual(order_2.order_adress, 'Испания. Валенсия. Пласа-де-ла-Рейна')
        self.assertEqual(order_2.order_phone_number, '+34-96-1234-567')

        self.assertEqual(order_3.order_id, '68592')
        self.assertEqual(order_3.order_products, 'Хлеб, Молоко, Кофе, Печенье')
        self.assertEqual(order_3.order_name, 'Романова Елена Николаевна')
        self.assertEqual(order_3.order_adress, 'Германия. Франкфурт. Цайль')
        self.assertEqual(order_3.order_phone_number, '+4-69-234-56-78')

        self.assertEqual(order_4.order_id, '53987')
        self.assertEqual(order_4.order_products, 'Яблоки, Чай, Сок, Колбаса')
        self.assertEqual(order_4.order_name, 'Семенова Татьяна Андреевна')
        self.assertEqual(order_4.order_adress, 'Италия. Венеция. Сан-Марко')
        self.assertEqual(order_4.order_phone_number, '+3-041-234-56-78')

        self.assertEqual(order_5.order_id, '84761')
        self.assertEqual(order_5.order_products, 'Вода, Сыр, Макароны, Печенье')
        self.assertEqual(order_5.order_name, 'Поляков Алексей Викторович')
        self.assertEqual(order_5.order_adress, 'Франция. Париж. Монмартр')
        self.assertEqual(order_5.order_phone_number, '+3-214-020-51-51')

    def test_should_check_address_errors(self):
        # given
        order_array_1 = ['42856', 'Сыр, Яблоки, Вода, Хлеб', 'Соболева Мария Петровна', 'Япония. Токио. Гиндза',
                         '+8-3-234-56-78', 'LOW']
        order_array_2 = ['73241', 'Печенье, Макароны, Сок, Чай', 'Чернов Владимир Александрович',
                         'Испания. Валенсия. Пласа-де-ла-Рейна', '+34-96-1234-567', 'MIDDLE']
        order_array_3 = ['68592', 'Хлеб, Молоко, Кофе, Печенье', 'Романова Елена Николаевна',
                         'Германия. Франкфурт. Цайль', '+4-69-234-56-78', 'MAX']
        order_array_4 = ['53987', 'Яблоки, Чай, Сок, Колбаса', 'Семенова Татьяна Андреевна',
                         'Италия. Венеция. Сан-Марко', '+3-041-234-56-78', 'LOW']
        order_array_5 = ['84761', 'Вода, Сыр, Макароны, Печенье', 'Поляков Алексей Викторович',
                         'Франция. Париж. Монмартр', '+3-214-020-51-51', 'MIDDLE']

        # when
        order_1 = Shop.Order(order_array_1)
        order_2 = Shop.Order(order_array_2)
        order_3 = Shop.Order(order_array_3)
        order_4 = Shop.Order(order_array_4)
        order_5 = Shop.Order(order_array_5)

        #then
        """Везде неверный формат адресса"""
        self.assertFalse(order_1.is_valid)
        self.assertFalse(order_2.is_valid)
        self.assertFalse(order_3.is_valid)
        self.assertFalse(order_4.is_valid)
        self.assertFalse(order_5.is_valid)

    def test_should_check_phone_errors(self):
        # given
        order_array_1 = ['42856', 'Сыр, Яблоки, Вода, Хлеб', 'Соболева Мария Петровна', 'a. a. a. a',
                         '+8-3-234-56-78', 'LOW']
        order_array_2 = ['73241', 'Печенье, Макароны, Сок, Чай', 'Чернов Владимир Александрович',
                         'a. a. a. a', '', 'MIDDLE']
        order_array_3 = ['68592', 'Хлеб, Молоко, Кофе, Печенье', 'Романова Елена Николаевна',
                         'a. a. a. a', '+4-69f-234-56-78', 'MAX']
        order_array_4 = ['53987', 'Яблоки, Чай, Сок, Колбаса', 'Семенова Татьяна Андреевна',
                         'a. a. a. a', '- - - -', 'LOW']
        order_array_5 = ['84761', 'Вода, Сыр, Макароны, Печенье', 'Поляков Алексей Викторович',
                         'a. a. a. a', '+3-2df14-0210-51-51', 'MIDDLE']

        # when
        order_1 = Shop.Order(order_array_1)
        order_2 = Shop.Order(order_array_2)
        order_3 = Shop.Order(order_array_3)
        order_4 = Shop.Order(order_array_4)
        order_5 = Shop.Order(order_array_5)

        #then
        """Везде неверный формат телефонного номера"""
        self.assertFalse(order_1.is_valid)
        self.assertFalse(order_2.is_valid)
        self.assertFalse(order_3.is_valid)
        self.assertFalse(order_4.is_valid)
        self.assertFalse(order_5.is_valid)

    def test_should_check_country_sort(self):
        #given
        input_arr = [
            ['73241', 'Печенье, Макароны, Сок, Чай', 'Чернов Владимир Александрович',
             'a. a. a. a', '+3-960-214-12-75', 'MIDDLE'],
            [
                '68592', 'Хлеб, Молоко, Кофе, Печенье', 'Романова Елена Николаевна',
                'c. a. a. a', '+4-609-214-23-56', 'MAX'],
            [
                '53987', 'Яблоки, Чай, Сок, Колбаса', 'Семенова Татьяна Андреевна',
                'b. a. a. a', '+3-041-214-56-78', 'LOW'],
            [
                '84761', 'Вода, Сыр, Макароны, Печенье', 'Поляков Алексей Викторович',
                'd. a. a. a', '+3-214-214-51-51', 'MIDDLE']
        ]

        shop = Shop(from_file=False, array=input_arr)
        #when
        A = shop.orders_array[0].order_country
        B = shop.orders_array[1].order_country
        C = shop.orders_array[2].order_country
        D = shop.orders_array[3].order_country

        #then
        self.assertTrue(A <= B)
        self.assertTrue(B <= C)
        self.assertTrue(C <= D)


    def test_should_check_prioritet_sort(self):
        #given
        input_arr = [
            [
                '73241', 'Печенье, Макароны, Сок, Чай', 'Чернов Владимир Александрович',
                'a. a. a. a', '+3-960-214-12-75', 'MIDDLE'],
            [
                '68592', 'Хлеб, Молоко, Кофе, Печенье', 'Романова Елена Николаевна',
                'a. a. a. a', '+4-609-214-23-56', 'MAX'],
            [
                '53987', 'Яблоки, Чай, Сок, Колбаса', 'Семенова Татьяна Андреевна',
                'a. a. a. a', '+3-041-214-56-78', 'LOW']
        ]
        shop = Shop(from_file=False, array=input_arr)

        #when
        shop.info()
        A = shop.orders_array[0].order_prioritet
        B = shop.orders_array[1].order_prioritet
        C = shop.orders_array[2].order_prioritet

        #then
        self.assertTrue(A <= B)
        self.assertTrue(B <= C)



if __name__ == '__main__':
    unittest.main()
