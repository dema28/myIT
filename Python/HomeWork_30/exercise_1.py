"""
Пользователь вводит с клавиатуры номер дня недели (1-7). Необходимо вывести
на экран названия дня недели. Например, если 1, то на экране надпись
понедельник, 2 — вторник и т.д
"""

day_to_week = int(input("Введите номер дня недели (1-7): "))

if day_to_week == 1:
    print("Понедельник")
elif day_to_week == 2:
    print("Вторник")
elif day_to_week == 3:
    print("Среда")
elif day_to_week == 4:
    print("Четверг")
elif day_to_week == 5:
    print("Пятница")
elif day_to_week == 6:
    print("Суббота")
elif day_to_week == 7:
    print("Воскресенье")
else:
    print("Некорректный номер дня недели")

