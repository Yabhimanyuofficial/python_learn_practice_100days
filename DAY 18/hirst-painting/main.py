"""
import colorgram

rgb_colors = []
colors = colorgram.extract('hirst.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
"""
import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(222, 232, 226), (208, 161, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (128, 189, 143), (83, 20, 44), (38, 42, 67), (186, 93, 105), (187, 139, 171), (84, 122, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (161, 202, 220), (45, 74, 77), (80, 73, 44), (57, 131, 122), (217, 176, 188), (220, 182, 167), (166, 207, 165)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list) )
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()