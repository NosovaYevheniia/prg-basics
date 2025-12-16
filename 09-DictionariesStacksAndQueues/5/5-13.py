import queue

def calculate(expression:str) -> int: #241+*
    # splitted_string = expression.split()
    # print(splitted_string)
    stack = queue.LifoQueue()
    for item in expression:
        if item.isdigit():
            stack.put(int(item))
        else:
            b = stack.get()
            a = stack.get()
            if item == "+":
                stack.put(a + b)
            elif item == "*":
                stack.put(a * b)
    return stack.get()
if __name__ == "__main__":
    print(calculate("241+*"))