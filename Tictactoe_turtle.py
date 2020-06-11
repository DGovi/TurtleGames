import turtle


def draw_board():
    for i in range(2):
        drawer.penup()
        drawer.goto(-300, 100 - 200 * i)
        drawer.pendown()
        drawer.forward(600)
    for i in range(2):
        drawer.penup()
        drawer.goto(100 - 200 * i, 300)
        drawer.pendown()
        drawer.setheading(-90)
        drawer.forward(600)


def draw_x(x, y):
    drawer.penup()
    drawer.goto(x + 45, y + 45)
    drawer.pendown()
    drawer.setheading(-135)
    drawer.forward(127)
    drawer.penup()
    drawer.goto(x - 45, y + 45)
    drawer.pendown()
    drawer.setheading(-45)
    drawer.forward(127)


def draw_o(x, y):
    drawer.penup()
    drawer.goto(x - 50, y)
    drawer.pendown()
    drawer.circle(50)


drawer = turtle.Turtle()
drawer.speed(10)
drawer.pensize(20)
drawer.hideturtle()

draw_board()
draw_o(0, 0)
turtle.done()
