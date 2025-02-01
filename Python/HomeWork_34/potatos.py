def cook_potatoes(potatoes, spice):
    print(f"1. Очистите и нарежьте {potatoes} картошки.")
    print("2. Разогрейте масло на сковороде.")
    if potatoes <= 2:
        print("3. Жарьте 10-15 мин.")
    elif 3 <= potatoes <= 5:
        print("3. Жарьте 15-20 мин.")
    else:
        print("3. Жарьте 20-25 мин.")

    spices = {
        "паприка": "добавьте паприку.",
        "чеснок": "добавьте чеснок.",
        "перец": "добавьте черный молотый перец."
    }
    print(f"4. Посолите и {spices.get(spice, 'добавьте специи.')}")
    print("5. Украсить зеленью.")

cook_potatoes(potatoes=3, spice="паприка")