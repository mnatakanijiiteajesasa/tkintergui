from turtle import Turtle, Screen
import random
Jim = Turtle()
screen = Screen()
for i in range (0,10):
    Jim.right(36)
    for i in range (0,5):
        Jim.right(72)
        Jim.forward(100)

screen.exitonclick()
