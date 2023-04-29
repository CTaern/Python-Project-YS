import random
import turtle
wn = turtle.Screen()
wn.bgcolor("Turquoise")

turtle0 = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle0.color("red")
turtle1.color("blue")
turtle2.color("green")

turtle0.speed(1)
turtle1.speed(1)
turtle2.speed(1)

turtle1.up()
turtle1.goto(0,-10)
turtle1.down()

turtle2.up()
turtle2.goto(0,-20)
turtle2.down()




x = random.random()
y = x*10
z = random.random()
v = z*10
c = random.random()
b = c*10

for i in range(10):
	turtle0.forward(y)
	turtle1.forward(v)
	turtle2.forward(b)
wn.exitonclick()
