# Define the function f(number1,number2,number3), which returns the difference between the largest and smallest 
# numbers. Sample result:
# f(7,4,9) returns 5
# f(2,12,8) returns 10

def f(number1: int, number2: int, number3: int) -> int:
    max_value = max(number1,number2, number3)
    min_value = min(number1, number2, number3)
    return max_value - min_value

if __name__ == "__main__":
    print(f(5, 6, 8))
    print(f(5, 8, 3))