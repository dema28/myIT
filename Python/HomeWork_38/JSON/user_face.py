from file import load_users


def display_users():
    users = load_users()
    if users:
        print("\nСписок пользователей:")
        for user in users:
            print(f"{user['id']}: {user['name']}")
    else:
        print("Файл users.json пуст или не найден.")


def get_user_by_id():
    users = load_users()
    if not users:
        print("Нет данных для поиска.")
        return

    try:
        user_id = int(input("\nВведите ID пользователя: "))
        user = next((user for user in users if user["id"] == user_id), None)

        if user:
            print("\nИнформация о пользователе:")
            print(f"Имя: {user['name']}")
            print(f"Email: {user['email']}")
            print(f"Телефон: {user['phone']}")
            print(f"Компания: {user['company']['name']}")
            print(f"Адрес: {user['address']['street']}, {user['address']['city']}")
        else:
            print("Пользователь с таким ID не найден.")
    except ValueError:
        print("Ошибка: введите числовое значение ID.")
