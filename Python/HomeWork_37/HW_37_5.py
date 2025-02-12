"""Напишите программу, которая запрашивает у пользователя имя JSON файла.
Попробуйте открыть файл и загрузить данные из него с использованием
модуля json.
Обработайте возможные ошибки, такие как отсутствие файла или
неправильный формат JSON, и выведите соответствующее сообщение об
ошибке."""


import json

def load_json_file():
    file = input("Введите имя файла для чтения: ")
    try:
        with open(file, 'r') as file:
            data = json.load(file)
            print(f"Данные из файла '{file}':")
            # или так print(data) так будет в строчку
            print(json.dumps(data, indent=4))
            return data
    except PermissionError:
        print(f"Нет прав доступа к файлу '{file}'.")
        return None
    except FileNotFoundError:
        print(f"Файл '{file}' не найден.")
        return None
    except json.JSONDecodeError:
        print(f"Неверный формат JSON в файле '{file}'.")
        return None
    except Exception as e:
        print(f"Error'{file}': {str(e)}")
        return None

load_json_file()


