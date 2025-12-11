employees = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

result = list(map(lambda employees: f"{employees[0].upper()}, {employees[1]}", employees))

for employees in result:
    print(employees)