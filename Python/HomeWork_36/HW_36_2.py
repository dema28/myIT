"""Напишите калькулятор, который запрашивает у пользователя два числа и
операцию ( + , - , * , / ).
Пример работы:
Ошибка: Файл не найден!
Программа завершена.
Обработайте ошибки:
1. Если введено не число → вывести: Ошибка: Введите только числа!
2. Если неверная операция → вывести: Ошибка: Операция не
поддерживается!
3. Если деление на ноль → вывести "Ошибка: Деление на ноль
невозможно!"""


def calculator():
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        operation = input("Введите операцию (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль невозможно!")
            result = num1 / num2
        else:
            raise ValueError("Операция не поддерживается!")

        print(f"Результат: {result}")

    except ValueError as e:
        if "could not convert string to float" in str(e):
            print("Ошибка: Введите только числа!")
        else:
            print(f"Ошибка: {e}")

    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")

    finally:
        print("Программа завершена.")

calculator()




