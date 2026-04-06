import turtle

screen = turtle.Screen()
alex = turtle.Turtle()
alex.speed(5)

alex.clear()
alex.up()
alex.goto(0, 0)
alex.down()

side = 100
sides = 6
angle = 360 / sides

for _ in range(sides):
    alex.forward(side)
    alex.left(angle)

alex.up()

alex.clear()
alex.speed(6)
alex.pensize(8)

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

radius = 60

for c in colors:
    alex.color(c)
    alex.goto(0, -radius)
    alex.down()
    alex.circle(radius, 180)
    alex.up()
    radius += 15

alex.hideturtle()

screen.mainloop()
