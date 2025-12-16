import queue

stack = queue.LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)

count = 0
while not stack.empty():
    x = stack.get()
    count += x
    print(count)
