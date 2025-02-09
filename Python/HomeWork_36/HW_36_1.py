"""Напишите программу, которая открывает файл data.txt, читает и выводит
его содержимое. Если файла нет, обработайте ошибку и выведите "Файл не найден!" .
Используйте finally, чтобы программа завершалась корректно.
"""

try:
    with open("data.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Файл не найден!")
finally:
    print("Программа завершена.")