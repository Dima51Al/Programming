""" калькулятор способен считать значения
многоступенчатых выражений по типу
(4234/(213+122*213)*213/(231-23*4))"""
def dell(string):
    """фукция деления"""
    return float(string.split("/")[0]) / float(string.split("/")[1])


def umn(string):
    """фукция умножения"""
    return float(string.split("*")[0]) * float(string.split("*")[1])


def summ(string):
    """ фукция суммирования"""
    return float(string.split("+")[0]) + float(string.split("+")[1])


def minus(string):
    """фукция вычетания"""
    return float(string.split("-")[0]) - float(string.split("-")[1])


def mega(string):
    """производит операцию над простым выражением (без скобок)"""
    left = 0
    right = 0
    while string.count("*") + string.count("/") > 0:

        if string[right] in "+-":
            right += 1
            left = right

        if string[right] == "/":
            right += 1

            if string[right] == "-":
                right += 1

            while string[right] in "0123456789.,":
                right += 1
                if len(string) == right:
                    break
            vir = dell(string[left:right])
            string = string[:left] + str(vir) + string[right:]

            right = 0
            left = 0
        if string[right] == "*":
            if string[right] == "-":
                right += 1
            right += 1
            while string[right] in "0123456789.,":
                right += 1
                if len(string) == right:
                    break
            vir = umn(string[left:right])
            string = string[:left] + str(vir) + string[right:]

            right = 0
            left = 0
        right += 1
    while (string.count("+") + string.count("-") - string[0].count("-")) > 0:

        if string[right] == "-":
            right += 1
            while string[right] in "0123456789.,":
                right += 1
                if len(string) == right:
                    break
            vir = minus(string[left:right])
            string = string[:left] + str(vir) + string[right:]

            right = 0
            left = 0
        if string[right] == "+":
            right += 1
            while string[right] in "0123456789.,":
                right += 1
                if len(string) == right:
                    break
            vir = summ(string[left:right])
            string = string[:left] + str(vir) + string[right:]

            right = 0
            left = 0
        right += 1
    return string


def algorithm(string):
    """алгоритм - ищет вложенные выражения и производит операции над ними"""
    while string.count("(") + string.count(")") > 0:
        left = 0
        right = 0
        while string[right] != ")":
            right += 1
            if string[right] == "(":
                left = right
        vir = mega(string[left + 1: right])
        string = string[:left] + str(vir) + string[right + 1:]
    return mega(string)


print(algorithm(input()))
