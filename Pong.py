import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Ping Pong Game with a Twist")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(40)
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bullet
bullet = turtle.Turtle()
bullet.speed(0)
bullet.shape("triangle")
bullet.color("yellow")
bullet.penup()
bullet.hideturtle()
bullet.goto(0, -250)
bullet.setheading(90)
bullet.dy = 20

# Obstacles
obstacles = []

def create_obstacle():
    obstacle = turtle.Turtle()
    obstacle.speed(0)
    obstacle.shape("square")
    obstacle.color("blue")
    obstacle.penup()
    obstacle.goto(random.randint(-350, 350), random.randint(0, 250))
    obstacles.append(obstacle)

# Paddle movement
def paddle_left():
    x = paddle.xcor()
    x -= 20
    if x < -350:
        x = -350
    paddle.setx(x)

def paddle_right():
    x = paddle.xcor()
    x += 20
    if x > 350:
        x = 350
    paddle.setx(x)

def fire_bullet():
    if not bullet.isvisible():
        bullet.setposition(paddle.xcor(), paddle.ycor() + 10)
        bullet.showturtle()

# Keyboard bindings
wn.listen()
wn.onkey(paddle_left, "Left")
wn.onkey(paddle_right, "Right")
wn.onkey(fire_bullet, "space")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collision
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Move the bullet
    if bullet.isvisible():
        bullet.sety(bullet.ycor() + bullet.dy)
        if bullet.ycor() > 290:
            bullet.hideturtle()

    # Bullet and obstacle collision
    for obstacle in obstacles:
        if bullet.distance(obstacle) < 20:
            bullet.hideturtle()
            obstacle.hideturtle()
            obstacles.remove(obstacle)

    # Randomly create obstacles
    if random.randint(1, 100) == 1:
        create_obstacle()
    
    # Ball and obstacle collision
    for obstacle in obstacles:
        if ball.distance(obstacle) < 20:
            ball.dx *= -1
            ball.dy *= -1

wn.mainloop()
