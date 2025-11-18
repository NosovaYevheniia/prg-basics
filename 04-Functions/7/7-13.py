# Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
# f(11) returns "1234567891011"
# f(4) returns "1234"

def f(n: int) -> str:
    arr = range(1, n+1)
    result = ""
    for i in arr:
        result = result + str(i)
    return result 

print(f(11))
print(f(4))
