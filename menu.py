#! /usr/bin/env python3
from time import sleep
from sense_hat import SenseHat
import requests
sense = SenseHat()

def show_up():
    sense.clear()
    sense.show_letter("1")

def show_down():
    sense.clear()
    sense.show_letter("3")

def show_left():
    sense.clear()
    sense.show_letter("2")

def show_right():
    sense.clear()
    sense.show_letter("4")

# Main stuff
sense.clear()
sense.show_letter("0")
sense.stick.direction_up = show_up
sense.stick.direction_down = show_down
sense.stick.direction_left = show_left
sense.stick.direction_right = show_right

# Do this to run it forever!
while True:
    pass
