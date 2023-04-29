class Rectangle:
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
    def area(self):
        return self.sideA * self.sideB

    def perimeter(self):
        return (self.sideA + self.sideB) * 2

r = Rectangle(5, 6)

print(r.area())
print(r.perimeter())