arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

def swap(arr:list):
    for row in arr:
        row_index = arr.index(row)
        temp = arr[row_index][0]
        arr[row_index][0] = arr[row_index][-1]
        arr[row_index][-1] = temp
    return arr

x = swap(arr)
print(x)