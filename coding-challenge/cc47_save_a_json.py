import json

def save_json(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

def read_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

names = {'name': 'Carol', 'sex': 'female', 'age': 55}

save_json(names)
output = read_json()
print(output)