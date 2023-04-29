class Car:
    def __init__(self, color, km):
        self.color = color
        self.km = km
    def __str__(self):
        return "The " + self.color + " car has " + str(self.km) + " km."

bluecar = Car("blue", 20000)
redcar = Car("red", 30000)

print(bluecar)
print(redcar)
