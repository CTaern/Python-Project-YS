import math
class Circle:
    def __init__(self, radius):
        self.r = radius
    def area(self):
        return math.pi * (self.r ** 2)
    def perimeter(self):
        return 2 * math.pi * self.r

c = Circle(10)

print(c.perimeter())
print(c.area())
print(Circle(10).perimeter())
