# Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:
# f(4) returns "*/*/*/*"
# f(1) returns "*"

def f(n: int) -> str:
    if n == 1:
        return "*"
    return "/".join("*"*n)

if __name__ == "__main__":
    print(f(4))
    print(f(1))