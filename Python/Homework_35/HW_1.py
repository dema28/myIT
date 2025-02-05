import json

def studentsBall(grades):
    return sum(grades) / len(grades)

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")

with open('students.json', 'r') as json_file:
    data = json.load(json_file)
    print(data)

    print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    if 'students' in data:
        for student in data['students']:
            name = student['name']
            grades = student['grades']
            aver_grade = studentsBall(grades)
            print(f"Имя студента: {name}, \nСредний балл: {aver_grade:.2f}")
    else:
        print("Ключ 'students' отсутствует в JSON-файле")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
