""" Напишите программу, которая запрашивает у пользователя три числа.
2. Попробуйте найти их среднее значение.
3. Обработайте возможные ошибки, такие как некорректный ввод любого из чисел,
и выведите сообщение с указанием, какое именно число введено неправильно."""

def filter():
    try:
        number_1 = float(input("Введите первое число: "))
        number_2 = float(input("Введите второе число: "))
        number_3 = float(input("Введите третье число: "))

        full = (number_1 + number_2 + number_3) / 3

        print(f"Среднее значение чисел: {full}")
    except ValueError:
        print("Ошибка! Введено некорректное число.")
    except Exception:
        print("Произошла ошибка.")

full = filter()


def filter():
    try:
        numbers = [float(input(f"Введите число {i + 1}: ")) for i in range(3)]
        average = sum(numbers) / len(numbers)
        print(f"Среднее значение чисел: {average}")
    except ValueError:
        print("Ошибка! Введено некорректное число.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

full = filter()


