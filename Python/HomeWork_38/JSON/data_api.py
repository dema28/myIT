import requests

URL = "https://jsonplaceholder.typicode.com/users"

def fetch_users():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка при получении данных:", response.status_code)
        return []
