arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(5):
    for number in range(5):
        arr[0][number] = number + 1
        arr[1][number] = number * 2
    
for row in arr:
    for i in row:
        print(i, end=" ")