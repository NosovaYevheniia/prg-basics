def occurs(number: int, array:list):
    if number not in array:
        return False
    return True

if __name__ == "__main__":
    number_inp = int(input("Enter a number: "))
    array = [15, 38, 7, 23, 14]
    array_space = " ".join(map(str, array))
    result = occurs(number_inp, array)
    print(type(result))
    print(f"Number: {number_inp}")
    print(f"Array: {array_space}")
    if result:
        print(f"Result: number {number_inp} appears in the array")
    else:
        print(f"Result: number {number_inp} does not appear in the array")