
def user():
    element = [1, 2, 3, 4, 5, 6, 7]

    try:
        index = int(input("Введите индекс: "))
        number = element[index]
        print(f"Элемент с индексом {index}: {number}")
    except ValueError:
        print("Ошибка: Индекс должен быть числом.")
    except IndexError:
        print("Ошибка: Индекс выходит за пределы списка.")
    return element

elements = user()














