import json
with open('newJson.json', 'r') as json_file:
    load_json = json.load(json_file)
# name = load_json['data']['search']['edges'][0]['node']['id']
id = load_json['data']['search']['edges']
print(id)

