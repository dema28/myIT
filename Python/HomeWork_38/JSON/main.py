from data_api import fetch_users
from file import save_users
from user_face import display_users, get_user_by_id

def main():
    print("Получение данных о пользователях...")
    users = fetch_users()
    if users:
        save_users(users)
        print("Данные сохранены в users.json")

    while True:
        print("\nМеню:")
        print("1. Показать всех пользователей")
        print("2. Найти пользователя по ID")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            display_users()
        elif choice == "2":
            get_user_by_id()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

main()
