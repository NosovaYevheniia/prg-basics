# The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given 
# string of digits is a valid binary number, or False otherwise. Sample result:
# f("101101") returns True
# f("1311a10100") returns False

def f(binary_number):
    for i in binary_number:
        if i not in ("0", "1"):
            return False
    return True
        
print(f("101101"))
print(f("1311a10100"))