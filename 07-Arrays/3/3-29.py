def create_2d_arr(x:int,y:int):
    zero_array = []
    for i in range(x):
        print(i)
        zero_array.append([])
        for number in range(y):
            print(i, number)
            zero_array[i].append(0)
    return zero_array


if __name__ == "__main__":
    x = create_2d_arr(3, 5)
    print(x)