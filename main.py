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
