""" Напишите программу, которая запрашивает у пользователя два числа и делит
одно на другое. Используйте try-except, чтобы обработать:
1. Ошибку, если введено не число.
2. Ошибку деления на ноль.
"""

def division():
    try:
        num1 = int(input("Введите 1-ое число: "))
        num2 = int(input("Введите 2-ое число: "))
        res = num1 / num2
        return res
    except ZeroDivisionError:
        print("Ошибка: деление на ноль.")
    except ValueError:
        print("Ошибка: введено не число.")
    finally:
        print("Программа завершена.")

result = division()
if result is not None:
    print(f"Результат деления: {result}")


