#subtract one from the first element of the array
#increase the last array element by 4
#multiple the middle array element by 2

Array = [1,2,3,4,5]
# Array2 = [0,2,3,4,5]
# Array3 = [0,2,3,4,9]
# Array5 = [0,2,6,4,9]

print(Array)
Array[0] = Array[0] - 1
print(Array)
Array[-1] = Array[-1] + 4
print(Array)
middleIndex = len(Array)//2
Array[middleIndex] = Array[middleIndex] * 2
# print(len(Array)//2)
# len(Array)//2 = len(Array)//2 * 2
print(Array)