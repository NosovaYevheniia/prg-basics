# Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:
# f(-7,8) returns 3
# f(-1,11) returns 0

def f(x: int, y: int) -> int:
  arr = range(x, y+1)
  count = 0
  for i in arr:
    if i < 0 and i%2 == 0:
      count = count + 1
  return count

if __name__ == "__main__":
  print(f(-7,8))
  print(f(-1,11))