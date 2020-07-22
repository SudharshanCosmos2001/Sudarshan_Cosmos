import turtle
wn=turtle.Screen()
wn.title("My First Pong Game")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0


#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("White")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("White")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Pong Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("White")
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = -0.5

#Score Title
pen = turtle.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0" ,align="center", font=("Courier", 24, "normal"))


#Moving A up
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

#Moving A down
def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

#Moving B up
def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

#Moving B down
def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#Allocating Paddle Movements
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Loop
while True:
    wn.update()


    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor()> 290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()< -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}" .format(score_a, score_b) ,align="center", font=("Courier", 24, "normal"))

        if score_a==10:
            break

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}   Player B: {}" .format(score_a, score_b) ,align="center", font=("Courier", 24, "normal"))

        if score_b==10:
            break

    if ball.xcor()> 340 and ball.xcor()< 350 and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor()> paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx*= -1
        


    if ball.xcor()< -340 and ball.xcor()> -350 and (ball.ycor()< paddle_a.ycor() + 50 and ball.ycor()> paddle_a.ycor()-50):
        ball.setx(-340)
        ball.dx*= -1

    
    
