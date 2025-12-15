import json

with open("voting.json", "r", encoding="utf-8") as file:
    content = json.load(file)

for key,value in content.items():
    print(f"{key}:{value}")