"""Создайте функцию factorial , которая принимает число и возвращает его
факториал. Используйте цикл для вычисления факториала.
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120
print(factorial(10))  # Output: 3628800
print(factorial(0))  # Output: 1
print(factorial(1))  # Output: 1
print(factorial(20))  # Output: 2432902008176640000
print(factorial(-5))  # Output: "Error: Factorial is not defined for negative numbers"