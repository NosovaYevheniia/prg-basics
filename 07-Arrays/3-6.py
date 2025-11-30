arr = [15, 8, 31, 47, 2, 19]

def count_arithmetic_mean(arr):
    length = len(arr)
    print(length)
    sum = 0
    index = 0
    while length > 0:
        sum += arr[index]
        print(sum)
        length -= 1
        # print(length)
        index += 1
    arithmetic_mean = sum / len(arr)
    return arithmetic_mean

x = count_arithmetic_mean(arr)
print(x)
print(arr)
