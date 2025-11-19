# A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns 
# True if the expression is a palindrome or False otherwise. Sample result:
# f("radar") returns True
# f("12-11-21") returns True
# f("book") returns False

def f(palindrome: str) -> bool:
    left = 0
    right = len(palindrome) - 1
    while (left < right):
        print(left)
        print(right)
        if palindrome[left] != palindrome[right]:
            return False
        left += 1
        right -= 1
    return True

if __name__ == "__main__":
    print(f("radar"))
    print(f("12-11-21"))
    print(f("book"))