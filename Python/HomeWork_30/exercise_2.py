"""
Пользователь вводит с клавиатуры номер месяца (1-12). Необходимо вывести на
экран название месяца. Например, если 1, то на экране надпись январь, 2 —
февраль и т.д.
"""

month_number = int(input("Введите номер месяца: "))

if month_number == 1:
    print("Январь")
elif month_number == 2:
    print("Февраль")
elif month_number == 3:
    print("Март")
elif month_number == 4:
    print("Апрель")
elif month_number == 5:
    print("Май")
elif month_number == 6:
    print("Июнь")
elif month_number == 7:
    print("Июль")
elif month_number == 8:
    print("Август")
elif month_number == 9:
    print("Сентябрь")
elif month_number == 10:
    print("Октябрь")
elif month_number == 11:
    print("Ноябрь")
elif month_number == 12:
    print("Декабрь")
else:
    print("Введено неверное число")