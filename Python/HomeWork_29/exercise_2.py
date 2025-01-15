number = input("Введите трёхзначное число: ")

if (number.isdigit() and len(number) == 3) or (number.startswith('-') and number[1:].isdigit() and len(number) == 4):
    abs_number = number[1:] if number.startswith('-') else number

    for digit in abs_number:
        print(digit)

    digit_sum = sum(int(digit) for digit in abs_number)
    if number.startswith('-'):
        digit_sum =- digit_sum

    print(digit_sum)
else:
    print("Bведите трёхзначное число.")
