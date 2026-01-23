import turtle

arvin = turtle.Turtle()
arvin.speed(0)
arvin.width(15)

screen = turtle.Screen()
screen.bgcolor("white")

colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

radius = 200

arvin.penup()
arvin.goto(-radius, -50)
arvin.setheading(0)
arvin.pendown()

for color in colors:
    arvin.color(color)
    arvin.circle(radius, 180)

    arvin.left(180)
    arvin.forward(15)
    arvin.left(180)
    arvin.right(90)
    arvin.forward(15)
    arvin.left(90)

    radius = radius - 15

turtle.done()
