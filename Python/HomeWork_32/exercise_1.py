"""
Создайте функцию greet , которая принимает имя пользователя и выводит
приветствие. Если имя не передано, должно выводиться "Hello, Guest!".
"""

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("Denis")
greet()