countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Vatican", "population":800},
    {"name":"Jamajka", "population":2839000},
    {"name":"Djibouti", "population":31168722},
    {"name":"Oman", "population":5494691},
]
print("COUNTRY", "POPULATION")
for country in countries:
    print((country["name"]), (country["population"]))