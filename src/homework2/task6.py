"""Определите, является ли число палиндромом (читается слева направо и справа
    налево одинаково).  Число положительное целое, произвольной длины. Задача
    требует работать только с числами (без конвертации числа в строку или
    что-нибудь еще)
"""


def palindrom(n):
    """Поиск числа фибоначчи.

    :param n: Число.
    :return: Bool. True или False. Является ли число палиндромом.
    """

    # write your code here
    if n < 0:
        return False

    duplicate = n
    reverse = 0
    while n > 0:
        reverse = reverse * 10 + (n % 10)
        n = n // 10
    return duplicate == reverse  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    n = int(input('Vvedite chislo: '))
    print(palindrom(n))
