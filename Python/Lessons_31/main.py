# """
# пользователь вводит 6 значное число, необходимо поменять в этом числе первую и шестую цифры,
# а также вторую и пятую.
# Если пользователь ввел не правильное число или текст следует вывести ошибку
# """

# number = input("Введите шестизначное число: ")
#
# if len(number) == 6 and number.isdigit():
#
#     first_digit = number[0]
#     second_digit = number[1]
#     third_digit = number[2]
#     fourth_digit = number[3]
#     fifth_digit = number[4]
#     sixth_digit = number[5]
#
#     number = sixth_digit + second_digit + third_digit + first_digit + fifth_digit + fourth_digit
#     print(f"Поменянное число: {number}")
# while len(number) != 6 or not number.isdigit():
#     print("Введено не правильное число.")
#     break
#
#
# """
# Выводить сообщение пока чило не бедет равно 6 знакам
# """

# number = input("Введите шестизначное число: ")
#
# while len(number)!= 6 or not number.isdigit():
#     print("Введено не правильное число.")
#
#     number = input("Введите шестизначное число: ")


# s = "1234"
# print(s.isdigit())
#
# s = "Hello"
# print(len(s))

"""
Напишите программу, которая:
Запрашивает у пользователя два целых числа.
Проверяет корректность ввода чисел (числа должны быть целыми). Если
ввод некорректный, программа повторно запрашивает число, пока
пользователь не введет правильное значение.
2. После успешного ввода:
Программа определяет диапазон между этими числами (включительно).
Если первое число меньше или равно второму, числа выводятся в
порядке возрастания.
Если первое число больше второго, числа выводятся в порядке убывания.

"""

# while True:
#     number_1 = input("Введите первое целое число: ")
#     number_2 = input("Введите второе целое число: ")
#
#     if number_1.isdigit() and number_2.isdigit():
#         number_1 = int(number_1)
#         number_2 = int(number_2)
#
#         if number_1 <= number_2:
#             for i in range(number_1, number_2 + 1):
#                 print(i)
#         else:
#             for i in range(number_1, number_2 - 1, -1):
#                 print(i)
#         break
#     else:
#         print("Введено некорректное число. Введите целые числа.")


while True:
    number_1 = input("Введите целое число: ")
    if number_1.isdigit():
        number_1 = int(number_1)
        break
    else:
        print("Введено некорректное число. Введите целое число.")

while True:
    number_2 = input("Введите целое число: ")
    if number_2.isdigit():
        number_2 = int(number_2)
        if number_1 <= number_2:
            for i in range(number_1, number_2 + 1):
                print(i)
        else:
            for i in range(number_1, number_2 - 1, -1):
                print(i)
        break
    else:
        print("Введено некорректное число. Введите целое число.")

























