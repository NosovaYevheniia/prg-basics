# In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a 
# boolean value. Then, create a program and use the function you defined. Sample result:
# A number: 7
# Number 7 in the range <2,15>: yes

def check(x: int, y: int, number: int) -> bool:
    arr = range(x, y+1)
    for i in arr:
        if i == number:
            return True
    return False

print(check(7, 5, 6))