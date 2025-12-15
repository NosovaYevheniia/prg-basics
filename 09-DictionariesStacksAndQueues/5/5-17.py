import json

with open("cities.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for cities in data:
    for key,value in cities.items():
        print(f"{key}:{value}")