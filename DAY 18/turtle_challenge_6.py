from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.bgcolor("black")
tim.speed(0)
colors = ["red", "green", "blue", "yellow"]

for i in range(200):
    tim.pencolor(colors[i % 4])
    tim.circle(i)
    tim.left(45)


