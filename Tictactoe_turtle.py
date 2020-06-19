import turtle
import random
import time

# drawing methods


def draw_board():
    board_drawer = turtle.Turtle()
    board_drawer.speed(20)
    board_drawer.pensize(20)
    board_drawer.color("white")
    for i in range(2):
        board_drawer.penup()
        board_drawer.goto(turtle.window_width() / 8 - turtle.window_width() / 4 *
                          i, turtle.window_height() / 3)
        board_drawer.pendown()
        board_drawer.setheading(270)
        board_drawer.forward(turtle.window_height() * 2 / 3)
    for i in range(2):
        board_drawer.penup()
        board_drawer.goto(turtle.window_height() / 3,
                          turtle.window_width() / 8 - turtle.window_width() / 4 * i)
        board_drawer.pendown()
        board_drawer.setheading(180)
        board_drawer.forward(turtle.window_height() * 2 / 3)


def write_message(message):
    writing_turtle.clear()
    writing_turtle.penup()
    writing_turtle.goto(-300, 300)
    writing_turtle.pendown()
    writing_turtle.write(message, font=("arial", 20))


def draw_x(x, y):
    x_drawer.penup()
    x_drawer.goto(x, y)
    x_drawer.pendown()
    x_drawer.setheading(45)
    x_drawer.speed(5)
    x_drawer.backward(45)
    x_drawer.forward(90)
    x_drawer.backward(45)
    x_drawer.speed(0)
    x_drawer.left(90)
    x_drawer.speed(5)
    x_drawer.forward(45)
    x_drawer.backward(90)
    x_drawer.forward(45)
    x_drawer.speed(0)


def draw_o(x, y):
    o_drawer.setheading(180)
    o_drawer.penup()
    o_drawer.goto(x, y + 50)
    o_drawer.pendown()
    o_drawer.circle(50)


def display_board_content(board):
    drawer.clear()
    current_element = 0

    for row in range(3):
        for column in range(3):
            current_element += 1
            xcor = -160 + 160 * column
            ycor = 160 - 160 * row
            drawer.penup()
            drawer.goto(xcor, ycor)
            drawer.pendown()
            if board[current_element] == "x":
                draw_x(xcor, ycor)
                continue
            elif board[current_element] == "o":
                draw_o(xcor, ycor)
                continue
            drawer.write(
                current_board[current_element], font=("Arial", 16))


# game methods
def play_game(board):
    display_board_content(board)
    game_is_finished = False
    turn = 0

    while not game_is_finished:
        thisTurn(board)
        game_is_finished = is_winning_move(board) or turn == 8
        if turn == 8:
            write_message("Game is tied")
        turn += 1
        display_board_content(board)


def thisTurn(board):
    global turn
    while True:
        try:
            if turn % 2 == 0:
                write_message("Player 1".upper())
                inputted_num = int(the_screen.numinput("Place your symbol",
                                                       "Where would you like to palce your symbol? (one of the numbers shown)", default=None, minval=1, maxval=9))
                if board[inputted_num] == "o" or board[inputted_num] == "x":
                    raise Exception
                board[inputted_num] = 'x'
            else:
                write_message("Player 2".upper())
                inputted_num = int(the_screen.numinput("Place your symbol",
                                                       "Where would you like to palce your symbol? (one of the numbers shown)", default=None, minval=1, maxval=9))
                board[inputted_num] = 'o'
            break
        except Exception:
            time.sleep(3)
    turn += 1


def is_winning_move(board):
        # check winning possibilities
    if (board[1] == board[2] == board[3]
        or board[4] == board[5] == board[6]
        or board[7] == board[8] == board[9]
        or board[1] == board[4] == board[7]
        or board[2] == board[5] == board[8]
        or board[3] == board[6] == board[9]
        or board[1] == board[5] == board[9]
            or board[3] == board[5] == board[7]):
        if turn % 2 == 1:
            write_message("Player 1 wins!".upper())
        elif turn % 2 == 0:
            write_message("player 2 wins!".upper())
        return True
    else:
        return False


# game time
current_board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 0

the_screen = turtle.Screen()
the_screen.title("Tic Tac Toe")
the_screen.bgcolor("black")

drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()
drawer.color("white")

writing_turtle = turtle.Turtle()
writing_turtle.speed(0)
writing_turtle.hideturtle()
writing_turtle.color("white")

x_drawer = turtle.Turtle()
x_drawer.color("green")
x_drawer.pensize(10)
x_drawer.speed(0)
x_drawer.hideturtle()

o_drawer = turtle.Turtle()
o_drawer.color("blue")
o_drawer.pensize(10)
o_drawer.speed(0)
o_drawer.hideturtle()

draw_board()
play_game(current_board)
write_message("Press anywhere to exit")


turtle.exitonclick()
