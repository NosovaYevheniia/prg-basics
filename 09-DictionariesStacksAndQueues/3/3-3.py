import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression:str):
    stack = queue.LifoQueue()

    for bracket in expression:
        if bracket in "([{":
            stack.put(bracket)

        elif bracket in ")]}":
            if stack.empty():
                return False
            
            top_item = stack.get()

            if (bracket == ")" and top_item != "(") or (bracket == "]" and top_item != "[") or \
                (bracket == "}" and top_item != "{"):
                return False
    return stack.empty()

if brackets_ok(expression1):
    print("expression1: brackets OK")
else:
    print("expression1: brackets NOT OK")

if brackets_ok(expression2):
    print("expression2: brackets OK")
else:
    print("expression2: brackets NOT OK")

if brackets_ok(expression3):
    print("expression3: brackets OK")
else:
    print("expression3: brackets NOT OK")



    