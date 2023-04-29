import turtle
wn = turtle.Screen()
alex = turtle.Turtle()

for a in ["yellow", "purple", "red",]:
	alex.color(a)
	alex.forward(50)
	alex.left(60)
	alex.forward(50)
	alex.left(60)	
	
wn.exitonclick()
