"""Напишите функцию reverse_string , которая принимает строку и возвращает ее в
обратном порядке.
"""

def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

print(reverse_string("Hello World"))  # Output: dlroW olleH
print(reverse_string("Python"))  # Output: nohtyP
print(reverse_string("1234567890"))  # Output: 0987654321
print(reverse_string("!@#$%^&*()"))  # Output: )*(&^%$#@!
