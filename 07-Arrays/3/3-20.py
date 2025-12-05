def numbers(arr:list):
    even_arr = []
    odd_arr = []
    for number in arr:
        if number%2 != 0:
            odd_arr.append(number)
            print(odd_arr)
        else:
            even_arr.append(number)
            print(even_arr)
    return even_arr + odd_arr
    
if __name__ == "__main__":
    arr = [7,9,2,4,5,6]
    x = numbers(arr)
    print(x)
    
# arr = [2,4,6,7,9,5]