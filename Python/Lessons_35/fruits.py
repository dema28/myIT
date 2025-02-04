import json
def fruit_favorites(fruit_list, file_new):
    fruit_list = '{ "apple": 10, "banana": 20, "cherry": 15, "date": 5, "orange": 8}'
    with open(f"{fruit_list}.json", "w") as file_new:
        json.dump(fruit_list, file_new)
create_fruit(fruit)



