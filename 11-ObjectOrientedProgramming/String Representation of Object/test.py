class Person:
    def __init__(self):
        self.name = "john doe"
        self.age = 24

    def __str__(self):
        return f"{self.name}, {self.age}"

person1 = Person()
print(person1)