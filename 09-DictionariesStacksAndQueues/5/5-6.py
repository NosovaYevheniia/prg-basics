basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

person = {}
basic_data.update(advanced_data)
person.update(basic_data)
print(person)