"""Создайте функцию print_numbers , которая принимает два числа start и end и
выводит все числа в указанном диапазоне. Если start > end , числа должны
выводиться в обратном порядке.
"""

def print_numbers(start, end):
    if start > end:
        for i in range(start, end - 1, -1):
            print(i)
    else:
        for i in range(start, end + 1):
            print(i)

print_numbers(10, 5)
print("--------------------------------")
print_numbers(5,10)

