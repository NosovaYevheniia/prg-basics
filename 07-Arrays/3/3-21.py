def check_array(arr1, arr2:list):
    for i in arr1:
        if arr2.count(i) == 0:
            return False
    return True

if __name__ == "__main__":
    x = check_array([1, 2, 3], [1, 2, 3])
    print(x)


