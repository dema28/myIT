year = int(input("Год: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("год високосный")
        else:
            print("год не високосный")
    else:
        print("год високосный")
else:
    print("год не високосный")


year = int(input("Год: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("год високосный")
else:
    print("год не високосный")