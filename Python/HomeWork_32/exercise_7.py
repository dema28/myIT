"""Напишите функцию even_numbers_in_range , которая принимает два числа и
возвращает список всех четных чисел в указанном диапазоне."""

def even_numbers_in_range(start, end):
    return [num for num in range(start, end + 1) if num % 2 == 0]

print(even_numbers_in_range(1, 10))  # [2, 4, 6, 8, 10]
print(even_numbers_in_range(5, 15))  # [6, 8, 10, 12, 14]
print(even_numbers_in_range(0, 20))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print(even_numbers_in_range(10, 0))  # [] (нет четных чисел в этом диапазоне)

