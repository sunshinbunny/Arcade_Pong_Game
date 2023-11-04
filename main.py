from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong, the Arcade Game!")
screen.tracer(False)

r_paddle=Paddle(position=(350, 0))
l_paddle=Paddle(position=(-350,0))
ball=Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")




game_is_on = True
while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #Detect collision with top wall
  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  #Detect collision with paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()


  #Detect when right paddle misses
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  #Detect when left paddle missed
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()



screen.exitonclick()

