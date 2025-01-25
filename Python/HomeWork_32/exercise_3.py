""" Создайте функцию is_even , которая принимает одно число и возвращает True ,
если число четное, и False в противном случае.
"""

def is_even(number):
    return number % 2 == 0

print(is_even(10))  # True
print(is_even(7))  # False
print(is_even(0))  # True
print(is_even(-5))  # False
print(is_even(2.5))  # False (число не является целым)
print(is_even(-3.7))  # False (число не является целым)
