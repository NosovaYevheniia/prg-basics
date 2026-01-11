import queue

def calculate(expression:str) -> int:
    splitted_string = expression.split()
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
    print(calculate("2 4 1 + *"))