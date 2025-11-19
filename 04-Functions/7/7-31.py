# Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 5**3.
# Tip: x**n = x * x**(n-1)

def power(x: int, n: int) -> int:
    if n == 0:
        return 1
    return x * power(x, n-1)
    
if __name__ == "__main__":
    print(power(5, 3))