# Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns 
# the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:
# f(3124,True) returns 6
# f(3124,False) returns 4
# f(20576,False) returns 12
# f(20576,True) returns 8
# f(13115,True) returns 0

def f(number: int, even:bool) -> int:
    result = 0
    s = str(number)
    for i in s:
        if even is True:
            if int(i) % 2 == 0:
                result = result + int(i)
        elif even is False:
            if int(i) % 2 != 0:
                result = result + int(i)
    return result

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))