# Products are marked with a special code consisting of 3 digits and afourth control digit. The forth digit is determined 
# by calculating the remainder of dividing the sum of the first three digits by 7. Define a function f(product_code) that 
# returns True if the product code is correct or False otherwise. Sample result:
# f("1082") returns True
# f("2035") returns True
# f("1114") returns False
# f("7071") returns False

def f(product_code: str) -> bool:
        if (int(product_code[0]) + int(product_code[1]) + int(product_code[2]) % 7 == int(product_code[3])):
                return True
        return False

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))