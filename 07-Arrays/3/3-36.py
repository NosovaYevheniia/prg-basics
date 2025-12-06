def array_change(arr_2d:list):
    result_arr = []
    for row in arr_2d:
        for number in row:
            result_arr.append(number)
    return result_arr

if __name__ == "__main__":
    matrix1 = [
        [2, 3],
        [1, 5],
    ]
    matrix2 = [
        [5, 0, 3, 7, 5],
        [9, 0, 9, 1, 2]
    ]
    matrix3 = [
        [2, 1],
        [3, 5],
        [7, 4],
        [2, 6]
    ]

    matrix1_result = array_change(matrix1)
    print(matrix1_result)
    matrix2_result = array_change(matrix2)
    print(matrix2_result)
    matrix3_result = array_change(matrix3)
    print(matrix3_result)