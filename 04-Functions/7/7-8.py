# The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay 
# for the purchased product. Sample result:
# f(23) returns 6
# f(8) returns 3
# f(2) returns 1
# f(0) returns 0

def f(amount_to_pay: int) -> int:
    coins = [5, 2, 1]
    count = 0
    for i in coins:
        count = count + amount_to_pay // i
        amount_to_pay = amount_to_pay % i
    return count

if __name__ == "__main__":
    print(f(23))
    print(f(8))
    print(f(2))
    print(f(0))