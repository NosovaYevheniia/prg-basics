import json

with open("dogs.json", "r", encoding="utf-8") as file:
    content = json.load(file)

for dogs in content:
    if dogs["age"] < 5:
        print(dogs)