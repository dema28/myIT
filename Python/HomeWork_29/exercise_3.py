
num1 = input("Введите первую цифру: ")
num2 = input("Введите вторую цифру: ")

if num1.isdigit() and num2.isdigit():
    number = int(num1 + num2)
    print("Склееное число:", number)
else:
    print("Пожалуйста, введите только цифры.")
