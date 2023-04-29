import turtle

def drawPolygon(x, t):
	for i in range(6):
		x.left(30)
		x.forward(t)
		x.left(30)
		

wn = turtle.Screen()
alex = turtle.Turtle()

wn.bgcolor("Turquoise")
alex.pensize(3)
alex.color("red")
alex.speed(1)

drawPolygon(alex, 60)

wn.exitonclick()
