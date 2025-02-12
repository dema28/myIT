# import json
#
# def studentsBall(grades):
#     return sum(grades) / len(grades)
#
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
#
# with open('students.json', 'r') as json_file:
#     data = json.load(json_file)
#     print(data)
#
#     print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
#
#     if 'students' in data:
#         for student in data['students']:
#             name = student['name']
#             grades = student['grades']
#             aver_grade = studentsBall(grades)
#             print(f"Имя студента: {name}, \nСредний балл: {aver_grade:.2f}")
#     else:
#         print("Ключ 'students' отсутствует в JSON-файле")
#
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

import json


def studentsBall(grades):
    if not grades:
        raise ValueError("Оценки отсутствуют")
    return sum(grades) / len(grades)


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

try:
    with open('students.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)

        print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

        if 'students' in data:
            for student in data['students']:
                try:
                    name = student.get('name', 'Неизвестный студент')
                    grades = student.get('grades', [])

                    aver_grade = studentsBall(grades)
                    print(f"Имя студента: {name}, \nСредний балл: {aver_grade:.2f}")
                except ValueError as e:
                    print(f"Имя студента: {name}, \nОшибка: {e}")
                except Exception as e:
                    print(f"Имя студента: {name}, \nОшибка при обработке данных: {e}")
        else:
            print("Ключ 'students' отсутствует в JSON-файле")

except FileNotFoundError:
    print("Ошибка: Файл 'students.json' не найден.")
except json.JSONDecodeError:
    print("Ошибка: Файл 'students.json' содержит некорректный JSON.")
except Exception as e:
    print(f"Произошла ошибка: {e}")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")