import turtle

def draw_circles(t, size, step):
    for _ in range(4):
        t.circle(size)
        size -= step

def draw_special(t, size, repeat, step):
    for _ in range(repeat):
        draw_circles(t, size, step)
        t.right(360 / repeat)

def draw_picture_nice():
    t = turtle.Turtle()
    t.speed(0)

    colors = ["white", "yellow", "blue", "orange", "red"]
    steps = [4, 5, 10, 19, 20]

    for i in range(len(colors)):
        t.color(colors[i])
        draw_special(t, 100, 10, steps[i])

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("black")
    draw_picture_nice()
    screen.mainloop()
