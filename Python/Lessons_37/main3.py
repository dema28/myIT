"""У вас есть JSON-файл users.json , который содержит информацию о
пользователях. Каждый пользователь имеет имя, возраст и адрес
электронной почты. Ваша задача — написать программу, которая:
1. Читает данные из файла.
2. Проверяет, что у каждого пользователя есть все три поля: имя, возраст
и адрес электронной почты.
3. Если какое-то поле отсутствует, программа должна сообщить об этом,
не прерывая работы"""

import json

def validate_user(user):
    errors = []
    if 'name' not in user:
        errors.append("отсутствует поле 'name'")
    if 'age' not in user:
        errors.append("отсутствует поле 'age'")
    if 'email' not in user:
        errors.append("отсутствует поле 'email'")
    return errors

def main():
    try:
        with open('new_file.json', 'r') as file:
            users = json.load(file)
    except FileNotFoundError:
        print("Файл 'new_file.json' не найден.")
        return
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON. Проверьте формат файла.")
        return

    for idx, user in enumerate(users, 1):
        errors = validate_user(user)
        if errors:
            print(f"Ошибки у пользователя {idx}: {', '.join(errors)}")
        else:
            print(f"Пользователь {idx}: все поля в порядке")

main()







