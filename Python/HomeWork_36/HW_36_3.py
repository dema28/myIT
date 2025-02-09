"""Использование as
Напишите код, который:
Пытается преобразовать строку в число ( int() ).
Если возникает ошибка, перехватывает её в except as e и выводит текст
ошибки.
Введите число: abc
Ошибка: invalid literal for int() with base 10: 'abc'
"""

try:
    number = int(input("Введите число: "))
except ValueError as e:
    print(f"Ошибка: {str(e)}")
finally:
    print("Программа завершила работу.")
