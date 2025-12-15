import json


# Read the contents of the json file
with open("voting.json", "r", encoding="utf-8") as file:
    # voting = {"Anna":5}
    # json.dump(voting, file)
    # file.close()
    content = json.load(file)
    print(content)

# Vote for a person
person_name = input('Name of the person you are voting for: ')
if person_name in content:
    content[person_name] += 1
else:
    content[person_name] = 1


# Save voting data to json file
with open("voting.json", "w", encoding="utf-8") as file:
    json.dump(content, file)
print(content)
