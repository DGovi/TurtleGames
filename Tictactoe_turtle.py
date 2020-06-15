import turtle


def draw_board():
    drawer.pensize(20)
    for i in range(2):
        drawer.penup()
        drawer.goto(turtle.window_width() / 8 - turtle.window_width() / 4 *
                    i, turtle.window_height() / 3)
        drawer.pendown()
        drawer.setheading(270)
        drawer.forward(turtle.window_height() * 2 / 3)
    for i in range(2):
        drawer.penup()
        drawer.goto(turtle.window_height() / 3,
                    turtle.window_width() / 8 - turtle.window_width() / 4 * i)
        drawer.pendown()
        drawer.setheading(180)
        drawer.forward(turtle.window_height() * 2 / 3)
    drawer.pensize(10)


def spread_turtles_out():
    global spread_turtles
    spread_turtles = []
    for int in range(9):
        spread_turtles.append(turtle.Turtle())
        spread_turtles[int].penup()
        spread_turtles[int].shape("turtle")
        spread_turtles[int].color("blue")

    spread_turtles[0].goto(-160, 160)
    spread_turtles[1].goto(0, 160)
    spread_turtles[2].goto(160, 160)
    spread_turtles[3].goto(-160, 0)
    spread_turtles[4].goto(0, 0)
    spread_turtles[5].goto(160, 0)
    spread_turtles[6].goto(-160, -160)
    spread_turtles[7].goto(0, -160)
    spread_turtles[8].goto(160, -160)


def draw_x(x, y):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.setheading(45)
    drawer.backward(45)
    drawer.forward(90)
    drawer.backward(45)
    drawer.left(90)
    drawer.forward(45)
    drawer.backward(90)
    drawer.forward(45)


def draw_o(x, y):
    drawer.setheading(180)
    drawer.penup()
    drawer.goto(x, y + 50)
    drawer.pendown()
    drawer.circle(50)


# GAME START
drawer = turtle.Turtle()
drawer.speed(10)
drawer.hideturtle()

draw_board()
spread_turtles_out()

spread_turtles[0].onclick(draw_x)

turtle.done()
turtle.exitonclick()
