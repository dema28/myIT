# def greet(name):
#     return f"Привет {name}!"
#
# def add(a,b):
#     return a + b




# try:
#     numbers = int(input("Введите число: "))
#     result = 10 / 0
#     print(f"Ваше чило: {numbers}")
# except ValueError:
#     print("Ошибка при выполнении операции сложения.")
# except ZeroDivisionError:
#     print("Ошибка: деление на ноль.")


    # try:
    #     file = open("exemple.txt", "r")
    #     content = file.read()
    #     print("Файл открыт успешно.")
    # except FileNotFoundError:
    #     print("Ошибка при открытии файла.")
    # finally:
    #     print("всегда будет выполнятся")


# try:
#     numbers = int(input("Number:"))
#     res = 10 / 0
# except Exception as e:
#     print(f"Ошибка: , {e}")


def add():
    try:
        a = 10
        b = "20"
        return a + b
    except TypeError as e:
        return f"Ошибка при выполнении операции сложения: {e}"