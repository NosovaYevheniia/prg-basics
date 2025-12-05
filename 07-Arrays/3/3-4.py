arr = [-15, 8, -31, 47, -2, 19]
maximum = 0
minimum = 0
for i in arr:
    if i < minimum:
        minimum = i
    elif i > maximum:
        maximum = i
print(maximum)
print(minimum)