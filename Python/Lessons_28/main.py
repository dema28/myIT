# username = "admin"
# password = "123"
#
# input_username = input("Введите логин: ")
# input_password = input("Введите пароль: ")
#
# isUsernameCorrect = username == input_username
# isPasswordCorrect = password == input_password
#
# if isUsernameCorrect and isPasswordCorrect:
#     print("Вы успешно вошли в систему!")
# else:
#     print("Неправильный логин или пароль!")
#
#
# number = 12.2345694576483
# rounded_number = round(number, 3)
# print(rounded_number)


# age = 18
# has_ticket = True
#
# if age >= 18 and has_ticket:
#     print("Вы можете войти в кинотеатр.")
# else:
#     print("Вы не можете войти в кинотеатр.")

#
# age1 = 30
#
# if age1 >= 18 and age1 <= 21:
#     print("1")
# elif age1 >= 21:
#     print("2")
# elif age1 >= 30:
#     print("3")


# num = input("Введите число: ")
#
# if num >= 1:
#     print("число положительное")
# elif num < 0:
#     print("число отрицательное")
# else:
#     print("равно нулю")


# num = 15
#
# if num % 2 == 0:
#     print("число четное")
# else:
#     print("число нечетное")


age = 70

if age < 18:
    print("Вы несовершеннолетний.")
elif age < 65:
    print("Вы взрослый.")
else:
    print("Вы пенсионер.")



age = 20
has_permission = True

if age >= 18:
    if has_permission:
        print("Вы можете войти.")
    else:
        print("У вас нет разрешения.")
else:
    print("Вы несовершеннолетний.")



number = int(input("Введите число: "))

if number > 0:
    print("Число положительное.")
elif number < 0:
    print("Число отрицательное.")
else:
    print("Число равно нулю.")





