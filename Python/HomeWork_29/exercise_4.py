
print("Выберите шкалу для ввода температуры:")
print("1 - Градусы Цельсия")
print("2 - Градусы Фаренгейта")
choice = input("Введите 1 или 2: ")

if choice == "1":
    celsius = input("Введите температуру в градусах Цельсия: ")
    try:
        celsius = float(celsius)
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius} градусов Цельсия соответствует {fahrenheit} градусам Фаренгейта.")
    except ValueError:
        print("Пожалуйста, введите корректное числовое значение.")
elif choice == "2":
    fahrenheit = input("Введите температуру в градусах Фаренгейта: ")
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit} градусов Фаренгейта соответствует {celsius} градусам Цельсия.")
    except ValueError:
        print("Пожалуйста, введите корректное числовое значение.")
else:
    print("Неверный выбор. Пожалуйста, запустите программу снова и выберите 1 или 2.")
