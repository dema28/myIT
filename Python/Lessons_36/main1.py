import  json

try:
    with open('inventory.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
except Exception as e:
    print(f"Ошибка при чтении файла: {str(e)}")
