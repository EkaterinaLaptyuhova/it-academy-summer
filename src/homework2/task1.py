"""Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
   цена, а также количество S товара Посчитайте общую цену в рублях и копейках
   за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    totals: int = (m * 100 + n) * s
    return str(totals // 100) + ' rubles ' + str(totals % 100) + ' kopecks'  # write return value here


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m = int(input('rubles: '))
    n = int(input('kopeiki: '))
    s = int(input('kol-vo tovara: '))
    print(total_sum(m, n, s))
