import turtle

wn = turtle.Screen()
taner = turtle.Turtle()

x = int(input("x: "))
taner.speed(1)

taner.forward( x * 3 )
taner.left(90)
taner.forward( x * 3 )
taner.left(90)
taner.forward( x * 3 )
taner.left(90)
taner.forward( x * 3 )

taner.left(90)
taner.forward( x * 2 )
taner.left(90)
taner.forward(x)
taner.left(90)
taner.forward(x)
taner.left(90)
taner.forward(x)

taner.penup()
taner.goto(0, 3 * x)
taner.pendown()

taner.left(150)
taner.forward(3 * x)
taner.right(120)
taner.forward(3 * x)

taner.penup()
taner.goto(0,0)
taner.pendown()

wn = exitonclick()
