import turtle

screen = turtle.Screen()

arvin = turtle.Turtle()
arvin.speed(3)
arvin.width(3)

arvin.color("red")
for i in range(4):
    arvin.forward(100)
    arvin.right(90)

arvin.penup()
arvin.goto(-150, -50)
arvin.pendown()

arvin.color("green")
for i in range(3):
    arvin.forward(100)
    arvin.left(120)

arvin.penup()
arvin.goto(100, -100)
arvin.pendown()

arvin.color("blue")
arvin.circle(50)

turtle.done()
