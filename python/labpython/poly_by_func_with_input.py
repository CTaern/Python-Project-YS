import turtle


def poly(x, y):
	angle = 360 / side
	for i in range(side):
		x.left(angle)
		x.forward(y)

side = int(input("Number of sides: "))
pen_size = int(input("Size of pen: "))
side_lenght = int(input("Lenght of size: "))
colorofturtle = input("Colour of polygon: ")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.pensize(pen_size)
alex.color(colorofturtle)

poly(alex, side_lenght)

wn.exitonclick()
