"""Создайте функцию greet_names , которая принимает список имен и для каждого
имени выводит приветствие."""

def greet_names(names):
    for name in names:
        print(f"Hello, {name}!")

greet_names(["Alice", "Bob", "Charlie"])

