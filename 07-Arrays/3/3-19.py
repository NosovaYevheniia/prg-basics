def grater_number(number, array):
    elements =[]
    for i in array:
        if i > number:
            elements.append(i)
    return elements

if __name__ == "__main__":
    inp = int(input("Enter a number: "))
    x = grater_number(inp, [3, 7 ,9, 11, 6, 9, 10, 5])
    print(x)