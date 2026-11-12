from turtle import *
from collections import deque
import os

flavors = {
        "chocolate": "#663B2A",
        "vanilla": "#d2a679",
        "mint": "#66ffcc",
        "strawberry": "#ff4d4d",
        "banana": "#EBD35F",
        "coffee": "#A15A36",
        "bubble gum": "#CC65AF"
    }

def clear_Terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def begining():
    penup()
    color("#000000")
    home()

def set_Up():
    # set up
    clear_Terminal()
    screen = Screen()
    screen.setup(width=962, height=850)
    bgcolor("#f25a5a")
    pensize(2.5)
    speed(0)
    hideturtle()
    begining()

def draw_Lines():
    color("#972121")
    x =481
    penup()
    right(90)
    goto(x,425)
    for i in range(7):
        pendown()
        forward(850)
        penup()
        x-=137.428571429
        goto(x, 425)
    begining()
