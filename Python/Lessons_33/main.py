# """ Прветствие по времени суток. Напишите функцию geet by time которая принимает имя и текущие время
# и выводит приветствие в зависимости от текущего часа суток. (в формате 24 часа)
# 1. Если время с 6 до 12 то "доброе уторо"
# 2. Если время с 12 до 18 то "добрый день"
# 3. Если время с 18 до 6 то "добрый вечер"
# В остальных случаях "Доброй ночи"
#
# Пример:
# get_greeting_by_time("Иван", "15:30") => "Добрый день, Иван!"
# get_greeting_by_time("Петр", "23:45") => "Доброй ночи, Петр!"
# get_greeting_by_time("Людмила", "08:15") => "Доброе утро, Людмила!"
# """

#
# def greet_by_time(name, current_time):
#     hour, minute = map(int, current_time.split(':'))
#     if 6 <= hour <= 12:
#         print(f"Доброе утро, {name}!")
#     elif 12 <= hour <= 18:
#         print(f"Добрый день, {name}!")
#     elif 18 <= hour <= 22 or 0 <= hour <= 6:
#         print(f"Добрый вечер, {name}!")
#     else:
#         print(f"Доброй ночи, {name}!")
#
# greet_by_time("Denis","8:15")
# greet_by_time("Guguta", "13:15")
# greet_by_time("Bob", "22:15")
# greet_by_time("Zhora", "23:15")
#
#
# print ("----------------------------------------------------------------")
#
#
# def greet_time (name, time):
#     hour = int(time)
#     if hour > 6 and hour < 12:
#         print(f"Доброе утро, {name}!")
#     elif hour > 12 and hour < 18:
#         print(f"Добрый день, {name}!")
#     elif hour > 18  and hour < 22:
#         print(f"Добрый вечер, {name}!")
#     else:
#         print(f"Доброй ночи, {name}!")
#
# greet_time("Denis", 8)
# greet_time("Guguta", 13)
# greet_time("Bob", 21)
# greet_time("Zhora", 23)
#
#
# # """ Таблица умножения. Создайте функцию multiplication table
# # которая принимает число n от пользователя и выводит таблицу умножения для этого числа от 1 до 10"""
# #
# #
# def multiplication_table(n):
#     for i in range(1, 11):
#         print(f"{n} * {i} = {n * i}")
#     print("--------------------------------------")
#     print("Таблица умножения создана")
#
# multiplication_table(4)
# greet_time("zoration",5)
#
# print("--------------------------------------")


"""Проверка простого числа напишите функцию is_prime которая принимает число и
возвращает True если ого простое и False в противном случае"""



# def is_prime(n):
#     # n = int(input("Введите число: "))
#     # if n <= 1:
#     #     return False
#     # if n == 2:
#     #     return True
#     return n % 2 == 0
#     #     return False
#     # return True
#
# print(is_prime(2))


def revers_list(list):
    reversed_list = list[::-1]
    return reversed_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(revers_list(list))



def reverse_list(list):
    reversed_list = []
    for i in range(len(list) - 1, -1, -1):
        reversed_list.append(list[i])
    return reversed_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(reverse_list(list))



def reverse_pget(list):
    return list[::-1]

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(reverse_pget(list))



def reverse_list_in_place(list):
    list.reverse()
    return list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(reverse_list_in_place(list))

