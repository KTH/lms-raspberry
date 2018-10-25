<LeftMouse>#! /usr/bin/env python3
from time import sleep
import time
from sense_hat import SenseHat
import requests
import _thread 

print("Running the monitor thingy...")

sense = SenseHat()

waiting = False

def current_time():
    return int(round(time.time() * 1000))

start_time=current_time() 

def animate(threadName, delay):
    ""
    while True:
        if animate:
            if status == "happy":
                happy()
            elif status == "medium":
                medium()
            elif status == "sad":
                sad()
    time.sleep(0.003)

# use one-char variable names to easilly display in cade
M = [30, 100, 100] 
i = [30,30, 30]

def get_top_of_face():
    # eye pixels are E 
    eye = i

    blinking = waiting
    if blinking:
        eye = i 
    else:
        eye = M 

    top_face = [
            i, i, i, i, i, i, i, i,
            i, i, i, i, i, i, i, i,
            i, i, eye, i, eye, i, i, i,
            ]
    return top_face


def medium():
    # use one-char variable names to easilly display in cade

    bottom_face = [
            i, i, i, i, i, i, i, i,
            i, i, i, i, i, i, i, i,
            i, M, M, M, M, M, i, i,
            i, i, i, i, i, i, i, i,
            i, i, i, i, i, i, i, i,
            ]


    sense.set_pixels(get_top_of_face() + bottom_face)


def sad():
    # use one-char variable names to easilly display in cade

    bottom_face = [
            i, i, i, i, i, i, i, i,
            i, i, i, i, i, i, i, i,
            i, i, M, M, M, i, i, i,
            i, M, i, i, i, M, i, i,
            M, i, i, i, i, i, M, i,
            ]


    sense.set_pixels(get_top_of_face() + bottom_face)


def happy():
    # use one-char variable names to easilly display in cade

    bottom_face = [
            M, i, i, i, i, i, M, i,
            M, i, i, i, i, i, M, i,
            i, M, i, i, i, M, i, i,
            i, i, M, M, M, i, i, i,
            i, i, i, i, i, i, i, i,
            ]


    sense.set_pixels(get_top_of_face() + bottom_face)


sense.set_rotation(180)
_thread.start_new_thread( animate, ("Thread-1", 2, ) )
status = "medium"
while True:
    animate = True
    waiting = True
    r = requests.get('https://app-r.referens.sys.kth.se/lms-monitor-of-monitor/api')
    sense.clear((0,0,0))
    if r.status_code != 200:
        animate = False
        sense.clear((255,0,0))
        sense.show_message("%s" % r.status_code)
    else:
        json = r.json()
        if any(part.get('color') == 'red' for part in json):
            status = "sad"
        elif all(part.get('color') == 'blue' for part in json):
            status = "happy"
        else:
            status = "medium"
    waiting = False
    sleep(3.0)

