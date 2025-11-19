# Define a function f(number) that returns the sum of repeated digits in a number. Sample result:
# f(1027) returns 0
# f(230335) returns 9
# f(513553007) returns 21

def f(number: int) -> int:
    sum = 0
    s = str(number)
    for i in s:
        if s.count(i) > 1:
            sum += int(i)        
    return sum 

print(f(1027))
print(f(230335))
print(f(513553007))