import turtle
import random
import time

class Dice():

    def __init__(self):
        self.dice = []
        self.current_side = None
        dice_sides = turtle.numinput(
            "Dice number", "How many sides for your dice? (min 1, max 12)", maxval=12, minval=1)
        for i in range(int(dice_sides)):
            self.dice.append(i + 1)

    def roll_dice(self):
        roll = random.choice(self.dice)
        writing_turtle = turtle.Turtle()
        writing_turtle.hideturtle()
        writing_turtle.write("Rolling Dice....." +
                             str(roll) + "!", font=("Arial", 14, "normal"))
        time.sleep(1)
        writing_turtle.clear()
        return roll


player1 = turtle.Turtle()
player1.shape("turtle")
player1.speed(5)

player1.hideturtle()
player1.color("green")
player1.penup()
player1.setpos(-250, 200)
player1.pendown()
player1.showturtle()

player1target = turtle.Turtle()
player1target.speed(50)
player1target.hideturtle()
player1target.penup()
player1target.setpos(250, 170)
player1target.pendown()
player1target.circle(30)

player2 = turtle.Turtle()
player2.shape("turtle")
player2.speed(5)

player2.hideturtle()
player2.color("blue")
player2.penup()
player2.setpos(-250, -200)
player2.pendown()
player2.showturtle()

player2target = turtle.Turtle()
player2target.speed(50)
player2target.hideturtle()
player2target.penup()
player2target.setpos(250, player2.ycor() - 30)
player2target.pendown()
player2target.circle(30)

dice = Dice()
turn = random.randint(1, 2)

writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
if turn % 2 == 0:
    writing_turtle.write("Player1 goes first!",  font=("Arial", 20, "normal"))
else:
    writing_turtle.write("Player2 goes first!",  font=("Arial", 20, "normal"))
time.sleep(2)
writing_turtle.clear()

while (player1.xcor() < player1target.xcor()) and (player2.xcor() < player2target.xcor()):
    if turn % 2 == 0:
        player1.forward(dice.roll_dice() * 20)
    else:
        player2.forward(dice.roll_dice() * 20)
    turn += 1

if turn % 2 == 0:
    turtle.write("Player 2 wins", font=("Arial", 20, "normal"))
else:
    turtle.write("player 1 wins", font=("Arial", 20, "normal"))
turtle.hideturtle()
turtle.done()
