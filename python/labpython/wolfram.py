import turtle

def drawFivePointStar(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

wolfram = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wolfram.pensize(3)
wolfram.speed(10)
wolfram.color("hotpink")

for l in range(5):
	drawFivePointStar(wolfram)
	wolfram.up()
	wolfram.left(144)
	wolfram.forward(350)
	wolfram.down()

wn.exitonclick()
