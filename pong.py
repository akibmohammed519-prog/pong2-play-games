import turtle
import time

wn = turtle.Screen()
wn.title("Pong Game : 2 Playes")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

paused = False
left_lives = 3
right_lives = 3

left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("cyan")
left_pad.shapesize(stretch_wid=5,stretch_len=1)
left_pad.penup()
left_pad.goto(-350 , 0)

right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("red")
right_pad.shapesize(stretch_wid=5,stretch_len=1)
right_pad.penup()
right_pad.goto(350 , 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3
ball.dy = 3

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.up()
pen.hideturtle()
pen.goto(0,260)

def score_update():
    pen.clear()
    pen.write(f"Left Lives: {left_lives} Right Lives: {right_lives}",
              align="center", font=("Arial", 15, "bold"))
score_update()

def left_up():
    y = left_pad.ycor()
    if y < 250:
        left_pad.sety(y + 20)

def left_down():
    y = left_pad.ycor()
    if y > -250:
        left_pad.sety(y - 20)
def right_up():
    y = right_pad.ycor()
    if y < 250:
        right_pad.sety(y + 20)
def right_down():
    y = right_pad.ycor()
    if y > -250:
        right_pad.sety(y - 20)

def toggle_pause():
    global paused
    paused = not paused

wn.listen()
wn.onkeypress(left_up, "q")
wn.onkeypress(left_down, "z")
wn.onkeypress(right_up, "Up")
wn.onkeypress(right_down, "Down")
wn.onkeypress(toggle_pause, "space")
while True:
    wn.update()

    if paused:
        continue
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        right_lives -= 1
        score_update()

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        left_lives -= 1
        score_update()

    if (340 < ball.xcor() < 350) and (right_pad.ycor() - 50 < ball.ycor() < right_pad.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (left_pad.ycor() - 50 < ball.ycor() < left_pad.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

    if left_lives == 0 or right_lives == 0:
        pen.goto(0,0)
        if left_lives == 0:
            pen.write("Right Player Win", align="center", font=("Arial", 24 ,"bold"))
        else:
            pen.write("Left Player Win", align="center", font=("Arial", 24, "bold"))
        break
    
    time.sleep(0.01)