import requests
import json
# import os
#
# os.mkdir("test")


# response = requests.get('http://api.github.com/')
# data = response.json()
#
# print(response.status_code)
# print(response.json().get('warnings'))
# if response.status_code == 200:
#     print('Request successful')
#     print(data)


url = "https://jsonplaceholder.typicode.com/users"

# GET request
response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    for user in user:
        print(f"User ID: {user['id']}, Name: {user['name']}, Email: {user['email']}")
else:
    print("Error:", response.status_code)