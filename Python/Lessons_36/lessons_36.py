age = 20

if age >= 18:
   print("Вы можете войти.")
else:
    print("Вы несовершеннолетний.")

status = "соверщенолетний" if age >= 18 else "несовершенолетний"
print(f"Ваш возраст {status}.")

a, b  = 10, 20


if a > b:
    max_v = a
else:
    max_v = b

max_v = a if a>b else b

