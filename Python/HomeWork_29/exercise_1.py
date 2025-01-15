number = input("Ведите двузначное число: ")
if (number.isdigit()) and len(number) == 2 or (number.startswith('-') and number[1:].isdigit() and len(number) == 3):
    if number.startswith('-'):
        print('-')
        print(number[1])
        print(number[2])
    else:
        print(number[0])
        print(number[1])
else:
    print("Введено неверное число.")