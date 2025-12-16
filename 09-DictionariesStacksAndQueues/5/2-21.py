import json

fav_book = {"Author":'Anna',
            "Pages":205,
            "Title":"Cat",
            "Co-author":"John"}

file_name = "favourite.json"

with open(file_name, "w", encoding="utf-8") as file:
    json.dump(fav_book, file, indent=4)

print("Data saved to", file_name)