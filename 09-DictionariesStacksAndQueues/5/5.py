import queue

stack = queue.LifoQueue()

stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)

count = 0
two_count = 0
while not stack.empty() and two_count < 2:
    x = stack.get()
    count += x
    two_count += 1
print(count)

