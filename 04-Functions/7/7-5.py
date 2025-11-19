import module_numbers

if __name__ == "__main__":
    number = int(input("Write 1st range number: "))
    number2 = int(input("Write 2nd range number: "))
    number3 = int(input("Write number: "))
    result = module_numbers.check(number, number2, number3)
    print(f"Number {number3} in the range {result}")