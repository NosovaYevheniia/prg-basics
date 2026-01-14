# A counter allows you to count arbitrary elements. Define a class C that allows you to create counters. The
# initial value of the counter is assigned when the object is created. The class contains the following methods: m1()
# (returns the value of the counter), m2() (increments the value of the counter by 1), m3() (decrements the value of
# the counter by 1), m4(n) (increments or decrements the value of the counter by n), __str__() (returns the value of
# the counter as a string). Example:
# c=C(5)
# c.m1() returns 5
# c.m2()
# c.m1() returns 6
# c.m4(-8)
# c.m1() returns -2
# c.m3()
# c.m1() returns -3
# c.m4(10)
# c.m1() returns 7
# c.__str__() returns "7" 

class C:
    def __init__(self, initial):
        self.value = initial

    def m1(self):
        return self.value
    
    def m2(self):
        self.value = self.value + 1
    
    def m3(self):
        self.value = self.value - 1
    
    def m4(self, n):
        self.value = self.value + n
    
    def __str__(self):
        return str(self.value)
    
c=C(5)
print(c.m1())
c.m2()
print(c.m1())
c.m4(-8)
print(c.m1())
c.m3()
print(c.m1())
c.m4(10)
print(c.m1())
c.__str__()
print(c.m1())