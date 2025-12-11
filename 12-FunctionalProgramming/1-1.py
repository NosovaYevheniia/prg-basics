###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   aver_mean = (x + y) / 2
   return aver_mean

# takes two numbers from keyboard
n1 = int(input("Eneter first number: "))
n2 = int(input("Enter second number: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')

